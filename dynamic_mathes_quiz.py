import random
import time
operaters = ["+", "-", "*", "/"]

min_operand = 3
miax_operand = 12
total_problems = 10

def generate_problem():

    left = random.randint(min_operand,miax_operand)

    right = random.randint(min_operand,miax_operand)

    operater = random.choice(operaters)

    exp = str(left) + " " + operater +" "+ str(right)

    answer = eval(exp)

    return exp, answer


wrong = 0
print("------------------------------")
print("please enter to start")

start_time = time.time()
for i in range(total_problems):
    expression,answer = generate_problem()

    while True:
        guess = input(f"Problem # {i+1} {expression} = ")

        if guess == str(answer):
            break


end_time = time.time()

total_time = end_time - start_time
print("----------------------------------")
print(f"Nice works you finished total_time = {total_time}")