# Mastermind
from random import choices, shuffle

colors = [
    "red",
    "green",
    "blue", 
    "orange", 
    "yellow",
    "purple",
    "brown"
]

GUESSES_MAX = 12


def play_game():
    game = True
    shuffle(colors)
    solution = choices(colors,k=4)
    # print(solution)
    print("initializing...")
    print("picking colors...")
    print("colors available...",colors)
    guesses = GUESSES_MAX
    while guesses > 0 and game:
        print("guesses remaining:",guesses)
        guess = input("enter guess: ")
        guess = guess.lower().split()
        if len(guess) != 4:
            print("failure: you must enter a guess for all four pegs")
            print("try again...")
            guesses = guesses - 1
            continue
        if guess == solution:
            print("success!")
            game = False
            break
        out = []
        count = 0
        for c in solution:
            g = guess[count]
            if g == c:
                out.append("hit")
            elif g in solution:
                out.append("close")
            else:
                out.append("miss")
            count = count + 1        
        print("failure:", out)
        print("try again...")
        guesses = guesses - 1

def mastermind():
    print("running mastermind...")
    
    while(True):
        play_game()
        again = input("play again? (y/n)")
        if again != 'y':
            return            
if __name__ == '__main__':
    mastermind()

