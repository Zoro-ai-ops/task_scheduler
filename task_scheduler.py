import heapq # built in module for heap operations

class TaskScheduler:
    def __init__(self):
        self.heap = []
        self.task_map = {}
        self.counter = 0 #A tie breaker for tasks with the same proiority

    def add_task(self, task_id, priority):
        self.counter += 1

        # Min-heap: lower numeric value means higher scheduling priority.
        entry = (priority, self.counter, task_id)
        heapq.heappush(self.heap, entry)
        self.task_map[task_id] = entry

    def peek_task(self):
        while self.heap:
            priority, _, task_id = self.heap[0]
            if task_id in self.task_map:
                return task_id, priority
            heapq.heappop(self.heap)
        return None

    def execute_first_task(self):
        while self.heap:
            priority, self.counter, task_id = heapq.heappop(self.heap)
            if task_id in self.task_map:
                del self.task_map[task_id]
                return task_id, priority
        return None

    def execute_all_tasks(self):
        executed_tasks = []

        while True:
            task = self.execute_first_task()
            if task is None:
                break
            executed_tasks.append(task)

        return executed_tasks

    def change_priority(self, task_id, new_priority):
        if task_id in self.task_map:
            del self.task_map[task_id]
            self.add_task(task_id, new_priority)

    def delete_task(self, task_id):
        if task_id in self.task_map:
            del self.task_map[task_id]
            return True
        return False

    def get_all_tasks(self):
        # Return tasks sorted by priority, then by insertion order.
        entries = list(self.task_map.values())

        def sort_key(entry):
            priority, counter, _ = entry
            return priority, counter

        entries.sort(key=sort_key)
        return [(task_id, priority) for priority, _, task_id in entries]