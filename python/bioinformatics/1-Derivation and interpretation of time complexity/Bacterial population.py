class Population():
    def __init__(self, m=0, n=0, k=0):
        self.type1 = m
        self.type2 = n
        self.type3 = k
        self.encounters = 0
        list_p = []
        first = [1] * m
        second = [2] * n
        third = [3] * k
        list_p.extend(first)
        list_p.extend(second)
        list_p.extend(third)
        self.population = list_p

    def plasmids(self):
        return (self.type1, self.type2, self.type3)

    def __str__(self):
        return "type I: {}, type II: {}, type III: {} (after {} encounters)".format(self.type1, self.type2, self.type3,
                                                                                    self.encounters)

    def __repr__(self):
        return "Population({}, {}, {})".format(self.type1, self.type2, self.type3)

    def size(self):
        total = self.type1 + self.type2 + self.type3
        return total

    def encounter(self, number1, number2):
        self.encounters += 1
        for num in range(1):
            list_p = self.population
            if list_p[number1] == list_p[number2]:
                break
            index_list = [1, 2, 3]
            for ele in index_list:
                index_list.remove(list_p[number1])
                index_list.remove(list_p[number2])
            list_p[number1] = index_list[0]
            list_p[number2] = index_list[0]
            self.type1 = list_p.count(1)
            self.type2 = list_p.count(2)
            self.type3 = list_p.count(3)


def simulation(population, final=1, interval=1):
    repetition = int(final / interval)
    for i in range(repetition):
        for random_number in range(interval):
            population.encounter(random_number, random_number + 1)
        print(population)


if __name__ == '__main__':
    import doctest

    doctest.testmod()

'''
population = Population(m=998, n=1, k=1)
print(population)
stdout
type I: 998, type II: 1, type III: 1 (after 0 encounters)
population
return
Population(998, 1, 1)
population.plasmids()
return
(998, 1, 1)
for i in range(population.size() - 1):
    population.encounter(i, i + 1)
print(population)
stdout
type I: 997, type II: 0, type III: 3 (after 999 encounters)
for i in range(population.size() - 1):
    population.encounter(i, i+1)
print(population)
stdout
type I: 997, type II: 3, type III: 0 (after 1998 encounters)
population = Population(m=998, n=1, k=1)
The figure below shows the evolution of an initial population with m=988, n=1 and k=1 through 10.000 random encounters. With a correct implementation of the class Population you should see that after some time, the three types of plasmids are about equally divided over the population.


'''
