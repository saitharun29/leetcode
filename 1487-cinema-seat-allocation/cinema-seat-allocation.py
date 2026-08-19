class Solution:
    def maxNumberOfFamilies(self, n, reservedSeats):
        rows = {}

        for row, seat in reservedSeats:
            if row not in rows:
                rows[row] = set()
            rows[row].add(seat)

        ans = 2 * n

        for seats in rows.values():
            left = all(i not in seats for i in range(2, 6))
            middle = all(i not in seats for i in range(4, 8))
            right = all(i not in seats for i in range(6, 10))

            if left and right:
                continue
            elif left or middle or right:
                ans -= 1
            else:
                ans -= 2

        return ans     