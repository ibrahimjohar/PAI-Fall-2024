#name: ibrahim johar farooqi
#date: 28 august 2024
#lab: 02
#task: 10

def build_message(**info):
    if not info:
        print("no info found.")
        return 
    
    for key, val in info.items():
        print(key,":",val)
        
    
build_message(name = "ibrahim", age = 20, city = "karachi")
