class Solution:
    def checkDivisibility(self, n: int) -> bool:
        curr=n
        s=0
        p=1
        while n>0:
            temp=n%10
            n=n//10
            s+=temp
            p*=temp
        return curr%(s+p)==0