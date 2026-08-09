class Solution:
    def stoneGameII(self, piles):
        n = len(piles)

        # suffix[i] = sum of piles[i:]
        suffix = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for M in range(1, n + 1):

                # If we can take all remaining piles
                if 2 * M >= n - i:
                    dp[i][M] = suffix[i]
                    continue

                best = 0

                for X in range(1, 2 * M + 1):
                    next_M = max(M, X)

                    current = suffix[i] - dp[i + X][next_M]
                    best = max(best, current)

                dp[i][M] = best

        return dp[0][1]