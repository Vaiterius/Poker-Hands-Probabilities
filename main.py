import random
from dataclasses import dataclass
from enum import Enum, auto


class Suit(Enum):
    CLUBS = auto()
    HEARTS = auto()
    SPADES = auto()
    DIAMONDS = auto()


class Rank(Enum):
    TWO = auto()
    THREE = auto()
    FOUR = auto()
    FIVE = auto()
    SIX = auto()
    SEVEN = auto()
    EIGHT = auto()
    NINE = auto()
    TEN = auto()
    JACK = auto()
    QUEEN = auto()
    KING = auto()
    ACE = auto()


@dataclass
class Card:
    rank: Rank
    suit: Suit

    def __str__(self):
        return f"{self.rank.name.lower()} of {self.suit.name.lower()}"



def main() -> None:
    card_holder: list[Card] = []

    generate_cards(card_holder)
    
    # TODO


def generate_cards(card_holder: list[Card]) -> None:
    ranks: list[Rank] = list(Rank)
    suits: list[Suit] = list(Suit)

    for rank in ranks:
        for suit in suits:
            card_holder.append(Card(rank, suit))


if __name__ == "__main__":
    main()