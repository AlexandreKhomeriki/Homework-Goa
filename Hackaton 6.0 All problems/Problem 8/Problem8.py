#შექმენით რაიმე string ტიპის ცვლადი და შეამოწმეთ palindrome'ა თუ არა.


text = "Father"

# Function that checkes palindrome
def is_palindrome(s):
    
    return s == s[::-1]

#Result
if is_palindrome(text):
    print(f'"{text}" არის palindrome.')
else:
    print(f'"{text}" არ არის palindrome.')  