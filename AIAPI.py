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
# :----------------------------------------------------------:
# : GET                :  Retrieves Data from server         :
# :                    :                                     :
# :--------------------:-------------------------------------:
# : POST               :       Submits data to server        :
# :                    :                                     :
# :----------------------------------------------------------:
# : PUT                :    Updates data already on server   : 
# :                    :                                     :
# :--------------------:-------------------------------------:
# : DELETE             :     Retrieves Data from server      :
# :                    :                                     :
# :----------------------------------------------------------:
#
# Response
#
# - response header contains useful information
# - version number HTTP/1.0
# - status code (200) meaning success
# - followed by a descriptive phrase (OK)
# :----------------------------------------------------------:
# : Response Start Line: HTTP/1.0 200 OK                     :
# :--------------------:-------------------------------------:
# : Response Header    : Server: Apache-                     :
# :                    : Cache:UNCHACHEABLE                  :
# :--------------------:-------------------------------------:
# : Response Body      : <!DOCTYPE html>                     :
# :                    : <html> </html>                      :
# :----------------------------------------------------------:
#
#
# status codes (examples)
# :----------------------------------------------------------:
# : 1xx                :  Informational                      :
# :                    :                                     :
# :--------------------:-------------------------------------:
# : 2xx                : Success                             :
# : 200                : OK                                  :
# :----------------------------------------------------------:
# : 3xx                : Redirection                         : 
# : 300                : Multiple Choices                    :
# :--------------------:-------------------------------------:
# : 4xx                : Client error                        :
# : 401                : Unauthorized                        :
# : 403                : Forbidden                           :
# : 404                : Not Found                           :
# :----------------------------------------------------------:
#
#################### 
# Requests in Python
#
# Requests is a Python Library that allows you to send HTTP/1.1 requests easily
# We can import the library as follows
import requests

# GET request via method GET to www.ibm.com
url='https://www.ibm.com/'
r=requests.get(url)
 
# view the status code using attribute (status_code)
r.status_code #200

# view request headers
print(r.request.headers)
# Parameters and response from web server 
# {'User-Agent': 'python-requests/2.29.0', 'Accept-Encoding': 'gzip, deflate, br', 'Accept': '*/*', 'Connection':
# 'keep-alive', 'Cookie': 
# '_abck=B66F82282229C1DE96822B95B1FA9E20~-1~YAAQk2rcF+WEhkGLAQAAsvPZRArK/jJe0ZOWzuNS07ozM5HnviHHufPXDhpeFk2i
# FGuqs2bk1ulzdvDTpqayMXmSH7qYHa8+Isl7jf+3tkak4JpE/2i7vuS3m5xKvSToaW10ZJA1XLK8g0mWMiA8R0plyD6itQ9su65rWHa9gFY8
# jgQ6fOiVwmp/afRSYVxarj0AiIv9CCg5iDHX+QNjPKUTLdNL+Nr15sGVnA1Z9dhcrw8Xsjtp8Iu8PnVp9SswimQ+tfBXzhPOjdp4at0URRkUM+
# AeebbHMBuTd0onIWis22/Fjqm6DDzN79zOLb7ipUrpfnYV71PEH5XwNxHELcqvQWPmCsEbiqtKaE5Y6derJ
# +7ZnIk=~-1~-1~-1; bm_sz=98D468F1AAEBF983FE59C36961207F58~YAAQk2rcF+aEhkGLAQAAsvPZRBXmGHnytNSzAxPir/i
# Cmuu9pHJt3UvM07dKOFINYsRaACIghk16lsespLXcpYN2GNbycF8tC3x+XjfHFWsOnyYYCBdPKjfUSctCIe71/KkDZPTYeo6y0Fk11s/
# MhwnFeFfxp5j89zX6fk4QXucADa+rTl4tFgtUUouE3qnIuTQcGOKBcSjdnIytvrZPvYaUxBHZfqz5j10hAD
# PECJ35vd3MH+XaFEcbBHCs2bVS1nMwwtb6LwdZkVVC7yScEdFU+nFkiv2WLsgupNO8P4Y=~3556914~3752753'}

# view HTTP response header, returns python dictionary of HTTP response headers
header=r.headers
print(r.headers)
# {'Content-Type': 'text/html;charset=utf-8', 'X-Dispatcher': 'prod-east-publish-0', 'X-Vhost': 'publish', 
# 'X-Content-Type-Options': 'nosniff', 'Last-Modified': 'Thu, 19 Oct 2023 08:27:21 GMT', 'X-Frame-Options': 
# 'SAMEORIGIN', 'CF-Cache-Status': 'DYNAMIC', 'Server': 'cloudflare', 'CF-RAY': '8187ad62c83a2429-IAD',
# 'Cache-Control': 'max-age=289', 'Expires': 'Thu, 19 Oct 2023 08:48:24 GMT', 'X-Akamai-Transformed': 
# '9 12476 0 pmb=mTOE,2', 'Content-Encoding': 'gzip', 'Date': 'Thu, 19 Oct 2023 08:43:35 GMT', 
# 'Content-Length': '12713', 'Connection': 'keep-alive', 'Vary': 'Accept-Encoding', 
# 'Strict-Transport-Security': 'max-age=31536000'}

# obtain the date
header['date'] # 'Thu, 19 Oct 2023 08:43:35 GMT'

# Content-Type indicates the type of data
header['Content-Type'] # 'text/html;charset=utf-8'

# encoding
r.encoding # 'utf-8'

# Content-Type is text/html = attribute text to display HTML in body
# - review the first 100 characters
r.text[0:100]
# '\n<!DOCTYPE HTML>\n<html lang="en-us">\n<head>\n    \n    \n    \n    \n    <meta charset="UTF-8"/>\n    <met'

########
# images
url='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/IDSNlogo.png'
r=requests.get(url)

print(r.headers)
# {'Date': 'Thu, 19 Oct 2023 08:48:00 GMT', 'X-Clv-Request-Id': '2beb5790-311e-4ca8-9fd2-66e526808d62', 
# 'Server': 'Cleversafe', 'X-Clv-S3-Version': '2.5', 'Accept-Ranges': 'bytes', 'x-amz-request-id': 
# '2beb5790-311e-4ca8-9fd2-66e526808d62', 'ETag': '"8bb44578fff8fdcc3d2972be9ece0164"', 
# 'Content-Type': 'image/png', 'Last-Modified': 'Wed, 16 Nov 2022 03:32:41 GMT', 'Content-Length': '78776'}

r.headers['Content-Type']
# 'image/png'

# image is response object that contains image as bytes-like object
# save it using a file object(specify the file path and name)
path=os.path.join(os.getcwd(),'image.png')
path
# '/resources/labs/authoride/IBMSkillsNetwork+PY0101EN/jupyterlite/files/Module 5/image.png'

# save file -> access body of response use attribute content -> save it using open function -> write method
with open(path,'wb') as f:
    f.write(r.content)
# view image 
    Image.open(path)  
    