class Solution:
    def __init__(self):
        self.dp={}
    
    def ways(self,A,sums,N):
        if N==0:
            if sums==0:
                return 1
            else:
                return 0
    
        #print(sums,N)
        if (sums,N) in self.dp.keys():
            return self.dp[(sums,N)]
        ans = self.ways(A,sums-A[N-1],N-1)+self.ways(A,sums+A[N-1],N-1)
    
        self.dp[(sums,N)]=ans
        return ans


    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        N=len(nums)
        return self.ways(nums,S,N)