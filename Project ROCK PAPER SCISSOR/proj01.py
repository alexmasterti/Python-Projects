import random

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.weapon_counts = {'rock': 0, 'paper': 0, 'scissors': 0}

    def choose_weapon(self):
        pass

    def update_score(self, result):
        if result == "win":
            self.score += 1

    def update_weapon_counts(self, weapon):
        self.weapon_counts[weapon] += 1


class HumanPlayer(Player):
    def choose_weapon(self):
        while True:
            choice = input("Choose your weapon: (R)ock, (P)aper, (S)cissors, or (Q)uit: ").lower()
            if choice in ['r', 'p', 's', 'q']:
                return choice
            else:
                print("Invalid choice. Please choose again.")


class ComputerPlayer(Player):
    def choose_weapon(self, human_weapon_counts):       
        if sum(human_weapon_counts.values()) > 0:
            preferred_weapon = max(human_weapon_counts, key=human_weapon_counts.get)
            if preferred_weapon == 'rock':
                return 'paper'
            elif preferred_weapon == 'paper':
                return 'scissors'
            else:
                return 'rock'
        else:
            return random.choice(['rock', 'paper', 'scissors'])


class Game:
    def __init__(self):
        self.user = HumanPlayer("HumanPlayer")
        self.computer = ComputerPlayer("ComputerPlayer")
        self.choices = {'r': 'rock', 'p': 'paper', 's': 'scissors'}
        self.outcomes = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}

    def compare_weapons(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "tie"
        elif self.outcomes[user_choice] == computer_choice:
            return "win"
        else:
            return "lose"

    def display_results(self, result, user_choice, computer_choice):
        print(f"You chose {user_choice}, Computer chose {computer_choice}.")
        print("You win!" if result == "win" else "You lose!" if result == "lose" else "It's a tie!")

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
        return True

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
    game = Game()
    game.play_game()
