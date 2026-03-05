class Solution:
    def subarraysXor(self, arr, k):
        freq = {}
        xr = 0
        count = 0
        
        for num in arr:
            xr ^= num
            
            if xr == k:
                count += 1
            
            if xr ^ k in freq:
                count += freq[xr ^ k]
            
            freq[xr] = freq.get(xr, 0) + 1
        
        return count
