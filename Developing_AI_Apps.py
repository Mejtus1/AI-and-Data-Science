# Python Conventions

# PEP-8 
# recommends using spaces instead of tabs for intendation 
# different IDEs interprent tab as 3 spaces others as 4 which can lead to non-uniformity in code
# guideline is to use 4 spaces for every tab in code 

def function1():
.... statement
.... statement # using 4 spaces instead of tabs 
#----------------------------------------------
def function():                   def function()
    statement1                       statement1
    statement2                       statement2
                                  class UserClass():
class UserClass():
# left side represents correct definition with blank space before class definition 
#----------------------------------------------
# Using spaces around operators and commas 
a =b+callable      # NOT 
k=function_1(a,b)  # RIGHT 
D=[1,2,3,4]        #

a = b + callable # Right format 
k = function_1(a,b)
D = [1, 2, 3, 4]


# Using functions for blocks of codes
# - create separate functions for functionalities
# - Increases execution speed of code
# - Supports reuse of code block 

#    RIGHT FORMAT                           WRONG FORMAT
def function_1(a, b):                       if a > b:
    if a > b: 
        c = c + 5                           c = c + 5
    else:                                   else:
        c = c - 3                           c = c - 3 
    return c

c = function_1(a, b)
# Function can be reused and recalled which saves time and readability 

# Naming functions and files 
# - use lowercase with underscores
# S = compSurfaceRadiation() [javascript file naming (camel case)]
# S = comp_surface_radiation() [python naming convention]
# 
# Python packages naming convention
# - underscores are discouraged 
# my_package = X, mypackage = good naming convention 

# Naming Classes using CamelCase
# - coding convention that helps distinguish between classes and functions 
# class Lam_squirrel_Cage: = X, class LamSquirrelCage: - good naming convention 

# Naming constants
# Capitalize all words
# Separate words with underscores
#    WRONG FORMAT                   RIGHT FORMAT
# maxfile
# Max_File_Upload_Size                MAX_FILE_UPLOAD_SIZE
# maxfileuploadsize 

# Static code analysis 
# - Commonly used to manage compliance
# - Evaluates style compliance without executing code
# - Find issues such as: Programming errors, Coding standard violations, 
# Undefined values, Syntax violations, Security vulnerabilities
# PyLint can be used to check Python code with guidelines of PEP8 


# Static Code Analysis
# - install pylint package
# - run Static Code Analysis on python program
# - check compliance score of python program
# - fix common mistakes and improve compliance score

# 1. install pylint package
pip3 install pylint==2.11.1

# 2. Create a new file named sample1.py
def add(number1, number2):
    return number1 + number2

num1 = 4
num2 = 5
total = add(num1, num2)
print("The sum of {} and {} is {}".format(num1, num2, total))
# saved as sample1.py

# 3. in terminal run pylint sample1.py
# - pylint goes through every line of code and gives list all non-compliant lines
# - also gives compliance score (10 is max)

# ************* Module sample1
# sample1.py:7:0: C0304: Final newline missing (missing-final-newline)
# sample1.py:1:0: C0114: Missing module docstring (missing-module-docstring)
# sample1.py:1:0: C0116: Missing function or method docstring (missing-function-docstring)
# sample1.py:4:0: C0103: Constant name "num1" doesn't conform to UPPER_CASE naming style (invalid-name)
# sample1.py:5:0: C0103: Constant name "num2" doesn't conform to UPPER_CASE naming style (invalid-name)
# sample1.py:6:0: C0103: Constant name "total" doesn't conform to UPPER_CASE naming style (invalid-name)
# sample1.py:7:6: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
# ------------------------------------
# Your code has been rated at -1.67/10

# 4. Correct mistakes identified by pylint
def add(number1, number2):
    return number1 + number2

NUM1 = 4
num2 = 5
total = add(NUM1, num2)
print("The sum of {} and {} is {}".format(NUM1, num2, total))

# 5. in terminal run pylint sample1.py 
pylint sample2.py
# Module sample2
# sample2.py:7:0: C0304: Final newline missing (missing-final-newline)
# sample2.py:1:0: C0114: Missing module docstring (missing-module-docstring)
# sample2.py:1:0: C0116: Missing function or method docstring (missing-function-docstring)
# sample2.py:5:0: C0103: Constant name "num2" doesn't conform to UPPER_CASE naming style (invalid-name)
# sample2.py:6:0: C0103: Constant name "total" doesn't conform to UPPER_CASE naming style (invalid-name)
# sample2.py:7:6: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
# -----------------------------------
# Your code has been rated at 0.00/10

# 6. correcting mistakes
'''
Function to returnt he addituion of two numbers
'''

def add(number1, number2):
    '''
    Returns the addition of number1 and number2 inputs
    '''
    return number1 + number2

NUM1 = 4
NUM2 = 5
TOTAL = add(NUM1, NUM2)
print("The sum of {} and {} is {}".format(NUM1, NUM2, TOTAL))

# ************* Module sample2
# sample2.py:14:6: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
# ------------------------------------------------------------------
# Your code has been rated at 8.33/10 (previous run: 6.67/10, +1.67)

