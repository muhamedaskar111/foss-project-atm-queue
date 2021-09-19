people=int(input("ENTER NUMBER OF people on the queue: "))
minimum=int(input("ENTER minimum amount that can be withdrawn: "))

amount=list(map(int, input("Enter amounts to be withdrawn: ").split())) #splitting and storing the amount the people want to withdraw
index=[x for x in range(1,people+1)]
print(index)
x=0
o=0
while len(amount)>0:
    if amount[x] <= minimum:
        amount.remove(amount[x])
        o+=1
                                    
    elif amount[x]> minimum:
        y=amount[x]-minimum
        z=index[o]
        amount.remove(amount[x])
        amount.append(y)
        index.remove(index[o])
        index.append(z)

        
 
print(index)
