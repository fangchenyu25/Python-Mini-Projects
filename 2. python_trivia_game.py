# list of questions
# store the answers
# randomly pick questions
# ask the questions
# see if they are corrrect
# keep track of the score
# tell the user their score

import random

questions = {
    "What is the keyword to define a function in Python?": "def",
    "Which data type is used to store True or False values?": "boolean",
    "What is the correct file extension for Python files?": ".py",
    "Which symbol is used to comment in Python?": "#",
    "What function is used to get input from the user?": "input",
    "How do you start a for loop in Python?": "for",
    "What is the output of 2 ** 3 in Python?": "8",
    "What keyword is used to import a module in Python?": "import",
    "What does the len() function return?": "length",
    "What is the result of 10 // 3 in Python?": "3",
    "What keyword is used to create a variable without assigning a value?": "None",
    "Which data type is used to store text in Python?": "string",
    "Which data type is used to store whole numbers in Python?": "integer",
    "Which data type is used to store decimal numbers in Python?": "float",
    "What function converts a string to an integer?": "int",
    "What function converts a string to a float?": "float",
    "What function converts a number to a string?": "str",
    "Which function returns the data type of a variable?": "type",
    "Which keyword is used to check the data type?": "isinstance",
    "What is the value of True + True in Python?": "2",
    "What is the symbol for floor division in Python?": "//",
    "What is the symbol for modulus (remainder) in Python?": "%",
    "What is the symbol for exponentiation in Python?": "**",
    "Which operator is used for logical AND in Python?": "and",
    "Which operator is used for logical OR in Python?": "or",
    "Which operator is used for logical NOT in Python?": "not",
    "What comparison operator checks for equality?": "==",
    "What comparison operator checks for inequality?": "!=",
    "What operator is used to assign a value to a variable?": "=",
    "What is the result of 5 % 2?": "1",
    "What method removes whitespace from both ends of a string?": "strip",
    "What method converts a string to lowercase?": "lower",
    "What method converts a string to uppercase?": "upper",
    "What method returns the number of occurrences of a substring?": "count",
    "What method replaces a substring with another string?": "replace",
    "What method returns the index of a substring?": "find",
    "What symbol is used to concatenate strings?": "+",
    "What keyword is used to define a multiline string?": "triple quotes",
    "What function returns the ASCII value of a character?": "ord",
    "What function returns the character for an ASCII value?": "chr",
    "What function adds an element to the end of a list?": "append",
    "What function removes and returns the last element of a list?": "pop",
    "What method sorts a list in place?": "sort",
    "What function returns a sorted copy of a list?": "sorted",
    "What method reverses a list in place?": "reverse",
    "How do you access the first element of a list named my_list?": "my_list[0]",
    "How do you access the last element of a list named my_list?": "my_list[-1]",
    "What keyword is used to loop over elements in a list?": "for",
    "Which function returns the number of elements in a list?": "len",
    "What method removes the first occurrence of an element in a list?": "remove",
    "Are tuples mutable or immutable in Python?": "immutable",
    "What symbol is used to define a tuple?": "parentheses",
    "How do you create a tuple with one element?": "(element,)",
    "Which function converts a list to a tuple?": "tuple",
    "Which function converts a tuple to a list?": "list",
    "How do you access the second element of a tuple named my_tuple?": "my_tuple[1]",
    "What is the keyword for unpacking tuples?": "unpack",
    "How do you check if an item exists in a tuple?": "in",
    "What is the length of the tuple (1, 2, 3)?": "3",
    "What symbol separates items in a tuple?": "comma",
    "What symbol is used to define a dictionary?": "curly braces",
    "What method returns all the keys in a dictionary?": "keys",
    "What method returns all the values in a dictionary?": "values",
    "What method returns all key-value pairs in a dictionary?": "items",
    "How do you access the value for key 'name' in a dictionary called my_dict?": "my_dict['name']",
    "What method removes a key-value pair from a dictionary?": "pop",
    "Which method removes all items from a dictionary?": "clear",
    "What is the default value returned by dict.get() if the key is not found?": "None",
    "What method updates a dictionary with another dictionary?": "update",
    "Which function creates a shallow copy of a dictionary?": "copy",
    "What symbol is used to define a set?": "curly braces",
    "What method adds an element to a set?": "add",
    "What method removes an element from a set (without error if missing)?": "discard",
    "What method removes and returns an arbitrary element from a set?": "pop",
    "What method removes all elements from a set?": "clear",
    "What method returns the union of two sets?": "union",
    "What method returns the intersection of two sets?": "intersection",
    "What method returns the difference of two sets?": "difference",
    "What method checks if one set is a subset of another?": "issubset",
    "What method checks if one set is a superset of another?": "issuperset",
    "What keyword starts a conditional statement?": "if",
    "What keyword is used for an alternative condition?": "elif",
    "What keyword is used for the default condition?": "else",
    "What keyword is used to exit a loop prematurely?": "break",
    "What keyword is used to skip the current loop iteration?": "continue",
    "What keyword is used to define a loop that executes while a condition is true?": "while",
    "What keyword is used to iterate over a sequence?": "for",
    "Which keyword is used to define an infinite loop intentionally?": "while True",
    "What keyword is used to create a placeholder block of code?": "pass",
    "What keyword is used to define a block of code that runs after a loop finishes?": "else",
    "What keyword is used to return a value from a function?": "return",
    "What keyword is used to define a lambda function?": "lambda",
    "What keyword allows a function to access a global variable?": "global",
    "What keyword creates a variable local to a function?": "local",
    "What keyword is used to pass any number of arguments to a function?": "*args",
    "What keyword is used to pass any number of keyword arguments to a function?": "**kwargs",
    "What is the default return value of a function that doesn’t return anything?": "None",
    "Which function gets help documentation for Python objects?": "help",
    "Which function shows all attributes of an object?": "dir",
    "Which function checks if an object is callable?": "callable",
    "What function is used to open a file in Python?": "open",
    "What mode is used to open a file for reading?": "r",
    "What mode is used to open a file for writing?": "w",
    "What mode is used to append to a file?": "a",
    "What mode is used to read and write a file?": "r+",
    "What keyword is used to handle exceptions?": "try",
    "What keyword is used to catch an exception?": "except",
    "What keyword is used to execute code if no exception occurs?": "else",
    "What keyword is used to run cleanup code after try/except?": "finally",
    "What function lists all built-in modules?": "help('modules')"
}

def python_trivia_game():
    questions_list = list(questions.keys())
    while True:
        total_questions = input(f"How many questions would you like to answer? (1-{len(questions)}): ")
        if total_questions.isdigit():
            total_questions = int(total_questions)
            if 1 <= total_questions <= len(questions):
                break
            else:
                print("Please enter a number between 1 and 10.")
        else:
            print("Please enter a valid number.")

    score = 0
    selected_questions = random.sample(questions_list, total_questions)
    
    for idx, question in enumerate(selected_questions):
        print(f"{idx + 1}. {question}")
        user_answer = input("Your answer: ").lower().strip()
        correct_answer = questions[question]

        if user_answer == correct_answer.lower():
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong. The correct answer is: {correct_answer}. \n")
        
    print(f"Game over! Your final score is: {score}/{total_questions} ({score/total_questions*100:.1f}%)")

while True:
    python_trivia_game()
    if input("Play again? (y/n): ").lower() != "y":
        break
