def is_palindrome(s):
    return s == s[::-1] #reverses the string and then compares it to the initial
    s = s.lower() #changes everything to lowercase

print(is_palindrome("madam"))