import base64

def encode(string):
    Encoded_string = ""
    length_of_the_string = len(string)
    if length_of_the_string > 1:
        for variable in string:
            ans = str(ord(variable)) + " " + \
                str(length_of_the_string+ord(variable)) + "&"
            Encoded_string += ans
    else:
        ans = str(ord(string)) + "&" + str(ord(string))
        Encoded_string += ans
    encoded = string.encode()
    return encoded


def decode(string):
    ans = string.split("&")
    ans1 = ""
    value = ""
    ans.pop()
    for ans in ans:
        x = ans.split()
        ans1 = chr(int(x[0]))
        value += ans1
    return value
