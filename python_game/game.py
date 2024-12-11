from tkinter import *
from PIL import Image, ImageTk
from random import randint

def resize_image(image, width, height):
    return image.resize((width, height), Image.Resampling.LANCZOS)

root = Tk()
root.title("Rock Scissors Paper")
root.geometry("600x500")
root.configure(bg="#2c3e50")


rock_img = resize_image(Image.open("rock.png"), 100, 100)
paper_img = resize_image(Image.open("paper.png"), 100, 100)
scissor_img = resize_image(Image.open("scissor.png"), 100, 100)

rock_img_comp = resize_image(Image.open("rock.png"), 100, 100)
paper_img_comp = resize_image(Image.open("paper.png"), 100, 100)
scissor_img_comp = resize_image(Image.open("scissor.png"), 100, 100)


rock_img = ImageTk.PhotoImage(rock_img)
paper_img = ImageTk.PhotoImage(paper_img)
scissor_img = ImageTk.PhotoImage(scissor_img)
rock_img_comp = ImageTk.PhotoImage(rock_img_comp)
paper_img_comp = ImageTk.PhotoImage(paper_img_comp)
scissor_img_comp = ImageTk.PhotoImage(scissor_img_comp)


user_label = Label(root, image=scissor_img, bg="#2c3e50")
comp_label = Label(root, image=scissor_img_comp, bg="#2c3e50")
user_label.grid(row=1, column=3, padx=10, pady=10)
comp_label.grid(row=1, column=1, padx=10, pady=10)

# Scores
playerScore = Label(root, text=0, font=("Helvetica", 18, "bold"), bg="#2980b9", fg="white", width=5)
compScore = Label(root, text=0, font=("Helvetica", 18, "bold"), bg="#c0392b", fg="white", width=5)
playerScore.grid(row=1, column=4, padx=10)
compScore.grid(row=1, column=0, padx=10)

# Indicators
user_indicator = Label(root, text="USER", font=("Helvetica", 16, "bold"), bg="#1abc9c", fg="white", width=10)
comp_indicator = Label(root, text="COMPUTER", font=("Helvetica", 16, "bold"), bg="#e74c3c", fg="white", width=10)
user_indicator.grid(row=0, column=3, pady=10)
comp_indicator.grid(row=0, column=1, pady=10)

# Message Display
msg = Label(root, text="", font=("Helvetica", 16), bg="#2c3e50", fg="white")
msg.grid(row=2, column=2)


round_label = Label(root, text="Round: 1 / 5", font=("Helvetica", 14), bg="#2c3e50", fg="white")
round_label.grid(row=3, column=2)

round_num = 1
max_rounds = 5

# Functions
def updateMessage(x):
    msg['text'] = x

def updateUserScore():
    score = int(playerScore["text"])
    score += 1
    playerScore["text"] = str(score)

def updateCompScore():
    score = int(compScore["text"])
    score += 1
    compScore["text"] = str(score)

def checkWin(player, comp):
    global round_num
    if player == comp:
        updateMessage("It's a Tie!")
    elif (player == "rock" and comp == "scissor") or \
         (player == "paper" and comp == "rock") or \
         (player == "scissor" and comp == "paper"):
        updateMessage("You Win!")
        updateUserScore()
    else:
        updateMessage("You Lose!")
        updateCompScore()

    
    round_num += 1
    if round_num <= max_rounds:
        round_label.config(text=f"Round: {round_num} / {max_rounds}")
    else:
        declare_winner()

def declare_winner():
    player = int(playerScore["text"])
    computer = int(compScore["text"])
    if player > computer:
        updateMessage("Game Over: You Win!")
    elif player < computer:
        updateMessage("Game Over: Computer Wins!")
    else:
        updateMessage("Game Over: It's a Tie!")

def updateChoice(x):
    if round_num > max_rounds:
        return  # Disable further clicks after max rounds
    
    # Computer choice
    compChoice = choices[randint(0, 2)]
    if compChoice == "rock":
        comp_label.configure(image=rock_img_comp)
    elif compChoice == "paper":
        comp_label.configure(image=paper_img_comp)
    else:
        comp_label.configure(image=scissor_img_comp)

    # User choice
    if x == "rock":
        user_label.configure(image=rock_img)
    elif x == "paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissor_img)

    checkWin(x, compChoice)


choices = ["rock", "paper", "scissor"]

rock = Button(root, text="ROCK", font=("Helvetica", 14), bg="#e74c3c", fg="white", command=lambda: updateChoice("rock"))
paper = Button(root, text="PAPER", font=("Helvetica", 14), bg="#3498db", fg="white", command=lambda: updateChoice("paper"))
scissor = Button(root, text="SCISSOR", font=("Helvetica", 14), bg="#2ecc71", fg="white", command=lambda: updateChoice("scissor"))

rock.grid(row=4, column=1, pady=20)
paper.grid(row=4, column=2, pady=20)
scissor.grid(row=4, column=3, pady=20)


root.mainloop()
