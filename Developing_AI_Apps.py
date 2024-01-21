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
# Module, Package and Library 
# - they are frequently used terms in python 

# Module
# - python module is a .py file containing Python definitions, statements, functions and classes 
# - module can be imported to other scripts and notebooks 
# Example: 
# module.py
def square(number):
    return number ** 2

def doubler(number):
    return number * 2

# importing 
from module import square, doubler
print("4^2=",square(4))
print("2*4="doubler(4))
# Output
# 4^2 = 16
# 2*4 = 8

# Package 
# - package is collection of python modules into a dictionary (directory) with __innit__.py file (that distingueshes it)
# - when we import module or package, corresponding object is always of type module
# - difference between module and package is only at file system level

# Library
# - collection of packages or single package
# - numpy, PyTorch, Pandas
# - terms package and library are used interchangeably 

# ------------------
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

# exercise 2 (packages)
# Create new module named geometry and add to mymath package
# Create a module name geometry
# Add function named area_of_rectangle that takes length and breadth as input and returns area of rectangle
# Add function named area_of_circle that takes radius as input and returns area of circle
# Modify __init__.py to include this module
# Import and test function area_of_circle from python terminal
# in terminal and mymath directory: 
# touch geometry (make sure you are inside mymath directory)
# inside geomeetry
def area_of_rectangle(length, breadth):
    """
    calculates are of a rectangle 
    """
    return length * breadth

def area_of_circle(radius):
    """
    function calculates are of a circle 
    """
    return 3.14 * (radius ** radius)
# geometry is added, next step is terminal 
# ---------------------------------------------------------------------------- #  
# /home/project$ python3                                                       # 
# Python 3.6.9 (default, Nov 25 2022, 14:10:45)                                # 
# [GCC 8.4.0] on linux                                                         # 
# Type "help", "copyright", "credits" or "license" for more information.       #
# >>> import mymath                                                            # 
# >>> mymath.geometry.area_of_rectangle(16, 8)                                 # 
# 128                                                                          # 
# >>> mymath.geometry.area_of_rectangle(5, 4)                                  # 
# 20                                                                           #
# >>> mymath.geometry.area_of_circle(5)                                        #
# 9812.5                                                                       #
# >>> mymath.geometry.area_of_circle(2)                                        #
# 12.56                                                                        #
# >>> exit()                                                                   #
# ---------------------------------------------------------------------------- #

##########################################################################################################
# Python Libraries and Frameworks for application development 
# - libraries are like toolkits for programming 
# - NumPy = mathematical calculations, Pandas = data manipulation and analysis, Matplotlib = data visualization 

# Python libraries for application development 
# Requests library = HTTP requests simplification 
# BeautifulSoup library = easy to scrape web information from web pages for iterating searching and modyfing
# SQLAlchemy = SQL toolkit and ORM (Object orientatino mapping) tool, gives APP developer full availbility of SQL 
# PyTest = testing framework allows users to create small simple tests

# Framework 
# - predefined structures for application development 
# - frameworks eases development process
# - simplifies debugging process
# - enables more functinoality with less code
# - improves database managment policy (pre build database tools)
# - provides a set of guidelines for application development
# - examples of frameworks: Django, Flask, Web2Py

# Frameworks & Packages
# - framework contains basic flow and architecture of application, which enables you to build complete application
# - Python library is set of packages that perform only specific functionality

##########################################################################################################
# Flask 
# - micro web framework 
# - Flask runs on python (2.2.2 + python 3.7)
# - created in 2004
# - minimal set of dependencies
# - community maintained extensions 

# Main features
# - build in web server
# - has debugger
# - uses standard python logging
# - has build in unit testing 
# - developers can access request and response objects 
# Additional features
# - provides static asset support 
# - provides dynamic templates
# - supports routing (Dynamic URLs, HTTP methods, redirecting)
# - enables error handling 

# Popular extensions 
# - Flask SQLAlchemy (adds support for ORM, sql alchemy to work with SQL objects in python)
# - Flask Mail (provides ability to set up SMTP mail server)
# - Flask Admin (lets you add admin interfaces to flask applications easily)
# - Flask Uploads (allows you to add customized files to your application)

# Django & Flask 
# Flask 
# - Minimal lightweight framework
# - Includes basic dependencies and is extensible
# - Flexible and lets developer take most decisions 
# Django 
# - Full-stack framework
# - Includes everything to create full-stack application 
# - Opinionated and makes most decisions 

##############
# Flask Basic applications 
# app.py file 
from flask import Flask
app = Flask(__name__) # instenciate Flash object as an app 

# adding routes 
# we want to return a message to our client from the server without running tha app 
# use @app decorator to define method 
# the @app takes an path as an argument 
from flask import Flask
app = Flask(__name__)
@app.route('/') # (takes any argument of / and returns html message in bold <b></b>)
def hello world():
    return "<b> My first Flask application in action! </b>"

# Run Flask with arguments
# --app: identifies python file to run (flask automatically looks for file to run in current directory)
# --debug: starts debug mode (development mode) (automatically restarts file on change)
# - in this case the app is stored in file app.py
# FLASK APPLICATION RUNNING IN DEVELOPMENT MODE
# flask --app server --debug run
#  * Serving Flask app 'server'
#  * Debug mode: on
# WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
#  * Running on http://127.0.0.1:5000
# Press CTRL+C to quit
#  * Restarting with stat
#  * Debugger is active!
#  * Debugger PIN: 132-428-810

# Returning JSON 
# 1. JSON method 1.
# return python dictionary and Flask will use JSON module to return JSON to client
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return {"message": "Hello World"}
#OUTPUT: 
"curl -X GET -i -w '\n' localhost:5000" 
HTTP/1.1 200 OK                           # response status 200 OK 
Server: Werkzeug/2.2.2 Python/3.8.0
Date: Wed, 29 Nov 2023 21:48:44 GMT
Content-Type: application/json
Content-Length: 31
Connection: close

{
    "message": "Hello World"
}

# JSON Method 2. 
# - jsonify() method 
# - pass in key value pairs 
# - returns JSON to client 
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return jsonify(message="Hello World")

##############
# Flask basics 
# objectives: 
# 1. create and run Flask server in development mode
# 2. Return JSON from an endpoint
# 3. Understand request object

# Terminal 
# mkdir lab
# - check python version installed 
# python3 --version
# Python 3.6.9
# pip install "Flask--2.2.2"
# install Flask version 2.2.2 (installing flask version 2.2.2)
# 
# Create the Hello World server
# 1. Create server.py file
#     touch /home/project/lab/server.py
# 2. Import Flask module
# from flask import Flask (importing into this file Flask module)
# 3. Create flask app 
# app = Flask(__name__)
# 4. Create the main route
# @app.route("/") (means root file)
# 5. define method for main root URL
# def index():
# 6. Return the “Hello World” message to the client
# return "Hello World"
# server.py file 
from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World"

# to run the server from terminal: 
# flask --app server --debug run (command to run server from terminal)
# (You should now be able to use CURL command on localhost:5000/)
# terminal is already running server, 
# you can use Split Terminal button to split terminal and run following command in second tab
#
# in a new terminal window use: 
# "curl -X GET -i -w '\n' localhost:5000" 
# HTTP/1.1 200 OK
# Server: Werkzeug/2.2.2 Python/3.8.0
# Date: Wed, 29 Nov 2023 21:48:44 GMT
# Content-Type: text/html; charset=utf-8
# Content-Length: 11
# Connection: close

# Hello World
# response from the server 

# Step 2: Return JSON
# You can return number of different content types from @app.route() methods
from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return {"message:": "Hello World"}
# we changed from html format to JSON format (app.route method supports this)
# run the server:
# flask --app server --debug run
# use get method: 
# curl -X GET -i -w '\n' localhost:5000
HTTP/1.1 200 OK
Server: Werkzeug/2.2.2 Python/3.8.0
Date: Wed, 29 Nov 2023 21:52:11 GMT
Content-Type: application/json
Content-Length: 32
Connection: close

{
  "message:": "Hello World"
}

########################
# Request and Response Objects - GET, POST methods
# Flask request object
# Flask response object 
# Request Object, all HTTP calls to Flask contain request object created from Flask.Request class

# Custom routes 
# app.route("/path") decorator defaults to GET HTTP method
# - use methods argument to only allow specific HTTP methods

app.route("/health")
def health():
     return jsonify(dict(status="OK")), 200 # GET method is implicit here

app.route("/health", methods=["GET"])
def heatlh():
     return jsonify(dict(status="OK")), 200 # GET method is explicitly specified

# health route with multiple HTTP method choices
app.route("/health", methods=["GET"])
def heatlh():
    if request.method == "GET": return jsonify(status="OK", method="GET"), 200

    if request.method == "POST": return jsonify(status="OK", method="POST"), 200
# output: 
   # $ curl -X GET http://localhost:5000/health {"method": "GET","status": "OK"}
   # $ curl -X POST http://localhost:5000/health {"method": "POST","status": "OK"}

# - all HTTP calls to Flask contain request object created from Flask contain object from Flask.Request class
# - when client requests resource from Flask server, it is handled by @app.route decorator

##########################
# Practice with Flask 

# cd /home/project 
# mkdir lab 
# cd lab 
from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "hello world"
# above code creates a Flask server and adds a home endpoint “/“ that returns the string hello world
# terminal run: 
#flask --app server --debug run
# flask --app server --debug run
# * Serving Flask app 'server'
# * Debug mode: on
# WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
# * Running on http://127.0.0.1:5000
# Press CTRL+C to quit
# * Restarting with stat
# * Debugger is active!
# * Debugger PIN: 132-428-810

# in order for server to run we need to 

# Terminal window 1 
# 127.0.0.1 - - [31/Dec/2023 05:21:30] "GET / HTTP/1.1" 200 -

# Split terminal window 2
# /home/project$ curl -X GET -i -w '\n' localhost:5000
# HTTP/1.1 200 OK
# Server: Werkzeug/2.2.3 Python/3.11.7
# Date: Sun, 31 Dec 2023 10:21:30 GMT
# Content-Type: text/html; charset=utf-8
# Content-Length: 11
# Connection: close

# hello world
# - Flask automatically sends HTTP 200 OK successful response when you sent back message

#---------------------------------------------------
# 1. Task "Send custom HTTP code back with a touple"
# - reuse server.py file you worked on in last part
# - create new method named no_content with @app.route decorator and URL of /no_content 
# - method does not have any arguments
# - return tuple with JSON message No content found
@app.route('/no_content')
def no_content():
    """Return 'No content found' with a status of 204

    Returns:
        tuple: JSON message and status code 204
    """
    return jsonify({'message': 'No content found'}), 204
# Terminal 1 output/input
# flask --app serer --debug run
#  * Serving Flask app 'server'
#  * Debug mode: on
# WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
#  * Running on http://127.0.0.1:5000
# Press CTRL+C to quit
#  * Restarting with stat
#  * Debugger is active!
#  * Debugger PIN: 132-428-810

# 127.0.0.1 - - [31/Dec/2023 07:21:21] "GET /no_content HTTP/1.1" 204 - # interaction with server 

# Terminal 2 output/input
3 X GET -i -w '\n' localhost:5000/no_contentrl -X
# HTTP/1.1 204 NO CONTENT                 # and HTTP code 204 
# Server: Werkzeug/2.2.3 Python/3.11.7
# Date: Sun, 31 Dec 2023 12:21:21 GMT
# Content-Type: application/json          # we need to have here application/json
# Connection: close

#---------------------------------------------------------------------------------------
# 2. task 
# - create second method named index_explicit with @app.route decorator and URL of /exp
# - method does not have any arguments
# - use make_response() method to create new response, set status to 200
@app.route('/exp') #make response module needs to be imported from Flask in order to run 
def index_explicit():
    resp = make_response({"message": "Hello World"})
    resp.status_code = 200
    return resp

# Terminal 1 output/input
# curl -X GET -i -w '\n' localhost:5000/exp
# HTTP/1.1 200 OK
# Server: Werkzeug/2.2.3 Python/3.11.7
# Date: Sun, 31 Dec 2023 12:33:23 GMT
# Content-Type: application/json
# Content-Length: 11
# Connection: close

# {
#   "message": "Hello World"
# }

# Terminal 2 output/input
# flask --app ser --debug run
#  * Serving Flask app 'server'
#  * Debug mode: on
# WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
#  * Running on http://127.0.0.1:5000
# Press CTRL+C to quit
#  * Restarting with stat
#  * Debugger is active!
#  * Debugger PIN: 132-428-810

127.0.0.1 - - [31/Dec/2023 07:33:23] "GET /exp HTTP/1.1" 200 - # interaction with server 

#---------------------------------------------------------------------------------------
# 3. task
# Process input arguments
# - it is common for clients to pass arguments in the URL. 
# - you will learn how to process arguments in this lab
# - lab provides list of people with their id, first name, last name, and address information in object
# - normally, this information is stored in a database, but you are using a hard coded list for your simple use case 
# - this data was generated with Mockaroo
# - client will send in requests in form of http://localhost:5000?q=first_name 
# = you will create method that will accept first_name as input and return person with that first name

 
# Copy following list to server.py file:
from flask import Flask, make_response
app = Flask(__name__)

data = [
    {
        "id": "3b58aade-8415-49dd-88db-8d7bce14932a",
        "first_name": "Tanya",
        "last_name": "Slad",
        "graduation_year": 1996,
        "address": "043 Heath Hill",
        "city": "Dayton",
        "zip": "45426",
        "country": "United States",
        "avatar": "http://dummyimage.com/139x100.png/cc0000/ffffff",
    },
    {
        "id": "d64efd92-ca8e-40da-b234-47e6403eb167",
        "first_name": "Ferdy",
        "last_name": "Garrow",
        "graduation_year": 1970,
        "address": "10 Wayridge Terrace",
        "city": "North Little Rock",
        "zip": "72199",
        "country": "United States",
        "avatar": "http://dummyimage.com/148x100.png/dddddd/000000",
    },
    {
        "id": "66c09925-589a-43b6-9a5d-d1601cf53287",
        "first_name": "Lilla",
        "last_name": "Aupol",
        "graduation_year": 1985,
        "address": "637 Carey Pass",
        "city": "Gainesville",
        "zip": "32627",
        "country": "United States",
        "avatar": "http://dummyimage.com/174x100.png/ff4444/ffffff",
    },
    {
        "id": "0dd63e57-0b5f-44bc-94ae-5c1b4947cb49",
        "first_name": "Abdel",
        "last_name": "Duke",
        "graduation_year": 1995,
        "address": "2 Lake View Point",
        "city": "Shreveport",
        "zip": "71105",
        "country": "United States",
        "avatar": "http://dummyimage.com/145x100.png/dddddd/000000",
    },
    {
        "id": "a3d8adba-4c20-495f-b4c4-f7de8b9cfb15",
        "first_name": "Corby",
        "last_name": "Tettley",
        "graduation_year": 1984,
        "address": "90329 Amoth Drive",
        "city": "Boulder",
        "zip": "80305",
        "country": "United States",
        "avatar": "http://dummyimage.com/198x100.png/cc0000/ffffff",
    }
]

# Let's confirm that data has been copied to file
@app.route("/data")
def get_data():
    try:
        if data and len(data) > 0:
            return {"message": f"Data of length {len(data)} found"}
        else:
            return {"message": "Data is empty"}, 500
    except NameError:
        return {"message": "Data not found"}, 404
    
# - above code simply checks if variable data exits 
# - if it does not, NameError is raised and HTTP 404 is returned
# - if data exists and is empty, HTTP 500 is returned
# - if data exists and is not empty, HTTP 200 success message is returned

# Terminal 1 output/input

# flask --app server --debug run
#  * Serving Flask app 'server'
#  * Debug mode: on
# WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
#  * Running on http://127.0.0.1:5000
# Press CTRL+C to quit
#  * Restarting with stat
#  * Debugger is active!
#  * Debugger PIN: 396-313-000
# 127.0.0.1 - - [01/Jan/2024 11:03:17] "GET /data HTTP/1.1" 200 -


# Terminal 2 output/input 

# curl -X GET -i -w '\n' localhost:5000/data
# HTTP/1.1 200 OK
# Server: Werkzeug/2.2.3 Python/3.11.7
# Date: Mon, 01 Jan 2024 16:03:17 GMT
# Content-Type: application/json
# Content-Length: 42
# Connection: close

# {
#   "message": "Data of length 5 found"
# }

# - create method called name_search with @app.route decorator
# - this method should be called when a client requests for the /name_search URL
# - method will not accept any parameter, however, will look for argument q in incoming request URL
# - this argument holds first_name client is looking for
# method returns:
# - person information with status of HTTP 400 if first_name is found in data
# - message of Invalid input parameter with status of HTTP 422 if argument q is missing from request
# - message of Person not found with status code of HTTP 404 if person is not found in data
from flask import request

@app.route("/name_search")
def name_search():
    """find a person in the database

    Returns:
        json: person if found, with status of 200
        404: if not found
        422: if argument q is missing
    """
    query = request.args.get("q")

    if not query:
        return {"message": "Invalid input parameter"}, 422

    for person in data:
        if query.lower() in person["first_name"].lower():
            return person

    return ({"message": "Person not found"}, 404)

# Terminal 1 output/input

# flask --app server --debug run
#  * Serving Flask app 'server'
#  * Debug mode: on
# WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
#  * Running on http://127.0.0.1:5000
# Press CTRL+C to quit
#  * Restarting with stat
#  * Debugger is active!
#  * Debugger PIN: 396-313-000
# 127.0.0.1 - - [01/Jan/2024 11:17:32] "GET /name_search?q=Abdel HTTP/1.1" 200 -
# 127.0.0.1 - - [01/Jan/2024 11:19:43] "GET /name_search HTTP/1.1" 422 -

# Terminal 2 output/input

# curl -X GET -i -w '\n' "localhost:5000/name_search?q=Abdel"
# HTTP/1.1 200 OK
# Server: Werkzeug/2.2.3 Python/3.11.7
# Date: Mon, 01 Jan 2024 16:17:32 GMT
# Content-Type: application/json
# Content-Length: 295
# Connection: close

{
  "address": "2 Lake View Point",
  "avatar": "http://dummyimage.com/145x100.png/dddddd/000000",
  "city": "Shreveport",
  "country": "United States",
  "first_name": "Abdel",
  "graduation_year": 1995,
  "id": "0dd63e57-0b5f-44bc-94ae-5c1b4947cb49",
  "last_name": "Duke",
  "zip": "71105"
}

# Next, test that the method returns HTTP 422 if the argument q is missing:

# curl -X GET -i -w '\n' "localhost:5000/name_search"
# HTTP/1.1 422 UNPROCESSABLE ENTITY
# Server: Werkzeug/2.2.3 Python/3.11.7
# Date: Mon, 01 Jan 2024 16:19:43 GMT
# Content-Type: application/json
# Content-Length: 43
# Connection: close

{
  "message": "Invalid input parameter"
}

#---------------------------------------------------------------------------------------
# 4. Task
# Add dynamic URLs
# - important part of back-end programming is creating APIs
# - API is contract between provider and user 
# - it is common to create RESTful APIs that can be called by front end or other clients 
# - in REST based API, resource information is sent as part of request URL
# For example, with your resource or persons, client can send following request:
GET http://localhost/person/unique_identifier
# - this request asks for person with unique identifier

# 4.1 Create GET /count endpoint
# - add @app.get() decorator for /count URL
# - define count function that simply returns number of items in data list
  @app.route("/count")
def count():
    try:
        return {"data count": len(data)}, 200
    except NameError:
        return {"message": "data not defined"}, 500
    
# 
    
# Terminal 1 input/output
flask --app server --debug run
 * Serving Flask app 'server'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 396-313-000
127.0.0.1 - - [01/Jan/2024 11:53:23] "GET /count HTTP/1.1" 200 -

# Terminal 2 input/output
curl -X GET -i -w '\n' "localhost:5000/count"
HTTP/1.1 200 OK
Server: Werkzeug/2.2.3 Python/3.11.7
Date: Mon, 01 Jan 2024 16:53:23 GMT
Content-Type: application/json
Content-Length: 22
Connection: close

{
  "data count": 5
}

# 4.2 Create GET /person/id endpoint
# - create new endpoint for http://localhost/person/unique_identifier 
# - method should be named find_by_uuid, It should take argument of type UUID and return person JSON if found
# - if  person is not found, method should return 404 with message of person not found
# - finally, client should only be able to call this method by passing valid UUID type id

# - if you pass in invalid UUID, server should return 404 message

# - pass in valid UUID that does not exist in data list
# - method should return 404 with message of person not found

# terminal 1 output/input
flask --app server --debug run
 * Serving Flask app 'server'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 396-313-000
127.0.0.1 - - [01/Jan/2024 11:53:23] "GET /count HTTP/1.1" 200 -
127.0.0.1 - - [01/Jan/2024 11:57:56] "GET /person/66c09925-589a-43b6-9a5d-d1601cf53287 HTTP/1.1" 200 -
127.0.0.1 - - [01/Jan/2024 11:59:34] "GET /person/not-a-valid-uuid HTTP/1.1" 404 -
127.0.0.1 - - [01/Jan/2024 12:02:20] "GET /person/11111111-589a-43b6-9a5d-d1601cf51111 HTTP/1.1" 404 -

# terminal 2 output/input
curl -X GET -i localhost:5000/person/66c09925-589a-43b6-9a5d-d1601cf53287
HTTP/1.1 200 OK
Server: Werkzeug/2.2.3 Python/3.11.7
Date: Mon, 01 Jan 2024 16:57:56 GMT
Content-Type: application/json
Content-Length: 294
Connection: close

{
  "address": "637 Carey Pass",
  "avatar": "http://dummyimage.com/174x100.png/ff4444/ffffff",
  "city": "Gainesville",
  "country": "United States",
  "first_name": "Lilla",
  "graduation_year": 1985,
  "id": "66c09925-589a-43b6-9a5d-d1601cf53287",
  "last_name": "Aupol",
  "zip": "32627"
}

# 
curl -X GET -i localhost:5000/person/not-a-valid-uuid
HTTP/1.1 404 NOT FOUND
Server: Werkzeug/2.2.3 Python/3.11.7
Date: Mon, 01 Jan 2024 16:59:34 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 207
Connection: close

<!doctype html>
<html lang=en>
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.</p>

# 
curl -X GET -i localhost:5000/person/11111111-589a-43b6-9a5d-d1601cf51111
HTTP/1.1 404 NOT FOUND
Server: Werkzeug/2.2.3 Python/3.11.7
Date: Mon, 01 Jan 2024 17:02:20 GMT
Content-Type: application/json
Content-Length: 36
Connection: close

{
  "message": "person not found"
}

# 4.3 Task 
# Create DELETE /person/id endpoint
# - implement DELETE endpoint to delete person resource
# - create new endpoint for DELETE http://localhost/person/unique_identifier
# - method should be named delete_by_uuid, it should take in argument of type UUID and delete person from data listwith that id 
# - if person is not found, method should return 404 with message of person not found
# - finally, client (curl) should call this method by passing valid UUID type id

# Test the DELETE /person/uuid URL by calling the endpoint.
# curl -X DELETE -i localhost:5000/person/66c09925-589a-43b6-9a5d-d1601cf53287

You can now use the count endpoint you added earlier to test if the number of persons has reduced by one.
curl -X GET -i localhost:5000/count

If you pass an invalid UUID, the server should return a 404 message.
curl -X DELETE -i localhost:5000/person/not-a-valid-uuid

Finally, pass in a valid UUID that does not exist in the data list. The method should return a 404 with a message of person not found.
curl -X DELETE -i localhost:5000/person/11111111-589a-43b6-9a5d-d1601cf51111

# Terminal 1 output/input
127.0.0.1 - - [01/Jan/2024 12:09:21] "DELETE /person/66c09925-589a-43b6-9a5d-d1601cf53287 HTTP/1.1" 200 -
127.0.0.1 - - [01/Jan/2024 12:09:41] "GET /count HTTP/1.1" 200 -
127.0.0.1 - - [01/Jan/2024 12:09:52] "DELETE /person/not-a-valid-uuid HTTP/1.1" 404 -
127.0.0.1 - - [01/Jan/2024 12:10:01] "DELETE /person/11111111-589a-43b6-9a5d-d1601cf51111 HTTP/1.1" 404 -

# Terminal 2 output/input 
curl -X DELETE -i localhost:5000/person/66c09925-589a-43b6-9a5d-d1601cf53287
HTTP/1.1 200 OK
Server: Werkzeug/2.2.3 Python/3.11.7
Date: Mon, 01 Jan 2024 17:09:21 GMT
Content-Type: application/json
Content-Length: 56
Connection: close

{
  "message": "66c09925-589a-43b6-9a5d-d1601cf53287"
}

curl -X GET -i localhost:5000/count
HTTP/1.1 200 OK
Server: Werkzeug/2.2.3 Python/3.11.7
Date: Mon, 01 Jan 2024 17:09:41 GMT
Content-Type: application/json
Content-Length: 22
Connection: close

{
  "data count": 4
}

curl -X DELETE -i localhost:5000/person/not-a-valid-uuid
HTTP/1.1 404 NOT FOUND
Server: Werkzeug/2.2.3 Python/3.11.7
Date: Mon, 01 Jan 2024 17:09:52 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 207
Connection: close

<!doctype html>
<html lang=en>
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.</p>
theia@theia-matuschmel13:/home/project$ curl -X DELETE -i localhost:5000/person/11111111-589a-43b6-9a5d-d1601cf51111
HTTP/1.1 404 NOT FOUND
Server: Werkzeug/2.2.3 Python/3.11.7
Date: Mon, 01 Jan 2024 17:10:01 GMT
Content-Type: application/json
Content-Length: 36
Connection: close

{
  "message": "person not found"
}

#---------------------------------------------------------------------------------------
# Task 5.
# Add error handlers
# - add application level global handlers to handle errors like 404(not found) and 500 (internal server error) 
# - recall from video that Flask makes it easy to handle these global error handlers using the errorhandler() decorator
# - if you make an invalid request to server now, Flask will return HTML page with 404 error 
# Something like this:

curl -X POST -i -w '\n' http://localhost:5000/notvalid
HTTP/1.1 404 NOT FOUND
Server: Werkzeug/2.2.2 Python/3.7.16
Date: Sun, 01 Jan 2023 23:21:54 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 207
Connection: close

<!doctype html>
<html lang=en>
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server. If you entered the URL manually, please check your spelling and try again.</p>

# - this is great, but you want to return JSON response for all invalid requests

# - create method called api_not_found with @app.errorhandler decorator
# - this method will return message of API not found with HTTP status code of 404 whenever client requests URL that does not lead to any endpoints defined by server

@app.errorhandler(404)
def api_not_found(error):
    return {"message": "API not found"}, 404

# Terminal output/input 1 
127.0.0.1 - - [01/Jan/2024 12:38:03] "POST /notvalid HTTP/1.1" 404 -
127.0.0.1 - - [01/Jan/2024 12:39:13] "POST /notvalid HTTP/1.1" 404 -

# Terminal output/input 2
curl -X POST -i -w '\n' http://localhost:5000/notvalid
HTTP/1.1 404 NOT FOUND
Server: Werkzeug/2.2.3 Python/3.11.7
Date: Mon, 01 Jan 2024 17:39:13 GMT
Content-Type: application/json
Content-Length: 33
Connection: close

{
  "message": "API not found"
}

#################################################################################################
# Deploying Web Apps using Flask 
# - Flask is a microframework for creating web applications 
# - supports CRUD
# Basic structure of Flask application 
# CREATE = POST/PUT method ( - can be used to create user, POST = creates object on every request, PUT = creates object or data only on first request and updates data on aditional requests)
# READ   = GET method ( - get data from server)
# UPDATE = UPDATE method ( - update existing data or objects )
# DELETE = DELETE method ( - delete existing data or objects )

# How to create a web application using flask 
# 1. pip install flask 
# 2. import flask
# 3. instantiate flask 
# 4. run the app 

# Hello World Application example
# in terminal pip install flask 
# touch FlaskAppExample
# cd FlaskAppExample
from flask import Flask
app = Flask("My first Application") # app is reference name 

@app.route('/') # define a root and method that will be invoked when this route is accessed
                # no GET, POST is specified, IF neither is specified GET is requested by defaulet
def hello() :   # method specified, will be invoked when system access the API endpoint and it will be runned 
    return 'Hello World:' # this will be returned when API is accessed

if __name__ == "__main__": # this web application will run only if __name__ equals __main__
    app.run(debug-True)

# Rendering templates example 
# Sample FLASK APPLICATION 
from flask import Flask, render_template, request # ( - request = to handle incoming request, render_template = to handle render requests)
app = Flask("My first Application") # 

@app.route('/sample') # /sample = render static HTML page, image is sourced from static directory
def getSampleHtml() : # method 
    return render_template ('sample.html') # method calls render_template 

@app.route('/user/ < username >', methods=['GET']) # < username > = parameter 
    def greetUser(username): 
    reutrn render_template("result.html", username=username)

@app.route('user', methods=['GET'])
def greetUserBasedOnReq():
    username = request.args.get("username")
    return render_template("result.html", username=username)

if __name__ == "__main__":
    app.run(debug=True)

#################################################################################################
# Decorators in Flask
# - decorators help in annotating methods and tell what particular method is meant for

# Method decorators
# - python code all output to be in JSON format

def jsonify_decorator(function):
    def modifyOutput():
        return {"output":function()}
    return modifyOutput

@jsonify_decorator
def hello():
    return 'hello world'

@jsonify_decorator
def add():
    num1 = input("Enter a number - ")
    num2 = input("Enter another number - ")
    return int(num1)+int(num2)
print(hello())
print(add())

# output of above python code will be:
# {'output': 'hello world'}
# Enter a number - 73
# Enter another number - 87 
# {'output': 160}

# - as can be seen method call has been wrapped with decorator
# - coder has free will to choose name of decorator, here it is jsonify_decorator

# - method decorator is also referred to as wrapper, which wraps output of function, that it decorates
# - in above code sample, jsonify-decorator is decorator method
# - we have added this decorator to hello() and add()
# - output of these method calls will now be wrapped and decorated with jsonify_decorator

##################
# Route decorators 
# - when you visit any domain you have root and then have other end-points you can access
# - examples below

# https://mydomain.com/
# https://mydomain.com/about
# https://mydomain.com/register

# to define these endpoints in Python we use what we call Route Decorators
@app.route("/")
def home():
    return "Hello World!"
# @app.route(“/“) is Python decorator that Flask provides to assign URLs in our app to functions easily 
# You can easily tell that decorator is telling our @app that whenever user visits our application’s domain, in our case, execute home() function

# - we can handle multiple routes with single function by just stacking additional route decorators above method which should be invoked when route is called
# - following is valid example of serving same “Hello World!” message for 3 separate routes:
@app.route("/")
@app.route("/home")
@app.route("/index")
def home():
    return "Hello World!"
# - route decorators also take method as second parameter, which can be set to type of HTTP methods, route will support

# - route decorator can also be more specific
# - to get details of user whose userId is U0001, you may go to http://mydomain.com/userdetails/U0001
# - it doesn’t make sense to define different route for each user you may be dealing with
# - in such cases, we define route like this
@app.route("/userdetails/<userid>")
def getUserDetails(userid):
    return "User Details for  "+userid

