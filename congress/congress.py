import heapq
from collections import OrderedDict

TESTFILE = "1990-in.txt"

# this constant is not specified in the report and I can't find it anywhere
# so for now, I took it as 10,000. But we won't get exact answers until we
# figure out what it should be.
constant = 10000

file_contents = []

with open(TESTFILE, 'r') as f:
    file_contents = f.readlines()

num_states = int(file_contents[0])
num_seats = int(file_contents[1])

heap = []
allocation = {}

for i in range(1, num_states):
    state_name = file_contents[2 * i].strip()
    state_population = int(file_contents[2 * i + 1])

    # python only has min-heap implementation, but our
    # use case require max-heap, hence the -ve  sign in
    # front of state_population.
    # The key for the priority queue is state_population and
    # the value is state_name.
    heap.append((-state_population, state_name))
    # every state is allocated at least one seat
    allocation[state_name] = 1

# this function heapifies our python list `heap` to form
# priority queue
heapq.heapify(heap)

# every state has been allocated one seat,
# rest of the seats are distributed in order of priority
seats_left = num_seats - num_states

for _ in range(seats_left):
    seats, state = heapq.heappop(heap)
    seats = -seats

    allocation[state] += 1

    # subtract the seats by constant, and push back into the heap
    seats -= constant
    heapq.heappush(heap, (-seats, state))

# dictionary can't be sorted in Python, so OrderedDict comes to
# our rescue. It's not necessary but this will allow us print
# results in sorted order
sorted_allocation = OrderedDict(sorted(allocation.items()))

for state, num_seats in sorted_allocation.items():
    print(state, num_seats)
