import random

def gen_random(num_count, begin, end):
    numbers = []
    for i in range(num_count):
        numbers.append(random.randint(begin, end))
    return numbers

if __name__ == '__main__':
    numbers = gen_random(5, 1, 3)
    print(numbers)