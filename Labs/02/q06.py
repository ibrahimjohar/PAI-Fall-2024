#name: ibrahim johar farooqi
#date: 28 august 2024
#lab: 02
#task: 06

def list_multiply(numList):
    result = 1
    for x in numList:
        result *= x
    return result

numList = [5, 3, 2]
print(f"Result: {list_multiply(numList)}")
