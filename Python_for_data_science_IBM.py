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
############################################################################################
