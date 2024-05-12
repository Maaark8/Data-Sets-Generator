import random

# random numbers in range 0-100000
def data_set_1(file, size):
    open(file, 'w').close()
    with open(file, 'a') as f:
        for i in range(size):
            rnd = random.randint(0, 100000)
            f.write(str(rnd) + " ")

# random numbers in range 0-9
def data_set_2(file, size):
    open(file, 'w').close()
    with open(file, 'a') as f:
        for i in range(size):
            rnd = random.randint(0, 9)
            f.write(str(rnd) + " ")

# decreasing numbers
def data_set_3(file, size):
    open(file, 'w').close()
    l = []
    for i in range(size):
        rnd = random.randint(0, 100000)
        l.append(rnd)
    l.sort(reverse=True)

    with open(file, 'a') as f:
        for x in l:
            f.write(str(x) + " ")

# alternating
def data_set_4(file, size):
    open(file, 'w').close()
    prev = 0
    with open(file, 'a') as f:
        for i in range(size):
            if i % 2 == 0:
                rnd = random.randint(prev, 100000)
                prev = rnd
            else:
                rnd = random.randint(0, prev)
                prev = rnd

            f.write(str(rnd) + " ")

# sorted numbers
def data_set_5(file, size):
    open(file, 'w').close()
    l = []
    for i in range(size):
        rnd = random.randint(0, 100000)
        l.append(rnd)
    l.sort()

    with open(file, 'a') as f:
        for x in l:
            f.write(str(x) + " ")
