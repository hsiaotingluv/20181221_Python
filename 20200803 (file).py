
# total number of ways to make changes
def cc(amount, kinds_of_coins):
    if amount == 0:
        return 1
    elif (amount < 0) or (kinds_of_coins == 0):
        return 0
    else:
        return cc(amount - first_demoination(kinds_of_coins), kinds_of_coins) + \
               cc(amount, kinds_of_coins - 1)

def first_demoination(kinds_of_coins):
    x = [1, 5, 10, 20, 50]
    return x[kinds_of_coins - 1]

def count_change(amount):
    return cc(amount, 5)



# with an infinite amount of coins
def cc(amt, kinds_of_coins, freq):
    if amt == 0:
        return 1
    elif (amt < 0) or (kinds_of_coins == 0):
        return 0
    else:
        types = [20, 50]
        
        if freq[kinds_of_coins - 1] > 0:
            temp = []
            for item in freq:temp.append(item)
            temp[kinds_of_coins - 1] -= 1

            return cc(amt - types[kinds_of_coins - 1], kinds_of_coins, temp) + \
                   cc(amt, kinds_of_coins-1, temp)
        else:
            return 0

freq = [5,1]
print(cc(100, 2, freq))

