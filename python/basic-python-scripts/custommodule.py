import random

def time_activity(*args, **kwargs):
    print("Custom Module")
    print(args)
    print(kwargs)
    print()
    
    min = sum(args) + random.randint(0,50)
    # print(min)

    choice = random.choice(list(kwargs.keys()))
    # print(choice)

    print(f"You have to spend {min} minutes on {kwargs[choice]}")

def order_food_CM(min_order, *args):
    print("Custom Module")
    print(f"You have ordered {min_order}")
    # print(args)
    for item in args:
        print(f"You have ordered {item}")

def vac_feedback(vac, efficacy):
    print("Custom Module")
    print(f"Vaccine {vac} is having efficacy of {efficacy}%")
    
    if(efficacy > 50 and efficacy <=75):
        print("Seems not so effective")
    elif(efficacy > 75 and efficacy <=90):
        print("Can consider this Vaccine")
    elif(efficacy >= 90):
        print("Will take the shot")
    else:
        print("Needs many more trials")