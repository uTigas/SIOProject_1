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