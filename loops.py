board_games = ["Settlers of Catan", "Carcassone", "Power Grid", "Agricola", "Scrabble"]

sport_games = ["football", "hockey", "baseball", "cricket"]

for game in board_games:
  print(game)



for promise in range(6):
  print("I will finish the python loops module!")



# While Loop Walkthrough
count = 0
print("Starting While Loop")
while count <= 3:
  # Loop Body
  # Print if the condition is still true
  print("Loop Iteration - count <= 3 is still true")
  # Print the current value of count 
  print("Count is currently " + str(count))
  # Increment count
  count += 1
  print(" ----- ")
print("While Loop ended")



single_digits = range(10)
squares = []

for item in single_digits:
  print(item)
  squares.append(item**2)
  
cubes = [item**3 for item in single_digits]
print(cubes)