#1st task  i am Muhammad Khalid Anwar

#1 print Hello world
print("Hello, World!")


#2 Print multiple items in one statement
name = "khalid" 
age = 24
city = "Akora Khattak"
print("Name: ",name ," Age: ",age," city: ",city)

#3 Print using escape characters 

print (" Welcome to Python! \n Let's learn coding.")


#4 Print quotes inside a string

print( 'He said, "Python is amazing!"')

#5 Print a pattern using stars 
for i in range(1,6):
    for j in range(0,i):
        print("*", end="")
    print("")

# 6  Formatted string output using f-strings 
name = input("enter is your Name ")
age = int(input("enter is your age "))

print("Hello, my name is ",name ," and I am ",age," Years old")

# 7 Table

number =int(input("Please enter a number: "))

for i in range(1,11,1):
    print(number,"x",i,"=",i*number)
    

#8 Align text with padding
print(f"{'Apple' : <10}  {'Banana': ^10}  {'Mango': >10}" )
print()

# 9 Output the result of a simple calculation

a = 5
b = 12
print(a," + ",b," = ",a+b)

#10. Print a formatted receipt 
print("- Item names \n- Quantity \n- Price\n- Total")




#                       Basic Keyword Exercises (1–10)




#1. Print a list of some common Python keywords.
print(
    "i)  if \nii) else \niii) match \niv)  try \nv)   catch \nvi)  input \nvii) length \nviii) filter \nix)   while \n x)   for "
)


#2. Print three keywords used for conditional statements in Python
x=int(input("Please enter x : "))
y=int(input("Please enter y : "))

if(x>y):
    print(f"{x} is greater than {y}  ")
elif(y<x):
    print(f"{y} is greater than {x}  ")
else:
    print(f"{x} is equal to {y}  ") 

#                           Or

print("Conditional Keywords:")
print("if, else, elif")

# 3. Print three keywords used in loops
print("Loop Keywords:")
print("for, while, break")

# 4. Print the Boolean keywords in Python
print("Boolean Keywords:")
print("True, False, and, or, not, is")

# 5. Manually sort and print five keywords alphabetically
print("Five Alphabetically Sorted Keywords:")
keywords = ["while", "if", "else", "return", "for"]
keywords.sort()
print(keywords)

# 6. Print keywords that represent constant values
print("Constant Value Keywords:")
print("True, False, None")


# 7. Print keywords used for flow control
print("Flow Control Keywords:")
print("break, continue, pass")

# 8. Create a print statement that uses the word 'if'
print("i am using  'if' is used to check conditions in Python")

# 9. Make a table using print
print("Keyword     | Use")
print("------------|----------------------")
print("if          | Conditional check")
print("while       | Loop")
print("break       | Exit loop")


# 10. Print all capital letter versions of 5 keywords
print("Capital Letter Versions:")
print("IF, ELSE, WHILE, BREAK, PASS")


#              Intermediate Conceptual Challenges (11–15)

# 11. Make a list (manually) of 10 Python keywords and print it
keywords_list = ['if', 'else', 'elif', 'for', 'while', 'break', 'continue', 'def', 'class', 'return']
print("10 Python Keywords:", keywords_list)

# 12. Print 5 keywords that cannot be used as variable names
print("Keywords that cannot be used as variable names:\n if, while, for, class, def")

# 13. Print a sentence that uses 3 keywords (in plain text)
print("Python uses if, else, and for to control the flow of code.\n")


# 14. Group and print keywords into 3 categories
conditional_keywords = ['if', 'else', 'elif']
looping_keywords = ['for', 'while', 'break', 'continue']
boolean_keywords = ['True', 'False', 'None', 'and', 'or', 'not', 'is']

print("Grouped Python Keywords:")
print("Conditional:", conditional_keywords)
print("Looping:", looping_keywords)
print("Boolean:", boolean_keywords)

# 15. Write a short explanation of why we can't use keywords as variable names
print("We can't use Python keywords as variable names because they have special meanings in the language.")








# 1. Welcome message
name = input("Enter your name: ")
print(f"Welcome, {name}!")


# 2. Sum of two numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Sum:", num1 + num2)


# 3. Favorite color
color = input("What is your favorite color? ")
print(f"Your favorite color is {color}.")


# 4. User's age
#when we use f in print statment then we can't write a , to add value
age = int(input("Enter your age: "))
print(f"You are {age} years old.")

# 5. City and country
city = input("Enter your city: ")
country = input("Enter your country: ")
print(f"You live in {city}, {country}.")



# 6. Difference of two numbers
num3 = int(input("Enter first number: "))
num4 = int(input("Enter second number: "))
print("Difference:", num3 - num4)
#look here if i use f in print then i will write code like this
# print(f"Difference: {num3-num4}")


# 7. Word to uppercase
word = input("Enter a word: ")
print(f"befor uppercase {word} after uppercase {word.upper()}")

# 8. Character count in sentence
sentence = input("Enter a sentence: ")
print("Character count:", len(sentence))


# 9. School name message
school = input("Enter your school name: ")
print(f"I study at {school}.")


# 10. Full name from first and last name
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print("Full name:", first_name + " " + last_name)


# 11. Age after 5 years
current_age = int(input("Enter your age: "))
print("Your age after 5 years will be:", current_age + 5)


# 12. Product of two numbers
num5 = int(input("Enter first number: "))
num6 = int(input("Enter second number: "))
print("Product:", num5 * num6)


# 13. Name and hobby
person_name = input("Enter your name: ")
hobby = input("Enter your hobby: ")
print(f"{person_name} likes {hobby}.")


#                               New Chapter



# 1. Convert a string "10" to an integer and add 5 to it
a="10"
print(int(a) + 5)  # Output: 15 but this convter is not paramanat ok 


# 2. Convert a string float to a float
a="7.9"
print(float(a))



# 3. Convert an integer to string and concatenate
print("The number is " + str(5))


# 4. Convert float 3.14 to int
print(int(3.14))  # Output: 3


# 5. Convert integer 1 to boolean
print(bool(1))  # Output: True


# 6. Convert string "False" to boolean
print(bool("False"))  # Output: True (non-empty string is True)


# 7. Take string input, convert to int, multiply by 2
num_str = input("Enter a number as string: ")
print("Multiplied by 2:", int(num_str) * 2)


# 8. Take float input, convert to int, print both
float_input = float(input("Enter a floating number: "))
int_converted = int(float_input)
print("Original:", float_input)
print("Converted to int:", int_converted)

# 9. Convert a number to a string and check type
num = 100
num_str = str(num)
print("Converted string:", num_str)
print("Type:", type(num_str))


# Bal Question number 10 da ok zaka pdf ke missing da 


# 11. Take two numbers as input and add as integers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum as integers:", a + b)

# 12. Convert string "25.5" to float and int
#string is not covert into int it show error
#so we 1st str convert into Float then Float into Int
val = "25.5"
val_float= float(val)
val_int= int(val_float)
print("float",type(val_float),val_float)
print("int",type(val_int),val_int)



# 13. Try converting "123abc" to int
a="123abc"
print(int(a)) #Output : ValueError: invalid literal for int() with base 10: '123abc'


# 14. Check if input is numeric and convert
s = input("Enter something to check if numeric: ")
if s.isnumeric():
    print("As int:", int(s))
else:
    print("Not numeric.")


# 15. Convert float to int and then to string
f = 9.99
i = int(f)
s = str(i)
print("Float:", f)
print("Int:", i)
print("String:",s)


#                       New Chapter


# 1. Print a string literal
print("Learning Python is fun!")

# 2. Create and print an integer and a float literal
int_literal = 10
float_literal = 3.14
print(int_literal, float_literal)


# 3. String literal using single and double quotes
single_quote = 'Hello'
double_quote = "World"
print(single_quote)
print(double_quote)


# 4. Boolean literal
print(True,",", False)


# 5. Create a variable with value None
x = None
print(x) # Output is : None

# 6. Print the type of each literal
print(type("Hello"))  # str
print(type(10))       # int
print(type(3.5))      # float
print(type(True))     # bool
print(type(None))     # NoneType



# 7. String literal for a sentence
print("Python’s simplicity is powerful.")


# 8. Concatenate two strings
str1 = "Python is"
str2 = " awesome!"
print(str1 + str2)

# 9. Mixed list: number, string, boolean
mixed_list = [42, "Hello", True, 34.5]
print(mixed_list)


# 10. Multi-line string using triple quotes
print("""This is
a multi-line
string literal.""")

# 11. Output of comparison with None
print(None == 0)      # False
print(None == False)  # False


