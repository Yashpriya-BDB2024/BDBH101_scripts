import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

def plot_quiz_results(correct_answers, incorrect_answers, skipped):
    categories = ['Correct', 'Incorrect', 'Skipped']
    values = [correct_answers, incorrect_answers, skipped]
    plt.figure(figsize=(7, 7))
    plt.pie(values, labels=categories, autopct='%1.1f%%', startangle=90, colors=['#4CAF50', '#F44336', '#FFC107'])
    plt.title('Quiz Results')
    plt.axis('equal')
    plt.show()