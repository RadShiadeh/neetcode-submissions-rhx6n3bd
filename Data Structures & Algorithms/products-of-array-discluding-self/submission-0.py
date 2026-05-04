class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_counts = 0
        prods = 1

        for n in nums:
            if n == 0:
                zero_counts += 1
                continue
            prods *= n
        
        res = []
        if zero_counts > 1:
            res = [0] * len(nums)
            return res
        for n in nums:
            if zero_counts:
                if n != 0:
                    res.append(0)
                else:
                    res.append(int(prods))
            else:
                val = prods//n
                res.append(val)
        
        return res