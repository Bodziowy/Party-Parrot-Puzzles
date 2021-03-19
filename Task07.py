from collections import Counter

sample_input1 = [
    "A: B, B, C, C, D",
    "B: D",
    "C: D"]

sample_input2 = [
    'A: B, C, C',
    'B: A',
    'D: B, C, B, C']

final_input = [
    "F: C, G",
    "G: B",
    "E: G, B, G, C, G",
    "D: G, G, F",
    "B: F",
    "C: E, E, B, B, D",
    "A: E, D, G"]


class Graph:
    def __init__(self, bridges_list):
        self.bridges = bridges_list
        self.vertices = set()

        # create a long list of every appearance of a Vertex from the bridges list
        vertices_list = list()
        for string in self.bridges:
            vertices_list.extend([string[0] for i in range(0, int((len(string) - 4) / 3))])
            vertices_list.extend([char for char in string if char.isalpha()])

        # create a dictionary by using Counter class from Collections library
        c = Counter(vertices_list)
        for vertex in c:
            self.vertices.add(Vertex(vertex, c[vertex]))

    def semi_eulerian(self):
        # If needed one can add it
        pass

    def eulerian(self):
        for vertex in self.vertices:
            if not vertex.even():
                return False
        return True

    def __str__(self):
        answer = self.eulerian()
        text_to_print = f"Answer: {answer}"
        text_to_print += f"\nThe graph is{' not' if not answer else ''} Eulerian:"
        for vertex in self.vertices:
            text_to_print += "\n" + vertex.__str__()
        return text_to_print


class Vertex:
    def __init__(self, name: str, degree: int = 0):
        self.name = name
        self.degree = degree

    def even(self):
        return bool(not self.degree % 2)

    def __str__(self):
        return f"Vertex {self.name} has {self.degree} degree"


Final_answer = Graph(final_input)
print(Final_answer)
