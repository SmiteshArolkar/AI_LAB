from collections import deque

def water_jug_paths(start, goal, capacity):
    visited = set()
    queue = deque([(start, [])])
    result_paths = []

    while queue:
        current_state, current_path = queue.popleft()

        if current_state == goal:
            result_paths.append(current_path + [current_state])

        visited.add(current_state)

        fill_jug1 = (capacity[0], current_state[1])
        if fill_jug1 not in visited:
            queue.append((fill_jug1, current_path + [current_state]))

        fill_jug2 = (current_state[0], capacity[1])
        if fill_jug2 not in visited:
            queue.append((fill_jug2, current_path + [current_state]))

        empty_jug1 = (0, current_state[1])
        if empty_jug1 not in visited:
            queue.append((empty_jug1, current_path + [current_state]))

        empty_jug2 = (current_state[0], 0)
        if empty_jug2 not in visited:
            queue.append((empty_jug2, current_path + [current_state]))

        pour_jug1_to_jug2 = (
            max(0, current_state[0] - (capacity[1] - current_state[1])),
            min(current_state[1] + current_state[0], capacity[1])
        )
        if pour_jug1_to_jug2 not in visited:
            queue.append((pour_jug1_to_jug2, current_path + [current_state]))

        pour_jug2_to_jug1 = (
            min(current_state[0] + current_state[1], capacity[0]),
            max(0, current_state[1] - (capacity[0] - current_state[0]))
        )
        if pour_jug2_to_jug1 not in visited:
            queue.append((pour_jug2_to_jug1, current_path + [current_state]))
            
    return result_paths


a = int(input("Enter the capacity of jug A: "))
b = int(input("Enter the capacity of jug B: "))
target = int(input("Enter the target amount: "))

start_state = (0, 0)
goal_state = (target, 0)
jug_capacities = (a, b)

result_paths = water_jug_paths(start_state,goal_state,jug_capacities)
for path in result_paths:
    print(path)
