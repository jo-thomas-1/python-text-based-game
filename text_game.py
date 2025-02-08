import time
import random

def slow_print(text, delay=0.05):
    """
    Prints text with a slight delay to enhance the storytelling experience.
    """
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def main_menu():
    """
    Displays the main menu and handles user selection.
    """
    while True:
        print("\n=== Text Adventure Game ===")
        print("1. Start New Game")
        print("2. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            start_game()
        elif choice == '2':
            slow_print("Thanks for playing! Goodbye.")
            break
        else:
            slow_print("Invalid choice. Please select again.")

def create_character():
    """
    Allows the player to create their character with a name and class.
    """
    slow_print("Welcome, adventurer! Let's create your character.")
    name = input("Enter your character's name: ")
    classes = ['Warrior', 'Mage', 'Rogue']
    print("Choose a class:")
    for index, cls in enumerate(classes, start=1):
        print(f"{index}. {cls}")
    
    while True:
        try:
            choice = int(input("Enter the number of your chosen class: "))
            if 1 <= choice <= len(classes):
                player_class = classes[choice - 1]
                break
            else:
                slow_print("Invalid selection. Try again.")
        except ValueError:
            slow_print("Please enter a valid number.")
    
    slow_print(f"Welcome, {name} the {player_class}! Your adventure begins now...")
    return {'name': name, 'class': player_class, 'inventory': [], 'health': 100}

def start_game():
    """
    Begins the main game loop with a structured storyline.
    """
    player = create_character()
    slow_print("You find yourself at the entrance of a dark forest. Do you enter?")
    
    while True:
        print("1. Enter the forest")
        print("2. Walk away")
        choice = input("What do you do? ")
        if choice == '1':
            enter_forest(player)
            break
        elif choice == '2':
            slow_print("You decide it's safer to stay away. Maybe another day...")
            break
        else:
            slow_print("Invalid choice. Please select again.")

def enter_forest(player):
    """
    Handles the forest adventure, leading to the main storyline.
    """
    slow_print("You step into the eerie forest, the trees whispering around you.")
    slow_print("As you walk further, you hear a rustling in the bushes...")
    
    print("1. Investigate the noise")
    print("2. Keep walking")
    choice = input("What do you do? ")
    if choice == '1':
        encounter_wolf(player)
    else:
        slow_print("You ignore the noise and continue your journey deeper into the forest.")
    
    slow_print("After walking for an hour, you arrive at an ancient ruin. A massive door stands before you, covered in strange symbols.")
    solve_puzzle(player)

def encounter_wolf(player):
    """
    Simulates an encounter with a wild wolf.
    """
    slow_print("A wild wolf jumps out, growling at you!")
    print("1. Fight the wolf")
    print("2. Run away")
    choice = input("What do you do? ")
    if choice == '1':
        fight_wolf(player)
    else:
        slow_print("You manage to escape, but barely. Your heart pounds as you run.")

def fight_wolf(player):
    """
    Handles combat with the wolf, including random outcomes.
    """
    slow_print("You engage in battle with the wolf!")
    if random.randint(1, 10) > 4:
        slow_print("You defeat the wolf and find a healing potion in its den!")
        player['inventory'].append('Healing Potion')
    else:
        slow_print("The wolf bites you before you drive it away. You lose 20 health.")
        player['health'] -= 20

def solve_puzzle(player):
    """
    Presents a simple puzzle to unlock the ancient door.
    """
    slow_print("An inscription reads: 'I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?'")
    answer = input("Enter your answer: ").strip().lower()
    if answer == 'echo':
        slow_print("The door rumbles open, revealing a grand chamber.")
        final_challenge(player)
    else:
        slow_print("The door remains shut. Try again.")
        solve_puzzle(player)

def final_challenge(player):
    """
    Leads to the final confrontation with the antagonist.
    """
    slow_print("Inside, a shadowy figure awaits you. The Sorcerer of the Forgotten Temple glares at you.")
    slow_print("'You have come far, but this is where your journey ends,' he hisses.")
    print("1. Attack the sorcerer")
    print("2. Try to reason with him")
    choice = input("What do you do? ")
    if choice == '1':
        fight_sorcerer(player)
    else:
        slow_print("You attempt to reason, but the sorcerer launches a spell! You have no choice but to fight.")
        fight_sorcerer(player)

def fight_sorcerer(player):
    """
    The final battle against the sorcerer.
    """
    slow_print("A fierce battle begins!")
    if random.randint(1, 10) > 5:
        slow_print("You overcome the sorcerer and claim victory! The temple's magic fades, and peace is restored.")
        slow_print("Congratulations, hero! You have completed your quest.")
    else:
        slow_print("The sorcerer defeats you with a powerful spell. Darkness consumes you...")
        slow_print("Game Over.")

def main():
    """
    Entry point of the game.
    """
    main_menu()

if __name__ == "__main__":
    main()
