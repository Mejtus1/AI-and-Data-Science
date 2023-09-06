#Types 
# int = 11
# float = 21.123

#Typecasting (changing data types)
# changing int to float 

#Boolean 
#True or False



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


############################################################################################
############################################################################################