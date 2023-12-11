import random
length=int(input("Enter the lemgth of password you want :"))

numbers = "1234567890" 
Lcase= "abcdefghijklmnopqrstuvwxyz"
Ucase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols ="!@#$%^&*()"


all= numbers + Lcase + Ucase + symbols

password="".join(random.sample(all,length))

print("The random generated password is :",password)