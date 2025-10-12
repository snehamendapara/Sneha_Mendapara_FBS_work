#2 Write a program to input any alphabet and check whether it is vowel or consonant.
vowel = ["a","e","i","o","u","A","E","I","O","U"]

character = input("Enter Alphabet : ")
if character in vowel :
    print("character is Vowel")   
else : 
    print("character is Consonant")