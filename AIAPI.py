# Application Programming Interface
# API lets two pieces of software talk to each other 
# Just like a function, you don't have to know how the API works, only its inputs and outputs
# essential type of API is a REST API that allows you to access resources via the internet

# Pandas is an API
# Pandas is actually set of software components, much of which is not even written in Python
import pandas as pd
import matplotlib.pyplot as plt

# You create a dictionary, this is just data
dict_={'a':[11,21,31],'b':[12,22,32]}

# When you create a Pandas object with the dataframe constructor, in API lingo this is an "instance"
# data in dictionary is passed along to pandas API
# then use dataframe to communicate with API
df=pd.DataFrame(dict_)
type(df)
# pandas.core.frame.DataFrame

# Python Program    --------------> 1.  Other Software Component 
#                         Data
# Python Program    <-------------- 2.  Other Software Component 

# When you call method head dataframe communicates with API displaying first few rows of dataframe
df.head()
#    	a	b
#    0	11	12
#    1	21	22
#    2	31	32

# When you call method mean, API will calculate mean and return value
df.mean()
# a    21.0
# b    22.0
# dtype: float64

###################################################################################################
# REST APIs
#
# Rest API's function by sending a request, request is communicated via HTTP message 
# HTTP message usually contains a JSON file
# This contains instructions for what operation we would like the service or resource to perform
# In a similar manner, API returns a response, via an HTTP message, this response is usually contained within a JSON
#
# When you use a web page your browser sends HTTP request to server where page is hosted
# Server tries to find desired resource by default "index.html"
# If your request is successful, the server will send object to client in an HTTP response
# This includes information like type of resource, length of resource, and other information
#
# HTTP protocol allows you to send and receive information through web including webpages, images, web resources
#
#                   Request
# Client/You    --------------> 1.  Web Server -:
#                      Response                 : index.html, image.png, File.txt
# Client/You    <-------------- 2.  Web Server -:
#
###############################
# Uniform Resource Locator: URL
#
# most popular way to find resources on the web
# parts of URL: 

# Scheme: protocol = http://
# Internet address or Base URL: location www.ibm.com, www.gitlab.com 
# Route: location on web server: /images/IDSNlogo.png

#########
# Request
#
# - GET method, this is an HTTP method.
# - location of the resource /index.html
# - HTTP version = /1.0
# - request header passes additional information with an HTTP request
# HTTP request is made, 
# HTTP method is sent (tells server what action to perform)
# :----------------------------------------------------------:
# : Request Start line :  Get/index.html HTTP/1.0            :
# :--------------------:-------------------------------------:
# : Request Header     : User-Agent: python-requests/2.21.0  :
# :                    : Accept-Encoding: gzip, deflate      :
# :----------------------------------------------------------:
#
#
#
#
#
#
#
