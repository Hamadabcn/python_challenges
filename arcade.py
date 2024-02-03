import sys
from rps import rps
from guess_number import guess_number

def play_game(name='PlayerOne'):
    welcome_back = False
    
    while True:
        if welcome_back == True:
            print(f"\n{name}, welcome back to the Arcade menu")
            
        player_choice = input("\n     Please choose a game:\n 1 For Rock Paper Scissors 🪨  🧻 ✂️\n 2 For Guess My Number 🔮 🔮 🔮\n\nOr Press \"x\" to Exit the Arcade\nGood Luck And Have Fun 🤞 😃 !\n\n")
        
        if player_choice not in ["1", "2", "x"]:
            print(f"\n{name}, please enter 1, 2, or x.")
            return play_game(name)
        
        welcome_back = True
        
        if player_choice == "1":
            rock_paper_scissors = rps(name)
            rock_paper_scissors()
        elif player_choice == "2":
            guess_my_number = guess_number(name)
            guess_my_number()
        else:
            print("\nSee you next time 🤗\n")
            sys.exit(f"Bye {name}! 👋\n")
            
if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Provides a personalized experience.")
    
    parser.add_argument('-n', '--name', metavar='name', required=True, help='The name of the person playing the game')
    
    args = parser.parse_args()
    
    print(f"\n{args.name}, welcome to the Arcade! 👍 🤖")
    
    play_game(args.name)
    