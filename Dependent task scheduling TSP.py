from collections import deque, defaultdict

def minimumTime(n, relations, time):
    # Step 1: Build the graph and in-degree array
    graph = defaultdict(list)
    in_degree = [0] * n
    for prev, next_ in relations:
        graph[prev - 1].append(next_ - 1)
        in_degree[next_ - 1] = in_degree[next_ - 1] + 1

    # Step 2: Initialize a queue for cities with no prerequisites
    queue = deque()
    dp = [0] * n  # dp[i] will store the minimum time to complete task at city i
    for i in range(n):
        if in_degree[i] == 0:
            queue.append(i)
            dp[i] = time[i]  # The time to complete a task with no prerequisites is just its duration

    # Step 3: Process tasks in topological order
    while queue:
        curr = queue.popleft()
        for neighbor in graph[curr]:
            # Update the dp value for the neighbor task
            dp[neighbor] = max(dp[neighbor], dp[curr] + time[neighbor])
            
            # Decrease the in-degree and add to the queue if it becomes 0
            in_degree[neighbor] = in_degree[neighbor] - 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Step 4: Return the maximum time from dp, which gives the total time to complete all tasks
    return max(dp)

# Example usage:
n = 3
relations = [[1, 3], [3, 2]]
time = [3, 5, 2]
print("Minimum time taken to finish all the tasks : ",minimumTime(n, relations, time))  # Output: 10

n = 3
relations = [[1, 3], [2, 3]]
time = [3, 2, 5]
print("Minimum time taken to finish all the tasks : ",minimumTime(n, relations, time))  # Output: 8

