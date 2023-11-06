import requests

link="http://localhost:5000/auth/login/safe"

file1 = open('static/10-million-password-list-top-10000.txt', 'r')
Lines = file1.readlines()
count=0
for line in Lines:
    r=requests.post(link,data={"username" : "Weak", "password" : line.strip()})
    if r.url!=link:
        print("Try ",count,": Password found! -> '", line.split(),"'")
        break
    count+=1
