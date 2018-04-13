from collections import Counter, defaultdict
import os
import sys


DATA_DIR = "."
graph_file_format = "words-{}.txt"
input_format = "words-{}-in.txt"
output_format = "words-{}-out.txt"


class Graph:
    def __init__(self, words):
        self.graph = defaultdict(list)
        for i, word in enumerate(words):
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
        if self.graph.get(word_1):
            print(self.bfs(word_1, word_2)[1])
        else:
            print(-1)

    def bfs(self, start, target):
        queue = []

        queue.append([start])
        queue.append(["NULL"])
        visited = {vertex: False for vertex in self.graph}

        level = 0

        while queue:

            path = queue.pop(0)

            if path == ["NULL"]:
                level += 1
                queue.append(["NULL"])
                path = queue.pop(0)
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
                    queue.append(new_path)

        return [], -1


if __name__ == "__main__":
    graph_file = sys.argv[1]
    input_file = sys.argv[2]

    # building a graph
    words = []
    with open(graph_file, 'r') as f:
        words = f.readlines()

    graph = Graph(words)

    # printing out the results
    inputs = []
    with open(input_file) as f:
        inputs = f.readlines()

    for ip in inputs:
        word_1, word_2 = ip.split()
        graph.distance_bw(word_1, word_2)
