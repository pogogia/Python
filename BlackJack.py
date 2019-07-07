import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
          'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

class Card:
    def __init__(self, suit,rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' +  self.suit


class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.deck.append(card)

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return 'The deck has:' + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single = self.deck.pop()
        return single


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.ace = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.ace += 1

    def adjust_ace_value(self):
        while self.value > 21 and self.ace:
            self.value -= 10
            self.ace -= 1


class Chips:
    def __init__(self, total = 100):
        self.total = total
        self.bet = 0
        print(self.total)

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


def take_bets(chips):
    while True:
        try:
            chips.bet = int(input("How many chips you want to bet: "))
        except ValueError:
            print("Sorry, bet can only be an integer")
        else:
            if chips.bet > chips.total:
                print("Sorry, you can't make this bet, your total is less than your betted amount.")
            else:
                break


def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_ace_value()


def hit_or_stand(deck,hand):
    global playing
    while True:
        decision = input("Do you want to hit or stand: 'h' or 's'")
        if decision[0].lower() == 'h':
            hit(deck, hand)
        elif decision[0].lower() == 's':
            print("Player stands. Dealer plays now.")
            playing = False
        else:
            print("Wrong input! Please try again.")
            continue
        break


def show_some(player, dealer):
    print("\nDealer's hand")
    print("<<card hidden>>")
    print('', dealer.cards[1])
    print("\n Player's Hand:", *player.cards, sep= '\n')


def show_all(player,dealer):
    #print("\nDealer's hand")
    print("\n Dealer's Hand:", *dealer.cards, sep='\n')
    print("Dealer's Hand = ", dealer.value)
    #print("\nPlayer's hand")
    print("\n Player's Hand:", *player.cards, sep='\n')
    print("Player's Hand = ", player.value)


def player_busts(player,dealer,chips):
    print("Player Busts!")
    chips.lose_bet()


def player_wins(player,dealer,chips):
    print("Player Wins!")
    chips.win_bet()


def dealer_wins(player,dealer,chips):
    print("Dealer Wins!")
    chips.lose_bet()


def dealer_busts(player,dealer,chips):
    print("Dealer busts, Player Wins")
    chips.win_bet()


def push(player, dealer):
    print("Its a tie !!! Its a push.")


def clear_screen():
    '''Clears the screen'''
    print('\n' * 10)


playing = True
while True:
    print("Welcome to BlackJack!!!")
    chips = int(input("How much chips you want: "))
    player_chips = Chips(chips)
    take_bets(player_chips)

    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    #player_hand.adjust_ace_value()

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    show_some(player_hand, dealer_hand)

    while playing:
        hit_or_stand(deck,player_hand)
        show_some(player_hand,dealer_hand)
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break
    if player_hand.value <=21:
        while dealer_hand.value < 17:
                hit(deck,dealer_hand)
                show_all(player_hand,dealer_hand)
        if dealer_hand.value > 21:
                dealer_busts(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value < player_hand.value:
                player_wins(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value > player_hand.value:
                show_all(player_hand,dealer_hand)
                dealer_wins(player_hand,dealer_hand,player_chips)
        else:
                show_all(player_hand, dealer_hand)
                push(player_hand,dealer_hand)
    print("\n Player's winnings stand at", player_chips.total)
    new_game = input("Do you want to play again? yes or no ")
    if new_game[0].lower() == 'y':
        playing = True
        clear_screen()
        continue
    else:
        print("Thanks for playing BlackJack!!")
        break