from collections import Counter, defaultdict
import os
import queue as q
import pprint
import time


pp = pprint.PrettyPrinter(indent=4)
DATA_DIR = "data"
test_cases = ["5757"]
graph_file_format = "words-{}.txt"
input_format = "words-{}-in.txt"
output_format = "words-{}-out.txt"


class Graph:
    def __init__(self, words):
        self.graph = defaultdict(list)
        for i, word in enumerate(words):
            print(i),
            self.insert(word.strip())

    def insert(self, word):
        """
        Inserts a word after checking every possiblity
        """
        if not self.graph.get(word):
            self.graph[word] = []

        for vertex, vertex_edges in self.graph.items():
            if vertex != word:
                if self.arc_possible(vertex, word):
                    self.graph[vertex].append(word)
                # also check the vice versa
                if self.arc_possible(word, vertex):
                    self.graph[word].append(vertex)

    def arc_possible(self, word_1, word_2):
        """
        Checks if arc is possible b/w word_1 and word_2.
        """
        res = True
        last_four_chars_freq = dict(Counter(word_1[-4:]))
        word_2_freq = dict(Counter(word_2))

        # print(word_1, word_2)
        # print(last_four_chars_freq)
        # print(word_2_freq)

        for char, char_freq in last_four_chars_freq.items():
            if char not in word_2_freq:
                res = False
                break
            else:
                if word_2_freq[char] < char_freq:
                    res = False
                    break

        return res

    def distance_bw(self, word_1, word_2):
        print("Distance b/w {} and {}".format(word_1, word_2))
        if self.graph.get(word_1):
            print("Path: {} \nDistance: {}".format(*self.bfs(word_1, word_2)))
        else:
            print([], -1)

    def bfs(self, start, target):
        queue = q.Queue()

        queue.put([start])
        queue.put(["NULL"])
        visited = {vertex: False for vertex in self.graph}

        level = 0

        while queue:

            path = queue.get()

            if path == ["NULL"]:
                level += 1
                queue.put(["NULL"])
                path = queue.get()
                if path == ["NULL"]:
                    break

            s = path[-1]
            visited[s] = True

            if s == target:
                return path, level

            for i in self.graph[s]:
                if visited[i] == False:
                    new_path = list(path)
                    new_path.append(i)
                    queue.put(new_path)

        return [], -1


if __name__ == "__main__":
    start = time.time()
    for tc in test_cases:
        graph_file = graph_file_format.format(tc)
        input_file = input_format.format(tc)
        output_file = output_format.format(tc)

        # building a graph
        words = []
        with open(os.path.join(DATA_DIR, graph_file), 'r') as f:
            words = f.readlines()

        graph = Graph(words)
        # pp.pprint(dict(graph.graph))
        print("Graph built!")

        # printing out the results
        inputs = []
        with open(os.path.join(DATA_DIR, input_file)) as f:
            inputs = f.readlines()

        for ip in inputs:
            word_1, word_2 = ip.split()
            graph.distance_bw(word_1, word_2)
            print("=="*10)

        # printing the expected results (for verification)
        expected_results = ""
        with open(os.path.join(DATA_DIR, output_file), 'r') as f:
            expected_results = f.read()

        print(expected_results)

    end = time.time()
    print("{} seconds".format(start-end))

