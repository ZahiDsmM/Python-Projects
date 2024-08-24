"""
Create a simple math quiz program that asks the user 5 random math questions 
(addition, subtraction, multiplication). 
At the end, show how many they got correct.

Requirements:
 - Use tuples to store questions and answers.
 - Use loops for asking multiple questions.
 - Use functions to generate questions and check answers.
 - Import random library to generate random values between 1-10

Sample Input/Output
Q1: 10 * 3 = 30
Correct!     
Q2: 2 * 10 = 5
Incorrect.  
Q3: 8 * 5 = 44
Incorrect.  
Q4: 6 - 2 = 4
Correct!     
Q5: 5 * 10 = 50
Correct!

You got 3 out of 5 correct!
"""
import random

all_questions = [] 
count_correct = 0

for i in range(5):
     n1 = random.randint(1,10)
     n2 = random.randint(1,10)
     operation = random.choice(['+', '-', '*'])
     
     if operation == '+':
          question = f"Q{i+1}: {n1} + {n2}"
          answer = n1+n2     
     if operation == '-':
          question = f"Q{i+1}: {n1} - {n2}"
          answer = n1-n2      
     if operation == '*':
          question = f"Q{i+1}: {n1} * {n2}"
          answer = n1*n2
     
     all_questions.append((question, answer))


for question, correct_answer in all_questions:
     user_answer = int(input(f"{question} = "))
     if user_answer == correct_answer:
          print("Correct!")
          count_correct +=1
     else:
          print("Incorrect!")

print(f"\nYou got {count_correct} out of 5 correct!")
