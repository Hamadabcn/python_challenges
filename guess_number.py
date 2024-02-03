import sys
import random

def guess_number(name='PlayerOne'):
    game_count = 0
    player_wins = 0
    
    def player_guess_number():
        nonlocal name
        nonlocal player_wins
        
        player_choice = input(f"\n{name}, guess which number I am thinking of... 1, 2, or 3.\n\n")
        
        if player_choice not in ["1", "2", "3"]:
            print(f"{name}, please enter 1, 2, or 3.")
            return player_guess_number()
        
        computer_choice = random.choice("123")
        
        print(f"\n{name}, you chose {player_choice}.")
        print(f"I was thinking about the number {computer_choice}\n")
        
        player = int(player_choice)
        
        computer = int(computer_choice)
        
        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins
            
            if player == computer:
                player_wins += 1
                return f"🥳 {name}, you win 🥳"
            else:
                return f"Sorry, {name}. Better luck next time.😣"
            
        game_result = decide_winner(player, computer)
        
        print(game_result)
        
        nonlocal game_count
        game_count += 1
        
        print(f"\nGame count: {game_count}")
        print(f"\n{name} wins: {player_wins}")
        print(f"\nYour winnings percentage: {player_wins/game_count:.2%}")
        
        print(f"\nPlay again, {name}?")
        
        while True:
            play_again = input("\nY to Play again \nQ to Quit\n")
            if play_again.lower() not in ['y', 'q']:
                continue
            else:
                break
            
        if play_again.lower() == 'y':
            return player_guess_number()
        else:
            print("\n🥳 🥳 🥳 🥳 🥳 🥳")
            print("\nThank you for playing 🤗\n")
            if __name__ == "__main__":
                sys.exit(f"\nBye {name}! Bye 🖖\n")
            else:
                return
            
    return player_guess_number

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Provides a personalized game experience.")
    
    parser.add_argument(
        '-n', '--name', metavar='name', required=True, help='The name of the person playing the game')
    
    args = parser.parse_args()
    
    guess_my_number = guess_number(args.name)
    guess_my_number()
    
    #py guess_number.py -n "name of the player" to play the game
            