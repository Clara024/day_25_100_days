print("Character Stats Generator")
print()

def rollDice(sides):
  import random
  dice = random.randint(1, sides)
  print("You have rolled a", dice)
  print()
  return dice

# The system will them roll 2 dice, one with 6 sides and one with 8 sides
def healthPoints():
  dice_1 = rollDice(6)
  dice_2 = rollDice(8)

#  The system will then multiply the numbers
  health = dice_1 * dice_2
  if health < 25:
    print("Uh Oh! This doesn't look good!")
    print()
  return health

# Get user input for character name
while True:
  charName = input("What is your Characters Name?: ")
  print()
  health = healthPoints()

# It give your Characters Health Score!"
  print(charName, "your health is:", health)
  print()
  restart = input("Would you like to create stats for another character?: ")
  print()
  if restart == "No":
    print("Thank you for creating your Character Stats!")
    break
  else:
    continue