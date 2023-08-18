import pygame
from pygame.locals import *
import random

# Initialize Pygame
pygame.init()

# Set up the game window
width = 640
height = 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Guess the Number')

# Set up colors
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)

# Set up fonts
font = pygame.font.Font(None, 36)

# Set up the game variables
secret_number = random.randint(1, 100)
num_guesses = 0

print(secret_number)

# Create an instance of the InputBox class
input_box = pygame.Rect(width // 2 - 100, height // 2, 200, 32)
input_text = ''
result = ''

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_RETURN:
                try:
                    # Get the player's guess from the input text
                    guess = int(input_text)
                    num_guesses += 1

                    # Compare the guess with the secret number
                    if guess < secret_number:
                        result = "Too low!"
                    elif guess > secret_number:
                        result = "Too high!"
                    else:
                        result = f"Congratulations! You guessed the number in {num_guesses} tries."
                        num_guesses = 0
                        secret_number = random.randint(1, 100)


                    # Clear the input text
                    input_text = ''
                except ValueError:
                    result = "Invalid guess!"
            elif event.key == K_BACKSPACE:
                input_text = input_text[:-1]
            else:
                input_text += event.unicode

    # Clear the screen
    screen.fill(BLACK)

    # Draw the game instructions
    instructions = font.render("Guess the number (between 1 and 100)", True, WHITE)
    screen.blit(instructions, (width // 2 - instructions.get_width() // 2, height // 2 - 50))

    # Draw the input box
    pygame.draw.rect(screen, WHITE, input_box, 2)
    input_surface = font.render(input_text, True, WHITE)
    screen.blit(input_surface, (input_box.x + 5, input_box.y + 5))

    # Draw the result
    result_text = font.render(result, True, WHITE)
    screen.blit(result_text, (width // 2 - result_text.get_width() // 2, height // 2 + 50))

    # Update the display
    pygame.display.flip()

# Quit the game
pygame.quit()
