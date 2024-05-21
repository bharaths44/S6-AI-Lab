import math

def display_state(jug1, jug2):
    print(f"{'JUG 1: ':>11}{jug1:<6} | {'JUG 2: ':>12}{jug2}")

def pour_water(jug1, jug2, capacity1, capacity2):
    pour_amount = min(jug1, capacity2 - jug2)
    jug1 -= pour_amount
    jug2 += pour_amount
    return jug1, jug2

def water_jug_solution(capacity1, capacity2, target_amount):
    jug1 = 0
    jug2 = 0
    print(f"Jug 1 Capacity: {capacity1} | Jug 2 Capacity: {capacity2}")
    
    while jug2 != target_amount : #and jug1 != target_amount
        if jug1 == 0:
            jug1 = capacity1
        elif jug2 == capacity2:
            jug2 = 0
        else:
            jug1, jug2 = pour_water(jug1, jug2, capacity1, capacity2)
        display_state(jug1, jug2)

first_jug = int(input("Enter the capacity of the first jug: "))
second_jug = int(input("Enter the capacity of the second jug: "))
target_amount = int(input("Enter the target liters of water: "))

if target_amount < first_jug or target_amount < second_jug:
    if target_amount % math.gcd(first_jug, second_jug) == 0:
        water_jug_solution(first_jug, second_jug, target_amount)
    else:
        print("This is not possible....")
else:
    print("This is not possible....")