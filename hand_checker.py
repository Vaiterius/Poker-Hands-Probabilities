from enum import Enum, auto

from card import Card, Suit, Rank


class HandChecker:
    """
    This utility class checks a hand (7 cards) and determines the highest-
    ranking poker hand. Start from the highest (Royal Flush) and go down
    the ranks until a match is found.
    """


    class HandRanking(Enum):
        ROYAL_FLUSH = auto()
        STRAIGHT_FLUSH = auto()
        FOUR_OF_A_KIND = auto()
        FULL_HOUSE = auto()
        FLUSH = auto()
        STRAIGHT = auto()
        THREE_OF_A_KIND = auto()
        TWO_PAIR = auto()
        PAIR = auto()
        HIGH_CARD = auto()
    

    @staticmethod
    def is_same_suit(card1: Card, card2: Card) -> bool:
        return card1.suit.value == card2.suit.value
    

    @staticmethod
    def is_same_rank(card1: Card, card2: Card) -> bool:
        return card1.rank.value == card2.rank.value
    

    @staticmethod
    def has_royal_flush(hand: list[Card]) -> bool:
        """ *assume only 5 cards*
        A royal flush is an ace, king, queen, jack, and 10 all in the same suit
        """
        # Check ranks first.
        has_ace: bool = False
        has_king: bool = False
        has_queen: bool = False
        has_jack: bool = False
        has_ten: bool = False

        for card in hand:
            if card.rank == Rank.ACE:
                has_ace = True
                continue
            elif card.rank == Rank.KING:
                has_king = True
                continue
            elif card.rank == Rank.QUEEN:
                has_queen = True
                continue
            elif card.rank == Rank.JACK:
                has_jack = True
                continue
            elif card.rank == Rank.TEN:
                has_ten = True
                continue
        
        # print(has_ace)
        # print(has_king)
        # print(has_queen)
        # print(has_jack)
        # print(has_ten)
        
        if not (
            has_ace and has_king and has_queen and has_jack and has_ten
        ):
            return False

        # Then check if all cards have the same suit.
        suit_value: Suit = hand[0].suit
        for card in hand:
            if card.suit != suit_value:
                return False
        
        return True
    

    @staticmethod
    def check_for_pair(hand: list[Card]) -> None:
        """
        A pair is any two cards with the same rank value
        """
        for i in range(len(hand)):
            for j in range(len(hand)):
                if i == j:
                    break
                if HandChecker.is_same_rank(hand[i], hand[j]):
                    print("Pair found!")
                    print(hand[i])
                    print(hand[j])

