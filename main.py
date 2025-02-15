from collections import deque

def breadth_first_search(stack):
    visited = set()
    queue = deque([(stack, [])])  # Store (current stack, sequence of flips)

    while queue:
        current_stack, flip_sequence = queue.popleft()

        # If stack is sorted, return the sequence of flips
        if current_stack.check_ordered():
            return flip_sequence

        # Try all possible flips
        for i in range(1, current_stack.num_books + 1):
            new_stack = current_stack.copy()
            new_stack.flip_stack(i)
            stack_tuple = (tuple(new_stack.order), tuple(new_stack.orientations))

            if stack_tuple not in visited:
                visited.add(stack_tuple)
                queue.append((new_stack, flip_sequence + [i]))

    return []  # No solution found


def depth_first_search(stack):
    visited = set()  # Track visited stack configurations
    stack_list = [(stack, [])]  # Store (current stack, sequence of flips)

    while stack_list:
        current_stack, flip_sequence = stack_list.pop()

        # Check if the current stack is ordered
        if current_stack.check_ordered():
            return flip_sequence  # Return the sequence of flips that sorted the stack

        # Try all possible flips
        for i in range(1, current_stack.num_books + 1):
            new_stack = current_stack.copy()  # Make a copy of the current stack
            new_stack.flip_stack(i)  # Apply the flip

            # Create a tuple to represent the state (order and orientations)
            stack_tuple = (tuple(new_stack.order), tuple(new_stack.orientations))

            # Only explore the new state if it has not been visited
            if stack_tuple not in visited:
                visited.add(stack_tuple)  # Mark the state as visited
                stack_list.append((new_stack, flip_sequence + [i]))  # Add new state and flip sequence

    return []  # No solution found if the loop ends
