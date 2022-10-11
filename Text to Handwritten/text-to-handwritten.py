# pip install -r requirements.txt
import pywhatkit


text = input("Enter the text : ")

try:
    pywhatkit.text_to_handwriting(text)
    print("Succesfull")

except:
    print("Soemthing went wrong please try again.")