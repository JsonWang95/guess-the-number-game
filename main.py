import random

def guess():
  player_guess = int(input("Make a guess: "))
  return player_guess

def compare(guess, answer):
  if guess == answer:
    return "win"
  elif guess > answer:
    return "high"
  else:
    return "low"

def play_game():
  is_game_over = False

  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

  if difficulty == "easy":
    attempt_left = 10
  elif difficulty == "hard":
    attempt_left = 5

  answer = random.randint(1, 100)


  while not is_game_over:
    print(f"You have {attempt_left} attempts remaining to guess the number.")
    player_guess = guess()
    result = compare(player_guess, answer)
    attempt_left -= 1

    if result == "win":
      is_game_over = True
      print(f"You got it! The answer was {answer}")
      
    elif result == "high":
      print("Too high.")
      if attempt_left != 0:
        print("Guess again.")
      else:
        print("You've run out of guesses, you lose.")
        is_game_over = True

    elif result == "low":
      print("Too low.")
      if attempt_left != 0:
        print("Guess again.")
      else:
        print("You've run out of guesses, you lose.")
        is_game_over = True

play_game()




