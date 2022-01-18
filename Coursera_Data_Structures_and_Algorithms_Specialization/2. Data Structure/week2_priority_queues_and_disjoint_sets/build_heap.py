# python3

"""Build a heap from ``data`` inplace.
Returns a sequence of swaps performed by the algorithm.
"""
# The following naive implementation just sorts the given sequence
# using selection sort algorithm and saves the resulting sequence
# of swaps. This turns the given array into a heap, but in the worst
# case gives a quadratic number of swaps.
#
# TODO: replace by a more efficient implementation



class covert_array_into_heap:
    def __init__(self,array):
        self.input = array
        self.size = len(self.input)
        self.swaps = []

    def shift(self, index):
        min_index = index
        left = 2 * index + 1
        right = 2 * index + 2
        if left < self.size and self.input[left] < self.input[min_index]:
            min_index = left
        if right < self.size and self.input[right] < self.input[min_index]:
            min_index = right
        if min_index != index:
            self.swaps.append((index, min_index))
            self.input[index], self.input[min_index] = self.input[min_index], self.input[index]
            self.shift(min_index)

    def build_heap(self):
        # start = self.size / stop = -1 / step = -1
        for index in range(self.size // 2 -1, -1 ,-1):
            self.shift(index)

def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    heap = covert_array_into_heap(data) #initialize default values
    covert_array_into_heap.build_heap(heap)
    swaps = heap.swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)

if __name__ == "__main__":
    main()
