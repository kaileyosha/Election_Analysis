#exercise one#
print("Hello World") #print is a command that will have the computer return whatever is in parentheses#

#exercise two#
counties= ["Arapahoe", "Denver", "Jefferson"] #this line of code creates a variable called counties, and identified the values in counties all of which are strings#
if counties[1]== "Denver": #this if statement says that if the first indexed value in the variable counties (ie the second value) is Denver...#
   print(counties[1]) #then the computer should display the value#

#exercise three#
temperature= int(input("What is the temperature outside?")) #this creates a variable, temperature, that requires the user to input the temperature outside#
if temperature > 80: #if the value entered is greater than 80...#
   print("Turn on the AC") #display Turn on the AC#
else: #otherwise#
    print("Open the windows") #display Open the windows#

#exercise four#

score= int(input("What was your test score?")) 

if score >= 90:
    print("Your grade is an A")
else: 
    if score >= 80:
        print("Your grade is a B")
    else: 
        if score >= 70: 
            print("Your grade is a C")
        else:
            if score >=60:
                print("Your grade is a D")
            else: 
                print("Your grade is an F")