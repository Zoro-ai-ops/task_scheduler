import heapq # built in module for heap operations

class TaskScheduler:
    def __init__(self):
        self.heap = []
        self.task_map = {}
        self.counter = 0 #A tie breaker for tasks with the same proiority

    def add_task(self, task_id, priority):
        self.counter += 1
        # Create entry with negative priority (max heap), counter, and task_id
        entry = (-priority, self.counter, task_id)
        heapq.heappush(self.heap, entry)
        self.task_map[task_id] = entry # Store mapping of task_id to entry for removal tracking

    def peek_task(self):#retrum max value or in this case the value with th highest priority
        while self.heap:
            priority, _, task_id = self.heap[0]
            if task_id in self.task_map:
                return task_id, -priority
            heapq.heappop(self.heap)
        return None

    def execute_task(self):
        while self.heap:
            priority, _, task_id = heapq.heappop(self.heap)
            if task_id in self.task_map:
                del self.task_map[task_id]
                return task_id, -priority
        return None

    def change_priority(self, task_id, new_priority):
        # Change priority by removing old entry and adding new one
        if task_id in self.task_map:
            del self.task_map[task_id]
            self.add_task(task_id, new_priority)

    def get_all_tasks(self):
        # Return list of all valid tasks with their priorities
        return [(task_id, -entry[0]) for task_id, entry in self.task_map.items()]
 
 #TEST
Sched = TaskScheduler()
Sched.add_task("Task1", 5)
Sched.add_task("Task2", 10)
Sched.add_task("Task3",6)

print(Sched.peek_task())

Sched.change_priority("Task1", 12)
print(Sched.peek_task())

