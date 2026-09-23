# SYSTEM DESIGN

## Problem Statement
This application is a Quiz Reviewer CLI tool designed for students.

## Requirements

### Functional
- [ ] Load quiz questions from a JSON file
- [ ] Display questions with choices
- [ ] Accept user answers
- [ ] Calculate and show final score
- [ ] Display correct answer after quiz

### Non-Functional
- Language: Python
- No external database
- Must run locally

## Architecture & Tech Stack

### Tech Stack

| Layer | Choice |
|---|---|
| Language | Python 3 |
| Framework | None (CLI-based application) |
| Storage | JSON file |
| Testing | pytest |

## Project Structure

project/
├── main.py        # Main program entry
├── quiz.py        # Quiz logic
├── questions.json # Quiz data
├── utils.py       # Helper functions
├── tests/
│   └── test_quiz.py
└── requirements.txt

## Data Model

### Entities (questions.json)
The application will store questions in a JSON array of objects.
- **Question**: 
  - `id` (integer)
  - `question_text` (string)
  - `choices` (list of strings)
  - `correct_answer` (string)

## API Contracts (Core Functions)

### `load_questions(filepath)`
- **Input:** `filepath` (string, path to `questions.json`)
- **Returns:** A list of Question dictionaries.
- **Effect:** Handles file reading, parses the JSON, and raises an error if the file is missing or corrupted.

### `run_quiz(questions_list)`
- **Input:** List of Question dictionaries.
- **Returns:** Final score (integer).
- **Effect:** Iterates through the questions, displays choices, accepts user input, and tracks the number of correct answers.

### `display_review(questions_list)`
- **Input:** List of Question dictionaries.
- **Returns:** None.
- **Effect:** Prints out the questions alongside their correct answers for the student to review after the quiz finishes.

## Testing Plan

### Unit Tests
- [ ] `test_load_questions_valid`: Successfully loads and parses valid JSON data from `questions.json`.
- [ ] `test_load_questions_invalid`: Properly handles a missing or corrupted JSON file without crashing.
- [ ] `test_score_calculation`: Correctly increments the user's score when the correct answer is selected.
- [ ] `test_invalid_user_input`: Gracefully handles invalid user input (e.g., typing a letter when a number choice is expected).

### Integration Tests
- [ ] Full flow: Load questions from JSON → run the quiz loop → accept user answers → display final score and review.

### How to Run
pytest tests/ -v