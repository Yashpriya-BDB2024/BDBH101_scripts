import welcome_Yashpriya
import quiz_operations_Yashpriya
import questions_Yashpriya
import result_Yashpriya

def main():
    welcome_Yashpriya.welcome_to_quiz()
    quiz_operations_Yashpriya.initialize_database()
    quiz_operations_Yashpriya.insert_bulk_questions(questions_Yashpriya.questions_list)

    correct_answers, incorrect_answers, skipped = quiz_operations_Yashpriya.start_quiz()
    result_Yashpriya.plot_quiz_results(correct_answers, incorrect_answers, skipped)

if __name__ == "__main__":
    main()
