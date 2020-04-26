def segregateRoots(bracket_expr) -> list:
    stack =[]
    output=[]
    temp=""
    for i in range(len(bracket_expr)):
        temp+=bracket_expr[i]
        if bracket_expr[i] =='[':
            stack.append(i)
        else:
            if len(stack)>0:
                stack.pop()
            
            # Root tree is found
            if len(stack)==0:
                output.append(temp)
                temp=""
    return output


def IsHappy(bracket_expr) ->bool:
    # Here each index will store the number of child nodes a particular node
    # is going to have, 0 -> indicates leaf nodes
    stack =[]

    no_of_child_nodes =-1
    for i in range(len(bracket_expr)):
        if len(stack)==0:
            stack.append(0)
        elif bracket_expr[i]=='[':
            stack[len(stack)-1]+=1
            stack.append(0)
        else:
            if stack[len(stack)-1]==0: #Leaf node
                stack.pop()
            else:
                if no_of_child_nodes==-1:
                    no_of_child_nodes=stack[len(stack)-1]
                    stack.pop()
                elif stack[len(stack)-1] == no_of_child_nodes:
                    stack.pop()
                else:
                    return False
    return True


def driver():
    t=int(input())
    while t>0:
        t-=1
        n=int(input())
        bracket_expr = input()
        seg_roots=segregateRoots(bracket_expr)
        count = 0
        
        for root in seg_roots:
            if IsHappy(root):
                count+=1
        print(count)
driver()