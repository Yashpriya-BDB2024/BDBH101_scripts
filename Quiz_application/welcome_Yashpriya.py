### Welcome the user

import matplotlib.pyplot as plt
def welcome_to_quiz():
    print("""
    \t\t\tWELCOME TO THE PYTHON SPRINT!\n
    \t\t\t\t\tThink.Test.Conquer
    """)
    fig, ax = plt.subplots(figsize=(8,5))
    ax.set_facecolor('#f4f4f4')
    ax.text(0.5, 0.5, 'WELCOME TO THE PYTHON SPRINT!', ha='center', va='center', fontsize=20, color='#4CAF50', weight='bold')
    ax.axis('off')
    plt.show()
    user_input = input("Are you ready? Press 'Enter' to begin!")

    print("Quiz Instructions : \n")
    print("""       1. This is a multiple-choice quiz to test your Python theory knowledge.
       2. You will have 10 MCQs in total.
       3. Each question has a time limit of 45 seconds.
       4. Each correct answer will earn you 1 point.
       5. Bonus points will be awarded based on how quickly you answer:
           - If you answer within 10 seconds, you will earn +2 bonus points.
           - If you answer within 30 seconds, you will earn +1 bonus point.
           - If you answer after 31-45 seconds, there will be no bonus points.
       6. Negative marks:
        -0.25 point will be deducted for each incorrect answer.
       7. Select the correct option by typing the corresponding letter (A, B, C, or D).\n
                          GOOD LUCK & ENJOY THE CHALLENGE!""")

def main():
    welcome_to_quiz()
if __name__ == "__main__":
    main()


