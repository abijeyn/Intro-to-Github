from utils import load_questions
from quiz import run_quiz, display_review

def main():
    filepath = 'questions.json'
    
    try:
        # Load the questions from JSON
        questions = load_questions(filepath)
        
        if not questions:
            print("No questions found in the file.")
            return

        print("--- Welcome to the Quiz Reviewer CLI ---")
        
        # Run the quiz logic and get the final score
        final_score = run_quiz(questions)
        
        # Display the final score
        print(f"\nYour final score: {final_score}/{len(questions)}")
        
        # Optionally display the review
        show_review = input("\nWould you like to review the correct answers? (y/n): ").lower()
        if show_review == 'y':
            display_review(questions)
            
        print("Thank you for using the Quiz Reviewer!")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
