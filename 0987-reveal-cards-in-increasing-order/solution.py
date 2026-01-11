class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        q=deque()
        for i in reversed(deck):
            if q:
                q.appendleft(q.pop())
            q.appendleft(i)
        return list(q)
