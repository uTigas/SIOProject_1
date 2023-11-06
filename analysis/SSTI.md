# Analysis CWE-1336: Improper Neutralization of Special Elements Used in a Template Engine

## Introduction 
Many web applications use template engines that allow developers to insert externally-influenced values into free text or messages in order to generate a full web page, document, message, etc. Such engines include Twig, Jinja2, Pug, Java Server Pages, FreeMarker, Velocity, ColdFusion, Smarty, and many others - including PHP itself. Some CMS (Content Management Systems) also use templates.

Template engines often have their own custom command or expression language. If an attacker can influence input into a template before it is processed, then the attacker can invoke arbitrary expressions, i.e. perform injection attacks. For example, in some template languages, an attacker could inject the expression "{{7*7}}" and determine if the output returns "49" instead. The syntax varies depending on the language.

We our case we are using Jinja2 to generate this templates.

## Example

We can search for products based on a url , i.e ```http://127.0.0.1:5000/products?minPrice=5&maxPrice=40&input=&category=Drinkware``` . But we can exploit this since our category field is vulnerable to SSTi.
The link ```http://127.0.0.1:5000/products?minPrice=5&maxPrice=40&input=&category={{2*2}}``` returns the following result.

![image](https://github.com/uTigas/SIOProject_1/assets/125353199/81135b32-37f2-4e2c-ad74-237fff2f3e06)

As we can see the category is 4 the result of 2*2. But this raises the question who did this calculation and why? The answer is that the server did , so that means that we are executing code on the server and because ```{{ }}``` signals to Jinga2 to render something that it.
If we try the link ```http://127.0.0.1:5000/products?minPrice=5&maxPrice=40&input=&category={{print("Hi")}}``` we will see something curious.

![image](https://github.com/uTigas/SIOProject_1/assets/125353199/e410f795-abcf-4bfe-bc9e-1eaca2c0e50e)

This error is the result of the template engine running in a sandbox where we cant do function calls directly i.e we cant do ```print("Hi")```.

