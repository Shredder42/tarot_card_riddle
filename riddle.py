'''
program outline:
* list of the cards 1-23
* pick card from list
* find factors function
* check if card has any factors
    * if so
        * add card to player score and cards to player list
        * add all factors to fate score
        * remove all those cards from card list
    * if not
        * tell player to pick different card
* check if any cards still have factors remaining
    * if so
        * pick a card
    * if not
        * game is over
        * add remaining cards to fate score
        * display socres and results
'''

playable_cards = [i for i in range(1, 24)]

def pick_card():
    # allows player to pick a card
    return int(input('Pick a card from the list of playable cards: '))

def find_factors(card):
    # finds the factors of a card
    factors_list = []
    for i in range(1, card):
        if card % i == 0:
            factors_list.append(i)
    return factors_list

def update_player_cards_and_score(card, player_cards, player_score):
    player_cards.append(card)
    player_score += card
    return player_cards, player_score


# def check_for_factors(card, card_list):


if __name__ == '__main__':
    player_cards = []
    player_score = 0
    fate_cards = []
    fate_score = 0
    card = pick_card()
    player_cards, player_score = update_player_cards_and_score(card, player_cards, player_score)
    print(f'Player cards: {player_cards}. Player score: {player_score}')
    print(playable_cards)
    print(find_factors(10))
