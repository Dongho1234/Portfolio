# python3
from collections import namedtuple

# n = independent threads (take jobs in order) = n_workers
# m = number of jobs (contain integers ti)
# t = jobs = times in second that takes any thread to process i jobs = time taken for jobs to be done
# out_put = (which thread process, when jobs are taken = when thread starts the job)

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])

class parallel_processing:
    def __init__(self, n_workers, jobs):
        self.n = n_workers
        self.jobs = jobs
        self.out_put = []
        self.naive_result = []
        for i in range(self.n):
            #initialize (n-1, start time)
            self.out_put.append([i,0])
        self.assigned = []

    def shift(self, index):
        min_index = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < self.n:
            #comparsion of which threads process
            if self.out_put[min_index][1] > self.out_put[left][1]:
                min_index = left
            elif self.out_put[min_index][1] == self.out_put[left][1] and self.out_put[min_index][0] > self.out_put[min_index][0]:
                min_index = left
        if right < self.n:
            if self.out_put[min_index][1] > self.out_put[right][1]:
                min_index = right
            elif self.out_put[min_index][1] == self.out_put[right][1] and self.out_put[min_index][0] > self.out_put[right][0]:
                min_index = right
        if min_index != index:
            self.out_put[min_index], self.out_put[index] = self.out_put[index], self.out_put[min_index]
            self.shift(min_index)

    def next_thread(self, job):
        next_worker = self.out_put[0][0]
        starting_time = self.out_put[0][1]
        self.assigned.append(AssignedJob(next_worker, starting_time))
        print(AssignedJob(next_worker, starting_time))
        print(self.out_put)
        self.out_put[0][1] += job
        self.shift(0)

    def naive(self, jobs):
        next_free_time = [0] * self.n
        for job in jobs:
            next_worker = min(range(self.n), key=lambda w: next_free_time[w])
            self.naive_result.append(AssignedJob(next_worker, next_free_time[next_worker]))
            next_free_time[next_worker] += job




def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    p_p = parallel_processing(n_workers, jobs)
    #if n_workers < 100:
    #    ans = p_p.naive(jobs)
    #    naive_assigned = p_p.naive_result
    #    for job in naive_assigned:
    #        print(job.worker, job.started_at)
    #else:
    for job in jobs:
        p_p.next_thread(job)

    assigned_jobs = p_p.assigned

    for ans in assigned_jobs:
        print(ans.worker, ans.started_at)

if __name__ == "__main__":
    main()
