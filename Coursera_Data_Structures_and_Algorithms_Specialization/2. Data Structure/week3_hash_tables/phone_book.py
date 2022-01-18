# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = query[1]
        if self.type == "add":
            self.name = query[2]


def process(query, phone_book):
    if query.type == "add":
        phone_book[query.number] = query.name
    elif query.type == "del":
        if phone_book.__contains__(query.number):
            del phone_book[query.number]
    else:
        response = 'not found'
        if phone_book.__contains__(query.number):
            response = phone_book[query.number]
        return response

def main():
    phone_book = {}
    n_queries = int(input())
    for _ in range(n_queries):
        query = Query(input().split())
        result = process(query, phone_book)
        if result: #unless add 119 police gives None
            print(result)

if __name__ == "__main__":
    main()
