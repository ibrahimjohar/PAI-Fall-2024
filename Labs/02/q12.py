#name: ibrahim johar farooqi
#date: 28 august 2024
#lab: 02
#task: 12

list_1 = ["key1", "key2", "key3", "key4"]
list_2 = ["ali", "ahmed", "jawad", "ibrahim"]

dictionary1 = {}
cnt = 0

for i in list_1:
    dictionary1[i] = {list_2[cnt]}
    cnt += 1

print(dictionary1)
