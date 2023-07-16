import pygame
import sys
import time
from random import choice
from card_functions import *

# Initialize Pygame
pygame.init()

# Set up the window and background
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Blackjack Table")
screen.fill((50, 50, 50))

# Define colors
BLACK = (0, 0, 0)
GREEN = (0, 128, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
green_table_loc = (200, 100, 400, 400)
#size
button_size = (90, 80)
#location top left corner
stand_button_loc = (207, 510)
hit_button_loc = (304, 510)
double_button_loc = (401, 510)
split_button_loc = (498, 510)
#both size and loc
stand_button_setup = ((stand_button_loc), (button_size))
hit_button_setup = ((hit_button_loc), (button_size))
double_button_setup = ((double_button_loc), (button_size))
split_button_setup = ((split_button_loc), (button_size))

#font for card faces
card_font = pygame.font.Font(None, 60)
#font for buttons
button_font = pygame.font.Font(None, 35)

#defining the location of the buttons for click logic
stand_button_rect = pygame.Rect(stand_button_loc, button_size)
hit_button_rect = pygame.Rect(hit_button_loc, button_size)
double_button_rect = pygame.Rect(double_button_loc, button_size)
split_button_rect = pygame.Rect(split_button_loc, button_size)

player_positions = {
    1: (340, 300),
    2: (365, 335),
    3: (390, 370),
    4: (415, 405),
    5: (460, 405),
    6: (505, 405)
}
dealer_positions = {
    1: (340, 120),
    2: (400, 120),
    3: (425, 155),
    4: (450, 190),
    5: (495, 190),
    6: (540, 190)
}

# Draw table and buttons
def draw_table_and_buttons():
    pygame.draw.rect(screen, (71, 150, 80), green_table_loc)
    pygame.draw.rect(screen, (255, 0, 0), stand_button_setup)
    text_surface = button_font.render("Stand", True, (50, 50, 50))
    screen.blit(text_surface, stand_button_loc)
    pygame.draw.rect(screen, (0, 255, 0), hit_button_setup)
    text_surface = button_font.render("Hit", True, (50, 50, 50))
    screen.blit(text_surface, (hit_button_loc))
    pygame.draw.rect(screen, (0, 0, 255), double_button_setup)
    text_surface = button_font.render("Double", True, (50, 50, 50))
    screen.blit(text_surface, (double_button_loc))
    pygame.draw.rect(screen, (255, 0, 255), split_button_setup)
    text_surface = button_font.render("Split", True, (50, 50, 50))
    screen.blit(text_surface, (split_button_loc))



# Build card
def display_card(player):
    card = draw_card()
    cardcolors = ["red", "black"]
    color = choice(cardcolors)
    #adds the position by one each time this function is called
    #the position refers to the position dictionaries
    if player:
        global player_card_position
        player_card_position=+1
        position = player_card_position
        x = player_positions[position][0]
        y = player_positions[position][1]
        
        track_dealer_hand_value(card[1])
    else:
        global dealer_card_position
        dealer_card_position=+1
        position = dealer_card_position
        x = dealer_positions[position][0]
        y = dealer_positions[position][1]
    pygame.draw.rect(screen, ("black"), (x-3, y-3, 56, 76))
    pygame.draw.rect(screen, ("white"), (x, y, 50, 70))
    text_surface = card_font.render(card, True, color)
    screen.blit(text_surface, (x + 2, y + 2))
    return card

def Xquit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
def click_decisions():
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if stand_button_rect.collidepoint(mouse_pos):
                    return ("stand")
            if hit_button_rect.collidepoint(mouse_pos):
                    return ("hit")
            if double_button_rect.collidepoint(mouse_pos):
                    return ("double")
            if split_button_rect.collidepoint(mouse_pos):
                    return ("split")
            

#state conditions
initial_state = True
betting_state = True
deal_cards_state = True
player_decision_state = True
dealer_draw_state = True
round_result_state = True
running = True
player_won = False
blackjack = False
# Game loop
while running:
    Xquit()
    
    #every game starts here
    while initial_state:
        Xquit()
        initial_state = True
        betting_state = True
        deal_cards_state = True
        player_decision_state = True
        dealer_draw_state = True
        round_result_state = True
        player_won = False
        blackjack = False
        draw_table_and_buttons()
        reset_hand_and_value()
        reset_card_positions()
        #with about 78% penetration
        if len(deck)<70:
            reshuffle()
        pygame.display.flip()
        break

    #betting
    '''while betting_state:
        Xquit()
        x_pos, y_pos = click_bets()
        break'''
    
    #dealing, blackjack would be directed here
    while deal_cards_state:
        Xquit()
        display_card(True)
        display_card(False)
        display_card(True)
        display_card(False)
        deal_cards_state = False
        if player_hand_value == 21 and dealer_hand_value != 21:
            player_won = True
            blackjack = True
            player_decision_state = False
            dealer_draw_state = False

             
        pygame.display.flip()
        break
    
    #stay, hit, double, split #buttons are active
    while player_decision_state:
        Xquit()
        click = click_decisions()
        if click:
            if click == "stand":
                player_decision_state = False
                break
            if click == "hit":
                display_card(True) 
            if click == "double":
                display_card(True)
        if player_hand_value >= 21:
             player_decision_state = False
             break
        pygame.display.flip()
    #draws until 17
    while dealer_draw_state:
        Xquit()
        if dealer_hand_value < 17:
             display_card(False)
        pygame.display.flip()
        break
    
    #take or add chips
    #display round result
    while round_result_state:
        Xquit()

        break
    
    draw_table_and_buttons()
    display_card("9", True, "1")
    display_card("T", True, "2")
    display_card("A", True, "3")
    display_card("Q", True, "4")
    display_card("2", True, "5")
    display_card("8", True, "6")
    display_card("9", False, "1")
    display_card("T", False, "2")
    display_card("A", False, "3")
    display_card("Q", False, "4")
    display_card("2", False, "5")
    display_card("8", False, "6")

    pygame.display.flip()
