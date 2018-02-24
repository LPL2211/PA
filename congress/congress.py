from collections import OrderedDict
import heapq
import math

TESTFILE = "1990-in.txt"

file_contents = []

# Uncomment this if you want to read from a file
"""
with open(TESTFILE, 'r') as f:
    file_contents = f.readlines()

num_states = int(file_contents[0])
num_seats = int(file_contents[1])
"""

num_states = int(input())
num_seats = int(input())

heap = []
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

    state_population = state_population/math.sqrt(2)

    # python only has min-heap implementation, but our
    # use case require max-heap, hence the -ve  sign in
    # front of state_population.
    # The key for the priority queue is state_population and
    # the value is state_name.
    heap.append((-state_population, state_name))
    # every state is allocated at least one seat
    # allocation[state_name] = 1
    allocation[state_name] = {"seats": 1, "population": state_population}

# this function heapifies our python list `heap` to form
# priority queue
heapq.heapify(heap)

# every state has been allocated one seat,
# rest of the seats are distributed in order of priority
seats_left = num_seats - num_states

for _ in range(seats_left):
    population, state = heapq.heappop(heap)

    allocation[state]["seats"] += 1
    current_seats = allocation[state]["seats"]

    population = allocation[state]["population"]/(math.sqrt(current_seats * (current_seats + 1)))

    heapq.heappush(heap, (-population, state))

# dictionary can't be sorted in Python, so OrderedDict comes to
# our rescue. It's not necessary but this will allow us print
# results in sorted order
sorted_allocation = OrderedDict(sorted(allocation.items()))

for state, state_info in sorted_allocation.items():
    print(state, state_info["seats"])
