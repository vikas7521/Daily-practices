class Solution:
    def minOperations(self, s: str, k: int) -> int:
        z = s.count('0')

        if z == 0:
            return 0

        m = (z + k - 1) // k   # ceil(z/k)

        while True:
            if (m * k - z) % 2 == 0:
                return m
            m += 1

            # safety condition (rare impossible case)
            if m > z + k:
                return -1
