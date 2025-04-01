import random
def game():
    print("You are playing a game..")
    score = random.randint(1, 62) 
    # fetch the score
    with open("./Hi-score.txt", "r") as f:
        highscore = f.read()
        if(highscore != "") :
            highscore = int(highscore)
        else :
            highscore = 0
    print(f"Your score is {score}")
    if(score > highscore) :
        with open("./Hi-score.txt", "w") as f:
            f.write(str(score))
    print("Game ended")
game()