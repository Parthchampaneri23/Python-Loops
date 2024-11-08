#Python program to check if the given string is a palindrome



def is_palindrome(s):
    for i in range(0, int(len(s)/2)):
        if s[i] != s[len(s)-i-1]:
            return False
    return True

s = "malayalam"
if is_palindrome(s):
    print("Yes, the string is a palindrome.")
else:
    print("No, the string is not a palindrome.")
