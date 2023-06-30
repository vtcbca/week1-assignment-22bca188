#7.Write a python script to enter any string, replace vowel with its position number.
#For Example: input: Amit
#             output:0m2t

def vowelchange(s):
    b=''
    a=('a','e','i','o','u','A','E','I','O','U')
    for index,j in enumerate(s):
        if(j in a):
            b+=str(index)
        else:
            b+=j
    
    print(f"The string '{s}' after change is '{b}' ")

s=input("Enter a string:")
vowelchange(s)
