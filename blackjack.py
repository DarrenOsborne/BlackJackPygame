import pygame
import sys
import time
import random

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
#location
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



player_positions = {
    "1": (340, 300),
    "2": (365, 335),
    "3": (390, 370),
    "4": (415, 405),
    "5": (460, 405),
    "6": (505, 405)
}
dealer_positions = {
    "1": (340, 120),
    "2": (400, 120),
    "3": (425, 155),
    "4": (450, 190),
    "5": (495, 190),
    "6": (540, 190)
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
def display_card(card, color, player, position):
    if player:
        x = player_positions[position][0]
        y = player_positions[position][1]
    else:
        x = dealer_positions[position][0]
        y = dealer_positions[position][1]
    pygame.draw.rect(screen, ("black"), (x-3, y-3, 56, 76))
    pygame.draw.rect(screen, ("white"), (x, y, 50, 70))
    text_surface = card_font.render(card, True, color)
    screen.blit(text_surface, (x + 2, y + 2))

def Xquit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

#state conditions
initial_state = True
betting_state = True
deal_cards_state = True
player_decision_state = True
dealer_draw_state = True
round_result_state = True
running = True
# Game loop
while running:
    Xquit()
    
    #every game starts here
    while initial_state():
        Xquit()
        draw_table_and_buttons()
        break

    #betting
    while betting_state():
        Xquit()
        break
    
    #dealing, blackjack would be directed here
    while deal_cards_state():
        Xquit()
        break
    
    #stay, hit, double, split #buttons are active
    while player_decision_state():
        Xquit()
        break
    
    #draws until 17
    while dealer_draw_state():
        Xquit()
        break
    
    #take or add chips
    #display round result
    while round_result_state():
        Xquit()
        break
    
    draw_table_and_buttons()
    display_card("9", "black", True, "1")
    display_card("T", "black", True, "2")
    display_card("A", "red", True, "3")
    display_card("Q", "red", True, "4")
    display_card("2", "black", True, "5")
    display_card("8", "red", True, "6")
    display_card("9", "black", False, "1")
    display_card("T", "black", False, "2")
    display_card("A", "red", False, "3")
    display_card("Q", "red", False, "4")
    display_card("2", "black", False, "5")
    display_card("8", "red", False, "6")

    pygame.display.flip()
