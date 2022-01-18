# python 3
# input
# first input = single integer 𝑚 in the first line — the number of buckets you should have
# second input = next line contains the number of queries N
# Next each of them contains one query in the format

# output
#  Print the result of each of the find and check queries, one result per line, in the same
#  order as these queries are given in the input

from collections import deque

class Query:
    def __init__(self, query):
        self.type = query[0]
        if self.type == "check":
            self.index = int(query[1])
        else:
            self.word = query[1]

class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        self.hash_table = list(deque() for i in range(self.bucket_count))

    def HashFunction(self, word):
        hash_value = 0
        for c in reversed(word):
            hash_value = (((hash_value * self._multiplier + ord(c)) % self._prime) + self._prime) % self._prime
        return hash_value % self.bucket_count

    def process_query(self, query):
        if query.type == 'check':
            if self.hash_table[query.index]:
                ans = self.hash_table[query.index]
                print(" ".join(ans))
            else:
                print()
        else:
            hash_value = self.HashFunction(query.word)
            if query.type == 'add':
                if query.word not in self.hash_table[hash_value]:
                    self.hash_table[hash_value].appendleft(query.word)
            elif query.type == 'del':
                if query.word in self.hash_table[hash_value]:
                    self.hash_table[hash_value].remove(query.word)
            elif query.type == 'find':
                if query.word in self.hash_table[hash_value]:
                    print('yes')
                else:
                    print('no')


if __name__ == '__main__':
    n_buckets = int(input())
    hash_table = QueryProcessor(n_buckets)
    n_queries = int(input())
    for i in range(n_queries):
        command = Query(input().split())
        hash_table.process_query(command)
