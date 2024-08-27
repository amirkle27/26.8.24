def check_guess (random_num: int, user_num: int) -> str:
    if not isinstance (user_num, int):
        raise ValueError
    if user_num > 100 or user_num < 0:
        raise ValueError ("Number out of range")
    if random_num == user_num:
        return "BINGO!!"
    if user_num < random_num:
        return "Guess higher"
    if user_num > random_num:
        return "Guess lower"

def play_guessing_game ():
    import random

    random_num = random.randint (1,100)
    while True:
        try:
            user_num:int = int(input("Please guess a number between 1-100:"))
            feedback:str = check_guess(random_num,user_num)
            print(feedback)
            if feedback=="BINGO!!":
                break
        except Exception as ex:
            print(ex)

play_guessing_game()