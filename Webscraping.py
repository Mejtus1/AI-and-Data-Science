# WEBSCRAPING 

install html5lib
install bs4
install requests

from bs4 import BeautifulSoup # this module helps in web scrapping.
import requests  # this module helps us to download a web page

# Beautiful Soup Objects
# Beautiful Soup is a Python library for pulling data out of HTML and XML files 
# This is accomplished by representing HTML as a set of objects with methods used to parse HTML
# We can navigate the HTML as a tree, and/or filter out what we are looking for
#
# Following HTML:
# %%html
# <!DOCTYPE html>
# <html>
# <head>
# <title>Page Title</title>
# </head>
# <body>
# <h3><b id='boldest'>Lebron James</b></h3>
# <p> Salary: $ 92,000,000 </p>
# <h3> Stephen Curry</h3>
# <p> Salary: $85,000, 000 </p>
# <h3> Kevin Durant </h3>
# <p> Salary: $73,200, 000</p>
# </body>
# </html>

# Can be stored in Python as:
html="<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3><b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p><h3> Stephen Curry</h3><p> Salary: $85,000, 000 </p><h3> Kevin Durant </h3><p> Salary: $73,200, 000</p></body></html>"

# to parse a document, pass it into BeautifulSoup constructor
# BeautifulSoup object represents document as nested data structure:
soup = BeautifulSoup(html, 'html5lib')
# First, document is converted to Unicode (similar to ASCII) and HTML entities are converted to Unicode Characters
# Beautiful Soup transforms a complex HTML document into a complex tree of Python objects
# The BeautifulSoup object can create other types of objects

# We can use method prettify() to display HTML in nested structure:
print(soup.prettify())
# <!DOCTYPE html>
# <html>
# <head>
#  <title>
#   Page Title
#  </title>
# </head>
# <body>
#  <h3>
#   <b id="boldest">
#    Lebron James
#   </b>
#  </h3>
#  <p>
#   Salary: $ 92,000,000
#  </p>
#  <h3>
#   Stephen Curry
#  </h3>
#  <p>
#   Salary: $85,000, 000
#  </p>
#  <h3>
#   Kevin Durant
#  </h3>
#  <p>
#   Salary: $73,200, 000
#  </p>
# </body>
#</html>

#####
#Tags

# Let's say we want title of page and name of top paid player
# We can use Tag -> object corresponds to an HTML tag in the original document, for example, tag title
tag_object=soup.title
print("tag object:",tag_object)
# tag object: <title>Page Title</title>

# we can see tag type bs4.element.Tag
print("tag object type:",type(tag_object))
# tag object type: <class 'bs4.element.Tag'>

# If there is more than one Tag with same name, first element with that Tag name is called 
# This corresponds to most paid player:
tag_object=soup.h3
tag_object
# <h3><b id="boldest">Lebron James</b></h3>

#################################
# Children, Parents, and Siblings
# As stated above, Tag object is a tree of objects
# We can access child of tag or navigate down branch as follows:
tag_child =tag_object.b
tag_child
# <b id="boldest">Lebron James</b>

# You can access parent with parent
parent_tag=tag_child.parent
parent_tag
# <h3><b id="boldest">Lebron James</b></h3>

# this is identical to:
tag_object
# <h3><b id="boldest">Lebron James</b></h3>

# tag_object parent is body element
tag_object.parent
# <body><h3><b id="boldest">Lebron James</b></h3><p> Salary: $ 92,000,000 </p><h3> Stephen Curry</h3><p> Salary: $85,000, 000 </p><h3> Kevin Durant </h3><p> Salary: $73,200, 000</p></body>

# tag_object sibling is paragraph element
sibling_1=tag_object.next_sibling
sibling_1
# <p> Salary: $ 92,000,000 </p>

# sibling_2 is header element, which is also a sibling of both sibling_1 and tag_object
sibling_2=sibling_1.next_sibling
sibling_2
# <h3> Stephen Curry</h3>

# Use object sibling_2 and method next_sibling to find salary of Stephen Curry:
sibling_2.next_sibling
# <p> Salary: $85,000, 000 </p>

#################
# HTML Attributes
# If tag has attributes, tag id="boldest" has an attribute id whose value is boldest
# You can access a tag's attributes by treating tag like a dictionary:
tag_child['id']
# 'boldest'

# You can access that dictionary directly as attrs:
tag_child.attrs
# {'id': 'boldest'}

# We can also obtain content of attribute of tag using Python get() method
tag_child.get('id')
# 'boldest'

##################
# Navigable String
# string corresponds to a bit of text or content within a tag
# Beautiful Soup uses NavigableString class to contain this text
# In our HTML we can obtain name of first player by extracting string of Tag object tag_child as follows:
tag_string=tag_child.string
tag_string
# 'Lebron James'

# we can verify type is Navigable String
type(tag_string)
# bs4.element.NavigableString

# A NavigableString is similar to a Python string or Unicode string. 
# To be more precise, the main difference is that it also supports some BeautifulSoup features. 
# We can convert it to string object in Python:
unicode_string = str(tag_string)
unicode_string
# 'Lebron James'

# Filter
# Filters allow you to find complex patterns, simplest filter is a string
#
#%%html
#<table>
#  <tr>
#    <td id='flight' >Flight No</td>
#   <td>Launch site</td> 
#    <td>Payload mass</td>
#   </tr>
#  <tr> 
#    <td>1</td>
#    <td><a href='https://en.wikipedia.org/wiki/Florida'>Florida</a></td>
#    <td>300 kg</td>
#  </tr>
#  <tr>
#    <td>2</td>
#    <td><a href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td>
#    <td>94 kg</td>
#  </tr>
#  <tr>
#    <td>3</td>
#    <td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a> </td>
#    <td>80 kg</td>
#  </tr>
#</table>

# Flight No	 Launch site	Payload mass
#   1	     Florida	     300 kg
#   2	     Texas	         94 kg
#   3	     Florida	     80 kg

# We can store it as a string in variable table:
table="<table><tr><td id='flight'>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr> <td>1</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a></td><td>300 kg</td></tr><tr><td>2</td><td><a href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td><td>94 kg</td></tr><tr><td>3</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a> </td><td>80 kg</td></tr></table>"

##########
# find All
# find_all() method looks through a tag's descendants and retrieves all descendants that match your filters
# Method signature for find_all(name, attrs, recursive, string, limit, **kwargs)

# NAME
# When we set name parameter to a tag name, method will extract all tags with that name and its children

table_rows=table_bs.find_all('tr')
table_rows
# [<tr><td id="flight">Flight No</td><td>Launch site</td> <td>Payload mass</td></tr>,
# <tr> <td>1</td><td><a href="https://en.wikipedia.org/wiki/Florida">Florida</a><a></a></td><td>300 kg</td></tr>,
#  <tr><td>2</td><td><a href="https://en.wikipedia.org/wiki/Texas">Texas</a></td><td>94 kg</td></tr>,
#  <tr><td>3</td><td><a href="https://en.wikipedia.org/wiki/Florida">Florida</a><a> </a></td><td>80 kg</td></tr>]

# result is a Python iterable just like a list, each element is a tag object:
first_row =table_rows[0]
first_row
# <tr><td id="flight">Flight No</td><td>Launch site</td> <td>Payload mass</td></tr>

# type is tag
print(type(first_row))
# <class 'bs4.element.Tag'>

# we can obtain child
first_row.td
# <td id="flight">Flight No</td>

# If we iterate through the list, each element corresponds to a row in the table:
for i,row in enumerate(table_rows):
    print("row",i,"is",row)
# row 0 is <tr><td id="flight">Flight No</td><td>Launch site</td> <td>Payload mass</td></tr>
# row 1 is <tr> <td>1</td><td><a href="https://en.wikipedia.org/wiki/Florida">Florida</a><a></a></td><td>300 kg</td></tr>
# row 2 is <tr><td>2</td><td><a href="https://en.wikipedia.org/wiki/Texas">Texas</a></td><td>94 kg</td></tr>
# row 3 is <tr><td>3</td><td><a href="https://en.wikipedia.org/wiki/Florida">Florida</a><a> </a></td><td>80 kg</td></tr>

# As row is cell object, we can apply method find_all to it and extract table cells in object cells using tag td, this is all the children with the name td
# result is a list, each element corresponds to a cell and is a Tag object, we can iterate through this list as well 
# We can extract content using string attribute
for i,row in enumerate(table_rows):
    print("row",i)
    cells=row.find_all('td')
    for j,cell in enumerate(cells):
        print('colunm',j,"cell",cell)
# row 0
# colunm 0 cell <td id="flight">Flight No</td>
# colunm 1 cell <td>Launch site</td>
# colunm 2 cell <td>Payload mass</td>
# row 1
# colunm 0 cell <td>1</td>
# colunm 1 cell <td><a href="https://en.wikipedia.org/wiki/Florida">Florida</a><a></a></td>
# colunm 2 cell <td>300 kg</td>
# row 2
# colunm 0 cell <td>2</td>
# colunm 1 cell <td><a href="https://en.wikipedia.org/wiki/Texas">Texas</a></td>
# colunm 2 cell <td>94 kg</td>
# row 3
# colunm 0 cell <td>3</td>
# colunm 1 cell <td><a href="https://en.wikipedia.org/wiki/Florida">Florida</a><a> </a></td>
# colunm 2 cell <td>80 kg</td>

# If we use a list we can match against any item in that list
list_input=table_bs .find_all(name=["tr", "td"])
list_input
# [<tr><td id="flight">Flight No</td><td>Launch site</td> <td>Payload mass</td></tr>,
# <td id="flight">Flight No</td>,
# <td>Launch site</td>,
# <td>Payload mass</td>,
# <tr> <td>1</td><td><a href="https://en.wikipedia.org/wiki/Florida">Florida</a><a></a></td><td>300 kg</td></tr>,
# <td>1</td>,
# <td><a href="https://en.wikipedia.org/wiki/Florida">Florida</a><a></a></td>,
# <td>300 kg</td>,
# <tr><td>2</td><td><a href="https://en.wikipedia.org/wiki/Texas">Texas</a></td><td>94 kg</td></tr>,
# <td>2</td>,
# <td><a href="https://en.wikipedia.org/wiki/Texas">Texas</a></td>,
# <td>94 kg</td>,
# <tr><td>3</td><td><a href="https://en.wikipedia.org/wiki/Florida">Florida</a><a> </a></td><td>80 kg</td></tr>,
# <td>3</td>,
# <td><a href="https://en.wikipedia.org/wiki/Florida">Florida</a><a> </a></td>,
# <td>80 kg</td>]

# ATRIBUTES
# If argument is not recognized it will be turned into a filter on tag's attributes 
# For example with id argument, Beautiful Soup will filter against each tag's id attribute
# For example, the first td elements have a value of id of flight, therefore we can filter based on that id value
table_bs.find_all(id="flight")
# [<td id="flight">Flight No</td>]

# We can find all elements that have links to Florida Wikipedia page:
list_input=table_bs.find_all(href="https://en.wikipedia.org/wiki/Florida")
list_input
# [<a href="https://en.wikipedia.org/wiki/Florida">Florida</a>,
#  <a href="https://en.wikipedia.org/wiki/Florida">Florida</a>]

# If we set the href attribute to True, regardless of what value is, code finds all tags with href value:
table_bs.find_all(href=True)
# [<a href="https://en.wikipedia.org/wiki/Florida">Florida</a>,
#  <a href="https://en.wikipedia.org/wiki/Texas">Texas</a>,
# <a href="https://en.wikipedia.org/wiki/Florida">Florida</a>]

# Using the logic above, find all the elements without href value
table_bs.find_all(href=False)
# [<html><head></head><body><table><tbody><tr><td id="flight">Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr> <td>1</td><td><a href="https://en.wikipedia.org/wiki/Florida">Florida</a><a></a></td><td>300 kg</td></tr><tr><td>2</td><td><a href="https://en.wikipedia.org/wiki/Texas">Texas</a></td><td>94 kg</td></tr><tr><td>3</td><td><a href="https://en.wikipedia.org/wiki/Florida">Florida</a><a> </a></td><td>80 kg</td></tr></tbody></table></body></html>,
# <head></head>,
# <body><table><tbody><tr><td id="flight">Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr> <td>1</td><td><a href="https://en.wikipedia.org/wiki/Florida">Florida</a><a></a></td><td>300 kg</td></tr><tr><td>2</td><td><a href="https://en.wikipedia.org/wiki/Texas">Texas</a></td><td>94 kg</td></tr><tr><td>3</td><td><a href="https://en.wikipedia.org/wiki/Florida">Florida</a><a> </a></td><td>80 kg</td></tr></tbody></table></body>,
# <table><tbody><tr><td id="flight">Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr> <td>1</td><td><a href="https://en.wikipedia.org/wiki/Florida">Florida</a><a></a></td><td>300 kg</td></tr><tr><td>2</td><td><a href="https://en.wikipedia.org/wiki/Texas">Texas</a></td><td>94 kg</td></tr><tr><td>3</td><td><a href="https://en.wikipedia.org/wiki/Florida">Florida</a><a> </a></td><td>80 kg</td></tr></tbody></table>,
# <tbody><tr><td id="flight">Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr> <td>1</td><td><a href="https://en.wikipedia.org/wiki/Florida">Florida</a><a></a></td><td>300 kg</td></tr><tr><td>2</td><td><a href="https://en.wikipedia.org/wiki/Texas">Texas</a></td><td>94 kg</td></tr><tr><td>3</td><td><a href="https://en.wikipedia.org/wiki/Florida">Florida</a><a> </a></td><td>80 kg</td></tr></tbody>,
# <tr><td id="flight">Flight No</td><td>Launch site</td> <td>Payload mass</td></tr>,
# <td id="flight">Flight No</td>,
# <td>Launch site</td>,
# <td>Payload mass</td>,
# <tr> <td>1</td><td><a href="https://en.wikipedia.org/wiki/Florida">Florida</a><a></a></td><td>300 kg</td></tr>,
# <td>1</td>,
# <td><a href="https://en.wikipedia.org/wiki/Florida">Florida</a><a></a></td>,
# <a></a>,
# <td>300 kg</td>,
# <tr><td>2</td><td><a href="https://en.wikipedia.org/wiki/Texas">Texas</a></td><td>94 kg</td></tr>,
# <td>2</td>,
# <td><a href="https://en.wikipedia.org/wiki/Texas">Texas</a></td>,
# <td>94 kg</td>,
# <tr><td>3</td><td><a href="https://en.wikipedia.org/wiki/Florida">Florida</a><a> </a></td><td>80 kg</td></tr>,
# <td>3</td>,
# <td><a href="https://en.wikipedia.org/wiki/Florida">Florida</a><a> </a></td>,
# <a> </a>,
# <td>80 kg</td>]

# Using soup object soup, find element with id attribute content set to "boldest"
soup.find_all(id="boldest")
# [<b id="boldest">Lebron James</b>]

# string
# With string you can search for strings instead of tags, where we find all elments with Florida:
 table_bs.find_all(string="Florida")

# find
# find_all() method scans entire document looking for results. 
# It’s useful if you are looking for one element, as you can use find() method to find first element in document
# Consider the following two tables:

# %%html
# <h3>Rocket Launch </h3>

# <p>
#<table class='rocket'>
#  <tr>
#    <td>Flight No</td>
#    <td>Launch site</td> 
#    <td>Payload mass</td>
#  </tr>
#  <tr>
#    <td>1</td>
#    <td>Florida</td>
#    <td>300 kg</td>
#  </tr>
#  <tr>
#    <td>2</td>
#    <td>Texas</td>
#    <td>94 kg</td>
#  </tr>
#  <tr>
#    <td>3</td>
#    <td>Florida </td>
#    <td>80 kg</td>
#  </tr>
#</table>
#</p>
#<p>

#<h3>Pizza Party  </h3>
  
    
#<table class='pizza'>
#  <tr>
#    <td>Pizza Place</td>
#    <td>Orders</td> 
#    <td>Slices </td>
#   </tr>
#  <tr>
#    <td>Domino's Pizza</td>
#    <td>10</td>
#    <td>100</td>
#  </tr>
#  <tr>
#    <td>Little Caesars</td>
#    <td>12</td>
#    <td >144 </td>
#  </tr>
#  <tr>
#    <td>Papa John's </td>
#    <td>15 </td>
#    <td>165</td>
#  </tr>

# store HTML as a Python string and assign two_tables:
two_tables="<h3>Rocket Launch </h3><p><table class='rocket'><tr><td>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr><td>1</td><td>Florida</td><td>300 kg</td></tr><tr><td>2</td><td>Texas</td><td>94 kg</td></tr><tr><td>3</td><td>Florida </td><td>80 kg</td></tr></table></p><p><h3>Pizza Party  </h3><table class='pizza'><tr><td>Pizza Place</td><td>Orders</td> <td>Slices </td></tr><tr><td>Domino's Pizza</td><td>10</td><td>100</td></tr><tr><td>Little Caesars</td><td>12</td><td >144 </td></tr><tr><td>Papa John's </td><td>15 </td><td>165</td></tr>"

# create a BeautifulSoup object two_tables_bs
two_tables_bs= BeautifulSoup(two_tables, 'html.parser')

# find first table using tag name table
two_tables_bs.find("table")
# <table class="rocket"><tr><td>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr><td>1</td><td>Florida</td><td>300 kg</td></tr><tr><td>2</td><td>Texas</td><td>94 kg</td></tr><tr><td>3</td><td>Florida </td><td>80 kg</td></tr></table>

# We can filter on class attribute to find second table, but because class is a keyword in Python, we add an underscore to differentiate them
two_tables_bs.find("table",class_='pizza')
# <table class="pizza"><tr><td>Pizza Place</td><td>Orders</td> <td>Slices </td></tr><tr><td>Domino's Pizza</td><td>10</td><td>100</td></tr><tr><td>Little Caesars</td><td>12</td><td>144 </td></tr><tr><td>Papa John's </td><td>15 </td><td>165</td></tr></table>

# Downloading And Scraping The Contents Of A Web Page
# Download contents of web page:
url = "http://www.ibm.com"

# use get to download contents of webpage in text format and store in a variable called data:
data  = requests.get(url).text 

# create a BeautifulSoup object using the BeautifulSoup constructor
soup = BeautifulSoup(data,"html5lib")  # create a soup object using the variable 'data'

Scrape all links
for link in soup.find_all('a',href=True):  # in html anchor/link is represented by the tag <a>
    print(link.get('href'))
https://www.ibm.com/cloud?lnk=intro

# Scrape all images Tags
for link in soup.find_all('img'):# in html image is represented by the tag <img>
    print(link)
    print(link.get('src'))
# <img alt="Portraits of IBM consultants" class="bx--image__img" id="image--984377471" loading="lazy" src="/content/dam/adobe-cms/default-images/home-consultants.component.crop-16by9-xl.ts=1697468608831.jpg/content/adobe-cms/us/en/homepage/_jcr_content/root/table_of_contents/simple_image"/>
# /content/dam/adobe-cms/default-images/home-consultants.component.crop-16by9-xl.ts=1697468608831.jpg/content/adobe-cms/us/en/homepage/_jcr_content/root/table_of_contents/simple_image

Scrape data from HTML tables
#The below url contains an html table with data about colors and color codes.
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/HTMLColorCodes.html"

# Before proceeding to scrape a web site, you need to examine contents and way data is organized on website
# Open the above url in your browser and check how many rows and columns there are in color table
# get the contents of the webpage in text format and store in a variable called data
data  = requests.get(url).text
soup = BeautifulSoup(data,"html5lib")

#find a html table in the web page
table = soup.find('table') # in html table is represented by the tag <table>

#Get all rows from the table
for row in table.find_all('tr'): # in html table row is represented by the tag <tr>
    # Get all columns in each row.
    cols = row.find_all('td') # in html a column is represented by the tag <td>
    color_name = cols[2].string # store the value in column 3 as color_name
    color_code = cols[3].text # store the value in column 4 as color_code
    print("{}--->{}".format(color_name,color_code))
# Color Name--->Hex Code#RRGGBB
# lightsalmon--->#FFA07A
# salmon--->#FA8072
# darksalmon--->#E9967A
# lightcoral--->#F08080
# coral--->#FF7F50
# tomato--->#FF6347
# orangered--->#FF4500
# gold--->#FFD700
# orange--->#FFA500
# darkorange--->#FF8C00
# lightyellow--->#FFFFE0
# lemonchiffon--->#FFFACD
# papayawhip--->#FFEFD5
# moccasin--->#FFE4B5
# peachpuff--->#FFDAB9
# palegoldenrod--->#EEE8AA
# khaki--->#F0E68C
# darkkhaki--->#BDB76B
# yellow--->#FFFF00
# lawngreen--->#7CFC00
# chartreuse--->#7FFF00
# limegreen--->#32CD32
# lime--->#00FF00
# forestgreen--->#228B22
# green--->#008000
# powderblue--->#B0E0E6
# lightblue--->#ADD8E6
# lightskyblue--->#87CEFA
# skyblue--->#87CEEB
# deepskyblue--->#00BFFF
# lightsteelblue--->#B0C4DE
# dodgerblue--->#1E90FF