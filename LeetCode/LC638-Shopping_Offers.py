# https://leetcode.com/problems/shopping-offers/
class Solution:
    
    def __init__(self):
        self.dp={}
    
    def optimal_cost(self,item_count,offers,price):
        if any(item_count) == False:
            return 0
        
        if item_count in self.dp.keys():
            return self.dp[item_count]
        
        # Standard Buy
        # One note: The earlier mistake I was making was to decrease
        # the item count by one and then recurse which unneccesarily
        # added to recursion overhead. Instead we could directly 
        # calculate the direct cost
        cost = sum(item_count[i]*price[i] for i in range(len(price)))
        
        #Offer Buy
        for offer in offers:
            new_item_count = list(item_count)
            
            #Validate if offer can be taken with current item_count
            if not all(new_item_count[i]-offer[i]>=0 for i in range(len(new_item_count))):
                continue
            
            
            offer_price = offer[len(offer)-1]
            new_item_count = tuple([new_item_count[i]-offer[i] for i in range(len( new_item_count))])
            cost=min(cost,self.optimal_cost(new_item_count,offers,price)+offer_price)
        
        self.dp[item_count]=cost
        return cost
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        
        item_count = tuple(needs)
        return self.optimal_cost(item_count,special,price)

'''
Unique Test Case
[9,6,1,5,3,4]
[[1,2,2,1,0,4,14],[6,3,4,0,0,1,16],[4,5,6,6,2,4,26],[1,1,4,3,4,3,15],[4,2,5,4,4,5,15],[4,0,0,2,3,5,13],[2,4,6,4,3,5,7],[3,3,4,2,2,6,21],[0,3,0,2,3,3,15],[0,2,4,2,2,5,24],[4,1,5,4,5,4,25],[6,0,5,0,1,1,14],[4,0,5,2,1,5,8],[4,1,4,4,3,1,10],[4,4,2,1,5,0,14],[2,4,4,1,3,1,16],[4,2,3,1,2,1,26],[2,4,1,6,5,3,2],[0,2,0,4,0,0,19],[3,1,6,3,3,1,23],[6,2,3,2,4,4,16],[5,3,5,5,0,4,5],[5,0,4,3,0,2,20],[5,3,1,2,2,5,8],[3,0,6,1,0,2,10],[5,6,6,1,0,4,12],[0,6,6,4,6,4,21],[0,4,6,5,0,0,22],[0,4,2,4,4,6,16],[4,2,1,0,6,5,14],[0,1,3,5,0,3,8],[5,5,3,3,2,0,4],[1,0,3,6,2,3,18],[4,2,6,2,2,5,2],[0,2,5,5,3,6,12],[1,0,6,6,5,0,10],[6,0,0,5,5,1,24],[1,4,6,5,6,3,19],[2,2,4,2,4,2,20],[5,6,1,4,0,5,3],[3,3,2,2,1,0,14],[0,1,3,6,5,0,9],[5,3,6,5,3,3,11],[5,3,3,1,0,2,26],[0,1,1,4,2,1,16],[4,2,3,2,1,4,6],[0,2,1,3,3,5,15],[5,6,4,1,2,5,18],[1,0,0,1,6,1,16],[2,0,6,6,2,2,17],[4,4,0,2,4,6,12],[0,5,2,5,4,6,6],[5,2,1,6,2,1,24],[2,0,2,2,0,1,14],[1,1,0,5,3,5,16],[0,2,3,5,5,5,6],[3,2,0,6,4,6,8],[4,0,1,4,5,1,6],[5,0,5,6,6,3,7],[2,6,0,0,2,1,25],[0,4,6,1,4,4,6],[6,3,1,4,1,1,24],[6,2,1,2,1,4,4],[0,1,2,3,0,1,3],[0,2,5,6,5,2,13],[2,6,4,2,2,3,17],[3,4,5,0,5,4,20],[6,2,3,4,1,3,4],[6,4,0,0,0,5,16],[3,1,2,5,0,6,11],[1,3,2,2,5,6,14],[1,3,4,5,3,5,18],[2,1,1,2,6,1,1],[4,0,4,0,6,6,8],[4,6,0,5,0,2,1],[3,1,0,5,3,2,26],[4,0,4,0,6,6,6],[5,0,0,0,0,4,26],[4,3,2,2,0,2,14],[5,2,4,0,2,2,26],[3,4,6,0,2,4,25],[2,1,5,5,1,3,26],[0,5,2,4,0,2,24],[5,2,5,4,5,0,1],[5,3,0,1,5,4,15],[6,1,5,1,2,1,21],[2,5,1,2,1,4,15],[1,4,4,0,0,0,1],[5,0,6,1,1,4,22],[0,1,1,6,1,4,1],[1,6,0,3,2,2,17],[3,4,3,3,1,5,17],[1,5,5,4,5,2,27],[0,6,5,5,0,0,26],[1,4,0,3,1,0,13],[1,0,3,5,2,4,5],[2,2,2,3,0,0,11],[3,2,2,1,1,1,6],[6,6,1,1,1,6,26],[1,5,1,2,5,2,12]]
[6,6,6,1,6,6]
''' 