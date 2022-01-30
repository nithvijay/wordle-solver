import inquirer
from blessed import Terminal

import solver
from fetch import get_solution

term = Terminal()


def ask_fetch():
    print(term.clear)
    choice = inquirer.list_input("Do you want to fetch today's solution from the website?", choices=['Yes', 'No'])
    if choice == "Yes":
        ans = get_solution()
        if ans:
            print(f"Today's word is: {ans}")
        else:
            print("Failed")
    else:
        return True


def read_data():
    with open("wordle_solver/wordle.txt", "r") as f:
        wordle = f.read().split()
    return wordle


def validate_words(answers, current):
    return len(current) == 5 and current.isalpha()


def make_questions(guessed_word):
    to_ret = []
    for i, letter in enumerate(guessed_word):
        to_ret.append(inquirer.List(i, message=f"Result from '{letter}'?",
                                    choices=['Incorrect', 'Misplaced', 'Perfect']))
    return to_ret


def game():
    position_dict = {0: "1st", 1: "2nd", 2: "3rd", 3: "4th", 4: "5th", 5: "6th"}
    perfect = []
    misplaced = []
    incorrect = []

    wordle = read_data()
    print("\nHere are 20 of the best words to choose...")
    print(list(solver.get_best_words(perfect, misplaced, incorrect, wordle, n=20)))
    print()
    for guess_index in range(6):
        # guess
        questions = [inquirer.Text(
            'word', message=f'What was your {position_dict[guess_index]} word?', validate=validate_words)]
        guessed_word = inquirer.prompt(questions)['word']
        print(term.clear)
        # results
        questions = make_questions(guessed_word)
        answers = inquirer.prompt(questions)

        for i, letter in enumerate(guessed_word):
            if answers[i] == "Perfect":
                perfect.append({"index": i, "character": letter})
            elif answers[i] == "Misplaced":
                misplaced.append({"index": i, "character": letter})
            else:
                incorrect.append(letter)
        print(term.clear)
        if len({perfect_dict['index'] for perfect_dict in perfect}) == 5:
            print("Congrats!")
            break

        print("\nHere are 20 of the best words to choose...")
        print(list(solver.get_best_words(perfect, misplaced, incorrect, wordle, n=20)))
        print()


if __name__ == "__main__":
    if ask_fetch():
        game()
