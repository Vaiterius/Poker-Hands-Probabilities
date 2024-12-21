import unittest

from card import Suit, Rank, Card
from hand_checker import HandChecker


class TestHandChecker(unittest.TestCase):

    def test_royal_flushes(self):
        # Has a royal flush.
        hand1: list[Card] = [
            Card(Rank.ACE, Suit.CLUBS),
            Card(Rank.KING, Suit.CLUBS),
            Card(Rank.QUEEN, Suit.CLUBS),
            Card(Rank.JACK, Suit.CLUBS),
            Card(Rank.TEN, Suit.CLUBS)
        ]
        self.assertTrue(HandChecker.has_royal_flush(hand1))