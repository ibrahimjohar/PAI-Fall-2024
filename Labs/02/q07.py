#name: ibrahim johar farooqi
#date: 28 august 2024
#lab: 02
#task: 07

def calculateAvgTemp(tList):
    sum = 0
    itemCount = 0
    
    for x in tList:
        sum += x
        itemCount += 1
        
    avg = sum/itemCount
    
    return avg

def sortList(tList):
    l = len(tList)
    
    for i in range(l):
        swap = False
        for j in range(0, l - i - 1):
            if tList[j] > tList[j+1]:
                temp = tList[j]
                tList[j] = tList[j+1]
                tList[j+1] = temp
                swap = True
        if not swap:
            break
    
    return tList
        
def deleteTemp(tList, date):
    tList.pop(date)
    
temperaturelist = [30, 32, 33, 35, 31, 29, 36, 34, 32, 31, 33, 34, 30, 29, 28, 
                32, 31, 33, 35, 30, 31, 29, 30, 32, 33, 35, 36, 34, 32, 30]

print("temperature list, recorded over a month: ")
print(temperaturelist)
print("average temperature: ", calculateAvgTemp(temperaturelist))
print("temperature list, recorded over a month in ascending order: ")
print(sortList(temperaturelist))
print("highest temp: ", temperaturelist[29])
print("lowest temp: ", temperaturelist[0])
print("removing temperature for day 3:")
deleteTemp(temperaturelist, 2)
print("temperature list, recorded over a month with day 3 temp removed: ")
print(temperaturelist)

    

