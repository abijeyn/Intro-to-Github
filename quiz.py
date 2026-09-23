def run_quiz(questions_list):
    """
    Iterates through questions, displays choices, accepts user input, and tracks correct answers.
    
    Input: List of Question dictionaries.
    Returns: Final score (integer).
    """
    score = 0
    for question in questions_list:
        print(f"\nQuestion: {question['question_text']}")
        for index, choice in enumerate(question['choices']):
            print(f"{index + 1}. {choice}")
        
        while True:
            user_input = input("Enter the number of your choice: ")
            try:
                choice_index = int(user_input) - 1
                if 0 <= choice_index < len(question['choices']):
                    user_answer = question['choices'][choice_index]
                    if user_answer == question['correct_answer']:
                        score += 1
                        print("Correct!")
                    else:
                        print(f"Incorrect. The correct answer was: {question['correct_answer']}")
                    break
                else:
                    print(f"Please enter a number between 1 and {len(question['choices'])}.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    
    return score

def display_review(questions_list):
    """
    Prints out the questions alongside their correct answers.
    
    Input: List of Question dictionaries.
    Returns: None.
    """
    print("\n--- Quiz Review ---")
    for question in questions_list:
        print(f"Q: {question['question_text']}")
        print(f"A: {question['correct_answer']}\n")
