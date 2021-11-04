def C_n_k(arr,n,k,start,curr,ans):

    if k==0:
        #Clone the list curr via curr[::] or else all elements 
        # of list will point to same reference
        ans.append(curr[::])
        return

    
    # In combinations, order is not important 
    # So to ensure we don't end up selecting same elements again
    # We do a for loop from (start to end) instead of (0 to end)
    # for loop indicates in current state our elements selection

    for i in range(start,n):

        # Notice we don't need used variable here as well not recur 
        # Same state again

        # Select an element
        curr.append(arr[i])
        C_n_k(arr,n,k-1,i+1,curr,ans)
        curr.pop()


arr = [1,2,3,4,5]
ans = []
C_n_k(arr,len(arr),3,0,[],ans)
print(ans)


    

    