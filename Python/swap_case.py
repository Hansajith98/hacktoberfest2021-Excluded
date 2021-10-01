def swap_case(s):            #Defining a function called swap_case
    res=''
    for letter in s:
        if(letter.islower()):   #Returns true if the characters in the string are in lowercase
            res=res+letter.upper()  #Converting the lowercase characters to uppercase characters
        else:
            res=res+letter.lower() #Converting the uppercase characters to lowercase characters
    return res
s=input("Enter a string:")
swap_case(s)     #Calling the function
    