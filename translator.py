from translate import Translator

def translate(from_language, to_language, input_text):
  translator= Translator(from_lang=from_language,to_lang=to_language)
  translation = translator.translate(input_text)
  return translation

from_language = input("Enter base language: ")
to_language = input("Enter translated language: ")
source_text = input("Enter text to translate: ")
print("Tranlated test is: ", translate(from_language, to_language, source_text))
