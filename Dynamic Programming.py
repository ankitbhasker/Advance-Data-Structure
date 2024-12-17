import math
class BranchAndBoundTSP:
    def tsp_dp(graph):
        n = len(graph)
        dp = [[None] * (1 << n) for _ in range(n)]

        def solve(pos, mask):
            if mask == (1 << n) - 1:
                return graph[pos][0] or float("inf")
            if dp[pos][mask] is not None:
                return dp[pos][mask]
        
            ans = float("inf")
            for city in range(n):
                if mask & (1 << city) == 0 and graph[pos][city] != 0:
                    ans = min(ans, graph[pos][city] + solve(city, mask | (1 << city)))
            dp[pos][mask] = ans
            return ans

        min_cost = solve(0, 1)
        return min_cost

# Example usage
print("Dynamic Programming Solution:", tsp_dp(graph))

    
    
