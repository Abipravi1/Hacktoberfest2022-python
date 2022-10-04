def palindrome(number, string_result = ''):
    if number < 1:
        return string_result
    else:
        if str(number) == str(number)[::-1]:
            string_result += (str(number)+" ")
        return palindrome(number-1, string_result)

palindrom_num = palindrome(100)

print(palindrom_num)