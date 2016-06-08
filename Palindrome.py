def reverse(text):
    return text[::-1]
    
def is_palindrome(text):
    return text.lower() == reverse(text).lower()
     
    
something = raw_input("Enter text to check: ")
if is_palindrome(something):
    print("Yes, it is a palindrome")
else:
    print("No, it is not a palindrome")