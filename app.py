import heapq
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# ===== YOUR ORIGINAL CODE (UNCHANGED) =====
class TaskScheduler:
    def __init__(self):
        self.heap = []
        self.task_map = {}
        self.counter = 0

    def add_task(self, task_id, priority):
        self.counter += 1
        entry = (-priority, self.counter, task_id)
        heapq.heappush(self.heap, entry)
        self.task_map[task_id] = entry

    def peek_task(self):
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
        if task_id in self.task_map:
            del self.task_map[task_id]
            self.add_task(task_id, new_priority)

    def get_all_tasks(self):
        return [(task_id, -entry[0]) for task_id, entry in self.task_map.items()]

scheduler = TaskScheduler()

@app.route("/")
def home():
    tasks = scheduler.get_all_tasks()
    next_task = scheduler.peek_task()
    return render_template("index.html", tasks=tasks, next_task=next_task)

@app.route("/add", methods=["POST"])
def add():
    task = request.form["task"]
    priority = int(request.form["priority"])
    scheduler.add_task(task, priority)
    return redirect("/")

@app.route("/execute")
def execute():
    scheduler.execute_task()
    return redirect("/")

@app.route("/change", methods=["POST"])
def change():
    task = request.form["task"]
    priority = int(request.form["priority"])
    scheduler.change_priority(task, priority)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)