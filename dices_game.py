import random

class Dice:
    faces = 6

    def __init__(self):
        self.value = 1

    def roll(self):
        self.value = random.randint(1, Dice.faces)
        return self.value

class SeveralDices:
    def __init__(self, number_of_dices):
        self.number_of_dices = number_of_dices
        self.dices = [Dice() for _ in range(number_of_dices)]

    def roll_all(self):
        return [dice.roll() for dice in self.dices]

    def get_values(self):
        return [dice.value for dice in self.dices]

    def get_total(self):
        return sum(dice.value for dice in self.dices)

    def is_double(self):
        values = self.get_values()
        return all(value == values[0] for value in values)

class Game:
    def __init__(self, target_score=200):
        self.dices = SeveralDices(2)
        self.target_score = target_score
        self.current_player = 0
        self.scores = [0, 0]

    def play_turn(self):
        print(f"Au joueur {self.current_player + 1} de jouer :")
        turn_total = 0

        while True:
            roll_result = self.dices.roll_all()
            roll_total = self.dices.get_total()
            print(f"De 1 : {roll_result[0]}  ,  De 2 :  {roll_result[1]}")
            print(f"Score du lancer : {roll_total}")

            if roll_total == 7:
                print("Total provisoire du tour : 0")
                turn_total = 0
                break

            if self.dices.is_double():
                roll_total *= 2
                print("Le score du lancer est doublé!")

            turn_total += roll_total
            print(f"Total provisoire du tour : {turn_total}")

            action = input("Saisir 0 pour arrêter ou 1 pour continuer : ")
            if action == '0':
                self.scores[self.current_player] += turn_total
                break

        self.scores[self.current_player] += turn_total
        print(f"Total du tour : {turn_total}")
        print(f"Score total du joueur {self.current_player + 1} : {self.scores[self.current_player]}\n")

        if self.scores[self.current_player] >= self.target_score:
            print(f"Le vainqueur est le joueur {self.current_player + 1}")
            return True

        self.current_player = 1 if self.current_player == 0 else 0
        return False

    def play_game(self):
        game_over = False
        while not game_over:
            game_over = self.play_turn()

if __name__ == "__main__":
    game = Game()
    game.play_game()
