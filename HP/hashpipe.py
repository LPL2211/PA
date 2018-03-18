from algs4.fundamentals.java_helper import java_string_hash


class Pipe:

    def __init__(self, key, val, height):
        self.key = key
        self.value = val
        self.height = height
        # store the idx of the highest box referencing a key
        self._top_reference = -1
        self._boxes = [None] * height

    @property
    def boxes(self):
        """
        Returns the references in top to bottom order.
        """
        return self._boxes[::-1]

    def __str__(self):
        """
        Prints the references from pipe in the order of top to bottom.
        """
        res = []
        for pipe in self.boxes:
            if pipe:
                res.append(pipe.key)
            else:
                res.append(None)
        return str(res)

    @property
    def top_reference(self):
        i = 0
        while i < self.height and self._boxes[i] is not None:
            i += 1
        return i - 1

    @property
    def next_pipe(self):
        return self._boxes[0]


class HashPipe:

    def __init__(self):
        self.root = Pipe(-float('inf'), None, 32)

    def size(self):
        pass

    def put(self, key, val):
        predecessor = self.floor(self.root, key)
        height = calculate_pipe_height(key)
        new_pipe = Pipe(key, val, height)

        if predecessor is None:
            for i in range(height):
                old_ref = self.root._boxes[i]
                self.root._boxes[i] = new_pipe
                new_pipe._boxes[i] = old_ref
            new_pipe._top_reference = height - 1
            self.root._top_reference = max(self.root.top_reference, height - 1)
            return

        if predecessor.key == key:
            predecessor.value = val
            return

        predecessor_height = predecessor.height

        for i in range(min(height, predecessor_height)):
            old_ref = predecessor._boxes[i]
            predecessor._boxes[i] = new_pipe
            new_pipe._boxes[i] = old_ref

        while height > predecessor_height:
            next_pipe = predecessor.next_pipe
            if next_pipe.height > predecessor_height:
                for i in range(predecessor_height,
                               min(next_pipe.height, height)):
                    new_pipe._boxes[i] = next_pipe
            predecessor_height = next_pipe.height

        new_pipe._top_reference = height - 1

    def get(self, key):
        pipe = self.lookup(self.root, key)
        return pipe.value if pipe else None

    def lookup(self, start, key):
        if start or start.key is None:
            return None

        if start.key == key:
            return start

        elif start.key < key:
            self.get(start._boxes[start.top_reference], key)

        else:
            refs = start._boxes
            top_ref = start.top_reference
            while top_ref >= 0:
                res = self.get(refs[top_ref], key)
                if res:
                    return res
                top_ref -= 1

        return None

    def floor(self, start, key):
        """
        Returns pipe, with smallest key greater than or equal to the `key`
        provided.
        """
        string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        for char in string[::-1]:
            if char < key and self.get(key):
                return self.lookup(self.root, key)

    def control(self, key, height):
        """
        Returns the key referenced at height `height`.
        """
        pipe = self.lookup(self.root, key)
        if pipe:
            return pipe._boxes[height].key
        return None

    def create_string_to_debug(self, pipe, string_so_far):
        if pipe is None:
            return
        string_so_far += str(pipe) + "\n"
        refs = pipe.boxes
        top_ref = pipe.top_reference

        if top_ref == -1:
            return string_so_far

        else:
            height = len(refs)
            first_occupied = height - (top_ref + 1)
            for p in refs[first_occupied:]:
                self.create_string_to_debug(p, string_so_far)

        return string_so_far

    def __str__(self):
        return self.create_string_to_debug(self.root, '')


def calculate_pipe_height(key):
    hash_code = java_string_hash(key)
    num_trailing_zeroes = 0

    while not hash_code & 1:
        num_trailing_zeroes += 1
        hash_code = hash_code >> 1

    return num_trailing_zeroes + 1


string = "SEARCHEXAMPLE"

hp = HashPipe()

for idx, char in enumerate(string):
    hp.put(char, idx)
    print(hp)
