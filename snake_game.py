import tkinter as tk
from tkinter import messagebox
import random

class SnakeWaterGunGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Water Gun Game")
        self.root.geometry("400x300")

        
        self.title_label = tk.Label(root, text="Snake, Water, Gun Game", font=("Arial", 16))
        self.title_label.pack(pady=10)

        
        self.instruction_label = tk.Label(root, text="Choose one option:", font=("Arial", 12))
        self.instruction_label.pack(pady=10)

        
        self.snake_button = tk.Button(root, text="Snake", width=10, command=lambda: self.play_game('s'))
        self.snake_button.pack(pady=5)

        self.water_button = tk.Button(root, text="Water", width=10, command=lambda: self.play_game('w'))
        self.water_button.pack(pady=5)

        self.gun_button = tk.Button(root, text="Gun", width=10, command=lambda: self.play_game('g'))
        self.gun_button.pack(pady=5)

        
        self.result_label = tk.Label(root, text="", font=("Arial", 12))
        self.result_label.pack(pady=20)

    def play_game(self, youstr):
        
        computer = random.choice([-1, 0, 1])
        youDict = {"s": 1, "w": -1, "g": 0}
        reverseDict = {1: "snake", -1: "water", 0: "gun"}

        you = youDict[youstr]

        
        result_text = f"You chose {reverseDict[you]}. Computer chose {reverseDict[computer]}.\n"

        
        if computer == you:
            result_text += "It's a draw!"
        else:
            if (computer == -1 and you == 1) or (computer == 1 and you == 0) or (computer == 0 and you == -1):
                result_text += "You win!"
            else:
                result_text += "You lose!"

        self.result_label.config(text=result_text)

if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeWaterGunGame(root)
    root.mainloop()
