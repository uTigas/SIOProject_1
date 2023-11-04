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









