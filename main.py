"""
Filename: main.py
Author: <Lastname, Firstname>
Created: <MM/DD/YYYY>
Instructor: Holtslander
"""
# import pygame
# import json
# from card import Card
# from Black_jack import BlackJack
#
#
# SCREEN_HEIGHT = 720
# SCREEN_WIDTH = 1280
#
# def main():
#     ##############################################
#     # Pygame initialization
#     ##############################################
#     pygame.init()
#     screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
#     clock = pygame.time.Clock()
#     running = True
#     screen.fill((0, 0, 0))
#
#     ##############################################
#     # Card object creation
#     ##############################################
#
#     # List that will store our card objects. We will be using it as a "stack" in this example.
#     cards = []
#
#     # Open the JSON file and load the contents into a list
#     json_path = "./card_setup.json"
#     with open(json_path, 'r') as c:
#         json_card_list = json.load(c)
#
#     # For each item in the list, create a card object and append it to our list of cards.
#     for entry in json_card_list:
#         cards.append(Card(entry["name"], entry["path"], entry["value"], entry["suit"]))
#
#     ##############################################
#     # Setting up Blackjack game
#     ##############################################
#     game = BlackJack(cards)
#
#     ##############################################
#     # Game loop
#     ##############################################
#     while running:
#         # Event loop
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#                 pygame.quit()
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 if event.button == 1:
#                     game.draw(cards).update(screen)
#
#
#         # Update the screen with the active surface
#         pygame.display.flip()
#         # Game FPS
#         clock.tick(30)
#
#
#
# if __name__ == '__main__':
#     main()


from Black_jack import BlackJack
import sys

def print_state(game, reveal_dealer=False):
    if reveal_dealer:
        dealer_cards, player_cards = game.show_full()
        print(f"\nDealer: {dealer_cards}  (value: {game.get_dealer_value()})")
    else:
        dealer_partial, player_cards = game.show_partial()
        print(f"\nDealer: {dealer_partial}")
    print(f"Player: {player_cards}  (value: {game.get_player_value()})\n")

def decide_winner(game):
    p_val = game.get_player_value()
    d_val = game.get_dealer_value()

    # immediate busts
    if p_val > 21:
        return "dealer"
    if d_val > 21:
        return "player"

    # compare
    if p_val > d_val:
        return "player"
    elif d_val > p_val:
        return "dealer"
    else:
        return "push"  # tie

def is_blackjack(person):
    return person.get_value() == 21 and len(person.get_cards()) == 2

def main():
    print("=== Console Blackjack ===")
    game = BlackJack()

    while True:
        answer = input("\nPress Enter to DEAL, or 'q' to quit: ").strip().lower()
        if answer == 'q':
            print("Bye!")
            sys.exit(0)

        # Deal initial
        game.deal_initial()
        print_state(game, reveal_dealer=False)

        # Check naturals (blackjack)
        player_blackjack = is_blackjack(game.player)
        dealer_blackjack = is_blackjack(game.dealer)
        if player_blackjack or dealer_blackjack:
            print_state(game, reveal_dealer=True)
            if player_blackjack and dealer_blackjack:
                print("Both have blackjack — push (tie).")
            elif player_blackjack:
                print("Player has blackjack! You win!")
            else:
                print("Dealer has blackjack. You lose.")
            continue  # next round

        # Player turn
        while True:
            move = input("Choose (H)it or (S)tand: ").strip().lower()
            if move not in ('h','s'):
                print("Type 'h' to hit or 's' to stand.")
                continue
            if move == 'h':
                card = game.hit_player()
                print(f"You drew: {card}")
                print(f"Player value: {game.get_player_value()}")
                if game.get_player_value() > 21:
                    print_state(game, reveal_dealer=True)
                    print("You busted! Dealer wins.")
                    break
                # else loop for next action
            else:  # stand
                print("You stand. Dealer's turn.")
                # Dealer plays
                game.dealer_play()
                print_state(game, reveal_dealer=True)
                # decide result
                if game.get_dealer_value() > 21:
                    print("Dealer busted! You win!")
                else:
                    result = decide_winner(game)
                    if result == "player":
                        print("You win!")
                    elif result == "dealer":
                        print("Dealer wins.")
                    else:
                        print("Push (tie).")
                break

        # done with round; ask to play again automatically loops to top
        # reset for next round
        game.reset()

if __name__ == '__main__':
    main()
