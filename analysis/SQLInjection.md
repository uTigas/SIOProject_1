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

- We could also make an udf that would achieve the same thing that our functionality from sqlite3 , separation between arguments and the prompt.








