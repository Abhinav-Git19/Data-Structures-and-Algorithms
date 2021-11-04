
def P_n_k(arr,n,k,used,curr,ans):

    # The function will select and arrange k items out of n items
    if k ==0:
        # This basically means we permuted all k items that we needed to
        ans.append(curr[::])
        return
    

    for i in range(n):
        # used array is meant to keep track of elements already used
        # so that we don't repeat that permutations and also the states
        if not used[i]:
            used[i]=True
            curr.append(arr[i])
            P_n_k(arr,n,k-1,used,curr,ans)

            #backtrack
            curr.pop()
            used[i]=False



sample_arr = [1,2,3,4,5]
used  = [False]*len(sample_arr)
ans = []
P_n_k(sample_arr,len(sample_arr),3,used,[],ans)

print(ans)


    