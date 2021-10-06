from threading import Thread
import time


class SearchAlgorithm1:

    def __init__(self, list_data: list, element):
        self.element = element
        self.list = list_data
        self.searching = True
        self.index = None

    def search(self):
        Thread(self.forward())
        self.reverse()
        return self.index

    def reverse(self):
        len_all = len(self.list)
        for i in range(len(self.list) - 1):
            try:
                if not self.searching:
                    break
                i = len_all - i
                if self.list[i] == self.element:
                    self.searching = False
                    self.index = i
                    break
            except Exception:
                pass

    def forward(self):
        for i in range(len(self.list) - 1):
            try:
                if not self.searching:
                    break
                if self.list[i] == self.element:
                    self.searching = False
                    self.index = i
                    break
            except Exception:
                pass


list_i = [i for i in range(800, 9800)]
print("Searching by my algorithm...")

index_element = SearchAlgorithm1(list_i, 8999).search()
print(index_element)
