#Chapter 6 Project
#10 range function
'''
def myRange(start, stop = None, step = None):
    
    if stop == None and step == None:
        start, stop, step = 0, start, 1
        print(numList(start, stop, step))
        
    elif stop != None and step == None:
        print(numList(start, stop, step = 1))
        
    else:
        print(numList(start, stop, step))

def numList(start, stop, step):
    numList = []
    if start < stop and step > 0:
        while start < stop:
            numList.append(start)
            start += step
        return numList
    elif start > stop and step < 0:
        while start > stop:
            numList.append(start)
            start += step
        return numList
'''
