def all_comb(arr,start,curr,ans):

    if start==len(arr):
        ans.append(curr[::])
        return

    
    #While including the elements in the set, you have 2 choices
    # You can include the element

    curr.append(arr[start])
    all_comb(arr,start+1,curr,ans)

    # Or don't include the element
    curr.pop()
    all_comb(arr,start+1,curr,ans)


arr = [1,2,3,4,5]
ans = []
all_comb(arr,0,[],ans)
print(ans)

