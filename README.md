# Breadth First Search & Depth First Search

---

### Setting up the Project

```
1. git clone YOUR-GITHUB-REPO-HERE
2. conda info --envs
3. conda activate environment_path
4. pip install -r requirements.txt
	- or pip install numpy


```

### File Structure:

### **main.py**

`main.py` contains the implementations of two search algorithms: **Breadth-First Search (BFS)** and **Depth-First Search (DFS)**. Both algorithms aim to find a sequence of flips that will sort a stack of textbooks. Here's a breakdown of what each part of `main.py` does:

1. **breadth_first_search(stack)**:

   - **Purpose**: This function performs a breadth-first search on a `TextbookStack` object to find the shortest sequence of flips that will sort the stack.
   - **How it works**:
     - It uses a queue (FIFO) to explore all possible stack configurations. The queue stores tuples of the current stack and the sequence of flips performed to reach that configuration.
     - It checks if the stack is ordered using the `check_ordered()` method. If the stack is sorted, it returns the sequence of flips.
     - If the stack isn't sorted, it generates all possible flips (from position 1 to the total number of books) and adds the resulting stacks to the queue.
     - If a new stack configuration hasn't been visited before, it adds it to the queue and continues until a solution is found.
     - **Output**: The function returns the sequence of flips that sorts the stack.

2. **depth_first_search(stack)**:
   - **Purpose**: This function performs a depth-first search to find a sequence of flips that will sort the stack, but it explores deeper into the stack configurations before backtracking.
   - **How it works**:
     - It uses a stack (LIFO) to explore different configurations. Similar to BFS, it stores tuples of the current stack and the sequence of flips performed.
     - It checks if the stack is ordered and returns the sequence of flips if sorted.
     - If not sorted, it generates all possible flips (from position 1 to the total number of books) and adds the resulting stacks to the stack for further exploration.
     - **Output**: The function returns the sequence of flips that sorts the stack.

---

### **textbook_stack.py**

`textbook_stack.py` contains the definition of the `TextbookStack` class, which represents a stack of textbooks and provides methods to manipulate and check the state of the stack. Here's a breakdown of its functionality:

1. \***\*init**(initial_order, initial_orientations)\*\*:

   - **Purpose**: This constructor initializes the stack with a given order and orientations.
   - `initial_order`: A list that specifies the order of textbooks (e.g., `[0, 1, 2]`).
   - `initial_orientations`: A list specifying the orientations of the books (e.g., `[0, 0, 1]`, where `0` means face-down and `1` means face-up).
   - It also performs validation to ensure the order and orientations are consistent.

2. **flip_stack(position)**:

   - **Purpose**: This method flips the books up to a specified position.
   - It reverses the order of books up to the given position and flips the orientations (face-up becomes face-down, and vice versa).

3. **check_ordered()**:

   - **Purpose**: This method checks if the stack is ordered.
   - It returns `True` if the books are in ascending order and all books are face-up (`1`), otherwise it returns `False`.

4. **copy()**:

   - **Purpose**: This method creates and returns a new copy of the current stack, preserving the same order and orientations.

5. \***\*eq**(other)\*\*:

   - **Purpose**: This method checks for equality between two `TextbookStack` objects. Two stacks are considered equal if both their order and orientations match.

6. \***\*str**()\*\*:

   - **Purpose**: This method provides a string representation of the stack, which shows its order and orientations.

7. **apply_sequence(stack, sequence)**:
   - **Purpose**: This function is used to apply a sequence of flips to a given stack and returns the resulting stack.
   - The `sequence` is a list of flip positions, and the function creates a copy of the stack, applies the flips in order, and returns the final stack.

---

### Summary of the Files:

- **`main.py`**: Implements the search algorithms (BFS and DFS) to find the sequence of flips needed to sort a stack of textbooks.
- **`textbook_stack.py`**: Defines the `TextbookStack` class, which models the stack of textbooks and provides methods to manipulate and check the stack's state.

## Testing Your Code:

Run this command to test the code:

```
python test.py
```
