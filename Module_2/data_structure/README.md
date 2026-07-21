# Module 2 – Advanced Python & Data Handling

## Objective

The objective of this module is to practice implementing fundamental data structures in Python and applying them to solve practical programming problems. This assignment covers linked lists, stacks, and queues while reinforcing their real-world applications and time complexity.

---

## Part 1 – Linked List

### Description

The `LinkedList` class was extended by implementing three new methods:

- **delete(target)**
  - Removes the first node containing the specified value.
  - Returns `True` if the value is found and deleted.
  - Returns `False` if the value is not found.

- **length()**
  - Traverses the linked list and returns the total number of nodes.
  - **Time Complexity:** O(n)

- **to_list()**
  - Converts the linked list into a standard Python list.
  - **Time Complexity:** O(n)

### Example Output

```text
Original List:
10 -> 20 -> 30 -> 40 -> 50 -> None

Length:
5

After deleting 30:
10 -> 20 -> 40 -> 50 -> None

Converted to Python list:
[10, 20, 40, 50]
```

---

## Part 2 – Stack: Bracket Validator

### Description

Implemented `is_balanced(text)` using a stack to determine whether brackets are properly matched.

Supported brackets:

- `()`
- `[]`
- `{}`

The function ignores all non-bracket characters and correctly validates nested brackets.

### Example Output

```text
is_balanced("()")             -> True
is_balanced("({[]})")         -> True
is_balanced("(]")             -> False
is_balanced("([)]")           -> False
is_balanced("hello (world)")  -> True
```

**Time Complexity:** O(n)

---

## Part 3 – Queue: Task Processor

### Description

Implemented a `TaskProcessor` class using `collections.deque` to simulate a First-In, First-Out (FIFO) queue.

Methods:

- **add_task(name)** – Adds a task to the end of the queue.
- **process_next()** – Removes and returns the oldest task.
- Returns `None` when the queue is empty.

### Example Output

```text
Add:
Task 1
Task 2
Task 3

Process:
Task 1
Task 2
Task 3
None
```

**Time Complexity**

- `add_task()` → O(1)
- `process_next()` → O(1)

---

## Data Structures Used

| Data Structure | Purpose |
|----------------|---------|
| Linked List | Store and manage sequential nodes |
| Stack | Validate balanced brackets using LIFO |
| Queue (`deque`) | Process tasks using FIFO |

---

## Time Complexity Summary

| Operation | Complexity |
|-----------|------------|
| Insert at End | O(n) |
| Delete Node | O(n) |
| Length | O(n) |
| Convert to List | O(n) |
| Bracket Validation | O(n) |
| Add Task | O(1) |
| Process Next Task | O(1) |

---

## What I Learned

Through this assignment, I learned how to:

- Implement and manipulate a singly linked list.
- Remove nodes safely from a linked list.
- Traverse a linked list to count and collect values.
- Use a stack to solve bracket-matching problems.
- Use a queue (`deque`) to process tasks in FIFO order.
- Analyze the time complexity of common data structure operations.
- Choose the appropriate data structure for different programming problems.
