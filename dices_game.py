import random
import tkinter as tk
from tkinter import messagebox

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
    def __init__(self, root, target_score=200):
        self.root = root
        self.dices = SeveralDices(2)
        self.target_score = target_score
        self.current_player = 0
        self.scores = [0, 0]
        self.turn_total = 0

        self.setup_ui()

    def setup_ui(self):
        self.root.title("Dice Game")
        self.root.configure(bg="#333333")

        self.label_player = tk.Label(self.root, text="Au joueur 1 de jouer", font=('Helvetica', 16), fg="#FFFFFF", bg="#333333")
        self.label_player.pack(pady=10)

        self.label_dice1 = tk.Label(self.root, text="De 1: 0", font=('Helvetica', 16), fg="#FFFFFF", bg="#333333")
        self.label_dice1.pack(pady=5)

        self.label_dice2 = tk.Label(self.root, text="De 2: 0", font=('Helvetica', 16), fg="#FFFFFF", bg="#333333")
        self.label_dice2.pack(pady=5)

        self.label_roll_total = tk.Label(self.root, text="Score du lancer: 0", font=('Helvetica', 16), fg="#FFFFFF", bg="#333333")
        self.label_roll_total.pack(pady=5)

        self.label_turn_total = tk.Label(self.root, text="Total provisoire du tour: 0", font=('Helvetica', 16), fg="#FFFFFF", bg="#333333")
        self.label_turn_total.pack(pady=5)

        self.button_roll = tk.Button(self.root, text="Lancer les dés", command=self.roll_dice, font=('Helvetica', 16), bg="#4CAF50", fg="#FFFFFF", activebackground="#45a049")
        self.button_roll.pack(pady=10)

        self.button_stop = tk.Button(self.root, text="Arrêter", command=self.stop_turn, font=('Helvetica', 16), bg="#4CAF50", fg="#FFFFFF", activebackground="#45a049")
        self.button_stop.pack(pady=10)

    def roll_dice(self):
        roll_result = self.dices.roll_all()
        roll_total = self.dices.get_total()

        self.label_dice1.config(text=f"De 1: {roll_result[0]}")
        self.label_dice2.config(text=f"De 2: {roll_result[1]}")
        self.label_roll_total.config(text=f"Score du lancer: {roll_total}")

        if roll_total == 7:
            self.turn_total = 0
            self.label_turn_total.config(text="Total provisoire du tour: 0")
            self.end_turn()
            return

        if self.dices.is_double():
            roll_total *= 2
            messagebox.showinfo("Double!", "Le score du lancer est doublé!")

        self.turn_total += roll_total
        self.label_turn_total.config(text=f"Total provisoire du tour: {self.turn_total}")

    def stop_turn(self):
        self.scores[self.current_player] += self.turn_total
        self.label_turn_total.config(text=f"Total du tour: {self.turn_total}")
        messagebox.showinfo("Tour terminé", f"Score total du joueur {self.current_player + 1}: {self.scores[self.current_player]}")
        
        if self.scores[self.current_player] >= self.target_score:
            messagebox.showinfo("Vainqueur", f"Le vainqueur est le joueur {self.current_player + 1}")
            self.root.quit()
            return

        self.current_player = 1 if self.current_player == 0 else 0
        self.turn_total = 0
        self.label_player.config(text=f"Au joueur {self.current_player + 1} de jouer")

    def end_turn(self):
        self.scores[self.current_player] += self.turn_total
        self.turn_total = 0
        self.label_turn_total.config(text="Total du tour: 0")
        self.current_player = 1 if self.current_player == 0 else 0
        self.label_player.config(text=f"Au joueur {self.current_player + 1} de jouer")

if __name__ == "__main__":
    root = tk.Tk()
    game = Game(root)
    root.mainloop()
