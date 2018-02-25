import math

from algs4.sorting.max_pq import MaxPQ


# Uncomment this if you want to read from a file
"""
TESTFILE = "1990-in.txt"
file_contents = []
with open(TESTFILE, 'r') as f:
    file_contents = f.readlines()

num_states = int(file_contents[0])
num_seats = int(file_contents[1])
"""

num_states = int(input())
num_seats = int(input())

pq = MaxPQ()
allocation = {}

# To read from a file, uncomment this
"""
for i in range(1, num_states):
    state_name = file_contents[2 * i].strip()
    state_population = int(file_contents[2 * i + 1])
"""

for i in range(num_states):
    state_name = input().strip()
    state_population = int(input())

    # every state is allocated at least one seat
    allocation[state_name] = {"seats": 1, "population": state_population}

    state_population = state_population/math.sqrt(2)

    # The key for the priority queue is state_population and
    # the value is state_name.
    pq.insert((state_population, state_name))

# every state has been allocated one seat,
# rest of the seats are distributed in order of priority
seats_left = num_seats - num_states

for _ in range(seats_left):
    population, state = pq.del_max()

    allocation[state]["seats"] += 1
    current_seats = allocation[state]["seats"]

    population = allocation[state]["population"]/(math.sqrt(current_seats * (current_seats + 1)))

    pq.insert((population, state))

for state, state_info in allocation.items():
    print(state, state_info["seats"])
