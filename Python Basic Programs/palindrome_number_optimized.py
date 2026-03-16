## Palindrome Checker

## Takes in a number or a string and checks if it is a palindrome
'''
>>> checkIfPalindrome("racecar")
True
>>> checkIfPalindrome(1234567890987654321)
True
>>> checkIfPalindrome(94835764385)
False

'''

value = str(input('Enter a string or a number: '));

def checkIfPalindrome(value):
    i = 0
    j = len(value) - 1
    
    while i < j:
        if value[i] is value[j]:
            i += 1
            j -= 1
        else:
            print(value + " is not a palindrome")
            return False
    
    print(value + " is a palindrome")
    return True
    
print(checkIfPalindrome(value))
