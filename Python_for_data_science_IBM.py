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

############################################################################################
#Conditions and Branching 


############################################################################################
############################################################################################
############################################################################################
############################################################################################
############################################################################################
