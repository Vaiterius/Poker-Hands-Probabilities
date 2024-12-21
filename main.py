import random

from card import Card, Suit, Rank
from hand_checker import HandChecker


def main() -> None:
    # Only hold the values of all cards for reference. Make a duplicate deck of
    # cards each time a game is played.
    cards: list[Card] = generate_cards()

    trial_royal_flushes(cards, num_trials=10)


def trial_royal_flushes(cards: list[Card], num_trials: int) -> None:
    hand: list[Card] = []
    hands_dealt_per_trial: list[int] = []

    for i in range(num_trials):
        counter: int = 0
        while True:
            hand = generate_hand(cards)
            if HandChecker.has_royal_flush(hand):
                print("\nRoyal Flush found!")
                print("HAND:")
                for card in hand:
                    print(card)
                hands_dealt_per_trial.append(counter)
                break
            counter += 1
        print(f"Trial #{i + 1}: {counter:,} hands dealt")
    
    print(f"Average hands dealt per trial: {round(sum(hands_dealt_per_trial) / len(hands_dealt_per_trial)):,}")



def generate_hand(cards: list[Card]) -> list[Card]:
    deck_copy: list[Card] = cards[:]
    hand: list[Card] = []

    for _ in range(5):
        card: Card = deck_copy.pop(random.randint(0, len(deck_copy) - 1))
        hand.append(card)

    return hand


def generate_cards() -> list[Card]:
    ranks: list[Rank] = list(Rank)
    suits: list[Suit] = list(Suit)

    cards: list[Card] = []

    for rank in ranks:
        for suit in suits:
            cards.append(Card(rank, suit))
    
    return cards


if __name__ == "__main__":
    main()
