#following Udemy course: 100 days of code by Angela Yu

#---------------average from a list WITHOUT using MEAN() or SUM()----------------
student_heights = input("Input a list of student heights ").split()
#need this to change list of str into list of int
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
#calculate the sum FOR numbers
summ = 0 
for x in student_heights:
    summ += x
#calculate the sum OF numbers
summ_of_students = 0
for student in student_heights:
  summ_of_students += 1
#print(f"number of students = {summ_of_students}")

#calculate the average
average=summ/summ_of_students
#round to no decimals
print(round(average, 0))


#---------------average from a list using MEAN()----------------
from statistics import mean

student_heights = input("Input student heights, using a space after each one: \n").split()
#need this to change list of str into list of int
for i in range(0, len(student_heights)): 
    student_heights[i] = int(student_heights[i])
#actual calculation
print(mean(student_heights))


#---------------average from a list using SUM()----------------
student_heights = input("Input student heights, using a space after each one: \n").split()
#need this to change list of str into list of int
for i in range(0, len(student_heights)): 
    student_heights[i] = int(student_heights[i])
#actual calculation
print(sum(student_heights)/len(student_heights))


#---------------the highest number from a list WITHOUT using MAX()----------------
student_score = input("Input a list of student scores ").split()
#need this to change list of str into list of int
for n in range(0, len(student_score)):
    student_score[n] = int(student_score[n])
#find the heighest number
number = 0 
for x in student_score:
    if x > number:
        number = x
print(number)


#---------------the highest number from a list using MAX() and MIN()----------------
student_score = input("Input a list of student scores ").split()
#need this to change list of str into list of int
for n in range(0, len(student_score)):
    student_score[n] = int(student_score[n])
#find the heighest number
print(max(student_score))
print(min(student_score))


#---------------FizzBuzz game----------------
for number in range (0, 101):
    #print(number)
    if number % 3 == 0 and number % 5 == 0:
        print('fizzBuzz')
    elif number % 3 == 0:
        print('fizz')
    elif number % 5 == 0:
        print('buzz')
    else:
        print(number)


#---------------PWD generator----------------
import random

print("\n\n-------------Welcome to the PyPassword Generator!------------------\n")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))

#total elements in the list
total_letters = len(letters)
letter=0
pwd_letters = []
#pick as many numbers as user requested
for letter in range(nr_letters):
    #pick a random from the list
    random_x = random.randint(0,(total_letters-1))
    pwd_letters.append(letters[random_x])
    #print(letters[random_x]) #QC
#print(pwd_letters) #QC

#total elements in the list
total_numbers = len(numbers)
number=0
pwd_numbers = []
#pick as many numbers as user requested
for number in range(nr_numbers):
    #pick a random from the list
    random_x = random.randint(0,(total_numbers-1))
    pwd_numbers.append(numbers[random_x])
    #print(numbers[random_x]) #QC
#print(pwd_numbers) #QC

#total elements in the list
total_symbols = len(symbols)
symbol=0
pwd_symbols = []
#pick as many symbols as user requested
for symbol in range(nr_symbols):
    #pick a random from the list
    random_x = random.randint(0,(total_symbols-1))
    pwd_symbols.append(symbols[random_x])
    #print(symbols[random_x]) #QC
#print(pwd_symbols) #QC

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

#glue all together
pwd_total1 = pwd_letters + pwd_numbers + pwd_symbols
print('Your GENERATED PWD:')
#print witout spaces
print(*pwd_total1,sep='')


pwd_total2 = pwd_total1 
#shuffle joint list
random.shuffle(pwd_total2)
print(*pwd_total2,sep='')
