class Solution:
    def minOperations(self, s: str, k: int) -> int:
        n = len(s)
        zeros = s.count('0')
        
        # We need to flip all zeros to 1
        # Each operation flips exactly k indices
        # If we do 'ops' operations, total flips = ops * k
        # Each index can be flipped multiple times
        # Net effect: index flipped odd times = changed, even times = unchanged
        
        # We need at least ceil(zeros/k) operations
        # But also: ops*k must have same parity as zeros
        # (since we need exactly zeros net flips, rest cancel out in pairs)
        # Also ops*k >= zeros and (ops*k - zeros) must be even (extra flips come in pairs)
        # And ops*k <= n (can't flip more distinct... wait, we CAN reuse indices across ops)
        # Actually each operation picks k DIFFERENT indices (within that operation)
        # but across operations indices can repeat
        
        # So: we need ops such that:
        # 1. ops * k >= zeros (enough total flips)
        # 2. (ops * k - zeros) % 2 == 0 (extra flips pair up)
        # 3. ops * k <= ops * n? No... each op uses k indices from n
        #    The remaining (ops*k - zeros) flips must be on '1's, coming in pairs
        #    So we need (ops*k - zeros) // 2 pairs of extra flips on 1s
        #    These 1s need to be flippable: n - zeros >= ... we need at least 1 non-zero
        #    if extra > 0. Actually we need (ops*k - zeros) extra flips distributed,
        #    but each '1' can absorb at most ops flips (once per operation).
        #    Constraint: we need enough '1's to absorb extra flips.
        #    But more simply: ops*k - zeros extra flips, each '1' can take multiple hits.
        #    The only real constraint is if zeros == n (all zeros), k must divide n... 
        #    Let me think differently.
        
        # Actually the constraints are:
        # - ops * k >= zeros
        # - (ops * k - zeros) % 2 == 0  
        # - If zeros < n: we can always redistribute extra flips on '1's as long as 
        #   we have at least one '1' (n > zeros), OR extra == 0
        # - If zeros == n: ops * k must equal n * m for some... actually if all zeros,
        #   we flip all in first op (if k==n), etc. The constraint is just ops*k >= n
        #   and parity... wait if zeros==n, same rules apply, extra flips go on previously
        #   flipped positions. We just need (ops*k - zeros) % 2 == 0 and ops*k >= zeros
        #   and if extra > 0, we need somewhere to put them: need k <= n always true,
        #   and if extra > 0, n - zeros... hmm if zeros == n, extra flips must go on 
        #   already-ones. After first batch, some are 1. It gets complex.
        #   
        # Simpler: extra = ops*k - zeros must be even and >= 0, AND
        # if extra > 0 then (n - zeros) >= 1 OR we can use already-flipped positions
        # Actually if extra > 0, we need at least one position that's currently '1' 
        # to flip twice (cancel). If zeros == n, impossible unless extra == 0.
        # If zeros == n and extra > 0: impossible.
        
        ones = n - zeros
        
        for ops in range(1, 2 * n + 1):
            total = ops * k
            if total < zeros:
                continue
            extra = total - zeros
            if extra % 2 != 0:
                continue
            if extra > 0 and ones == 0:
                continue
            return ops
        
        return -1
