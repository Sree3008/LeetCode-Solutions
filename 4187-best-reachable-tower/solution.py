class Solution:
    def bestTower(self, towers: List[List[int]], center: List[int], radius: int) -> List[int]:
        x,y=center
        best=[-1,-1]
        m_q=-1
        for i,j,k in towers:
            if abs(i-x)+abs(j-y)<=radius:
                if k>m_q or (k==m_q and [i,j]<best):
                    m_q=k
                    best=[i,j]
        return best
