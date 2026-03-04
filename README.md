# task_scheduler
A Python DSA practice project. Schedules tasks based on priority

Task Scheduler Using Priority Queue (Console Application)

Project Overview

The Task Scheduler is a console-based Python application that allows
users to manage and execute tasks based on their priority.

The scheduler ensures that:

-   Higher-priority tasks are executed first
-   Tasks with equal priority follow the order they were added
-   Users can dynamically add, update, view, and execute tasks

This project demonstrates the use of fundamental Data Structures and
Algorithms.

------------------------------------------------------------------------

Learning Objectives

This project helps to understand:

-   Priority queues
-   Heap operations
-   Greedy scheduling
-   Dictionary usage
-   Data Structures and Algorithms

------------------------------------------------------------------------

Features

1.  Add Task
2.  View Next Task
3.  Execute Task
4.  Display Pending Tasks
5.  Change Task Priority
6.  Exit

------------------------------------------------------------------------

Data Structures Used

Priority Queue (Heap)

Used to access highest priority task efficiently.

Time Complexity:

Insert: O(log n)
Remove: O(log n)
View: O(1)

------------------------------------------------------------------------

Dictionary

Used for fast lookup of tasks.

Example:

tasks = { “Study”: 5, “Sleep”: 2 }

------------------------------------------------------------------------

Algorithm Used

Greedy Scheduling Algorithm

Always selects the highest priority task first.

------------------------------------------------------------------------

Project Structure

[empty]

------------------------------------------------------------------------

User Interface

===== TASK SCHEDULER =====

1.  Add Task
2.  View Next Task
3.  Run Tasks
4.  Display All Tasks
5.  Change Task Priority
6.  Exit

------------------------------------------------------------------------

Functions Required

add_task()
view_next_task()
run_tasks()
display_tasks()
change_task_priority()
show_menu()
main()

------------------------------------------------------------------------

Error Handling

Empty scheduler → “No tasks available”

Task not found → “Task does not exist”

Duplicate task → “Task already exists”

Duplicate priority → Run based on last added

------------------------------------------------------------------------

How to Run

python scheduler.py

------------------------------------------------------------------------

Real‑World Applications

-   Operating systems
-   CPU scheduling
-   Job scheduling
-   Printer queues

------------------------------------------------------------------------

Assignment Checklist

Priority Queue used ✔
Dictionary used ✔
Heap operations ✔
Greedy scheduling ✔
Console application ✔

------------------------------------------------------------------------

Conclusion

This project demonstrates how priority queues can be used to build
efficient task scheduling systems.
