"""
Porter Hatch
Feb 5 2023
application
"""

import requests 
import random
import html
from tkinter import *
import tkinter as tk

#session_token = None
#&token={session_token
root = tk.Tk()
root.title('Trivia Game')

continue_flag = tk.BooleanVar()
continue_flag.set(False)



def get_question(num_questions=1):
    global session_token
    response = requests.get(f"https://opentdb.com/api.php?amount={num_questions}")
    data = response.json()
    #if 'token' in data:
        #session_token = data['token']
    #print(response)
    #print(data)
    questions = []
    #if data['results']:
    for result in data['results']:
        question = html.unescape(result['question'])
        correct_answer = result['correct_answer']
        incorrect_answers = result['incorrect_answers']
        choices = [correct_answer] + incorrect_answers
        random.shuffle(choices)
        questions.append([question, choices, correct_answer])
    #print(questions)
    return questions

def ask_question(question_list):
    global continue_flag
    continue_flag.set(False)


    for question in question_list:
        q = question[0]
        choices = question[1]
        correct = question[2]
                
        question_label = tk.Label(root, text = f"Question: {q}")
        question_label.pack()
        
        choices_label = tk.Label(root, text = f"Choices: {choices}")
        choices_label.pack()
    
        see_answer = tk.Label(root, text = "press ENTER to see the correct answer.")
        see_answer.pack()

        continue_button = tk.Button(root, text = "ENTER", command = continue_program)
        continue_button.pack()

        root.wait_variable(continue_flag)
    
        answer_label = tk.Label(root, text = f"Answer: {correct}")
        answer_label.pack()

def continue_program():
    global continue_flag
    continue_flag.set(True)



def mainloop():

    def begin_questions():
        get_question_label.destroy()
        continue_button.destroy()

        num_questions = int(num_questions_entry.get())
        num_questions_entry.destroy()

        question_list = get_question(num_questions)
        ask_question(question_list)

    get_question_label = tk.Label(root, text = "How many trivia questions would you like? ")
    get_question_label.pack()

    num_questions_entry = tk.Entry(root)
    num_questions_entry.pack()
        
    continue_button = tk.Button(root, text="ENTER", command=begin_questions)
    continue_button.pack()
    
    

    root.mainloop()
    
if __name__ == "__main__":
    mainloop()
