import time  # For adding delays

class Characters():
    def __init__(self, name, type, health, power ):
        self.name = name
        self.type = type
        self.health = health
        self.power = power

    def attack(self, target):
        damage = self.power
        target.health -= damage
        print(f'{self.name} ({self.type}) attacks {target.name} ({target.type}) dealing {damage} damage. {target.name}\'s health is now {target.health}.'.title())

# Available characters
characters = {
    "Barbarian": Characters('Barbarians', 'Ground', 70, 25),
    "Archer": Characters('Archers', 'Ground & Air', 60, 30),
    "Goblin": Characters('Goblins', 'Ground', 40, 40),
    "Giant": Characters('Giant', 'Ground', 150, 50),
    "Balloon": Characters('Balloons', 'Air', 120, 80),
    "Wizard": Characters('Wizard', 'Ground & Air', 90, 60)
}

def choose_character(player_name):
    print(f"\n--- {player_name}'s Round to Choose ---")
    print("Available Characters:")
    for name in characters:
        print(f"- {name}")
    while True:
        choice = input("Choose a character: ").strip().title()
        if choice in characters:
            return characters[choice]
        else:
            print("Invalid character choice. Please choose from the list.")

print("--- Battle Begins! ---")

player1_char = choose_character("Player 1")
print(f"Player 1 chose: {player1_char.name} ({player1_char.type}), Health: {player1_char.health}, Power: {player1_char.power}")

player2_char = choose_character("Player 2")
print(f"Player 2 chose: {player2_char.name} ({player2_char.type}), Health: {player2_char.health}, Power: {player2_char.power}")

print("\n--- Battle Simulation ---")

# Battle loop until one character's health drops to 0 or below
round = 1
while player1_char.health > 0 and player2_char.health > 0:
    print(f"\n--- Round {round} ---")
    time.sleep(1)  # Add a small delay for better readability

    # Player 1's attack
    print(f"{player1_char.name} is attacking...")
    player1_char.attack(player2_char)
    if player2_char.health <= 0:
        break

    time.sleep(1)

    # Player 2's attack
    print(f"{player2_char.name} is attacking...")
    player2_char.attack(player1_char)
    if player1_char.health <= 0:
        break

    round += 1

print("\nBattle Ended! ->")

# Determine the winner
if player1_char.health <= 0 and player2_char.health <= 0:
    print("It's a tie! Both characters were defeated.")
elif player1_char.health <= 0:
    print(f"{player2_char.name} is the winner!")
else:
    print(f"{player1_char.name} is the winner!")

print(f"\nFinal Health ->")
print(f"{player1_char.name}'s health: {player1_char.health}")
print(f"{player2_char.name}'s health: {player2_char.health}")