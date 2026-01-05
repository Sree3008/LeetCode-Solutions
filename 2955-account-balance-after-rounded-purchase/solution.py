class Solution:
    def accountBalanceAfterPurchase(self, n: int) -> int:
        res=n%10
        if res<5:
            res=n-res
        elif res>=5: 
            res=n+(10 -res)
        return 100-res
