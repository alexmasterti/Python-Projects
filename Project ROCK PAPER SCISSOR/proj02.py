import random

#Parent class
class Player:
    # Initialize the player with a name, score, and weapon counts
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.weapon_counts = {'rock': 0, 'paper': 0, 'scissors': 0}

    # This method prompts the player to choose a weapon
    def choose_weapon(self):
        pass

    # This method updates the player's score based on the result of the game
    def update_score(self, result):
        if result == "win":
            self.score += 1

    # This method updates the count of each weapon the player has chosen
    def update_weapon_counts(self, weapon):
        self.weapon_counts[weapon] += 1

#Child class
class HumanPlayer(Player):
    # Initialize the Human player
    def __init__(self, name):
        super().__init__(name)
        
    # This method prompts the human player to choose a weapon
    def choose_weapon(self):
        while True:
            choice = input("Choose your weapon: (R)ock, (P)aper, (S)cissors, or (Q)uit: ").lower()
            if choice in ['r', 'p', 's', 'q']:
                return choice
            else:
                print("Invalid choice. Please choose again.")

#Child class
class ComputerPlayer(Player):
    # Initialize the computer player and set previous_choice to None
    def __init__(self, name):
        super().__init__(name)
        self.previous_choice = None

    # This method chooses a weapon for the computer player
    def choose_weapon(self, human_weapon_counts):
        
        # If there is a previous choice, use the win-stay, lose-shift strategy
        if self.previous_choice:
            if human_weapon_counts['rock'] > human_weapon_counts['paper'] and human_weapon_counts['rock'] > human_weapon_counts['scissors']:
                return 'paper'
            elif human_weapon_counts['paper'] > human_weapon_counts['rock'] and human_weapon_counts['paper'] > human_weapon_counts['scissors']:
                return 'scissors'
            elif human_weapon_counts['scissors'] > human_weapon_counts['rock'] and human_weapon_counts['scissors'] > human_weapon_counts['paper']:
                return 'rock'
        
        # If there is no previous choice or the strategy doesn't apply, choose randomly
        return random.choice(['rock', 'paper', 'scissors'])

class Game:
    # Initialize the game with a human player, a computer player, choices, and outcomes
    def __init__(self):
        self.user = HumanPlayer("You")
        self.computer = ComputerPlayer("Computer")
        self.choices = {'r': 'rock', 'p': 'paper', 's': 'scissors'}
        self.outcomes = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}
        
    # Compare the weapons chosen by the user and the computer to determine the result
    def compare_weapons(self, user_choice, computer_choice):        
        if user_choice == computer_choice:
            return "tie"
        elif self.outcomes[user_choice] == computer_choice:
            return "win"
        else:
            return "lose"
        
    # Display the results of the game
    def display_results(self, result, user_choice, computer_choice):        
        print(f"You chose {user_choice}, Computer chose {computer_choice}.")
        print("You win!" if result == "win" else "You lose!" if result == "lose" else "It's a tie!")

    # Play one round of the game
    def play_round(self):        
        user_choice = self.user.choose_weapon()
        if user_choice == 'q':
            return False
        
        computer_choice = self.computer.choose_weapon(self.user.weapon_counts)
        
        result = self.compare_weapons(self.choices[user_choice], computer_choice)
        
        self.user.update_score(result)
        self.computer.update_score('win' if result == 'lose' else 'lose')
        
        self.user.update_weapon_counts(self.choices[user_choice])
        self.computer.update_weapon_counts(computer_choice)
        
        self.display_results(result, self.choices[user_choice], computer_choice)
        
        # Update computer's previous choice
        self.computer.previous_choice = computer_choice
        
        return True

    # Play the game until the user chooses to quit
    def play_game(self):        
        print("Let's play Rock, Paper, Scissors!")
        while self.play_round():
            pass
        print("\nGame over!")
        print(f"Final score - {self.user.name}: {self.user.score}, {self.computer.name}: {self.computer.score}")
        print("Your weapon choices:")
        for weapon, count in self.user.weapon_counts.items():
            print(f"{weapon.capitalize()}: {count}")


if __name__ == "__main__":
    # Create a new game instance and start playing
    game = Game()
    game.play_game()
