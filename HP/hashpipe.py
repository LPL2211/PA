from algs4.fundamentals.java_helper import java_string_hash


class Pipe:

    def __init__(self, key, val, height, predecessor=None):
        self.key = key
        self.value = val
        self.height = height
        self.previous_pipe = predecessor
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
                res.append(".")
        return " ".join(res)

    @property
    def top_reference(self):
        i = 0
        while i < self.height and self._boxes[i] is not None:
            i += 1
        return i - 1

    @property
    def next_pipe(self):
        return self._boxes[0]

    def key_at_height(self, height):
        return self._boxes[height].key if height<=self.top_reference else None


class HashPipe:

    def __init__(self):
        self.root = Pipe(-float('inf'), "ROOT", 32, None)

    def size(self):
        pass

    def put(self, key, val):
        if self.exists(key):
            self.lookup(self.root, key).value = val
            return

        predecessor = self.floor(self.root, key)
        height = calculate_pipe_height(key)
        new_pipe = Pipe(key, val, height)
        new_pipe.previous_pipe = predecessor

        # print("predecessor is {}".format(predecessor.key))

        # min element till now
        if predecessor.value is "ROOT":
            for i in range(height):
                old_ref = self.root._boxes[i]
                self.root._boxes[i] = new_pipe
                new_pipe._boxes[i] = old_ref
            return

        # key already exists
        if predecessor.key == key:
            predecessor.value = val
            return

        # otherwise, update the references
        predecessor_height = predecessor.height
        next_pipe = predecessor.next_pipe

        if next_pipe:
            next_pipe.previous_pipe = new_pipe

        # fit upto the common height
        for i in range(min(height, predecessor_height)):
            old_ref = predecessor._boxes[i]
            predecessor._boxes[i] = new_pipe
            new_pipe._boxes[i] = old_ref

        # if our new pipe is taller than the predecessor
        # we need to add forward references
        while height > predecessor_height and next_pipe:
            if next_pipe.height > predecessor_height:
                # doubt
                for i in range(predecessor_height,
                               min(next_pipe.height, height)):
                    new_pipe._boxes[i] = next_pipe
                predecessor_height = min(next_pipe.height, height)
            next_pipe = next_pipe.next_pipe

        # we also need to check backward references
        if height > predecessor.height:
            covered_height = predecessor.height
            predecessor = predecessor.previous_pipe
            while predecessor is not None and covered_height < height:
                if predecessor.height > covered_height:
                    for i in range(covered_height, min(predecessor.height, height)):
                        predecessor._boxes[i] = new_pipe
                    covered_height = min(predecessor.height, height)
                predecessor = predecessor.previous_pipe

    def get(self, key):
        pipe = self.lookup(self.root, key)
        return pipe.value if pipe else None

    def exists(self, key):
        return True if self.lookup(self.root, key) else False

    def lookup(self, start, key):
        if key is None:
            # print("None key found for lookup")
            return None

        # A none reference
        if start is None or start.key is None:
            # print("Looking for {} in none Pipe".format(key))
            return None

        # print("Lookup for {} with pipe as {}".format(key, start.key))

        # Found!
        if start.key == key:
            return start

        top_ref = start.top_reference

        if top_ref == -1:
            # print("Empty pipe encountered with key {} while looking for {}".format(start.key, key))
            pass

        elif start._boxes[top_ref].key <= key:
            return self.lookup(start._boxes[top_ref], key)

        else:
            refs = start._boxes
            top_ref -= 1
            while top_ref >= 0:
                res = self.lookup(refs[top_ref], key)
                if res:
                    return res
                top_ref -= 1

        return None

    def floor(self, start, key):
        """
        Returns pipe, with largest key smaller than or equal to the `key`
        provided.
        """
        string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        for char in string[::-1]:
            # hack
            if char < key and self.exists(char):
                return self.lookup(self.root, char)
            else:
                # print("Key {}, not found.".format(char))
                pass

        return self.root

    def control(self, key, height):
        """
        Returns the key referenced at height `height`.
        """
        pipe = self.lookup(self.root, key)
        if pipe:
            return pipe.key_at_height(height)
        else:
            return None

    def create_string_to_debug(self, pipe, string_so_far):
        if pipe is None:
            return string_so_far

        string_so_far += str(pipe) + "\n*"
        refs = pipe._boxes
        top_ref = pipe.top_reference

        # print(pipe.key, top_ref)

        if top_ref == -1:
            return string_so_far

        else:
            for p in refs[:top_ref + 1]:
                string_so_far += self.create_string_to_debug(p, string_so_far)

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



import string
# ex = list(string.ascii_uppercase)
ex = list("SEARCHEXAMPLE")
H =  HashPipe()
j=0
for k in ex:
    print("Insert: ", k)
    H.put(k, j)
    cl = [ H.control(-float('inf'), h) for h in range(32) ]
    #        print(cl)
    print( " ".join(x if x else '.' for x in cl) + "  : " + "ROOT" )
    for g in range(j+1):
        cl = [ H.control(ex[g], h) for h in range(32) ]
        #        print(cl)
        pipe = H.lookup(H.root, ex[g])
        prev = pipe.previous_pipe.key if pipe.previous_pipe else "None"
        nxt = pipe.next_pipe.key if pipe.next_pipe else "None"
        print( " ".join(x if x else '.' for x in cl) + "  : " + ex[g] + " {} {}".format(pipe.height, prev, nxt))
    j += 1
