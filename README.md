# task_scheduler
A Python Data Structures Project. Schedules tasks based on priority

Project Overview

The Task Scheduler is a python GUI application that executes and
schedules tasks based on their priority.
Tasks are added and the **Estimated Time of Completion (ETC)** is
calculated based on the text "length" or text "count".

How it works (overview):
-   User adds a task and sets the priority
-   Higher-priority tasks are executed first
-   Tasks with equal priority follow the order they were added
-   Application shows the ETC for each task

------------------------------------------------------------------------

Features

Tasks List
   
Add a task
   --> Task, Priority
   
Delete a task
   --> Recycle bin
   --> * Next priority takes the priority of deleted task in succession
   
Run tasks
   --> Reorders tasks on priority
   --> Executes tasks one by one based on priority
   --> Sidebar opens to show finished tasks

Interrupt
   --> Stops all taks from running

...

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

Functions Required

[empty]

------------------------------------------------------------------------

Error Handling

[empty]

------------------------------------------------------------------------

How to Run

[empty]

