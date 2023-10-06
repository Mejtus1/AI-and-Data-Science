#Types 
# int = 11
# float = 21.123

#Typecasting (changing data types)
# changing int to float 

#Boolean 
#True or False

#Exercise: 
#What version of Python are we using
import sys
print(sys.version)¨
#3.11.2 (main, May  3 2023, 04:00:05) Clang 17.0.0 
#(https://github.com/llvm/llvm-project) df82394e7a2d06506718cafa347b

print("Hello world!")

print(type(12.0)) #<class 'float'>
type(float(2)) #Convert integer 2 to a float
int(1.1) #Casting 1.1 to integer will result in loss of information

############################################################################################
#Expressions and Variables
#Expressions describe a type of operation the computers perform
#Expressions are operations the python performs

#Methematical expressions 
print(5+5)
print(4-4)
print(4*4)
print(4/4)
print(25//6) 
#python follows mathematical conventions 

#Variables
my_variable = 1
print(my_variable)
#Variable names should be correlated with values or value they represent 

##
#Exercises:
name = "Michael Jackson"
print(name[0]) #M
print(name[6]) #l
print(name[13]) #o
#negative indexing:
print(name[-1]) #n
print(name[-15]) #M
#number of characters in a string
len("Michael Jackson") #15
#obtain multiple characters from a string using slicing
name[0:4] #'Mich'
name[8:12] #'Jack'
#Stride
#every second element 
print(name[::2]) #'McalJcsn'
print(name[0:5:2]) #'Mca'

#Concatenate Strings
statement = name + "is the best" # Concatenate two strings
3 * "Michael Jackson" # Print the string for 3 times

#Escape Sequences
print(" Michael Jackson \n is the best" ) # New line escape sequence
print(" Michael Jackson \t is the best" ) # Tab escape sequence

#String Operations
a = "Thriller is the sixth studio album"
print("before upper:", a)
b = a.upper() #THRILLER IS THE SIXTH STUDIO ALBUM
print("After upper:", b)
# Convert all the characters in string to upper case

# Replace the old substring with the new target substring is the segment has been found in the string
a = "Michael Jackson is the best"
b = a.replace('Michael', 'Janet')
b #'Janet Jackson is the best'



############################################################################################
#String Operations 
#String is a sequence of characters 
Name = "Vicky"
#each Character is represented by a index (starts at 0) 
#V = 0, i = 1, c = 2, k = 3, y = 4

#we can concatenate strings 
Name = "Vicky"
Statement = Name + "is my name"
print(Statement)
3* "Vicky" #3 copies of the string 

#\n represents a new line in a string
print("Hello, my name is \n Vicky") 

#String Methods and functinos 
#.upper()
A="Hey there"
B = A.upper() #value of B is similar to A but all the characters ale upper case

C = "Hey there"
D = C.replace("Hey","hello") #replaces Hey with hello



############################################################################################
#Lists and Touples
#one of key data types in python 

#Touples 
#Touples are an oredered sequence
#Touples are written as comma- separated elements within parentheses
Ratings = (10,9,6,5,10,8,9,6,2)
touple1 = ("disco",10,1.2) #more data types
# all touples can be accesed through an index
touple1[0] #"disco"
touple1[1] #"10"
touple1[2] #"1.2"

say_what=('say',' what', 'you', 'will')
say_what[-1] #'will'

#Touples Slicing 
tuple A=(1,2,3,4,5)
A[1:4] #(2, 3, 4)
#picking touple numbers is always one number larger than we want 

#Touple Length
tuple B=(1,2,3,4,5)
len(B) #5

#Touples are immutable 
ratings = (10, 9, 1, 8, 7, 8, 5, 7, 5)
ratings1 = ratings 
ratings[1] # = 
ratings1[1] # = 
#when we change something in ratings1 it doesnt change in ratings 
ratings = (5, 7, 3, 10)

#Touple Nesting
#a touple can contain another touples 
NT = (1, 2, ("pop", "rock"),(3,4),("disco",(1,2)))
NT[0][1]# = 1, 2
NT[2][1]# = "rock"
NT[2][1]# = 3
NT[2][1]# = "disco"
#We can even access Elements and characters inside Touples 
NT[2][1][1]# = "r"

#Touple Exercises
tuple1 = ("disco",10,1.2 ) #('disco', 10, 1.2)
type(tuple1) #touple
# Print the variable on each index
print(tuple1[0]) #disco
print(tuple1[1]) #10
print(tuple1[2]) #1.2
print(type(tuple1[0])) #<class 'str'>
print(type(tuple1[1])) #<class 'int'>
print(type(tuple1[2])) #<class 'float'>
# Use negative index
tuple1[-1] #1.2
# Concatenate two tuples
tuple2 = tuple1 + ("hard rock", 10)
tuple2 #('disco', 10, 1.2, 'hard rock', 10)
# Slice from index 0 to index 2
tuple2[0:3] #('hard rock', 10)
# Get the length of tuple
len(tuple2) #5

Ratings = (0, 9, 6, 5, 10, 8, 9, 6, 2)
# Sort the tuple
RatingsSorted = sorted(Ratings)
RatingsSorted #[0, 2, 5, 6, 6, 8, 9, 9, 10]

# Create a nest tuple
NestedT =(1, 2, ("pop", "rock") ,(3,4),("disco",(1,2)))

# Print element on each index
print("Element 0 of Tuple: ", NestedT[0]) #1
print("Element 1 of Tuple: ", NestedT[1]) #2
print("Element 2 of Tuple: ", NestedT[2]) #('pop', 'rock')
print("Element 3 of Tuple: ", NestedT[3]) #(3, 4)
print("Element 4 of Tuple: ", NestedT[4]) #('disco', (1, 2))

# Print element on each index, including nest indexes
print("Element 2, 0 of Tuple: ",   NestedT[2][0]) #pop  
print("Element 2, 1 of Tuple: ",   NestedT[2][1]) #rock
print("Element 3, 0 of Tuple: ",   NestedT[3][0]) #3
print("Element 3, 1 of Tuple: ",   NestedT[3][1]) #4
print("Element 4, 0 of Tuple: ",   NestedT[4][0]) #disco
print("Element 4, 1 of Tuple: ",   NestedT[4][1]) #(1,2)

# Print the first element in the second nested tuples
NestedT[2][1][0] #'r'
# Print the second element in the second nested tuples
NestedT[2][1][1] #'o'

# sample tuple
genres_tuple = ("pop", "rock", "soul", "hard rock", "soft rock", \
                "R&B", "progressive rock", "disco") 
len(genres_tuple) # 8
# Access the element, with respect to index 3
genres_tuple[3] #'hard rock'
# Use slicing to obtain indexes 3, 4 and 5
genres_tuple[3:6] #('hard rock', 'soft rock', 'R&B')
# Find the first two elements of the tuple genres_tuple
genres_tuple[0:2]
# Find the first index of "disco"
genres_tuple.index("disco")

#LISTS
# - lists are oslo ordered sequences
# - lists are peresnted with square brackets
# - list is MUTABLE
L = ["Vicky", 10.1, 2001,[12002]]

B=[1,2,[3,'a'],[4,'b']]
B[3][1] #"b"

#[1,2,3]+[1,1,1] = [1, 2, 3, 1, 1, 1]

.append and .extend
G = [1,2,3]
G.extend [1,2,3] #[1,2,3,1,2,3]

H = ["Vicky", "Guy", 11]
H.append ["Vicky2", "Vicky3"] #["Vicky", "Guy", 11,["Vicky2", "Vicky3"]]

#deleting an element from a list 
I = ["Vicky2", "Vicky3"]
del(A[1]) #Deletes "Vicky3"

#Converting a string to a LIST 
#The method split separates a string into a list based on the argument. 
#If there is no argument as in this case the string is split using spaces
"Hello Mike".split() #["Hello","Mike"]
"A,B,C,D".split(",") #["A","B","C","D"]

#Aliasing 
#Multiple Lists reffering to the same object is known as aliasing

##
#Exercises:
#create a list
L = ["Michael Jackson", 10.1, 1982] # # #

#Lists can contain strings, floats, and integers
["Michael Jackson", 10.1, 1982, [1, 2], ("A", 1)]

#last two elements
G = ["Michael Jackson", 10.1,1982,"MJ",1]
G[3:5] #['MJ', 1]

#add new elements to the list
L = [ "Michael Jackson", 10.2]
L.extend(['pop', 10])
L #['Michael Jackson', 10.2, 'pop', 10]

#As lists are mutable, we can change them
# Change the element based on the index
A = ["disco", 10, 1.2]
print('Before change:', A)
A[0] = 'hard rock'
print('After change:', A)

#delete an element of a list
# Split the string, default is by space
'hard rock'.split() #['hard', 'rock']

#Split the string by comma
'A,B,C,D'.split(',') #['A', 'B', 'C', 'D']

#Copy and Clone List
#When we set one variable B equal to A, both A and B are referencing the same list in memory
A = ["hard rock", 10, 1.2]
B = A
print('A:', A) A: #['hard rock', 10, 1.2]
print('B:', B) B: #['hard rock', 10, 1.2]

#You can clone list A by using the following syntax
# Clone (clone by value) the list A
B = A[:]
B

#Create a list a_list, with the following elements 1, hello, [1,2,3] and True
a_list = [1, "hello", [1,2,3], True]
print(a_list)
#Find the value stored at index 1 of a_list
a_list[1]
#Retrieve the elements stored at index 1, 2 and 3 of a_list
a_list[1:4]
#Concatenate the following lists A = [1, 'a'] and B = [2, 1, 'd']
A = [1, 'a'] 
B = [2, 1, 'd']
A + B

#Shopping list 

#Create an empty list
Shopping_list=[]
#Now store the number of items to the shopping_list
Shopping_list=["Watch","Laptop","Shoes","Pen","Clothes"]
#Add a new item to the shopping_list
Shopping_list.append("Football")
#Print First item from the shopping_list
print(Shopping_list[0])
#Print Last item from the shopping_list
print(Shopping_list[-1])
#Print the entire Shopping List
print(Shopping_list)
#Print the item that are important to buy from the Shopping List
print(Shopping_list[1:3])
#Change the item from the shopping_list
Shopping_list[3] = "Notebook"
#Delete the item from the shopping_list that is not required
del (shopping_list[4])

############################################################################################
#Dictionaries
#type of collection 
#dictionary has keys and values 
#dictionaries are denoted with curly Brackets {}
#the keys have to be immutable and unique
#the values can be immutable, mutable and duplicates
#Each key and value pair is spearated by comma 

{"key":1, "key2":"2", "key3":[1,2,3], "key4":(4,5,3)}

{"a":1,"b":2} #keys = "a","b"

Dict={"A":1,"B":"2","C":[3,3,3],"D":(4,4,4),'E':5,'F':6}
Dict["D"] #(4, 4, 4)

DICTA["Thriller": "1982", "Back in Black": "1980", "The Bodyguard":"1992"] 
DICTA["Graduation"] = "2007" #Adds value 2007 with new key code Graduation
"The Bodyguard"in DICTA  #"The Bodyguard":"1992"

del(DICT["Thriller"]) #gets rid of the key Thriller

#to see ale the keys in the dictionary we use method .keys
DICTA.keys() #outputs DICTA
DICTA.values() #returns values 

############################################################################################
#Sets
#- are type of collection like touples and lists
#- are unordered (do not record element position)
#- have only unique elements (there is only one particular element in a set)
#- to define a set are used Curly brackets
#- when set is created with duplicated items, they will not be present once the set is created

{"A","A"} #set will only contain value once {"A"} 

#typecasting
#lists can be converted to sets using function set()
type(set([1,2,3])) # set will be created

#.add()
#add an element to a set 

#.remove()
#deletes and element from set 

#in 
#looks for an item in set 
"Who" in set

#unionized containtment elements in sets
{'a','b'} & {'a'} # {'a'} (outputs only elements which are in both sets)

album_set_1 = {"Bon Apetit", "Last Friday Night", "E.T."}
album_set_3 = {"Bon Apetit", "Last Friday Night"}
album_set_3.issubset(album_set1) = True

#SETS EXERCISES
set1 = {"pop", "rock", "soul", "hard rock", "rock", "R&B", "rock", "disco"}
set1

# Convert list to set
album_list = [ "Michael Jackson", "Thriller", 1982, "00:42:19", \
              "Pop, Rock, R&B", 46.0, 65, "30-Nov-82", None, 10.0]
album_set = set(album_list)             
album_set

#Set Operations
# Sample set
A = set(["Thriller", "Back in Black", "AC/DC"])
# Add element to set
A.add("NSYNC")
# Try to add duplicate element to the set
A.add("NSYNC") # nothing will happen as there can be no duplicates in a set
# Remove the element from set
A.remove("NSYNC")

#Sets Logic Operations
album_set1 = set(["Thriller", 'AC/DC', 'Back in Black'])
album_set2 = set([ "AC/DC", "Back in Black", "The Dark Side of the Moon"])
print(album_set1, album_set2)
# intersect of two sets
intersection = album_set1 & album_set2
# Find the difference in set1 but not set2
album_set1.difference(album_set2)  
# Find the union of two sets
album_set1.union(album_set2)


############################################################################################
#Conditions and Branching 
equal: ==
not equal: !=
greater than: >
less than: <
greater than or equal to: >=
less than or equal to: <=
Comparison Operators

# Condition Equal
a = 5
a == 6 #False

# Greater than Sign
i = 6
i > 5 #True

# Inequality Sign
i = 2
i != 6 #True
i != 2 #False

# Use Equality sign to compare the strings
"ACDC" == "Michael Jackson" #False
# Use Inequality sign to compare the strings
"ACDC" != "Michael Jackson" #True
#A	65	N	78	a	97	n	110
#B	66	O	79	b	98	o	111
#C	67	P	80	c	99	p	112
#D	68	Q	81	d	100	q	113
#E	69	R	82	e	101	r	114
#F	70	S	83	f	102	s	115
#G	71	T	84	g	103	t	116
#H	72	U	85	h	104	u	117
#I	73	V	86	i	105	v	118
#J	74	W	87	j	106	w	119
#K	75	X	88	k	107	x	120
#L	76	Y	89	l	108	y	121
#M	77	Z	90	m	109	z	122
# Compare characters
'B' > 'A' #True 66 > 65
# Compare characters
'BA' > 'AB' #True (first letter takes precedence in ordering)

Branching (if else elif statements)
Branching allows us to run different statements for different inputs

# If statement example
age = 19
#expression that can be true or false
if age > 18:
    #expression that is run if the condition is true
    print("you can enter" ) #you can enter
#The statements after the if statement will run regardless if the condition is true or false 
print("move on")

#The else statement runs a block of code if none of the conditions are True before it 
# Else statement example
age2 = 18

if age2 > 18:
    print("you can enter" )
else:
    print("go see Meat Loaf" ) # go see Meat Loaf
print("move on")

#The elif statement, short for else if, allows us to check
#additional conditions if the condition statements before it are False

# Elif statment example
age3 = 18

if age3 > 18:
    print("you can enter" )
elif age3 == 18:
    print("go see Pink Floyd")
else:
    print("go see Meat Loaf" )

print("move on")


# Condition statement example
album_year = 1983

if album_year > 1980:
    print("Album year is greater than 1980")
else:
    print("less than 1980")

print('do something..')

# Logical operators
# used when you want to compare more than one condition
# and, or, not
#The and statement is only True when both conditions are true
# Condition statement example
album_year3 = 1990

if(album_year3 < 1980) or (album_year3 > 1989):
    print ("Album was not made in the 1980's")
else:
    print("The Album was made in the 1980's ")

# Condition statement example
album_year = 1983 # The not statement checks if the statement is false
if not (album_year == 1984):
    print ("Album year is not 1984")

#QUIZ
#Write an if statement to determine if an album had a rating greater than 8
rating = 8.5
if rating > 8:
    print ("This album is Amazing!")
#Part2
rating2 = 8
if rating2 > 8:
    print("This album is Amazing!")
else:
    print("Album is OK.")
#Part3
album4 = 1991
if album4 < 1980:
    print("Album came out before 1980.")
elif album4 == 1991 or album4 == 1993:
    print("Album came out in year 1991 or 1993")

############################################################################################
#Loops in Python
#repeated executions are performed by loops

#What is for loop?
#The for loop enables you to execute a code block multiple times
# For loop example
dates = [1982,1980,1973]
N = len(dates)
for i in range(N):
    print(dates[i])  

#sequence of numbers from 0 to 7
for i in range(0, 8):
    print(i)

# Use for loop to change the elements in list
squares = ['red', 'yellow', 'green', 'purple', 'blue']
for i in range(0, 5):
    print("Before square ", i, 'is',  squares[i])
    squares[i] = 'white'
    print("After square ", i, 'is',  squares[i])

# Loop through the list and iterate on both index and element value
squares=['red', 'yellow', 'green', 'purple', 'blue']
for i, square in enumerate(squares):
    print(i, square)

#What is while loop
#keep executing a code block until a certain condition is met
# While Loop Example
dates = [1982, 1980, 1973, 2000]
i = 0
year = dates[0]

while(year != 1973):    
    print(year)
    i = i + 1
    year = dates[i]
    
print("It took ", i ,"repetitions to get out of loop.")

#Exercises:
#Write a for loop that prints out all the elements between -5 and 5 using the range function
for i in range(-5, 5):
    print(i)

#Print the elements of the following list
Genres=[ 'rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop']
for Genre in Genres:
    print(Genre)

#Write a for loop that prints out the following list
for square in squares:
    print(square)

#Write a while loop...
PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
i = 0
Rating = PlayListRatings[0]
while(i < len(PlayListRatings) and Rating >= 6):
    print(Rating)
    i = i + 1 # This prints the value 10 only once 
    Rating = PlayListRatings[i]
    i = i + 1 #Try uncommenting the line and comment the previous i = i + 1, 
    #and see the difference, 10 value will get printed twice because when the loop starts it will print Rating and then with PlayListRatings[0], it will again assign the value 10 to Ratings.

#Write a while loop...
squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
new_squares = []
i = 0
while(i < len(squares) and squares[i] == 'orange'):
    new_squares.append(squares[i])
    i = i + 1
print (new_squares)
############################################################################################
#Functions in Python

#Functions
#There are two types of functions :
#Pre-defined functions
#User defined functions
#What is a Function?
#You can define functions to provide the required functionality. Here are simple rules to define a function in Python:

#Functions blocks begin def followed by the function name and parentheses ().
#There are input parameters or arguments that should be placed within these parentheses.
#You can also define parameters inside these parentheses.
#There is a body within every function that starts with a colon (:) and is indented.
#You can also place documentation before the body.
#The statement return exits a function, optionally passing back a value

#First function example: Add 1 to a and store as b
def add(a):
    """
    add 1 to a
    """
    b = a + 1
    print(a, "if you add one", b)
    return(b)

# Get a help on add function
help(add)  #add 1 to a

# Call the function add()
add(1)  #1 if you add one 2

# Call the function add()
add(2)  #2 if you add one 3


# Define a function for multiple two numbers
def Mult(a, b):
    c = a * b
    return(c)
    print('This is not printed')
result = Mult(12,2)
print(result) #24

# Use mult() multiply two integers
Mult(2, 3) #6

# Use mult() multiply two floats
Mult(10.0, 3.14) #31.40

# Use mult() multiply two different type values together
Mult(2, "Michael Jackson ")
# But later in a program it can cause us an issues since it will expect integers and get strings

#Variables
#The input to a function is called a formal parameter
#A variable that is declared inside a function is called a local variable. 
#The parameter only exists within the function (i.e. the point where the function starts and stops).
#A variable that is declared outside a function definition is a global variable, 
#and its value is accessible and modifiable throughout the program. We will discuss more about global variables at the end of the lab.

# Function Definition
def square(a):
    # Local variable b
    b = 1
    c = a * a + b
    print(a, "if you square + 1", c) 
    return(c)

#If there is no return statement, the function returns None
def MJ():
    print('Michael Jackson')
    
def MJ1():
    print('Michael Jackson')
    return(None)
# See the output
MJ()
MJ1()

#Create a function con that concatenates two strings using the addition operation:
# See what functions returns are
print(MJ())
print(MJ1())

#Functions Make Things Simple
#Consider the two lines of code in Block 1 and Block 2: the procedure for each block is identical. 
#The only thing that is different is the variable names and values

#Block 1:
# a and b calculation block1
a1 = 4
b1 = 5
c1 = a1 + b1 + 2 * a1 * b1 - 1
if(c1 < 0):
    c1 = 0 
else:
    c1 = 5
c1   

#Block 2:
# a and b calculation block2
a2 = 0
b2 = 0
c2 = a2 + b2 + 2 * a2 * b2 - 1
if(c2 < 0):
    c2 = 0 
else:
    c2 = 5
c2   

#A function combines many instructions into a single line of code
#Once a function is defined, it can be used repeatedly
# Make a Function for the calculation above
def Equation(a,b):
    c = a + b + 2 * a * b - 1
    if(c < 0):
        c = 0 
    else:
        c = 5
    return(c) 


#Pre-defined functions

#The print() function
album_ratings = [10.0, 8.5, 9.5, 7.0, 7.0, 9.5, 9.0, 9.5] 
print(album_ratings)

# sum() adds every element in a list or tuple together
sum(album_ratings)

# Show the length of the list or tuple
len(album_ratings)

#Using if/else Statements and Loops in Functions

# Function example
# "return" statement is very useful 
def type_of_album(artist, album, year_released):
    
    print(artist, album, year_released)
    if year_released > 1980:
        return "Modern"
    else:
        return "Oldie"
    
x = type_of_album("Michael Jackson", "Thriller", 1980)
print(x)

#print out each element in a list
def PrintList(the_list):
    for element in the_list:
        print(element)

PrintList(['1', 1, 'the man', "abc"]) #1, 1, the man, abc

#Setting default argument values in your custom functions
#You can set a default value for arguments in your function. 
#isGoodRating() function create a threshold: 
#Perhaps by default, we should have a default rating of 4

# Example for setting param with default value
def isGoodRating(rating=4): 
    if(rating < 7):
        print("this album sucks it's rating is",rating)
        
    else:
        print("this album is good its rating is",rating)
# Test the value with default value and with input
isGoodRating() #this album sucks it's rating is 4
isGoodRating(10) #this album is good its rating is 10

#Global variables
# Example of global variable
artist = "Michael Jackson" #Global varaible 
def printer1(artist):
    internal_var1 = artist #local variable 
    print(artist, "is an artist")
printer1(artist)

artist = "Michael Jackson"
def printer(artist):
    global internal_var             #assigned a local variable to global 
    internal_var= "Whitney Houston"
    print(artist,"is an artist")
printer(artist) 
printer(internal_var)


#Scope of a Variable
#The scope of a variable is the part of that program where that variable is accessible 
#Variables that are declared outside of all function definitions, 
#such as the myFavouriteBand variable in the code shown here, 
#are accessible from anywhere within the program

# Example of global variable
myFavouriteBand = "AC/DC"
def getBandRating(bandname):
    if bandname == myFavouriteBand:
        return 10.0
    else:
        return 0.0
print("AC/DC's rating is:", getBandRating("AC/DC"))
print("Deep Purple's rating is:",getBandRating("Deep Purple"))
print("My favourite band is:", myFavouriteBand)

# Example of global variable and local variable with the same name
myFavouriteBand = "AC/DC"
def getBandRating(bandname):
    myFavouriteBand = "Deep Purple"
    if bandname == myFavouriteBand:
        return 10.0
    else:
        return 0.0
print("AC/DC's rating is:",getBandRating("AC/DC"))
print("Deep Purple's rating is: ",getBandRating("Deep Purple"))
print("My favourite band is:",myFavouriteBand)
#two myFavouriteBand variable definitions, first one of these has a global scope
#the second of them is a local variable
#Deep Purple will receive a rating of 10.0 when passed to the getBandRating function
#outside of the getBandRating function, the getBandRating s local variable is not defined

# Collections and Functions
# When the number of arguments are unknown for a function, They can all be packed into a tuple as shown
def printAll(*args): # All the arguments are 'packed' into args which can be treated like a tuple
    print("No of arguments:", len(args)) 
    for argument in args:
        print(argument)
#printAll with 3 arguments
printAll('Horsefeather','Adonis','Bone')
#printAll with 4 arguments
printAll('Sidecar','Long Island','Mudslide','Carriage')

#No of arguments: 3
#Horsefeather
#Adonis
#Bone

#No of arguments: 4
#Sidecar
#Long Island
#Mudslide
#Carriage

#Functions can be incredibly powerful and versatile
#They can accept (and return) data types, objects and even other functions as arguments. 
def addItems(list):
    list.append("Three")
    list.append("Four")

myList = ["One","Two"]
addItems(myList)
myList #['One', 'Two', 'Three', 'Four']

Quiz on Functions

Come up with a function that divides the first input by the second input
def div(a, b):
    return(a/b)

Use the function con for the following question
def con(a, b):
    return(a + b)

############################################################################################
#What is an Exception?
#An exception is an error that occurs during the execution of code
#This error causes the code to raise an exception and if not prepared to handle it will halt the execution of the code.
#Examples:
1/0 #ZeroDivisionError occurs when you try to divide by zero
y = a + 5 #NameError use the variable a when it was not defined
a = [1, 2, 3]
a[10] #IndexError tried to access data from a list using an index that does not exist for this list

#Exception Handling
#A try except will allow you to execute code that might raise an exception 
#and in the case of any exception or a specific one we can handle or catch the exception and execute specific code
#This will allow us to continue the execution of our program even if there is an exception

#Python tries to execute the code in the try block 
#In this case if there is any exception raised by the code in the try block, 
#it will be caught and the code block in the except block will be executed 
#After that, the code that comes after the try except will be executed

a = 1
try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
    print("Success a=",a)
except:
    print("There was an error")        
#Please enter a number to divide a 5
#Success a= 0.2

#Try Except Specific
#A specific try except allows you to catch certain exceptions and also execute certain code depending on the exception 
#This is useful if you do not want to deal with some exceptions and the execution should halt 
#It can also help you find errors in your code that you might not be aware of 
#Furthermore, it can help you differentiate responses to different exceptions 
#In this case, the code after the try except might not run depending on the error
a = 1
try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
    print("Success a=",a)
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")
#Please enter a number to divide a 8
#Success a= 0.125

#Please enter a number to divide a 
#You did not provide a number

#Please enter a number to divide a 0
#The number you provided cant divide 1 because it is 0

#Try Except Else and Finally
#else allows one to check if there was no exception when executing the try block 
#this is useful when we want to execute something only if there were no errors
a = 1
try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")
else:
    print("success a=",a)
finally:
    print("Processing Complete")
#Please enter a number to divide a 5
#success a= 0.2
#Processing Complete

#Please enter a number to divide a 
#You did not provide a number
#Processing Complete

#Exercise
def safe_divide(numerator,denominator):
    try:
        result = numerator / denominator
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None
# Test case
numerator=int(input("Enter the numerator value:-"))
denominator=int(input("Enter the denominator value:-"))
print(safe_divide(numerator,denominator)) 
#Enter the numerator value:- 3
#Enter the denominator value:- 2
#1.5

############################################################################################
#Classes and objects
#For this Class explanation we need to import objects library to better understand 
import matplotlib.pyplot as plt
%matplotlib inline  

# Create a class Circle
class Circle(object):
    
    # Constructor
    def __init__(self, radius=3, color='blue'):
        self.radius = radius
        self.color = color 
    
    # Method
    def add_radius(self, r):
        self.radius = self.radius + r
        return(self.radius)
    
    # Method
    def drawCircle(self):
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.show()  

#Creating an instance of a class Circle
# Create an object RedCircle
RedCircle = Circle(10, 'red')
# dir command to get a list of the object's methods
dir(RedCircle)
# Print the object attribute radius
RedCircle.radius # 10 
# Set the object attribute radius
RedCircle.radius = 1
RedCircle.radius

#We can draw the object by using the method drawCircle():
RedCircle.drawCircle()

# Use method to change the object attribute radius
print('Radius of object:',RedCircle.radius)
RedCircle.add_radius(2)
print('Radius of object of after applying the method add_radius(2):',RedCircle.radius)
RedCircle.add_radius(5)
print('Radius of object of after applying the method add_radius(5):',RedCircle.radius)

######
#The Rectangle Class
class Rectangle(object):
    
    # Constructor
    def __init__(self, width=2, height=3, color='r'):
        self.height = height 
        self.width = width
        self.color = color
    
    # Method
    def drawRectangle(self):
        plt.gca().add_patch(plt.Rectangle((0, 0), self.width, self.height ,fc=self.color))
        plt.axis('scaled')
        plt.show()
        
# Create a new object rectangle
SkinnyBlueRectangle = Rectangle(2, 3, 'blue')

# Print the object attribute height
SkinnyBlueRectangle.height 
# Print the object attribute width
SkinnyBlueRectangle.width
# Print the object attribute color
SkinnyBlueRectangle.color
# Use the drawRectangle method to draw the shape
SkinnyBlueRectangle.drawRectangle()

# Create a new object rectangle
FatYellowRectangle = Rectangle(20, 5, 'yellow')
# Print the object attribute height
FatYellowRectangle.height 
# Print the object attribute width
FatYellowRectangle.width
# Print the object attribute color
FatYellowRectangle.color
# Use the drawRectangle method to draw the shape
FatYellowRectangle.drawRectangle()

############################################################################################
#Reading Files with Open


# Read the Example1.txt
example1 = "example1.txt"
file1 = open(example1, "r")

# Print the path of file
file1.name

# Print the mode of file, either 'r' or 'w'
file1.mode

# Read the file and assign it to a variable
FileContent = file1.read()
FileContent

# Print the file with '\n' as a new line
print(FileContent)

# Type of file content
type(FileContent)

#It is very important that the file is closed in the end
#This frees up resources and ensures consistency across different python versions
# Close file after finish
file1.close()

#A Better Way to Open a File
#- using the with statement is better practice, it automatically closes the file even if the code encounters an exception 
#- the code will run everything in the indent block then close the file object.
# Open file using with
with open(example1, "r") as file1:
    FileContent = file1.read()
    print(FileContent) #This is line 1 
                       #This is line 2
                       #This is line 3

# Verify if the file is closed
file1.closed #True

# Read first four characters
with open(example1, "r") as file1:
    print(file1.read(4)) #This 
# If we call the method again, the next 4 characters are called
with open(example1, "r") as file1:
    print(file1.read(4)) #This
    print(file1.read(4)) # is 
    print(file1.read(7)) #line 1
    print(file1.read(15))#This is line 2

# read one line of the file at a time using the method readline()
with open(example1, "r") as file1:
    print("first line: " + file1.readline())
    #first line: This is line 1 

#- we can also pass an argument to readline() to specify the number of charecters we want to read 
#- unlike  read(),  readline() can only read one line at most
with open(example1, "r") as file1:
    print(file1.readline(20)) # does not read past the end of line
    print(file1.read(20)) # Returns the next 20 chars
#This is line 1 

#This is line 2
#This 

# Iterate through the lines
with open(example1,"r") as file1:
        i = 0;
        for line in file1:
            print("Iteration", str(i), ": ", line)
            i = i + 1

############################################################################################
#Writing Files
# Write line to file
exmp2 = '/Example2.txt'
with open(exmp2, 'w') as writefile:
    writefile.write("This is line A")

# Read file
with open(exmp2, 'r') as testwritefile:
    print(testwritefile.read()) #This is line A

# Write lines to file
with open(exmp2, 'w') as writefile:
    writefile.write("This is line A\n")
    writefile.write("This is line B\n")

# Check whether write to file
with open(exmp2, 'r') as testwritefile:
    print(testwritefile.read()) #This is line A
                                #This is line B

# Sample list of text
Lines = ["This is line A\n", "This is line B\n", "This is line C\n"]

# Write the strings in the list to text file
with open('/Example2.txt', 'w') as writefile:
    for line in Lines:
        print(line)
        writefile.write(line)
#This is line A
#This is line B
#This is line C

# Verify if writing to file is successfully executed
with open('/Example2.txt', 'r') as testwritefile:
    print(testwritefile.read())

#setting the mode to w overwrites all the existing data in the file
with open('/Example2.txt', 'w') as writefile:
    writefile.write("Overwrite\n")
with open('/Example2.txt', 'r') as testwritefile:
    print(testwritefile.read())
#Overwrite


#Appending Files
#write to files without losing any of the existing data by setting the mode argument to append: a
with open('/Example2.txt', 'a') as testwritefile:
    testwritefile.write("This is line C\n")
    testwritefile.write("This is line D\n")
    testwritefile.write("This is line E\n")
#you can verify the file has changed by running the following cell
with open('/Example2.txt', 'r') as testwritefile:
    print(testwritefile.read())


#Additional modes
#It's fairly ineffecient to open the file in a or w and then reopening it in r to read any lines 
# r+ : Reading and writing. Cannot truncate the file.
# w+ : Writing and reading. Truncates the file.
# a+ : Appending and Reading. Creates a new file, if none exists. You dont have to dwell on the specifics of each mode for this lab.
with open('/Example2.txt', 'a+') as testwritefile:
    testwritefile.write("This is line E\n")
    print(testwritefile.read())

# .tell() - returns the current position in bytes
# .seek(offset,from) - changes the position by 'offset' bytes with respect to 'from' 

with open('/Example2.txt', 'a+') as testwritefile:
    print("Initial Location: {}".format(testwritefile.tell()))
    
    data = testwritefile.read()
    if (not data):  #empty strings return false in python
            print('Read nothing') 
    else: 
            print(testwritefile.read())
            
    testwritefile.seek(0,0) # move 0 bytes from beginning.
    
    print("\nNew Location : {}".format(testwritefile.tell()))
    data = testwritefile.read()
    if (not data): 
            print('Read nothing') 
    else: 
            print(data)
    
    print("Location after read: {}".format(testwritefile.tell()) )

# Initial Location: 55
# Read nothing

# New Location : 0
# Overwrite
# This is line C
# This is line D
# This is line E

# Location after read: 55
######## 

#Copy a File

# Copy file to another
with open('/Example2.txt','r') as readfile:
    with open('/Example3.txt','w') as writefile:
          for line in readfile:
                writefile.write(line)

############################################################################################
#PANDAS 
#Pandas is a popular library for data analysis built on top of the Python programming language
#Pandas generally provide two data structures for manipulating data
#DataFrame, Series

#A DataFrame is a two-dimensional data structure = data is aligned in a tabular fashion in rows and columns

#A Pandas DataFrame will be created by loading the datasets from existing storage
#Storage can be SQL Database, CSV file, Excel file
#It can also be created from the lists, dictionaries, and from a list of dictionaries

#Series 
#represents a one-dimensional array of indexed data. It has two main components :
# An array of actual data, An associated array of indexes or data labels, 
# Index is used to access individual data values


# Pandas: DataFrame
# let us import the Pandas Library
import pandas as pd # as meaning alias 

#
#Define a dictionary 'x'
x = {
    'Name': ['Rose','John', 'Jane', 'Mary'], 
     'ID': [1, 2, 3, 4], 
     'Department': ['Architect Group', 'Software Group', 'Design Team', 'Infrastructure'], 
     'Salary':[100000, 80000, 50000, 60000]
     }
#casting the dictionary to a DataFrame
df = pd.DataFrame(x) #using pd = pandas, function DataFrame for our dictionary x 
#display the result df
df
#Name	ID	Department	Salary
#0	Rose	1	Architect Group	100000
#1	John	2	Software Group	80000
#2	Jane	3	Design Team	50000
#3	Mary	4	Infrastructure	60000


#Column Selection

#Retrieving the "ID" column and assigning it to a variable x
x = df[['ID']]
x
#ID
# 0  1
# 1	 2 
# 2	 3
# 3	 4

#check the type of x
type(x)
#pandas.core.series.Series

#Access to multiple columns
#Retrieving the Department, Salary and ID columns and assigning it to a variable z
z = df[['Department','Salary','ID']]
z
#	 Department	Salary	ID
# 0	 Architect Group	100000	1
# 1	 Software Group	80000	2
# 2	 Design Team	50000	3
# 3	 Infrastructure	60000	4

############################################################################################
#PANDAS basics exercise

a = {
     'Student':['David', 'Samuel', 'Terry', 'Evan'],
     'Age':['27', '24', '22', '32'],
     'Country':['UK', 'Canada', 'China', 'USA'],
     'Course':['Python','Data Structures','Machine Learning','Web Development'],
     'Marks':['85','72','89','76']
    }
df1 = pd.DataFrame(a)
df1
#   Student	 Age	Country	    Course	          Marks
#0	David	 27	    UK	        Python	          85
#1	Samuel	 24	    Canada	    Data Structures	  72
#2	Terry	 22	    China	    Machine Learning  89
#3	Evan	 32	    USA	        Web Development	  76

b = df1[['Marks']]
b
#	Marks
#0	85
#1	72
#2	89
#3	76

c = df1[['Course', 'Country']]
c
#Course	Country
#0	Python	UK
#1	Data Structures	Canada
#2	Machine Learning	China
#3	Web Development	USA

##!!!!##
#To view the column as a series, just use one bracket

# Get the Student column as a series Object
x = df1['Student']
x

#0     David
#1    Samuel
#2     Terry
#3      Evan
#Name: Student, dtype: object

#check the type of x
type(x)
# pandas.core.series.Series

############################################################################################
#loc() and iloc() functions

# loc() = label-based data selecting method 
# (pass the name of the row or column that we want to select)
# includes the last element of the range passed in it
# Syntax = loc[row_label, column_label]

# iloc() = indexed-based selecting method 
# (pass an integer index in the method to select a specific row/column)
# This method does not include the last element of the range passed in it
# Syntax = iloc[row_index, column_index]

# Access the value on the first row and the first column
df.iloc[0, 0]
# 'Rose'

# Access the value on the first row and the third column
df.iloc[0,2]
# 'Architect Group'

# Access the column using the name
df.loc[0, 'Salary']
# 100000

#	ID	Department	Salary
#Name			
#Rose	1	Architect Group	100000
#John	2	Software Group	80000
#Jane	3	Design Team	50000
#Mary	4	Infrastructure	60000

df2=df
df2=df2.set_index("Name")

df2.loc['Jane', 'Salary']
#50000

df2. loc['Jane', 'Department']
#'Design Team'

df2.iloc[3, 2]
#60000

#Slicing 
#Slicing uses the [] operator to select a set of rows and/or columns from a DataFrame

df.iloc[0:2, 0:3] # 0:2 = 0,1 ; 0:3 = Name, ID, Department 
#	Name	ID	Department
#0	Rose	1	Architect Group
#1	John	2	Software Group

df.loc[0:2,'ID':'Department']
#   ID	Department
#0	1	Architect Group
#1	2	Software Group
#2	3	Design Team

df2.loc['Rose':'Jane', 'ID':'Department'] #From Tose to Jane, select ID and Department 
#        ID	Department
#Name		
#Rose	1	Architect Group
#John	2	Software Group
#Jane	3	Design Team

############################################################################################
#Artist	            Album	            Released	    Length	    Genre	                   recording sales (millions)	Claimed sales (millions)	Released	Soundtrack	Rating (friends)
#Michael Jackson	    Thriller	        1982	        00:42:19	Pop, rock, R&B	            46	                                65	                30-Nov-82		            10.0
#AC/DC	            Back in Black	    1980	        00:42:11	Hard rock	                26.1	                            50	                25-Jul-80		            8.5
#Pink Floyd	 The Dark Side of the Moon	1973	        00:42:49	Progressive rock	        24.2	                            45	                01-Mar-73		            9.5
#Whitney Houston	    The Bodyguard	    1992	        00:57:44	Soundtrack/R&B, soul, pop	26.1	                            50	                25-Jul-80	    Y	        7.0
#Meat Loaf	        Bat Out of Hell	    1977	        00:46:33	Hard rock, progressive rock	20.6	                            43	                21-Oct-77		            7.0
#Eagles	            Their Greatest Hits (1971-1975)		00:43:08	Rock, soft rock, folk rock	32.2	                            42	                17-Feb-76		            9.5
#Bee Gees	        Saturday Night Fever 1977	        1:15:54	    Disco	                    20.6	                            40	                15-Nov-77	    Y	        9.0
#Fleetwood Mac	    Rumours	             1977	        00:40:01	Soft rock	                27.9	                            40	                04-Feb-77		            9.5

#Introduction to PANDAS 
# Dependency needed to install file 

# If running the notebook on your machine, else leave it commented
#!pip install xlrd

#!pip install openpyxl 
import piplite
await piplite.install(['xlrd','openpyxl'])

# Import required library
import pandas as pd

# Read data from CSV file

# csv_path = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/TopSellingAlbums.csv'
# df = pd.read_csv(csv_path)

from pyodide.http import pyfetch
import pandas as pd

filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/TopSellingAlbums.csv"

async def download(url, filename):
    response = await pyfetch(url)
    if response.status == 200:
        with open(filename, "wb") as f:
            f.write(await response.bytes())


await download(filename, "TopSellingAlbums.csv")
df = pd.read_csv("TopSellingAlbums.csv")

# Read data from Excel File and print the first five rows
xlsx_path = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/jupyterlite/files/Module%205/data/TopSellingAlbums.xlsx'

await download(xlsx_path, "TopSellingAlbums.xlsx")
df = pd.read_excel("TopSellingAlbums.xlsx")
df.head()

# Access to the column Length
x = df[['Length']]
x
#Length
#0	0:42:19
#1	0:42:11
#2	0:42:49
#3	0:57:44
#4	0:46:33
#5	0:43:08
#6	1:15:54
#7	0:40:01

#Viewing Data and Accessing Data

# Get the column as a series
x = df['Length']
x
#0    0:42:19
#1    0:42:11
#2    0:42:49
#3    0:57:44
#4    0:46:33
#5    0:43:08
#6    1:15:54
#7    0:40:01
#Name: Length, dtype: object

# Get the column as a dataframe
x = df[['Artist']] 
type(x) #pandas.core.frame.DataFrame

# Access to multiple columns
y = df[['Artist','Length','Genre']]
y
#Artist	Length	Genre
#0	Michael Jackson	0:42:19	pop, rock, R&B
#1	AC/DC	0:42:11	hard rock
#2	Pink Floyd	0:42:49	progressive rock
#3	Whitney Houston	0:57:44	R&B, soul, pop
#4	Meat Loaf	0:46:33	hard rock, progressive rock
#5	Eagles	0:43:08	rock, soft rock, folk rock
#6	Bee Gees	1:15:54	disco
#7	Fleetwood Mac	0:40:01	soft rock

# Access the value on the first row and the first column
df.iloc[0, 0]
#'Michael Jackson'

# Access the value on the second row and the first column
df.iloc[1,0]
#'AC/DC'

# Access the value on the first row and the third column
df.iloc[0,2]
#1982

# Access the column using the name
df.loc[1, 'Artist']
#'AC/DC'

# Access the column using the name
df.loc[0, 'Released']
#1982

# Access the column using the name
df.loc[1, 'Released']
#1980

# Slicing the dataframe
df.iloc[0:2, 0:3]
#	Artist	  Album	             Released
#0	Michael   Jackson Thriller	 1982
#1	AC/DC	  Back in Black	     1980

# Slicing the dataframe using name
df.loc[0:2, 'Artist':'Released']
#	Artist	  Album	             Released
#0	Michael   Jackson Thriller	 1982
#1	AC/DC	  Back in Black	     1980

############################################################################################
## 

# Create a python list
a = ["0", 1, "two", "3", 4]

# Print each element
print("a[0]:", a[0])
print("a[1]:", a[1])
print("a[2]:", a[2])
print("a[3]:", a[3])
print("a[4]:", a[4])

# Numpy
# python library used for arrays, linear algebra, fourier transform, and matrices 
# NumPy = numerical python 

import numpy as np # np is used as alias

# Create a numpy array
a = np.array([0, 1, 2, 3, 4])
a #array([0, 1, 2, 3, 4])

# Print each element
print("a[0]:", a[0]) #a[0]: 0
print("a[1]:", a[1]) #a[1]: 1
print("a[2]:", a[2]) #a[2]: two
print("a[3]:", a[3]) #a[3]: 3
print("a[4]:", a[4]) #a[4]: 4

#NumPy version string
print(np.__version__) #1.24.2

# Check the type of the array
type(a) #numpy.ndarray

# Check the type of the array
type(a) #dtype('int32')

# Check the type of the values stored in numpy array
a.dtype #

b = np.array([3.1, 11.02, 6.2, 213.2, 5.2])
type(b)
b.dtype #
# float 64

# Assign value
# change the value of the array
# Create numpy array
c = np.array([20, 1, 2, 3, 4])
c #array([20,  1,  2,  3,  4])

# Assign the first element to 100
c[0] = 100
c #array([100,   1,   2,   3,   4])

# Assign the 5th element to 0
c[4] = 0
c #array([100,   1,   2,   3,   0])

a = np.array([10, 2, 30, 40,50])
a[1] = 20
a #

Slicing
taking the elements from the given index to another given index
# Slicing the numpy array
d = c[1:4]
d #array([1, 2, 3])

# Set the fourth element and fifth element to 300 and 400
c[3:5] = 300, 400
c #array([100,   1,   2, 300, 400])

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5:2]) #[2 4]
#define the steps in slicing: [start:end:step]

# If we don't pass start its considered 0
print(arr[:4]) #[1 2 3 4]

# If we don't pass end it considers till the length of array
print(arr[4:]) #[5 6 7]

# If we don't pass step its considered 1
print(arr[1:5:]) #[2 3 4 5]

# Print the even elements in the given array
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(arr[0:9:1] #[2 4 6 8]

# Assign Value with List
# select more than one specific index
# Create the index list
select = [0, 2, 3, 4]
select #[0, 2, 3, 4]

# Use List to select elements
d = c[select]
d #array([100,   2, 300, 400])

# Assign the specified elements to new value
c[select] = 100000
c #array([100000,      1, 100000, 100000, 100000])

#Other Attributes
# Create a numpy array
a = np.array([0, 1, 2, 3, 4])
a #array([0, 1, 2, 3, 4])

# The attribute size is the number of elements in the array
# Get the size of numpy array
a.size #5

# Get the number of dimensions of numpy array 
a.ndim #1

# Get the shape/size of numpy array
# size of the array in each dimension
a.shape #(5,)

#exercise 
b = np.array([10, 20, 30, 40, 50, 60, 70])
b.ndim #1 dimensional array
b.shape #(7,) number of elements in each dimension 
b.size #7

Numpy Statistical Functions
# Create a numpy array
a = np.array([1, -1, 1, -1])

# Get the mean of numpy array
mean = a.mean()
mean # 0.0

# Get the standard deviation of numpy array
standard_deviation=a.std()
standard_deviation # 1.0

# Create a numpy array
b = np.array([-1, 2, 3, 4, 5])
b # array([-1,  2,  3,  4,  5])

# Get the biggest value in the numpy array
max_b = b.max()
max_b # 5

# Get the smallest value in the numpy array

min_b = b.min()
min_b # -1

c = np.array([-10, 201, 43, 94, 502])

# Exercise
#Find the sum of maximum and minimum value in the given numpy array
c = np.array([-10, 201, 43, 94, 502])
max_c = c.max()
max_c
    
min_c = c.min()
min_c
    
Sum = (max_c +min_c)
Sum

########################
# Numpy Array Operations

# Array Addition
u = np.array([1, 0])
v = np.array([0, 1])
z = np.add(u, v)
z # array([1, 1])

# vector addition
# Plotting functions


import time # time functionality in python 
import sys # allows python to work with your system
import numpy as np #numerical python library

import matplotlib.pyplot as plt #matplotlib visualization library for python 
%matplotlib inline  

def Plotvec1(u, z, v):
    
    ax = plt.axes() # to generate the full window axes
    
    ax.arrow(0, 0, *u, head_width=0.05, color='r', head_length=0.1)# Add an arrow to the  U Axes with arrow head width 0.05, color red and arrow head length 0.1
    plt.text(*(u + 0.1), 'u')#Adds the text u to the Axes 
    
    ax.arrow(0, 0, *v, head_width=0.05, color='b', head_length=0.1)# Add an arrow to the  v Axes with arrow head width 0.05, color red and arrow head length 0.1
    plt.text(*(v + 0.1), 'v')#Adds the text v to the Axes 
    
    ax.arrow(0, 0, *z, head_width=0.05, head_length=0.1)
    plt.text(*(z + 0.1), 'z')#Adds the text z to the Axes 

    plt.ylim(-2, 2)#set the ylim to bottom(-2), top(2)
    plt.xlim(-2, 2)#set the xlim to left(-2), right(2)

# Plot numpy arrays
Plotvec1(u, z, v)

#Exercise
arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])

# Enter your code here
j = np.add(arr1, arr2)
j #array([30, 32, 34, 36, 38, 40])


# Array subtraction 
aa = np.array([10, 20, 30])
aa

bb = np.array([5, 10, 15])
bb

c = np.subtract(a, b)
print(c) #[ 5 10 15]

#Exercise
arr3 = np.array([10, 20, 30, 40, 50, 60])
arr4 = np.array([20, 21, 22, 23, 24, 25])

# Enter your code here
gg = np.subtract(arr3, arr4)
gg

#Array Multiplication
# Create a numpy array
x = np.array([1, 2])
x #array([1, 2])
# Create a numpy array
y = np.array([2, 1])
y #array([2, 1])
# Numpy Array Multiplication
z = np.multiply(x, y)
z #array([2, 2])

#Exercise 
arr7 = np.array([10, 20, 30, 40, 50, 60])
arr8 = np.array([2, 1, 2, 3, 4, 5])
ggg = np.multiply(arr7, arr8)
ggg #array([ 20,  20,  60, 120, 200, 300])


# Array Division
q = np.array([10, 20, 30])
q # array([10, 20, 30])
w = np.array([2, 10, 5])
w # array([ 2, 10,  5])
e = np.divide(a, b)
e # array([2., 2., 2.])

# Exercise
arr5 = np.array([10, 20, 30, 40, 50, 60])
arr7 = np.array([3, 5, 10, 8, 2, 33])
arrr = np.divide(arr5, arr7)
arrr #array([ 3.33333333,  4.        ,  3.        ,  5.        , 25.        ,1.81818182])

############
#Dot Product
# dot product of the two numpy arrays u and v is given by
X = np.array([1, 2])
Y = np.array([3, 2])

# Calculate the dot product
np.dot(X, Y) #7

#Elements of X
print(X[0]) # 1
print(X[1]) # 2 

#Elements of Y
print(Y[0]) # 3
print(Y[1]) # 2

# Elemtns of X              Elements of Y 
#  X[0]   X[1]              Y[0]    Y[1]
# X = X[1, 2]               Y = [3, 2]
# X.Y = [ (X[0] * Y[0]) + (X[1] * Y[1]) ]
#              [(1 * 3) + (2 * 2)]
#                 [  3  +  4  ]
#                       7

#Exercise
arr1 = np.array([3, 5])
arr2 = np.array([2, 4])
arr7 = np.dot(arr1, arr2)
arr7 #26


#Adding Constant to a Numpy Array
# Create a constant to numpy array
u = np.array([1, 2, 3, -1]) 
u #array([ 1,  2,  3, -1])

# Add the constant to array
u + 1 #array([2, 3, 4, 0])

#Exercise
#Add Constant 5 to the given numpy array ar
arrr5 = np.array([1, 2, 3, -1]) 
arrr5 + 1 # array([2, 3, 4, 0])

######################
#Mathematical Functions

# The value of pi
np.pi #3.141592653589793

# Create the numpy array in radians
x = np.array([0, np.pi/2 , np.pi])

# Calculate the sin of each elements
y = np.sin(x)
y #array([0.0000000e+00, 1.0000000e+00, 1.2246468e-16])

#Linspace
#Linspace returns evenly spaced numbers over a specified interval
#numpy.linspace(start, stop, num = int value)
#
#start : start of interval range
#
#stop : end of interval range
#
#num : Number of samples to generate

# Makeup a numpy array within [-2, 2] and 5 elements
np.linspace(-2, 2, num=5) 
#array([-2., -1.,  0.,  1.,  2.])

# Make a numpy array within [-2, 2] and 9 elements
np.linspace(-2, 2, num=9) 
#array([-2. , -1.5, -1. , -0.5,  0. ,  0.5,  1. ,  1.5,  2. ])

# Make a numpy array within [0, 2π] and 100 elements 
x = np.linspace(0, 2*np.pi, num=100)
x #array([0.        , 0.06346652, 0.12693304, 0.19039955, 0.25386607,
       #0.31733259, 0.38079911, 0.44426563, 0.50773215, 0.57119866,
       #0.63466518, 0.6981317 , 0.76159822, 0.82506474, 0.88853126,
       #0.95199777, 1.01546429, 1.07893081, 1.14239733, 1.20586385,
       #1.26933037, 1.33279688, 1.3962634 , 1.45972992, 1.52319644,
       #1.58666296, 1.65012947, 1.71359599, 1.77706251, 1.84052903,
       #1.90399555, 1.96746207, 2.03092858, 2.0943951 , 2.15786162,
       #2.22132814, 2.28479466, 2.34826118, 2.41172769, 2.47519421,
       #2.53866073, 2.60212725, 2.66559377, 2.72906028, 2.7925268 ,
       #2.85599332, 2.91945984, 2.98292636, 3.04639288, 3.10985939,
       #3.17332591, 3.23679243, 3.30025895, 3.36372547, 3.42719199,
       #3.4906585 , 3.55412502, 3.61759154, 3.68105806, 3.74452458,
       #3.8079911 , 3.87145761, 3.93492413, 3.99839065, 4.06185717,
       #4.12532369, 4.1887902 , 4.25225672, 4.31572324, 4.37918976,
       #4.44265628, 4.5061228 , 4.56958931, 4.63305583, 4.69652235,
       #4.75998887, 4.82345539, 4.88692191, 4.95038842, 5.01385494,
       #5.07732146, 5.14078798, 5.2042545 , 5.26772102, 5.33118753,
       #5.39465405, 5.45812057, 5.52158709, 5.58505361, 5.64852012,
       #5.71198664, 5.77545316, 5.83891968, 5.9023862 , 5.96585272,
       #6.02931923, 6.09278575, 6.15625227, 6.21971879, 6.28318531])
# We can apply the sine function to each element in the array x and assign it to the array y
# Calculate the sine of x list
y = np.sin(x)
# Plot the result
plt.plot(x, y)

#####################
#Iterating 1-D Arrays
arr1 = np.array([1, 2, 3])
print(arr1)
# [1 2 3]

for x in arr1:
  print(x)
# 1
# 2
# 3

##########
# Exercise
# Implement the following vector subtraction in numpy: u-v
u = np.array([1, 0])
v = np.array([0, 1])
u - v # array([ 1, -1])

# Multiply the numpy array z with -2
z = np.array([2, 4])
z * -2 # array([-4, -8])

# Consider the list [1, 2, 3, 4, 5] and [1, 0, 1, 0, 1] 
# Cast both lists to a numpy array then multiply them together
ee = np.array([1, 2, 3, 4, 5])
ff = np.array([1, 0, 1, 0, 1])
ee * ff 

###########
import time 
import sys
import numpy as np 

import matplotlib.pyplot as plt
%matplotlib inline  

def Plotvec2(a,b):
    ax = plt.axes()# to generate the full window axes
    ax.arrow(0, 0, *a, head_width=0.05, color ='r', head_length=0.1)#Add an arrow to the  a Axes with arrow head width 0.05, color red and arrow head length 0.1
    plt.text(*(a + 0.1), 'a')
    ax.arrow(0, 0, *b, head_width=0.05, color ='b', head_length=0.1)#Add an arrow to the  b Axes with arrow head width 0.05, color blue and arrow head length 0.1
    plt.text(*(b + 0.1), 'b')
    plt.ylim(-2, 2)#set the ylim to bottom(-2), top(2)
    plt.xlim(-2, 2)#set the xlim to left(-2), right(2)

# Convert the list [-1, 1] and [1, 1] to numpy arrays a and b. 
# Then, plot the arrays as vectors using the fuction Plotvec2 and find their dot product
a = np.array([-1, 1])
b = np.array([1, 1])
Plotvec2(a, b)
print("The dot product is", np.dot(a,b))

# Convert the list [1, 0] and [0, 1] to numpy arrays a and b
# Then, plot the arrays as vectors using the function Plotvec2 and find their dot product
a = np.array([1, 0])
b = np.array([0, 1])
Plotvec2(a, b)
print("The dot product is", np.dot(a, b))

# Convert the list [1, 1] and [0, 1] to numpy arrays a and b 
# Then plot the arrays as vectors using the fuction Plotvec2 and find their dot product
ggg = np.array([1, 1])
ttt = np.array([0, 1])
Plotvec2(ggg, ttt)
print("The dot product is", np.dot(ggg,ttt))

# Convert the list [1, 2, 3] and [8, 9, 10] to numpy arrays arr1 and arr2
# Then perform Addition , Subtraction , Multiplication , Division and Dot Operation on the arr1 and arr2
arr1 = np.array([1, 2, 3])
arr2 = np.array([8, 9, 10])

arr3 = np.add(arr1, arr2)
arr3

arr4 = np.subtract(arr1, arr2)
arr4

arr5 = np.multiply(arr1, arr2)
arr5

arr6 = np.divide(arr1, arr2)
arr6

arr7 = np.dot(arr1, arr2)
arr7


arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([6, 7, 8, 9, 10])


# Convert the list [1, 2, 3, 4, 5] and [6, 7, 8, 9, 10] to numpy arrays arr1 and arr2 
# Then find the even and odd numbers from arr1 and arr2
# Starting index in slice is 1 as first even element(2) in array1 is at index 1
even_arr1 = arr1[1:5:2]
print("even for array1",even_arr1)
    
# Starting index in slice is 0 as first odd element(1) in array1 is at index 0
odd_arr1=arr1[0:5:2]
print("odd for array1",odd_arr1)

# Starting index in slice is 0 as first even element(6) in array2 is at index 0
even_arr2 = arr2[0:5:2]
print("even for array2",even_arr2)
    
# Starting index in slice is 1 as first odd element(7) in array2 is at index 1
odd_arr2=arr2[1:5:2]
print("odd for array2",odd_arr2)

# even for array1 [2 4]
# odd for array1 [1 3 5]
# even for array2 [ 6  8 10]
# odd for array2 [7 9]

####################
# 2D Numpy in Python

# Import the libraries
import numpy as np 
import matplotlib.pyplot as plt

# Create a list
a = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]
a # [[11, 12, 13], [21, 22, 23], [31, 32, 33]]

# Convert list to Numpy Array
# Every element is the same type
A = np.array(a)
A # array([[11, 12, 13],
         # [21, 22, 23],
         # [31, 32, 33]])
  
# Show the numpy array dimensions
A.ndim # 2 

# Show the numpy array size
A.size # 9 

# Accessing different elements of a Numpy Array
#array([[11, 12, 13],
#       [21, 22, 23],
#       [31, 32, 33]])

# Access the element on the second row and third column
A[1, 2] # 23 

# Access the element on the second row and third column
A[1][2] # 23 

# Access the element on the first row and first column
A[0][0] # 11

# Access the element on the first row and first and second columns
A[0][0:2] # array([11, 12])

# Access the element on the first and second rows and third column
A[0:2, 2] # array([13, 23])

# Create a numpy array X
X = np.array([[1, 0], [0, 1]]) 
X # array([[1, 0],
#          [0, 1]])

# Create a numpy array Y 
Y = np.array([[2, 1], [1, 2]]) 
Y # array([[2, 1],
#          [1, 2]])

# Add X and Y
Z = X + Y
Z # array([[3, 1],
#          [1, 3]])

#Multiply

# Create a numpy array Y
Y = np.array([[2, 1], [1, 2]]) 
Y # array([[2, 1],
#          [1, 2]])

# Multiply Y with 2
Z = 2 * Y
Z #
# array([[4, 2],
#        [2, 4]])

# Create a numpy array Y
Y = np.array([[2, 1], [1, 2]]) 
Y # array([[2, 1],
#          [1, 2]])

# Create a numpy array X
X = np.array([[1, 0], [0, 1]]) 
X # array([[1, 0],
#          [0, 1]])

# Multiply X with Y
Z = X * Y
Z # array([[2, 0],
#          [0, 2]])

# Create a matrix A
A = np.array([[0, 1, 1], [1, 0, 1]])
A # array([[0, 1, 1],
#          [1, 0, 1]])

# Create a matrix B
B = np.array([[1, 1], [1, 1], [-1, 1]])
B # array([[ 1,  1],
#          [ 1,  1],
#          [-1,  1]])

We use the numpy function dot to multiply the arrays together
# Calculate the dot product
Z = np.dot(A,B)
Z # array([[0, 2],
#          [0, 2]])

# Calculate the sin of Z
np.sin(Z)
# array([[0.        , 0.90929743],
#        [0.        , 0.90929743]])

# Create a matrix C
C = np.array([[1,1],[2,2],[3,3]])
C # array([[1, 1],
          #[2, 2],
      #    [3, 3]])

# Get the transposed of C
C.T # array([[1, 2, 3],
#           [1, 2, 3]])

# Exercise
# Consider the following list a, convert it to Numpy Array
a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
A = np.array(a)
A # array([[ 1,  2,  3,  4],
#          [ 5,  6,  7,  8],
#          [ 9, 10, 11, 12]])


# Calculate the numpy array size
np.size(A) # 12

# Access the element on the first row and first and second columns
A[0, 0:2] # array([1, 2])

# Perform matrix multiplication with the numpy arrays A and B
B = np.array([[0, 1], [1, 0], [1, 1], [-1, 0]])
C = np.dot(A, B)
C #array([[ 1,  4],
#         [ 5, 12],
#         [ 9, 20]])

