###########################################################
# RapydScript Standard Library
# Author: Alexander Tsepkov
# Copyright 2013 Pyjeon Software LLC
# License: Apache License    2.0
# This library is covered under Apache license, so that
# you can distribute it with your RapydScript applications.
###########################################################

# basic implementation of Python's 'random' library

# JavaScript's Math.random() does not allow seeding its random generator, to bypass that, this module implements its own
# version that can be seeded. I decided on RC4 algorithm for this.

# please don't mess with this from the outside

ρσ_seed_state = {'key': [], 'key_i': 0, 'key_j': 0}


def ρσ_get_random_byte():
    ρσ_seed_state.key_i = (ρσ_seed_state.key_i + 1) % 256
    ρσ_seed_state.key_j = (ρσ_seed_state.key_j +
                           ρσ_seed_state.key[ρσ_seed_state.key_i]) % 256
    ρσ_seed_state.key[ρσ_seed_state.key_i], ρσ_seed_state.key[ρσ_seed_state.key_j] = \
            ρσ_seed_state.key[ρσ_seed_state.key_j], ρσ_seed_state.key[ρσ_seed_state.key_i]
    return ρσ_seed_state.key[(ρσ_seed_state.key[ρσ_seed_state.key_i] + \
            ρσ_seed_state.key[ρσ_seed_state.key_j]) % 256]


def seed(x=Date().getTime()):
    ρσ_seed_state.key_i = ρσ_seed_state.key_j = 0
    if jstype(x) is 'number':
        x = x.toString()
    elif jstype(x) is not 'string':
        raise TypeError("unhashable type: '" + jstype(x) + "'")
    for i in range(256):
        ρσ_seed_state.key[i] = i
    j = 0
    for i in range(256):
        j = (j + ρσ_seed_state.key[i] + x.charCodeAt(i % x.length)) % 256
        ρσ_seed_state.key[i], ρσ_seed_state.key[j] = ρσ_seed_state.key[
            j], ρσ_seed_state.key[i]


seed()


def random():
    n = 0
    m = 1
    for i in range(8):
        n += ρσ_get_random_byte() * m
        m *= 256
    return v'n / 0x10000000000000000'


# unlike the python version, this DOES build a range object, feel free to reimplement
def randrange():
    return choice(range.apply(this, arguments))


def randint(a, b):
    return int(random() * (b - a + 1) + a)


def uniform(a, b):
    return random() * (b - a) + a


def choice(seq):
    if seq.length > 0:
        return seq[Math.floor(random() * seq.length)]
    else:
        raise IndexError()


# uses Fisher-Yates algorithm to shuffle an array
def shuffle(x, random_f=random):
    for i in range(x.length):
        j = Math.floor(random_f() * (i + 1))
        x[i], x[j] = x[j], x[i]
    return x


# similar to shuffle, but only shuffles a subset and creates a copy
def sample(population, k):
    x = population.slice()
    for i in range(population.length - 1, population.length - k - 1, -1):
        j = Math.floor(random() * (i + 1))
        x[i], x[j] = x[j], x[i]
    return x.slice(population.length - k)


#import stdlib
#a = range(50)
#random.seed(5)
#print(random.choice(a))
#print(random.shuffle(a))
#print(random.randrange(10))
#print(random.randint(1,5))
#print(random.uniform(1,5))
#print(random.sample(range(20),5))
