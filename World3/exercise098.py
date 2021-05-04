# Objective: Make a program that have a function called counter().
# This function will receive three arguments: begin, end and step, and will execute the count.
# This function will execute three counters:
# a) By 1 to 10, step 1
# b) By 10 to 0, step 2
# c) A custom counter

# Programmer: Hugo Leça Ribeiro

from time import sleep


def counter(begin, end, step):
    if (begin < end and step < 0) or step == 0:
        step = 1
    print(f'We will count from {begin} to {end} by {abs(step)} by {abs(step)}:')
    if begin < end:
        for number in range(begin, end + 1, step):
            print(f'{number} ', end="", flush=True)
            sleep(0.5)
        print(" FIM\n~~~~~~~~~~~~~~~~~~~~~\n")
    else:
        if step > 0:
            step *= -1
        for number in range(begin, end - 1, step):
            print(f'{number} ', end="", flush=True)
            sleep(0.5)
        print(" FIM\n~~~~~~~~~~~~~~~~~~~~~\n")


# a
counter(1, 10, 1)

# b
counter(10, 0, -2)

# c
begin = int(input("\nInput here the begin: "))
end = int(input("Input here the end: "))
step = int(input("Input here the step: "))
print()
counter(begin, end, step)
