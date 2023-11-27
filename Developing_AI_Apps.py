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

##########################################################################################################
# Unit testing 
# - method to validate if units of code are operating as designed
# - unit is smaller, testable part of application
# - to unit test we will use unittest.py library (installed Python module providing framework containing test functionality)

# - unit testing through publishing to the production code base
# - 1. first phase (test unit on your local system)
# - 2. If test fails, you will determine reason for failure and fix issue
# - 3. test again unit
# - 4. After unit test passes, you will need to test unit in server environment, 
# such as continuous integration continuous delivery (or CI/CD) test server

# unit file 
# mymodule.py file 
def square(number):
    return number ** 2

def doubler(number:)
    return number * 2 

unit test file 
# test_mymodule.py
import unittest # import unittest library

from mymodule import square, doubler #import from mymodule.py functions square and doubler
class TestMyModule(unittest.TestCase): # build unittesting class to call test from single calss object 
    def test_square(self):
        self.assertEqual(square(2), 4) # assertion methods

    def test_doubler(self):
        self.assertEqual(double(0), 0) # assertion methods 
       
if __name__ == '__main__':
      unittest.main()


# unit test exercise 
# mymodule.py
def square(number):
    """
    This function returns the square of a given number
    """
    return number ** 2

def double(number):
    """
    This function returns twice the value of a given number
    """
    return number * 2

# Write the unit tests for square function
# When 2 is given as input the output must be 4.
# When 3.0 is given as input the output must be 9.0.
# When -3 is given as input the output must not be -9.

# Write the unit tests for double function
# When 2 is given as input the output must be 4.
# When -3.1 is given as input the output must be -6.2.
# When 0 is given as input the output must be 0.

# test_mymodule.py
# import unittest

from mymodule import square, double

class TestSquare(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(square(2), 4) # test when 2 is given as input the output is 4.
        self.assertEqual(square(3.0), 9.0)  # test when 3.0 is given as input the output is 9.0.
        self.assertNotEqual(square(-3), -9)  # test when -3 is given as input the output is not -9.
        

class TestDouble(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(double(2), 4) # test when 2 is given as input the output is 4.
        self.assertEqual(double(-3.1), -6.2) # test when -3.1 is given as input the output is -6.2.
        self.assertEqual(double(0), 0) # test when 0 is given as input the output is 0.
        
unittest.main()

# python3 test_mymodule.py 
# ..
# ----------------------------------------------------------------------
# an 2 tests in 0.000s
# 
# OK


# exercise 2
# Write test cases for these scenarios
# When 2 and 4 are given as input the output must be 6.
# When 0 and 0 are given as input the output must be 0.
# When 2.3 and 3.6 are given as input the output must be 5.9.
# When the strings ‘hello’ and ‘world’ are given as input the output must be ‘helloworld’.
# When 2.3000 and 4.300 are given as input the output must be 6.6.
# When -2 and -2 are given as input the output must not be 0. (Hint : Use assertNotEqual)

# mymodule2.py
def add(a,b):
    """
    This function returns the sum of the given numbers
    """
    return a + b

# test_mymodule2.py
import unittest

from mymodule import add

class TestAdd(unittest.TestCase):
    def test1(self):
        self.assertEqual(add(2,4), 6)
        self.assertEqual(add(0,0), 0)
        self.assertEqual(add(2,4), 6)
        self.assertEqual(add('hello','world'), 'helloworld')
        self.assertEqual(add(2.3000,4.300), 6.6)
        self.assertNotEqual(add(-2,-2), 0)

unittest.main()
# python3 test_mymodule.py 
# .
# ----------------------------------------------------------------------
# Ran 1 test in 0.000s
# 
# OK

##########################################################################################################
# Packaging 
# 

# Packaging exercise 
# 1. Create package 
# Create new folder 
# in VSC -> File -> New folder -> mymath
# Create module basic.py
# in VSC -> File -> New File -> basic.py (make sure you are in mymath directory) otherwise mv basic.py mymath/
# inside basic.py write:
def square(number):
    """
    This function returns the square of a given number
    """
    return number ** 2

def double(number):
    """
    This function returns twice the value of a given number
    """
    return number * 2

def add(a, b):
    """
    This function returns the sum of given numbers
    """
    return a + b
# Create new module stats.py
# File -> New File -> stats.py (make sure you are in mymath directory)
# inside stats.py write
def mean(numbers):
    """
    This function returns the mean of the given list of numbers
    """
    return sum(numbers)/len(numbers)

def median(numbers):
    """
    This function returns median of the given list of numbers
    """
    numbers.sort()
   
    if len(numbers) % 2 == 0:
       median1 = numbers[len(numbers) // 2]
       median2 = numbers[len(numbers) // 2 - 1]
       mymedian = (median1 + median2) / 2
    else:
       mymedian = numbers[len(numbers) // 2]
    return mymedian
# create new file __init__.py
# File -> New File -> __init__.py (make sure you are in mymath directory)
# directory mymath should look like this mymath
#    mymath
#    mymath/__init__.py
#    mymath/basic.py
#    mymath/statistics.py

# Verify package 
# Terminal -> python3 (invoke python3 and load pyhton interpreter)
# at python prompt type: import mymath (if runs without errors it was successfully loaded)
#  At python prompt type mymath.basic.add(3,4)
# You should see an output 7 on screen
# At python prompt type mymath.stats.mean([3,4,5])
# You should see an output 4.0 on screen
# Type exit() to quit python interpreter
# ------------------------------------------------------------------------- #
# python3                                                                   #
# Python 3.6.9 (default, Nov 25 2022, 14:10:45)                             #
# [GCC 8.4.0] on linux                                                      # 
# Type "help", "copyright", "credits" or "license" for more information.    #
# >>> import mymath                                                         # 
# >>> mymath.basic.add(3,4)                                                 # 
# 7                                                                         # 
# >>> mymath.stats.mean([3,4,5])                                            # 
# 4.0                                                                       #
# >>> exit()                                                                #
# ------------------------------------------------------------------------- #