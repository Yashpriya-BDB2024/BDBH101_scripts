## Quiz Operations
import sqlite3
import time

def initialize_database():
    conn = sqlite3.connect("quiz.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS questions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            option_a TEXT NOT NULL,
            option_b TEXT NOT NULL,
            option_c TEXT NOT NULL,
            option_d TEXT NOT NULL,
            answer TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def insert_bulk_questions(questions_list):
    conn = sqlite3.connect("quiz.db")
    cursor = conn.cursor()
    cursor.executemany("""
        INSERT INTO questions (question, option_a, option_b, option_c, option_d, answer)
        VALUES (?, ?, ?, ?, ?, ?)
    """, questions_list)
    conn.commit()
    conn.close()

def question_generator():
    conn = sqlite3.connect("quiz.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, question, option_a, option_b, option_c, option_d, answer FROM questions")
    rows = cursor.fetchall()
    conn.close()
    for row in rows:
        yield {
            "id": row[0],
            "question": row[1],
            "options": [f"1) {row[2]}", f"2) {row[3]}", f"3) {row[4]}", f"4) {row[5]}"],
            "answer": row[6]
        }

def map_key_to_answer(key):
    key_map = {
        "1": "A",
        "2": "B",
        "3": "C",
        "4": "D",
        "0": "SKIP"
    }
    return key_map.get(key.upper(), None)

def start_quiz():
    print("\nWelcome to the Python Sprint Quiz!")
    print("Answer the following questions or press '0' to skip.\n")
    questions = question_generator()
    correct_answers = 0
    incorrect_answers = 0
    skipped = 0
    score = 0
    for q in questions:
        print("\nQuestion:")
        print(q["question"])
        for option in q["options"]:
            print(option)
        start_time = time.time()
        user_input = input("\nYour answer (1, 2, 3, 4 or '0' to skip): ").strip().upper()
        end_time = time.time()
        time_taken = end_time - start_time
        mapped_answer = map_key_to_answer(user_input)
        if mapped_answer == "SKIP":
            skipped += 1
            print("Question skipped!\n")
            continue
        bonus_points = 0
        if time_taken <= 10:
            bonus_points = 2
        elif time_taken <= 30:
            bonus_points = 1
        if mapped_answer == q["answer"]:
            print(f"Correct! You earned {1 + bonus_points} points.\n")
            score += (1 + bonus_points)
            correct_answers += 1
        elif mapped_answer is not None:
            print(f"Incorrect! The correct answer was {q['answer']}. You lost 0.25 point.\n")
            score -= 0.25
            incorrect_answers += 1
        else:
            print("Invalid input! Moving to the next question.\n")
        if time_taken > 45:
            print("Time's up! Moving to the next question.\n")
    print(f"Congratulations! Your final score is: {score}")

    return correct_answers, incorrect_answers, skipped