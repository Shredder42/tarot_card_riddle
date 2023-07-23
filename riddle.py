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

def find_factors(card):
    # finds the factors of a card
    factors_list = []
    for i in range(1, card):
        if card % i == 0:
            factors_list.append(i)
    return factors_list

if __name__ == '__main__':
    print(playable_cards)
    print(find_factors(10))
