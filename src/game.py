from modules.db_modules import *
from random import randint


class Game:
    def __init__(self, lives=3):
        self.lives = lives

    @staticmethod
    def line(length):
        print("-" * length)

    @staticmethod
    def game_title():
        Game.line(20)
        print("Welcome to the game!")
        Game.line(20)

    @staticmethod
    def difficulties_menu():
        difficulties = ["Easy", "Medium", "Hard", "Very Hard", "Impossible"]
        for index, difficulty in enumerate(difficulties):
            print(f"[{index}] {difficulty}")
            Game.line(20)

    def full_game(self):
        self.lives = 3
        Game.game_title()
        Game.difficulties_menu()
        difficulty = int(input("Choose a difficulty: "))

        Game.line(20)

        if difficulty == 0:  # Easy
            limit = 10

        if difficulty == 1:  # Medium
            limit = 20

        if difficulty == 2:  # Hard
            limit = 35

        if difficulty == 3:  # Very Hard
            limit = 50

        if difficulty == 4:  # Impossible
            limit = 100

        CPU_number = randint(0, limit)
        print(f"The computer chose a number between 0 and {limit}. Try to guess it!")

        Game.line(20)
        while self.lives > 0:
            guess = int(input("Guess: "))
            if guess == CPU_number:
                print("You won!")
                return
            print(f"Oops, wrong number. You have {self.lives} lives left. Try again!")
            self.lives -= 1

        Game.line(20)
        print("You lost!")

        Game.line(20)
        continue_game = str(input("Want to play again? [Y/N]: ")).strip().title()[0]
        if continue_game == "Y":
            process_one = Game()
            process_one.full_game()

        elif continue_game == "N":
            print("Thanks for playing!")
            exit()


process_one = Game()
process_one.full_game()
