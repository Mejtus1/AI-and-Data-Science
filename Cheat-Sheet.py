#-------------------------------------------------------------------------------------------------------
Python Basics

# Comments	
# Comments are lines of text that are ignored by Python interpreter when executing code<./td>	
# This is a comment

#-------------------------------------------------------------------------------------------------------

# Concatenation	
# Combines (concatenates) strings.	
# Syntax:
concatenated_string = string1 + string2 
# Example:
result = "Hello" + " John"</td>

#-------------------------------------------------------------------------------------------------------

# Data Types	
# - Integer - Float - Boolean - String	

# Example:
x=7 
# Integer Value 
y=12.4 
# Float Value 
is_valid = True 
# Boolean Value 
is_valid = False 
# Boolean Value 
F_Name = "John" 
# String Value

#-------------------------------------------------------------------------------------------------------


# Indexing	
# Accesses character at a specific index	
# Example:
my_string="Hello" 
char = my_string[0]

#-------------------------------------------------------------------------------------------------------

# len()	
# Returns length of string
# Syntax:
len(string_name) 
# Example:
my_string="Hello" 
length = len(my_string)

#-------------------------------------------------------------------------------------------------------

# lower()	
# Converts string to lowercase
# Example:
my_string="Hello" 
uppercase_text = my_string.lower()

#-------------------------------------------------------------------------------------------------------

# print()	
# Prints the message or variable inside ()	
# Example:
print("Hello, world") 
print(a+b)

#-------------------------------------------------------------------------------------------------------

# Python Operators	
#- Addition (+): Adds two values together.
#- Subtraction (-): Subtracts one value from another.
#- Multiplication (*): Multiplies two values.
#- Division (/): Divides one value by another, returns a float.
#- Floor Division (//): Divides one value by another, returns the quotient as an integer.
#- Modulo (%): Returns the remainder after division.	Example:
#
#x = 9 y = 4 
#result_add= x + y # Addition 
#result_sub= x - y # Subtraction 
#result_mul= x * y # Multiplication 
#result_div= x / y # Division 
#result_fdiv= x // y # Floor Division 
#result_mod= x % y # Modulo</td>

#-------------------------------------------------------------------------------------------------------

# replace()	
# Replaces substrings.	
# Example:
my_string="Hello" 
new_text = my_string.replace("Hello", "Hi")

#-------------------------------------------------------------------------------------------------------

# Slicing	
# Extracts a portion of the string
# Syntax:
substring = string_name[start:end] 
# Example:
my_string="Hello" substring = my_string[0:5]

#-------------------------------------------------------------------------------------------------------

# split()	
# Splits string into a list based on a delimiter
# Example:
my_string="Hello" 
split_text = my_string.split(",")

#-------------------------------------------------------------------------------------------------------

# strip()	
# Removes leading/trailing whitespace	
# Example:
my_string="Hello" 
trimmed = my_string.strip()

#-------------------------------------------------------------------------------------------------------

# upper()	
# Converts string to uppercase.	
# Example:
my_string="Hello" 
uppercase_text = my_string.upper()

#-------------------------------------------------------------------------------------------------------

# Variable Assignment	
# Assigns a value to a variable	
# Syntax:
variable_name = value 
# Example:
name="John" # assigning John to variable name 
x = 5 # assigning 5 to variable x

#-------------------------------------------------------------------------------------------------------
########################################################################################################
# Python Data Structures Part-2

# Creating a Dictionary	
# dictionary is built-in data type that represents collection of key-value pairs
# Dictionaries are enclosed in curly braces {}
# Example:
dict_name = {} #Creates an empty dictionary
person = { "name": "John",  "age": 30, "city": "New York"}

#-------------------------------------------------------------------------------------------------------

# Accessing Values	
# You can access values in dictionary using their corresponding keys
Syntax:
Value = dict_name["key_name"]
Example:
name = person["name"]
age = person["age"]

#-------------------------------------------------------------------------------------------------------

# Add or modify
# Inserts new key-value pair into dictionary
# If key already exists, value will be updated; otherwise, a new entry is created
# Syntax:
dict_name[key] = value
# Example:
person["Country"] = "USA" # A new entry will be created.
person["city"] = "Chicago"  # Update the existing value for the same key

#-------------------------------------------------------------------------------------------------------

# del	
# Removes specified key-value pair from dictionary
# Raises a KeyError if key does not exist
# Syntax:
del dict_name[key]
# Example:
del person["Country"]

#-------------------------------------------------------------------------------------------------------

# update()	
# update() method merges provided dictionary into existing dictionary, adding or updating key-value pairs
# Syntax:
dict_name.update({key: value})
# Example:
person.update({"Profession": "Doctor"})

#-------------------------------------------------------------------------------------------------------

# clear()	
# clear() method empties dictionary, removing all key-value pairs within it
# After this operation, dictionary is still accessible and can be used further
# Syntax:
dict_name.clear()
# Example:
grades.clear()

#-------------------------------------------------------------------------------------------------------

# key existence	
# You can check for existence of a key in a dictionary using  in keyword
# Example:
if "name" in person:
    print("Name exists in the dictionary.")

#-------------------------------------------------------------------------------------------------------

# copy()	
# Creates shallow copy of dictionary. 
# new dictionary contains same key-value pairs as original, but they remain distinct objects in memory
# Syntax:
new_dict = dict_name.copy()
# Example:
new_person = person.copy()
new_person = dict(person) # another way to create a copy of dictionary

#-------------------------------------------------------------------------------------------------------

# keys()	
# Retrieves all keys from dictionary and converts them into list 
# Useful for iterating or processing keys using list methods
# Syntax:
keys_list = list(dict_name.keys())
# Example:
person_keys = list(person.keys())

#-------------------------------------------------------------------------------------------------------

# values()	
# Extracts all values from dictionary and converts them into a list
# This list can be used for further processing or analysis
# Syntax:
values_list = list(dict_name.values())
# Example:
person_values = list(person.values())

#-------------------------------------------------------------------------------------------------------

# items()	
# Retrieves all key-value pairs as tuples and converts them into a list of tuples
# Each tuple consists of a key and its corresponding value
# Syntax:
items_list = list(dict_name.items())
# Example:
info = list(person.items())

#-------------------------------------------------------------------------------------------------------

#######
# Sets

# add()	
# Elements can be added to set using `add()` method 
# Duplicates are automatically removed, as sets only store unique values	
# Syntax:
set_name.add(element) 
# Example:
fruits.add("mango")

#-------------------------------------------------------------------------------------------------------

# clear()	
# `clear()` method removes all elements from set, resulting in empty set 
# updates set in-place	
# Syntax:
set_name.clear() 
# Example:
fruits.clear()</td>

#-------------------------------------------------------------------------------------------------------

# copy()	
# `copy()` method creates shallow copy of set
# Any modifications to copy won't affect original set	
# Syntax:
new_set = set_name.copy() 
# Example:
new_fruits = fruits.copy()

#-------------------------------------------------------------------------------------------------------

# Defining Sets	
# set is unordered collection of unique elements
# Sets are enclosed in curly braces `{}`
# useful for storing distinct values and performing set operations
# Example:
empty_set = set() #Creating an Empty 
Set fruits = {"apple", "banana", "orange"}

#-------------------------------------------------------------------------------------------------------

discard()	
# `discard()` method to remove specific element from set 
# Ignores if element is not found.	
# Syntax
set_name.discard(element) 
# Example:
fruits.discard("apple")

#-------------------------------------------------------------------------------------------------------

# issubset()	
# `issubset()` method checks if current set is a subset of another set
# It returns True if all elements of current set are present in other set, otherwise False	
# Syntax:
is_subset = set1.issubset(set2)
# Example:
is_subset = fruits.issubset(colors)

#-------------------------------------------------------------------------------------------------------

# issuperset()	
# `issuperset()` method checks if current set is superset of another set 
# returns True if all elements of other set are present in current set, otherwise False
# Syntax:
is_superset = set1.issuperset(set2)
# Example:
is_superset = colors.issuperset(fruits)

#-------------------------------------------------------------------------------------------------------

# pop()	
# `pop()` method removes and returns an arbitrary element from set
# raises `KeyError` if set is empty 
# use this method to remove elements when order doesn't matter	
# Syntax:
removed_element = set_name.pop() 
# Example:
removed_fruit = fruits.pop()

#-------------------------------------------------------------------------------------------------------

# remove()	
# Use the `remove()` method to remove specific element from set 
# Raises `KeyError` if the element is not found	
# Syntax:
set_name.remove(element) 
# Example:
fruits.remove("banana")

#-------------------------------------------------------------------------------------------------------

# Set Operations	
# Perform various operations on sets: `union`, `intersection`, `difference`, `symmetric difference`	
# Syntax:
union_set = set1.union(set2) 
intersection_set = set1.intersection(set2) 
difference_set = set1.difference(set2) 
sym_diff_set = set1.symmetric_difference(set2) 
# Example:
combined = fruits.union(colors) 
common = fruits.intersection(colors) 
unique_to_fruits = fruits.difference(colors) 
sym_diff = fruits.symmetric_difference(colors)

#-------------------------------------------------------------------------------------------------------

# update()	
# `update()` method adds elements from another iterable into set
# maintains uniqueness of elements	
# Syntax:
set_name.update(iterable) 
# Example:
fruits.update(["kiwi", "grape"])


#-------------------------------------------------------------------------------------------------------
########################################################################################################
# Fundamentals Cheat Sheet

# AND	
# Returns `True` if both statement1 and statement2 are `True` Otherwise, returns `False`	
# Syntax:
statement1 and statement2 
# Example:
marks = 90
attendance_percentage = 87
if marks >= 80 and attendance_percentage >= 85:
    print("qualify for honors")
else:
    print("Not qualified for honors")
# Output = qualify for honors



# Class Definition	
# Defines blueprint for creating objects and defining their attributes and behaviors	
# Syntax:
class ClassName: # Class attributes and methods 
# Example:
class Person: 
    def __init__(self, name, age): 
        self.name = name 
        self.age = age



# Define Function	
# A `function` is reusable block of code that performs specific task or set of tasks when called	
# Syntax:
def function_name(parameters): # Function body 
# Example:
def greet(name): print("Hello,", name)



# Equal(==)	
# Checks if two values are equal	
# Syntax:
# variable1 == variable2 
# Example 1:
5 == 5 
# returns True
# Example 2:
age = 25 age == 30 
# returns False

# For Loop	
# `for` loop repeatedly executes block of code for specified number of iterations or over 
# sequence of elements (list, range, string, etc.)	
# Syntax:
for variable in sequence: # Code to repeat 
# Example 1:
for num in range(1, 10): 
    print(num) 
# Example 2:
fruits = ["apple", "banana", "orange", "grape", "kiwi"] 
for fruit in fruits:
    print(fruit)



# Function Call	
# function call is act of executing code within function using provided arguments	
# Syntax:
function_name(arguments) 
# Example:
greet("Alice")



# Greater Than or Equal To(>=)	
# Checks if value of variable1 is greater than or equal to variable2	
# Syntax:
# variable1 >= variable2 
# Example 1:
5 >= 5 and 9 >= 5 
# returns True
# Example 2:
quantity = 105 
minimum = 100 
quantity >= minimum 
# returns True

# Greater Than(>)	
# Checks if value of variable1 is greater than variable2
# Syntax:
# variable1 > variable2 
# Example 1: 9 > 6
returns True
# Example 2:
age = 20 
max_age = 25 
age > max_age 
# returns False



# If Statement	
# Executes code block `if` condition is `True`	
# Syntax:
if condition: #code block for if statement 
# Example:
if temperature > 30: 
print("It's a hot day!")



# If-Elif-Else	
# Executes the first code block if condition1 is `True`, otherwise checks condition2, and so on
# If no condition is `True`, else block is executed
# Syntax:
if condition1:
# Code if condition1 is True
elif condition2:
# Code if condition2 is True
else:
# Code if no condition is True
Copied!
# Example:
score = 85  # Example score
if score >= 90:
    print("You got an A!")
elif score >= 80:
    print("You got a B.")
else:
    print("You need to work harder.")
# Output = You got a B.



# If-Else Statement	
# Executes first code block if condition is `True`, otherwise second block
# Syntax:
if condition: # Code, if condition is True 
else: # Code, if condition is False 
# Example:
if age >= 18:
    print("You're an adult.")
else:
    print("You're not an adult yet.")



# Less Than or Equal To(<=)	
# Checks if value of variable1 is less than or equal to variable2	
# Syntax:
# variable1 <= variable2 			 
# Example 1:
5 <= 5 and 3 <= 5 
# returns True
# Example 2:
size = 38 
max_size = 40 
size <= max_size 
# returns True



# Less Than(<)	
# Checks if value of variable1 is less than variable2
# Syntax:
# variable1 < variable2 
# Example 1:
4 < 6 
# returns True
# Example 2:
score = 60 
passing_score = 65 
score < passing_score 
# returns True



# Loop Controls	
# `break` exits loop prematurely
# `continue` skips rest of current iteration and moves to next iteration
# Syntax:
for: # Code to repeat 
    if # boolean statement
        break 
for: # Code to repeat  
    if # boolean statement
        continue
# Example 1:
for num in range(1, 6):
    if num == 3:
        break
    print(num)
# Example 2:
for num in range(1, 6):
    if num == 3:
        continue
    print(num)



# NOT	
# Returns `True` if variable is `False`, and vice versa	
# Syntax:
!variable 
# Example:
!isLocked 
# returns True if the variable is False (i.e., unlocked)



# Not Equal(!=)	
# Checks if two values are not equal	
# Syntax:
variable1 != variable2 
# Example:
a = 10 
b = 20 
a != b 
# returns True
# Example 2:
count=0 
count != 0 
# returns False



# Object Creation	Creates an instance of a class (object) using the class constructor.	Syntax:
object_name = ClassName(arguments) 
# Example:
person1 = Person("Alice", 25)
# OR	
# Returns `True` if either statement1 or statement2 (or both) are `True` 
# Otherwise, returns `False`	
# Syntax:
# statement1 || statement2
# Example:
"Farewell Party Invitation" 
Grade = 12 grade == 11 or grade == 12 
# returns True



# range()	
# Generates a sequence of numbers within a specified range	
# Syntax:
range(stop) 
range(start, stop) 
range(start, stop, step) 
# Example:
range(5) #generates a sequence of integers from 0 to 4. 
range(2, 10) #generates a sequence of integers from 2 to 9. 
range(1, 11, 2) #generates odd integers from 1 to 9.



# Return Statement	`Return` is keyword used to send value back from function to its caller	
# Syntax:
return value 
# Example:
def add(a, b): return a + b 
result = add(3, 5)



# Try-Except Block	
# Tries to execute code in try block 
# If exception of specified type occurs, code in except block is executed	
# Syntax:
try: # Code that might raise an exception except 
ExceptionType: # Code to handle the exception 
# Example:
try: 
    num = int(input("Enter a number: ")) 
except ValueError: 
    print("Invalid input. Please enter a valid number.")



# Try-Except with Else Block	
# Code in the `else` block is executed if no exception occurs in the try block.	
# Syntax:
try: # Code that might raise an exception except 
ExceptionType: # Code to handle the exception 
else: # Code to execute if no exception occurs 
# Example:
try: 
    num = int(input("Enter a number: ")) 
except ValueError: 
    print("Invalid input. Please enter a valid number") 
else: 
    print("You entered:", num)



# Try-Except with Finally Block	
# Code in the `finally` block always executes, regardless of whether exception occurred	
# Syntax:
try: # Code that might raise an exception except 
ExceptionType: # Code to handle the exception 
finally: # Code that always executes 
# Example:
try: 
    file = open("data.txt", "r") 
    data = file.read() 
except FileNotFoundError: 
    print("File not found.") 
finally: 
    file.close()



# While Loop	
# `while` loop repeatedly executes block of code as long as a specified condition remains `True`	
# Syntax:
while condition: # Code to repeat 
# Example:
count = 0 while count < 5: 
    print(count) count += 1



#-------------------------------------------------------------------------------------------------------
########################################################################################################
#Working with Data in Python Cheat Sheet

# File opening modes	
# Different modes to open files for specific operations
# Syntax: r (reading) w (writing) a (appending) + (updating: read/write) b (binary, otherwise text)
# Examples: 
with open("data.txt", "r") as file: content = file.read() 
print(content) 
with open("output.txt", "w") as file: file.write("Hello, world!") 
with open("log.txt", "a") as file: file.write("Log entry: Something happened.") 
with open("data.txt", "r+") as file: content = file.read() file.write("Updated content: " + content)</td>



# File reading methods	
# Different methods to read file content in various ways	
# Syntax:
file.readlines() # reads all lines as a list
readline() # reads the next line as a string
file.read() # reads the entire file content as a string
# Example:
with open("data.txt", "r") as file:
    lines = file.readlines()
    next_line = file.readline()
    content = file.read()



# File writing methods	
# Different write methods to write content to file	
# Syntax:
file.write(content) # writes a string to the file
file.writelines(lines) # writes a list of strings to the file
# Example:
lines = ["Hello\n", "World\n"]
with open("output.txt", "w") as file:
    file.writelines(lines)



# Iterating over lines	
# Iterates through each line in file using a `loop`	
# Syntax:
for line in file: # Code to process each line
# Example:
with open("data.txt", "r") as file:
for line in file: print(line)



# Open() and close()	
# Opens a file, performs operations, and explicitly closes file using close() method	
# Syntax:
file = open(filename, mode) # Code that uses the file
file.close()
# Example:
file = open("data.txt", "r")
content = file.read()
file.close()



# with open()	
# Opens file using with block, ensuring automatic file closure after usage	
# Syntax:
with open(filename, mode) as file: # Code that uses the file
# Example:
with open("data.txt", "r") as file:
content = file.read()



# Pandas
# Package/Method	
# Description	
# Syntax and Code Example
.read_csv()	
# Reads data from a `.CSV` file and creates DataFrame	
# Syntax:
dataframe_name = pd.read_csv("filename.csv") 
# Example: 
df = pd.read_csv("data.csv")



# .read_excel()	
# Reads data from excel file 
dataframe_name = pd.read_excel("filename.xlsx")
# Example:
df = pd.read_excel("data.xlsx")



# .to_csv()	
# Writes DataFrame to CSV file	
# Syntax:
dataframe_name.to_csv("output.csv", index=False)
# Example:
df.to_csv("output.csv", index=False)



# Access Columns	
# Accesses a specific column using [] in the DataFrame	
# Syntax:
dataframe_name["column_name"] # Accesses single column
dataframe_name[["column1", "column2"]] # Accesses multiple columns
# Example:
df["age"]
df[["name", "age"]]



# describe()	
# Generates statistics summary of numeric columns in DataFrame	
# Syntax:
dataframe_name.describe()
# Example:
df.describe()



# drop()	
# Removes specified rows or columns from DataFrame
# axis=1 indicates columns. 
# axis=0 indicates rows.	
# Syntax:
dataframe_name.drop(["column1", "column2"], axis=1, inplace=True)
dataframe_name.drop(index=[row1, row2], axis=0, inplace=True)
# Example:
df.drop(["age", "salary"], axis=1, inplace=True) # Will drop columns
df.drop(index=[5, 10], axis=0, inplace=True) # Will drop rows



# dropna()	
# Removes rows with missing NaN values from DataFrame
# axis=0 indicates rows.	
# Syntax:
dataframe_name.dropna(axis=0, inplace=True)
# Example:
df.dropna(axis=0, inplace=True)



# duplicated()	
# Duplicate or repetitive values or records within data set	
# Syntax:
dataframe_name.duplicated()
# Example:
duplicate_rows = df[df.duplicated()]



# Filter Rows	
# Creates new DataFrame with rows that meet specified conditions
# Syntax:
filtered_df = dataframe_name[(Conditional_statements)]
# Example:
filtered_df = df[(df["age"] > 30) & (df["salary"] < 50000)



# groupby()	
# Splits DataFrame into groups based on specified criteria, enabling subsequent aggregation, transformation, or analysis within each group	
# Syntax:
grouped = dataframe_name.groupby(by, axis=0, level=None, as_index=True,
sort=True, group_keys=True, squeeze=False, observed=False, dropna=True)
# Example:
grouped = df.groupby(["category", "region"]).agg({"sales": "sum"})



# head()	
# Displays first n rows of DataFrame.	
# Syntax:
dataframe_name.head(n)
# Example:
df.head(5)



# Import pandas	
# Imports Pandas library with alias pd	
# Syntax:
import pandas as pd
# Example:
import pandas as pd



# info()	
# Provides information about DataFrame, including data types and memory usage	
# Syntax:
dataframe_name.info()
# Example:
df.info()



# merge()	
# Merges two DataFrames based on multiple common columns	
# Syntax:
merged_df = pd.merge(df1, df2, on=["column1", "column2"])
# Example:
merged_df = pd.merge(sales, products, on=["product_id", "category_id"])



# print DataFrame	
# Displays content of DataFrame
# Syntax:
print(df) # or just type df
# Example:
print(df)



# replace()	
# Replaces specific values in a column with new values	
# Syntax:
dataframe_name["column_name"].replace(old_value, new_value, inplace=True)
# Example:
df["status"].replace("In Progress", "Active", inplace=True)



# tail()	
# Displays last n rows of DataFrame	
# Syntax:
dataframe_name.tail(n)
# Example:
df.tail(5)



# Numpy
# Package/Method	
# Description	Syntax and Code Example
# Importing NumPy	Imports NumPy library	
# Syntax:
import numpy as np
# Example:
import numpy as np

# np.array()	
# Creates one or multi-dimensional array
# Syntax:
array_1d = np.array([list1 values]) # 1D Array
array_2d = np.array([[list1 values], [list2 values]]) # 2D Array
# Example:
array_1d = np.array([1, 2, 3]) # 1D Array
array_2d = np.array([[1, 2], [3, 4]]) # 2D Array

#-------------------------------------------------------------------------------------------------------

# Numpy Array Attributes	
# - Calculates the mean of array elements
# - Calculates the sum of array elements
# - Finds the minimum value in the array
# - Finds the maximum value in the array
# - Computes dot product of two arrays	Example:
np.mean(array)
np.sum(array)
np.min(array
np.max(array)
np.dot(array_1, array_2)



#-------------------------------------------------------------------------------------------------------
########################################################################################################
#API's and Data Collection

#-------------------------------------------------------------------------------------------------------
		
# Access value of specific attribute of HTML element	
# Syntax:
attribute = element[(attribute)]
# Example:
href = link_element[(href)]

#-------------------------------------------------------------------------------------------------------

# BeautifulSoup()	
# Parse HTML content of web page using BeautifulSoup. 
# parser type can vary based on project.	
# Syntax:
soup = BeautifulSoup(html, (html.parser))
# Example:
html = (https://api.example.com/data) soup = BeautifulSoup(html, (html.parser))

#-------------------------------------------------------------------------------------------------------

# delete()	
# Send DELETE request to remove data or resource from server
# DELETE requests delete specified resource on server	
# Syntax:
response = requests.delete(url)
# Example:
response = requests.delete((https://api.example.com/delete))

#-------------------------------------------------------------------------------------------------------

# find()
# Find first HTML element that matches specified tag and attributes	
# Syntax:
element = soup.find(tag, attrs)
# Example:
first_link = soup.find((a), {(class): (link)})

#-------------------------------------------------------------------------------------------------------

# find_all()	
# Find all HTML elements that match specified tag and attributes	
# Syntax:
elements = soup.find_all(tag, attrs)
# Example:
all_links = soup.find_all((a), {(class): (link)})</td>

#-------------------------------------------------------------------------------------------------------

# findChildren()	
# Find all child elements of HTML element	
# Syntax:
children = element.findChildren()
# Example:
child_elements = parent_div.findChildren()

#-------------------------------------------------------------------------------------------------------

# get()	
# Perform GET request to retrieve data from a specified URL
# GET requests are typically used for reading data from an API 
# response variable will contain server's response, which you can process further	
# Syntax:
response = requests.get(url)
# Example:
response = requests.get((https://api.example.com/data))

#-------------------------------------------------------------------------------------------------------

# Headers	
# Include custom headers in request 
# Headers can provide additional information to server, such as authentication tokens or content types	
# Syntax:
headers = {(HeaderName): (Value)}
# Example:
base_url = (https://api.example.com/data) headers = {(Authorization): (Bearer YOUR_TOKEN)} response = requests.get(base_url, headers=headers)

#-------------------------------------------------------------------------------------------------------

# Import Libraries	
# Import necessary Python libraries for web scraping	
# Syntax:
from bs4 import BeautifulSoup

#-------------------------------------------------------------------------------------------------------

# json()	
# Parse JSON data from response
# This extracts and works with data returned by API
# response.json() method converts JSON response into Python data structure (usually dictionary or list)	
# Syntax:
data = response.json()
# Example:
response = requests.get((https://api.example.com/data)) data = response.json()

#-------------------------------------------------------------------------------------------------------

# next_sibling()	
# Find next sibling element in the DOM
# Syntax:
sibling = element.find_next_sibling()
# Example:
next_sibling = current_element.find_next_sibling()

#-------------------------------------------------------------------------------------------------------

# parent	
# Access parent element in Document Object Model (DOM)	
# Syntax:
parent = element.parent
# Example:
parent_div = paragraph.parent

#-------------------------------------------------------------------------------------------------------

# post()	
# Send POST request to specified URL with data 
# Create or update POST requests using resources on server 
# data parameter contains data to send to server, often in JSON format
# Syntax:
response = requests.post(url, data)
# Example:
response = requests.post((https://api.example.com/submit), data={(key): (value)})

#-------------------------------------------------------------------------------------------------------

# put()	
# Send PUT request to update data on server
# PUT requests are used to update existing resource on server with data provided in data parameter, typically in JSON format	
# Syntax:
response = requests.put(url, data)
# Example:
response = requests.put((https://api.example.com/update), data={(key): (value)})

#-------------------------------------------------------------------------------------------------------

# Query parameters	
# Pass query parameters in URL to filter or customize request
# Query parameters specify conditions or limits for requested data
# Syntax:
params = {(param_name): (value)}
# Example:
base_url = "https://api.example.com/data"
params = {"page": 1, "per_page": 10}
response = requests.get(base_url, params=params)

#-------------------------------------------------------------------------------------------------------

# select()	
# Select HTML elements from parsed HTML using CSS selector
# Syntax:
element = soup.select(selector)
# Example:
titles = soup.select((h1))

#-------------------------------------------------------------------------------------------------------

# status_code	
# Check HTTP status code of response 
# HTTP status code indicates result of request (success, error, redirection)
# Use HTTP status codeIt can be used for error handling and decision-making in your code	
# Syntax:
response.status_code
# Example:
url = "https://api.example.com/data"
response = requests.get(url)
status_code = response.status_code

#-------------------------------------------------------------------------------------------------------

# tags for find() and find_all()	
# Specify any valid HTML tag as tag parameter to search for elements of that type
# common HTML tags that you can use with tag parameter
# Tag Example:
# - (a): Find anchor () tags.
# - (p): Find paragraph ((p)) tags.
# - (h1), (h2), (h3), (h4), (h5), (h6): Find heading tags from level 1 to 6 ( (h1),n (h2)).
# - (table): Find table () tags.
# - (tr): Find table row () tags.
# - (td): Find table cell ((td)) tags.
# - (th): Find table header cell ((td))tags.
# - (img): Find image ((img)) tags.
# - (form): Find form ((form)) tags.
# - (button): Find button ((button)) tags.

#-------------------------------------------------------------------------------------------------------

# text	
# Retrieve text content of HTML element	
# Syntax:
text = element.text
# Example:
title_text = title_element.text

