from random import shuffle, randint

#delcaring all global variables
deck = []
count = 0
player_hand_value = 0
player_hand = 0
dealer_hand_value = 0
dealer_hand = 0
player_card_position = 0
dealer_card_position = 0

#initializes the deck which is (6 decks worth of cards 2-A * 4 * 6)
def reshuffle():
  global deck
  deck = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A",
"2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A",
"2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A",
"2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A",
"2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A",
"2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A",
"2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A",
"2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A",
"2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A",
"2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A",
"2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A",
"2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A",
"2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A",
"2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A",
"2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A",
"2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A",
"2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A",
"2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A",
"2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A",
"2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A",
"2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A",
"2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A",
"2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A",
"2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
  shuffle(deck)
  update_count("reset")

#updates the count
def update_count(card):
  global count
  if card in ["2","3", "4", "5", "6"]:
    count+=1
  elif card in ["7","8", "9"]:
    count+=0
  elif card in ["T", "J", "Q", "K", "A"]:
    count+=1
  else: #called when the deck is shuffled again
    count=0


#draws a card form the back of the shuffled deck
def draw_card():
  global deck
  card = deck.pop()
  update_count(card)
  #turning the string into an int
  track_player_hand_value(card)
  return card

def track_player_hand_value(card):
    values = {'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 10, 'Q': 10, 'K': 10}
    global player_hand, player_hand_value  # Declare global variables
    player_hand.append(card)

    # Calculate the total value of the hand
    hand_value = sum([values[card] for card in player_hand])

    # Adjust for soft total if Ace is present and hand total exceeds 21
    if 'A' in player_hand and hand_value > 21:
        num_aces = player_hand.count('A')
        for _ in range(num_aces):
            hand_value -= 10
            if hand_value <= 21:
                break

    player_hand_value = hand_value

def track_dealer_hand_value(card):
    values = {'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 10, 'Q': 10, 'K': 10}
    global dealer_hand, dealer_hand_value  # Declare global variables
    dealer_hand.append(card)

    # Calculate the total value of the hand
    hand_value = sum([values[card] for card in dealer_hand])

    # Adjust for soft total if Ace is present and hand total exceeds 21
    if 'A' in dealer_hand and hand_value > 21:
        num_aces = dealer_hand.count('A')
        for _ in range(num_aces):
            hand_value -= 10
            if hand_value <= 21:
                break

    dealer_hand_value = hand_value

def reset_hand_and_value():
  global player_hand_value, dealer_hand_value, player_hand, dealer_hand
  player_hand_value = 0
  dealer_hand_value = 0
  player_hand = []
  dealer_hand = []


def reset_card_positions():
  global player_card_position
  global dealer_card_position
  player_card_position = 0
  dealer_card_position = 0


'''count = 0
player_turn = True
dealer_total = 0
player_total = 0
player_busted = False
dealer_first_card = draw_card()
player_first_draw = [draw_card(), draw_card()]

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
  print("You lost.")'''