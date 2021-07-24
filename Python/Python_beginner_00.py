# 00 Print

#print("Hello World!")



# 01 Drawing Shape

# print("   /|")
# print("  / |")
# print(" /  |")
# print("/___|")



# 02 Variables

# character_name= "John"
# character_age= "33"
# is_male= True
# print("He is: " +    character_name + "!")
# print("He is: " +    character_age + ".")
# character_age= 33
# #print("He is: "  character_age  "!")

# 03 Working with String

# print("Giraffe\nAcademy")
# print("Giraffe\"Academy\"")

# phrase= "Giraffe Academy"
# print(phrase.lower())
# print(phrase.upper())
# print(phrase.isupper())
# print(phrase.upper().isupper())
# print(len(phrase))
# print(phrase[0])
# print(phrase.index("A"))
# print(phrase.replace("Giraffe", " Elephant "))






#04 working with number

# print( 2*3/2.5 )
# print(10%3)

# my_number= -5
# print("My number is: "  + str(my_number) )
# print(abs(my_number))
# print(pow(2,5))
# print(round(3.5))



# 05 Getting input from users

# my_name= input("enter your name: ")
# print(my_name)






# 06 Calculate

# num1= input("Enter a number: ")
# num2= input("Enter another number: ")
# result= num1 + num2
# # result= int(num1) + int(num2)
# print("The result is: %d" %(result)  )

# 07 List

# friends = [ "John", "Kevin", "Jim", "Oscar", "Toby"]
# print(friends)
# print(friends[0])
# friends[0]= "Mike"
# print(friends[0])
# print(friends[-1])
# print(friends[2:])
# print(friends.index("Kevin"))






# 08 List Function

# friends= [ "John", "Kevin", "Jim", "Oscar", "Toby"]
# lucky_number= [ 0,1,2,5,7,11 ]
# friends.append("Henry")
# print(friends)
# friends.extend(lucky_number)
# print(friends)
# friends.insert(0, "Calva")
# print(friends)
# friends.remove("Calva")
# print(friends)
# #friends.clear()
# friends.insert(5,"John")
# print("The time appear of \"John\" is: %d"%friends.count("John"))
# friends.sort()
# print(friends)
# friends.reverse()
# print(friends)
# friends2= friends.copy()
# print(friends2)





#9 Tuples

# coordinates = (4, 5)
# print(coordinates[0])
# #coordinates[0]= 3  => error





#10 Fuction

# def say_hi( name, age ):
    # print("Hello %s, your age is: %d "%(name, age))
    
# say_hi("Milke", 33)


# def Sum_func( a, b ):
    # return ( a + b )
# result= Sum_func(1,4) 
# print(result)


#11 If Statement

# def tall_male():
    # is_tall= input("You are tall?")
    # is_male= input("You are male?")
    # if is_male and is_tall:
        # print("You are tall male")
    # elif is_male and not(is_tall):
        # print("You are male and not tall")
    # else:
        # print("You are not above")
        
# def isMaximum( num1, num2, num3):
    # temp= num1
    # if num2 > temp:
        # temp= num2
    # if num3 > temp:
        # temp= num3
    # return temp
    
# result= isMaximum(3,8,5)
# print(result)

#op= input("Enter the operator!")
# if op == "+" :
  # print( num1 + num2)
    # if op == "-" :
        # return num1 - num2
    # if op == '/' :
        # return num1/num2
        
# result= Caculate(6, 3)
# print(result) 

# if i in "hello":
    # i= o;





#12 Dictionaries

# moth_convert={
    # 1 : "January",
    # 2 : "February",
    # 3 : "March",
    # "Apr" : "April",
    # "May" : "May",
    # "Jun" : "June",
    # "Jul" : "July",
    # "Aug" : "August",
    # "Sep" : "September",
    # "Oct" : "October",
    # "Nov" : "November",
    # "Dec" : "December",
# }
# print(moth_convert["Nov"])
# print(moth_convert.get(1))




#13 Loop

# i= 0
# while i< 10:
    # print(i)
    # i+= 1

# for letter in "Giraffe Academy":
    # print(letter)
    
# friends= ["Jim", "Kaven", "Ki"]
# for friend in friends:
    # print(friend)
    
# for index in range(3, 10):
    # print(index)
    
# maxx= input("Enter maxx:")    
# for i in range(3, maxx+1):
    # print(i)
    




#14 Exponent Function
#print(2**3)






#15 2D list and nest loop

# number_grid= [
    # [ 1,2,3 ],
    # [ 4,5,6 ],
    # [ 7,8,9 ],
    # [ 0 ]
# ]
# print(number_grid[1][1])





# 16 Try Exception

# try:
    # number = int(input("Enter the number:"))
    # print(number)
# except ValueError as err:
    # print(err)
    # #print("ValueError")
# except ZeroDivisionError:
    # print("ZeroDivisionError")





#17 Read files



#18 Modules and pip
# Key word: list of modules of python, python-docx
# import ext
# print(ext.number)
# result= ext.add_cal(1,5)
# print(result)




# 19 Object and Class

# class Student:
    
    # def __init__(self, name, major, gpa, is_on_probation):
        # self.name= name
        # self.major= major
        # selnf.gpa= gpa
        # self.is_on_probation= is_on_probatio


# from student import Student

# student1= Student("Jim", "Mechatronics", 4.2, True)
# student2= Student("Kite", "Mechatronics", 4.2, True)

# print(student2.name)   



# from Question import Questions


# question_prompt= [
    # "What color of the apple?\n(a)Red\n(b)Greem\n(c)Blue\n\n",
    # "What color of the banana?\n(a)Red\n(b)Greem\n(c)Blue\n\n",
    # "What color of the orange?\n(a)Red\n(b)Greem\n(c)Blue\n\n"
# ]
# #print(question_prompt[0])

# questions= [
    # Questions(question_prompt[0], 1),
    # Questions(question_prompt[1], 2),
    # Questions(question_prompt[2], 3)
# ]


# def run_test(questions):
    # score= 0
    # for question in questions:
        # answer= input(question.prompt)
        # if answer == question.answer:
            # score+= 1
    # print("you got: %d\n"%score)

# run_test(questions)





#20 Object Function

# from student import Student

# student1= Student("John", "Mechatronics", 3.5, True)

# print(student1.on_honor_roll())





# 21 Inhenritance

#from Chef import Chef
from chineseChef import chineseChef

myChef= chineseChef()

myChef.make_chicken()
myChef.make_bread()