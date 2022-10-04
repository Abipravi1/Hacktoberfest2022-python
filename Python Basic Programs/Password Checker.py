import re
print("YOUR PASSWORD SHOULD HAVE ATLEAST A NUMBER AND A LOWER CASE")
print("IT SHOULD BE ATLEAST 10 CHARACTERS LONG")
print("IT SHOULD START WITH AN UPPER CASE AND END WITH A SPECIAL CHARACTER")
password = input("ENTER YOUR PASSWORD: ")
length = len(password)
lower_case = re.search("[a-z]+",password)
upper_case = re.search("[A-Z]+",password[0])
special_char = re.search(r"\W+",password[length-1])
number = re.search("\d+",password)
if(lower_case == None):
    print("INVALID PASSWORD. ATLEAST ONE LOWER CASE REQUIRED")
if(upper_case == None):
    print("INVALID PASSWORD. UPPER CASE REQUIRED IN FIRST POSITION")
if(special_char == None):
    print("INVALID PASSWORD. SPECIAL CHARACTER REQUIRED IN LAST POSITION")
if(number == None):
    print("INVALID PASSWORD. ATLEAST ONE NUMBER REQUIRED")
if(length<10):
    print("INVALID PASSWORD. ATLEAST 10 CHARACTERS REQUIRED")
if((lower_case!=None) and (upper_case!=None) and (special_char!=None) and (number!= None) and (length>=10)):
    print("VALID PASSWORD. HENCE ACCEPTED")
