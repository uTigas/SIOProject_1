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
![image](https://github.com/uTigas/SIOProject_1/assets/125353199/30e5f5fb-f7c1-4c91-8061-aece1169c217)

#### Weak code

![image](https://github.com/uTigas/SIOProject_1/assets/125353199/c9d5a5f8-d6bd-4819-bdf4-b9a1aafde750)

In this piece of code we assume that category is safe so it can be treated has html. ( templates/products.html )

Also on the function products() on Blueprints/shop.py we never validate if the category field is an existing one or if it just garbage.

#### Fix 

- If we omit the safe tag jinga2 ( our template engine ) will assume that the input is unsafe and only treat it has text.

![image](https://github.com/uTigas/SIOProject_1/assets/125353199/b1c90437-3c9e-4f99-ba53-a23c40f1a128)

![image](https://github.com/uTigas/SIOProject_1/assets/125353199/2d845765-6f1e-40a3-989c-1564e4fa3509)

- If we validate if the category exists we can on the server indicate correct steps to fix the problem.

![image](https://github.com/uTigas/SIOProject_1/assets/125353199/827a3648-83a7-41d1-aaba-62706fd6899d)

![image](https://github.com/uTigas/SIOProject_1/assets/125353199/55a4e7a9-9c68-4497-a5ca-62f2c1ac4696)


### Stored XSS Attack

#### Example

We can write reviews for a product.

![image](https://github.com/uTigas/SIOProject_1/assets/125353199/a9d6e9f7-dd3a-4c1d-9656-3f67922705ca)

But we can insert a malicious payload in the review that will then be stored on the server. Users then accessing this webpage will render the malicious payload.

![image](https://github.com/uTigas/SIOProject_1/assets/125353199/a66876dc-7e6e-4946-b8f1-f533da1035f9)

After we load the page again we get:

![image](https://github.com/uTigas/SIOProject_1/assets/125353199/3d10f1d8-cd73-4fa1-8b4a-212b4fd55beb)

#### Weak code

![image](https://github.com/uTigas/SIOProject_1/assets/125353199/1fc178b6-ef97-4a10-831b-145e12385e66)

We assume that the review is safe so the contents of it are treated like html.

Also we dont check on the server side if the review migth have malicious code.

#### Fix 

- Just omit the safe tag and the review will only be treated as text.
![image](https://github.com/uTigas/SIOProject_1/assets/125353199/c53ecf37-a7fa-4fff-b0c6-ac66378aedab)

![image](https://github.com/uTigas/SIOProject_1/assets/125353199/dc2f727c-95ac-4234-9367-6e4c673ef5fe)

- We could also parse the review and check if it has any potencial malicous payload and reject it but for our case we assumed that the review is only text so this is uneccesary and just removing the safe tag is enough.

###  CSRF Attack

#### Example

![image](https://github.com/uTigas/SIOProject_1/assets/125353199/6f58765f-a5a1-44b0-9935-1e79b1ead970)

We can also target different servers using an XSS attack in this example we use the image tag to make a request to a server with the credentials of a user who visits the page with the malicious review.

![image](https://github.com/uTigas/SIOProject_1/assets/125353199/1326ef61-d4ad-4535-9907-d1a46945f880)

As we can see a GET request to ```https://vulnerable-bank.com/transfer.jsp?amount=1000&to_nib=12345300033233``` was sent and a normal user migth have been unware of this.

#### Fix 

- Don´t allow stored XSS Attack and reflected XSS Attack with the strategies diccussed above.

- Enable CORS or a secure Content Security Policy so that the browser knows what to not load.

![image](https://github.com/uTigas/SIOProject_1/assets/125353199/a4874939-1a63-42cb-82de-2a54a16df10b)

















