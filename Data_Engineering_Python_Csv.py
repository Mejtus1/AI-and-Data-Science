# Data Engineering
# - is one of most critical and foundational skills in any data scientists toolkit

########################
# Data Engineering Process
# There are several steps in Data Engineering process

# Extract 
# - Data extraction is getting data from multiple sources
# - Data extraction from a website using Web scraping or gathering information from 
# data that are stored in different formats(JSON, CSV, XLSX)

# Transform 
# - Transforming data means removing  data that we dont need for further analysis and converting 
# data in format that all data from multiple sources is in same format

# Load 
# - Loading data inside a data warehouse
# - Data warehouse essentially contains large volumes of data that are accessed to gather insights

###################################
# Working with different file formats
# - in real-world, people rarely get neat tabular data
# - mandatory for any data scientist (or data engineer) to be aware of different file formats
# - common challenges in handling data and best, most efficient ways to handle this data in real life

# File Format
# - is standard way in which information is encoded for storage in a file
# - first file format specifies whether file is a binary or ASCII file
# - second, it shows how information is organized
# (comma-separated values (CSV) file format stores tabular data in plain text)

# To identify a file format, you can usually look at file extension to get idea
# - file saved with name "Data" in "CSV" format will appear as Data.csv
# - by noticing .csv extension, we can clearly identify that it is CSV file and data is stored in tabular format
# - various formats for a dataset, .csv, .json, .xlsx 
# - dataset can be stored in different places, on your local machine or sometimes online

# file formats and how to read them in Python:
# 1. Comma-separated values (CSV) file format
# 2. JSON file Format
# 3. XLSX file format

#############################################
# 1. Comma-separated values (CSV) file format
# - comma-separated values file format falls under a spreadsheet file format
# - in spreadsheet file format, data is stored in cells
# - each cell is organized in rows and columns 
# - column in spreadsheet file can have different types
# - column can be of string type, a date type, or an integer type
# - each line in CSV file represents an observation, or commonly called a record
# - each record may contain one or more fields which are separated by a comma

# Reading data from CSV in Python
# Pandas Library is useful tool that enables us to read various datasets into Pandas data frame

# - read a CSV file in Pandas Library.
# - use pandas.read_csv() function to read the csv file
# - In parentheses, we put file path along with a quotation mark as argument, so pandas will read file into a data frame from that address
# - file path can be either a URL or your local file address
import piplite
await piplite.install(['seaborn', 'lxml', 'openpyxl'])

import pandas as pd

from pyodide.http import pyfetch

filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/addresses.csv"

async def download(url, filename):
    response = await pyfetch(url)
    if response.status == 200:
        with open(filename, "wb") as f:
            f.write(await response.bytes())

await download(filename, "addresses.csv")

df = pd.read_csv("addresses.csv", header=None)

# Adding column name to DataFrame
# We can add columns to an existing DataFrame using its columns attribute
df.columns =['First Name', 'Last Name', 'Location ', 'City','State','Area Code']
df

# Selecting a single column
# To select first column 'First Name', you can pass column name as a string to indexing operator
df["First Name"]

# Selecting multiple columns
# To select multiple columns, you can pass a list of column names to indexing operator.
df = df[['First Name', 'Last Name', 'Location ', 'City','State','Area Code']]
df

# Selecting rows using .iloc and .loc
# Now, lets see how to use .loc for selecting rows from our DataFrame
# loc() : loc() is label based data selecting method which means that we have to pass name of row or column which we want to select

# To select the first row
df.loc[0]

# To select the 0th,1st and 2nd row of "First Name" column only
df.loc[[0,1,2], "First Name" ]

# Now, let's see how to use .iloc for selecting rows from our DataFrame
# iloc() : iloc() is a indexed based selecting method which means that we have to pass integer index in method to select specific row/column

# To select the 0th,1st and 2nd row of "First Name" column only
df.iloc[[0,1,2], 0]

# Transform Function in Pandas
# Python's Transform function returns a self-produced dataframe with transformed values after applying function specified in its parameter

#import library
import pandas as pd
import numpy as np

#creating a dataframe
df=pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=['a', 'b', 'c'])
df

# we want to add 10 to each element in a dataframe:
#applying transform function
df = df.transform(func = lambda x : x + 10)
df

# Now we will use DataFrame.transform() function to find square root to each element of the dataframe
result = df.transform(func = ['sqrt'])
result


#################
#JSON file Format
# JSON (JavaScript Object Notation) is a lightweight data-interchange format 
# It is easy for humans to read and write

# JSON is built on two structures:

# A collection of name/value pairs
# - in various languages, this is realized as an object, record, struct, dictionary, hash table, keyed list, or associative array

# An ordered list of values 
# - in most languages, this is realized as an array, vector, list, or sequence

# JSON is language-independent data format
# - was derived from JavaScript, many modern programming languages include code to generate and parse JSON-format data
# - very common data format with a diverse range of applications
# - text in JSON is done through quoted string which contains values in key-value mappings within { }
# - similar to dictionary in Python
# - python supports JSON through a built-in package called json
# - to use this feature, we import the json package in Python script
import json

# Writing JSON to a File
# - usually called serialization 
# - process of converting an object into a special format which is suitable for transmitting over network or storing in file or database
# - to handle data flow in a file, JSON library in Python uses dump() or dumps() function to convert Python objects into respective JSON object
# - makes it easy to write data to files
import json
person = {
    'first_name' : 'Mark',
    'last_name' : 'abc',
    'age' : 27,
    'address': {
        "streetAddress": "21 2nd Street",
        "city": "New York",
        "state": "NY",
        "postalCode": "10021-3100"
    }
}

# serialization using dump() function
# json.dump() method can be used for writing to JSON file
# Syntax: json.dump(dict, file_pointer)
# Parameters:
# - dictionary = name of the dictionary which should be converted to JSON object
# - file pointer = pointer of the file opened in write or append mode
with open('person.json', 'w') as f:  # writing JSON object
    json.dump(person, f)

# serialization using dumps() function
# json.dumps() helps in converting dictionary to JSON object
# takes two parameters:
# - dictionary = name of the dictionary which should be converted to JSON object.
# - indent = defines the number of units for indentation

# Serializing json  
json_object = json.dumps(person, indent = 4) 
  
# Writing to sample.json 
with open("sample.json", "w") as outfile: 
    outfile.write(json_object) 

print(json_object)
# - python objects are now serialized to file
# - for deserialize it back to Python object, we use load() function

# Reading JSON to a File
# - process is usually called Deserialization 
# - it is reverse of serialization 
# - converts special format returned by serialization back into usable object

# Using json.load()
# - JSON package has json.load() function loads json content from json file into dictionary
# takes one parameter:
# - File pointer = file pointer that points to JSON file

import json 
# Opening JSON file 
with open('sample.json', 'r') as openfile: 
    # Reading from json file 
    json_object = json.load(openfile) 
print(json_object) 
print(type(json_object))


##################
# XLSX file format
# - XLSX is Microsoft Excel Open XML file format
# - another type of Spreadsheet file format
# - In XLSX data is organized under cells and columns in sheet

# Reading data from XLSX file
# - load data from XLSX file and define sheet name
# - loading data you can use Pandas library in python
import pandas as pd
# Not needed unless you're running locally
# import urllib.request
# urllib.request.urlretrieve("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/file_example_XLSX_10.xlsx", "sample.xlsx")

filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/file_example_XLSX_10.xlsx"

async def download(url, filename):
    response = await pyfetch(url)
    if response.status == 200:
        with open(filename, "wb") as f:
            f.write(await response.bytes())

await download(filename, "file_example_XLSX_10.xlsx")

df = pd.read_excel("file_example_XLSX_10.xlsx")

df


# XML file format
# - XML also known as Extensible Markup Language
# - it is markup language
# - certain rules for encoding data 
# - XML file format is human-readable and machine-readable file format
# - pandas does not include any methods to read and write XML files

# Writing with xml.etree.ElementTree
# - xml.etree.ElementTree module comes built-in with Python 
# - provides functionality for parsing and creating XML documents 
# - ElementTree represents XML document as tree
# - move across document using nodes which are elements and sub-elements of XML file
import xml.etree.ElementTree as ET
# create the file structure
employee = ET.Element('employee')
details = ET.SubElement(employee, 'details')
first = ET.SubElement(details, 'firstname')
second = ET.SubElement(details, 'lastname')
third = ET.SubElement(details, 'age')
first.text = 'Shiv'
second.text = 'Mishra'
third.text = '23'
# create a new XML file with the results
mydata1 = ET.ElementTree(employee)
# myfile = open("items2.xml", "wb")
# myfile.write(mydata)
with open("new_sample.xml", "wb") as files:
    mydata1.write(files)

# Reading with xml.etree.ElementTree

# Not needed unless running locally
# !wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Sample-employee-XML-file.xml

import xml.etree.ElementTree as etree

filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Sample-employee-XML-file.xml"

async def download(url, filename):
    response = await pyfetch(url)
    if response.status == 200:
        with open(filename, "wb") as f:
            f.write(await response.bytes())

await download(filename, "Sample-employee-XML-file.xml")

# You would need to firstly parse an XML file and create a list of columns for data frame, then extract useful information from the XML file and add to a pandas data frame.
# Here is sample code that you can use:

tree = etree.parse("Sample-employee-XML-file.xml")

root = tree.getroot()
columns = ["firstname", "lastname", "title", "division", "building","room"]

datatframe = pd.DataFrame(columns = columns)

for node in root: 

    firstname = node.find("firstname").text

    lastname = node.find("lastname").text 

    title = node.find("title").text 
    
    division = node.find("division").text 
    
    building = node.find("building").text
    
    room = node.find("room").text
    
    datatframe = datatframe.append(pd.Series([firstname, lastname, title, division, building, room], index = columns), ignore_index = True)
datatframe

# Reading xml file using pandas.read_xml function
# We can also read downloaded xml file using read_xml function present in pandas library which returns Dataframe object
# Herein xpath we mention set of xml nodes to be considered for migrating  to dataframe which in this case is details node under employees
df=pd.read_xml("Sample-employee-XML-file.xml", xpath="/employees/details") 

# Save Data
# Pandas enables us to save dataset to csv using dataframe.to_csv() method, add file path and name along with quotation marks in parentheses
datatframe.to_csv("employee.csv", index=False)

# We can also read and save other file formats, we can use similar functions to pd.read_csv() and df.to_csv() for other data formats. 
# functions are listed in following table:
# 
# Read/Save Other Data Formats
# Data Formate	Read	Save
# csv	pd.read_csv()	df.to_csv()
# json	pd.read_json()	df.to_json()
# excel	pd.read_excel()	df.to_excel()
# hdf	pd.read_hdf()	df.to_hdf()
# sql	pd.read_sql()	df.to_sql()
# ...	...	...

####################
# Binary File Format
# - "Binary" files are any files where format isn't made up of readable for humans characters and only 1s and 0s 
# - contains formatting information that only certain applications or processors can understand
# - humans can read text files, binary files must be run on the appropriate software or processor before humans can read them
# - binary files can range from image files like JPEGs or GIFs, audio files like MP3s or binary document formats like Word or PDF

# Reading Image file
# Python supports very powerful tools when it comes to image processing

# PIL 
# - is Python Imaging Library which provides python interpreter with image editing capabilities
# importing PIL 
from PIL import Image 

# Uncomment if running locally
# import urllib.request
# urllib.request.urlretrieve("https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/dog-puppy-on-garden-royalty-free-image-1586966191.jpg", "dog.jpg")
filename = "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/dog-puppy-on-garden-royalty-free-image-1586966191.jpg"
async def download(url, filename):
    response = await pyfetch(url)
    if response.status == 200:
        with open(filename, "wb") as f:
            f.write(await response.bytes())
await download(filename, "dog.jpg")

# Read image 
img = Image.open('dog.jpg') 
# Output Images 
display(img)

###############
# Data Analysis
# - how to approach data acquisition in various ways and obtain necessary insights from a dataset 
# - load the data into Jupyter Notebook
# - gain some fundamental insights via Pandas Library 
# - Diabetes Dataset is online source and it is in CSV format 

# About this Dataset
# Context: 
# This dataset is originally from the National Institute of Diabetes and Digestive and Kidney Diseases. 
# The objective of dataset is to diagnostically predict whether or not a patient has diabetes, based on certain diagnostic measurements included in dataset. 
# Several constraints were placed on the selection of these instances from a larger database. 
# In particular, all patients here are females at least 21 years of age of Pima Indian heritage.
# Content: 
# The datasets consists of several medical predictor variables and one target variable, Outcome. 
# Predictor variables includes the number of pregnancies the patient has had, their BMI, insulin level, age, and so on.
# We have 768 rows and 9 columns. First 8 columns represent features and last column represent target/label.

# Import pandas library
import pandas as pd

filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/diabetes.csv"
async def download(url, filename):
    response = await pyfetch(url)
    if response.status == 200:
        with open(filename, "wb") as f:
            f.write(await response.bytes())
await download(filename, "diabetes.csv")
df = pd.read_csv("diabetes.csv")

# After reading dataset, we can use dataframe.head(n) method to check top n rows of the dataframe, where n is an integer. 
# Contrary to dataframe.head(n), dataframe.tail(n) will show you bottom n rows of dataframe.
# show the first 5 rows using dataframe.head() method
print("The first 5 rows of the dataframe") 
df.head(5)

# To view the dimensions of dataframe, we use .shape parameter
df.shape

#################################
# Statistical Overview of dataset
df.info()
# - df method prints information about DataFrame including index dtype and columns, non-null values and memory usage

df.describe()
# - Pandas describe() used to view basic statistical details like percentile, mean, standard deviation... of a data frame, series of numeric values. 
# - when this method is applied to series of strings, it returns different output

# Identify and handle missing values
# We use Python's built-in functions to identify missing values
# There are two methods to detect missing data:
#  .isnull()
#  .notnull()
# output is boolean value indicating whether value that is passed into argument is in fact missing data

missing_data = df.isnull()
missing_data.head(5)
# "True" stands for missing value, while "False" stands for not missing value

# Count missing values in each column
# Using for loop in Python, we can quickly figure out number of missing values in each column. 
# As mentioned above, "True" represents a missing value, "False" means the value is present in the dataset. In the body of the for loop the method ".value_counts()" counts the number of "True" values.

for column in missing_data.columns.values.tolist():
    print(column)
    print (missing_data[column].value_counts())
    print("")    
#  there is no missing values in the dataset

# Correct data format
# Check all data is in correct format (int, float, text or other)

# In Pandas, we use
#  .dtype() to check the data type
#  .astype() to change the data type
# Numerical variables should have type 'float' or 'int'

df.dtypes
# As we can see above, All columns have correct data type

###############
# Visualization
# Visualization is one of best way to get insights from dataset
# Seaborn and Matplotlib are two of Python's most powerful visualization libraries

# import libraries
import matplotlib.pyplot as plt
import seaborn as sns
labels= 'Diabetic','Not Diabetic'
plt.pie(df['Outcome'].value_counts(),labels=labels,autopct='%0.02f%%')
plt.legend()
plt.show()
# - 65.10% females are Diabetic and 34.90% are Not Diabetic. 