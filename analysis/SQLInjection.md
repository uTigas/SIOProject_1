# Analysis CWE-89: SQL Injection

## Introduction 

SQL injection attacks represent a serious threat to any database-driven site.The methods behind an attack
are easy to learn and the damage caused can range from considerable to complete system compromise.

## Vulnerabilities 

### Basic Injection to Bypass Login 

#### Example

We have a simple login form on http://127.0.0.1:5000/auth/login and we also have an admin user called ```admin_user```. But this form is vulnerable to a simple sql injection.
By simply writing ``` admin_user'-- // ``` on the username and a random string for the password we can login to the admin account.
![image](https://github.com/uTigas/SIOProject_1/assets/125353199/8dcde9c2-ba10-44f5-bca5-59aa0b774c4a)
![image](https://github.com/uTigas/SIOProject_1/assets/125353199/43ef5739-baf8-465e-b4bf-8242cb512393)

#### Weak code 
![image](https://github.com/uTigas/SIOProject_1/assets/125353199/a8f3bd7b-c2eb-4345-9fc6-a4611eed8015)

We are making the sql command based on string concatenation which allows to do a simple sql injection. ( Blueprints/auth.py login() function )

#### Fix 

- We can use a builtin functionality from the sqlite3 python library that allows us to build safe sql commands very simply.

![image](https://github.com/uTigas/SIOProject_1/assets/125353199/a7d964b2-04a3-43e5-b2d1-dc7d564e1b6a)

- We can refactor the logic of our login so that it isnt vulnerable to this attack. In this example the ```check_password_hash()``` must always run and cant be skipped.

![image](https://github.com/uTigas/SIOProject_1/assets/125353199/18d2de35-ad85-458d-85da-8056e5100270)

- We could also make an udf that would achieve the same thing that our functionality from sqlite3 , separation between arguments and the sql command.

### Basic injection on product listing to get names of all users

#### Example

We can search for products using a string but this field is vulnerable to sql injection.

![image](https://github.com/uTigas/SIOProject_1/assets/125353199/c7f1df89-f433-4924-b87a-d081579c61fe)

```' ORDER BY 4 -- //```
We can check that is vulnerable by ordering the products in a different order also we can see that we can only order up to the 4th collumn.
After we know that we are working with 4 collumns we can add information to the product listing. For example with ```' UNION SELECT 1,2,3,4,5 -- // ```

![image](https://github.com/uTigas/SIOProject_1/assets/125353199/0be2f68c-5dfa-4757-a14a-00278925e310)

But we can cause a bit more damage with ```' UNION SELECT  Username , ID , Password , Role FROM User ORDER BY 2 -- //```

![image](https://github.com/uTigas/SIOProject_1/assets/125353199/4436cba5-efa7-4342-b766-a889cba4e250)

Which gives us a list of the username and the corresponding encrypted password.

#### Weak code

![image](https://github.com/uTigas/SIOProject_1/assets/125353199/edf2f1ae-6e16-43c7-8837-9ce45723f4a3)

Once again we are building our SQL commands using concatenation of strings. ( Blueprints/shop.py products() function ) 

#### Fix 

- We can deploy a similar strategy used above and use the sqlite3 python functionality to prevent SQL injection.

![image](https://github.com/uTigas/SIOProject_1/assets/125353199/d6a7588f-aea9-4dbb-bd32-6aff9352de8e)

![image](https://github.com/uTigas/SIOProject_1/assets/125353199/63218a15-91f2-41fd-8a16-f4058e310b31)



















