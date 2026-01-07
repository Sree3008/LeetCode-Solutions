class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        c=c1=c2=0
        for i in moves:
            if i=='L':
                c+=1
            if i=='R':
                c1+=1
            if i=='_':
                c2+=1
        return abs(c-c1)+c2
