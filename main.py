import random
from word import Word
from man import Man
import console_printing


def main():
    letters = random.randint(4, 7)

    word = Word(letters)
    man = Man()

    while not man.isHanged() and not word.if_won():
        console_printing.refresh(word, man)
        guess = console_printing.get_guess(word, man)

        if word.check_letter(guess):
            console_printing.refresh(word, man)
            console_printing.correct_guess()

        else:
            man.addBodyPart()
            console_printing.refresh(word, man)
            console_printing.incorrect_guess()

    if word.if_won():
        console_printing.winning_message(word)

    else:
        console_printing.losing_message(word)

if __name__ == "__main__":
    main()
