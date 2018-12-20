#!/usr/bin/env python3

# LeetCode #846: Hand of Straights
# https://leetcode.com/problems/hand-of-straights/description/

from collections import defaultdict


class Solution:
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        result = self.count_cards(hand)
        self.card_count, self.num_cards = result
        return self.can_arrange_cards(W)

    def count_cards(self, hand):
        card_count = defaultdict(int)
        num_cards = 0
        for card in hand:
            card_count[card] += 1
            num_cards += 1
        return card_count, num_cards

    def can_arrange_cards(self, W):
        lowest = min(self.card_count.keys())
        while self.num_cards > 0:
            while self.card_count[lowest] == 0:
                del self.card_count[lowest]
                lowest = min(self.card_count.keys())
            for i in range(W):
                if self.card_count[lowest + i] == 0:
                    return False
                self.card_count[lowest + i] -= 1
                self.num_cards -= 1
                if self.card_count[lowest + i] == 0:
                    del self.card_count[lowest + i]
        return True
