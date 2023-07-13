import random

#6 decks worth of cards 2-A * 4 * 6
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A",
"2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A",
"2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A",
"2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A",
"2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A",
"2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A",
"2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A",
"2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A",
"2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A",
"2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A",
"2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A",
"2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A",
"2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A",
"2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A",
"2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A",
"2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A",
"2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A",
"2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A",
"2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A",
"2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A",
"2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A",
"2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A",
"2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A",
"2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

def draw_random_card():
  count = 0
  rand = random.randint(0,12)
  if rand < 9:
    total = rand+2
  elif rand == 12: 
    total = 11
  else:
    total = 10

  if rand<5:
    count = 1
  elif rand>7:
    count = -1
  return [(cards[rand]), count, total]



count = 0
player_turn = True
dealer_total = 0
player_total = 0
player_busted = False
dealer_first_card = draw_random_card()
player_first_draw = [draw_random_card(), draw_random_card()]

#setting the initial game state
print(f"Dealer has: {dealer_first_card[0]} ?")
print(f"You drew: {player_first_draw[0][0]} {player_first_draw[1][0]}")
player_total = player_total + player_first_draw[0][2] + player_first_draw[1][2]

while(player_turn):
  response = str(input("H or S: "))
  if response in "h":
    print()
  elif response =="s":
    break

  rand_card = draw_random_card()
  print(rand_card[0])
  player_total = player_total + rand_card[2]

  if player_total>21:
    player_busted = True
    break
  
rand_card = draw_random_card()
print(f"Dealer has: {dealer_first_card[0]} {rand_card[0]}")

dealer_total = dealer_total + dealer_first_card[2] + rand_card[2]
while dealer_total < 17 and not player_busted:
  rand_card = draw_random_card()
  print(f"Dealer drew: {rand_card[0]}")
  dealer_total = dealer_total + rand_card[2]

if player_busted:
  print("You busted!!! You lose.")
elif dealer_total > 21:
  print("You won, the dealer busted.")
elif player_total > dealer_total:
  print("You won, you beat the dealer.")
elif player_total == dealer_total:
  print("Tie. Push.")
else:
  print("You lost.")