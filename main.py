import string
import random

def generate_password(minLength, lowerCase = True, numbers=True, specialCharacter = True):
    upperCases = string.ascii_uppercase
    lowerCases = string.ascii_lowercase
    digit = string.digits
    specialCharacters = string.punctuation
    
    character = upperCases
    
    if lowerCase:
        character += lowerCases
        
    if numbers:
        character += digit
        
    if specialCharacter:
        character += specialCharacters
    
    pswd = ""
    
    meets_criteria = False
    has_lowerCase = False
    has_numbers = False
    has_specialCharacter = False
    
    while not meets_criteria or len(pswd) < meets_criteria:
        newChar = random.choice(character)
        pswd += newChar
        
        if newChar in lowerCases:
            has_lowerCase = True
        
        if newChar in digit:
            has_numbers = True
        
        if newChar in specialCharacters:
            has_specialCharacter = True
            
        meets_criteria = True
        
        if lowerCase:
            meets_criteria = has_lowerCase
        
        if numbers:
            meets_criteria = has_numbers
           
        if  specialCharacter:
            meets_criteria = has_specialCharacter

    return pswd
    
if __name__=='__main__':
    pswdLength = int(input("Enter Length: "))
    print(generate_password(pswdLength))