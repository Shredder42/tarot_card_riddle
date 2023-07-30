'''
program outline:
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



def pick_card(playable_cards):
    # allows player to pick a card
    choice = int(input('Pick a card from the list of playable cards: '))
    has_factor = determine_factors_present(choice, playable_cards)
    # print(determine_factors_present(choice, playable_cards))
    while not has_factor:
        choice = int(input('You must pick a card from the playable cards list and the card must have a factor present. Pick again: '))
        has_factor = determine_factors_present(choice, playable_cards)
    return choice

def find_factors(card):
    # finds the factors of a card
    factors_list = []
    for i in range(1, card):
        if card % i == 0:
            factors_list.append(i)
    return factors_list

def determine_factors_present(choice, playable_cards):
    factors_list = find_factors(choice)
    for factor in factors_list:
        if factor in playable_cards:
            return True
    return False

def update_player_score_and_cards(card, player_score, player_cards):
    player_score += card
    player_cards.append(card)
    return player_score, player_cards

def update_fate_cards_and_score(factors_list, fate_score, fate_cards):
    for item in factors_list:
        if item not in fate_cards:
            fate_score += item
            fate_cards.append(item)
    return fate_score, fate_cards

def remove_playable_cards(playable_cards, card, factors_list):
    playable_cards.remove(card)
    for item in factors_list:
        if item in playable_cards:
            playable_cards.remove(item)
    return playable_cards

def print_playable_cards(playable_cards):
    print(f'Playable cards are: {playable_cards}')

def determine_if_factors_remaining(playable_cards):
    factors = False
    for card in playable_cards:
        temp_factors = find_factors(card)
        for factor in temp_factors:
            if factor in playable_cards:
                factors = True
                break
    return factors

def left_over_cards(playable_cards, fate_score, fate_cards):
    for item in playable_cards:
        fate_score += item
    fate_cards += playable_cards
    return fate_score, fate_cards

def game_result(player_score, player_cards, fate_score, fate_cards):
    if player_score > fate_score:
        print(f'You won! Your score: {player_score}: Fate score: {fate_score}')
    else:
        print(f'You lost! Your score: {player_score}: Fate score: {fate_score}')
    print(f'You finished with these cards {player_cards}')
    print(f'Fate finished with these cards: {fate_cards}')



def main():
    playable_cards = [i for i in range(1, 24)]
    player_score = 0
    player_cards = []
    fate_score = 0
    fate_cards = []
    factors_remain = True
    while factors_remain:
        print_playable_cards(playable_cards)
        card = pick_card(playable_cards)
        factors_list = find_factors(card)
        player_score, player_cards = update_player_score_and_cards(card, player_score, player_cards)
        fate_score, fate_cards = update_fate_cards_and_score(factors_list, fate_score, fate_cards)
        print(f'Player score: {player_score}. Player cards: {player_cards}')
        print(f'Fate score: {fate_score}. Fate cards: {fate_cards}')
        playable_cards = remove_playable_cards(playable_cards, card, factors_list)
        factors_remain = determine_if_factors_remaining(playable_cards)
    fate_score, fate_cards = left_over_cards(playable_cards, fate_score, fate_cards)
    game_result(player_score, player_cards, fate_score, fate_cards)


if __name__ == '__main__':
    main()




