import random
# Run the program, enter the number of coins to flip, get results

def cointosspc():
    number = input("How many times to flip a coin?: ")
    heads = 0
    tails = 0
    for amount in range(int(number)):
        flip = random.randint(0, 1)
        if flip == 0:
            print("Heads")
            heads += 1
        else:
            print("Tails")
            tails += 1
    percentage = heads / int(number)
    print("{} heads and {} tails".format(heads, tails))
    print("Percentage of heads is {:.0%}".format(percentage))


cointosspc()
