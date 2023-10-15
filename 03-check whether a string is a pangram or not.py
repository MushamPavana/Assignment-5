#Write a Python function to check whether a string is a pangram or not.
#Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
#For example : "The quick brown fox jumps over the lazy dog".

def check(str):
    alphabet = "abcdefghijklmnopkrstuvwxyz"
    for char in alphabet:
        if char not in str.lower():
            return False
    return True  
str = input("enter the sentence")
if(check(str) == True):
    print("the entered sentence is pangram")
else:
    print("the entered sentence is not pangram")