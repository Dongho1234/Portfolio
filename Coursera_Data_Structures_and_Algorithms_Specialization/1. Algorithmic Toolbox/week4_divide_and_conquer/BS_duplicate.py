def binary_search(keys, query):
    # sorted list
    # For query
    # find numbers of the position in key
    left = 0
    right = len(keys) - 1
    answer_list = []

    while left <= right:
        mid = (left + right) // 2
        if keys[mid] > query:
            right = mid - 1
        elif keys[mid] < query:
            left = mid + 1
        else: #keys[mid] == query:
            if mid - 1 < 0:
                return mid
            if keys[mid-1] != query:
                return mid
            right = mid -1
    return -1

if __name__ == '__main__':
    fking_dum, input_keys = input(), list(map(int, input().split()))
    fking_dum2, input_queries = input(), list(map(int, input().split()))
    answer = []
    for q in input_queries:
        ans = binary_search(input_keys, q)
        print(ans, end=' ')
