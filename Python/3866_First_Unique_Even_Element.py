#3866. First Unique Even Element

class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:

        enique_numbers = {}

        for i in nums:
            if i % 2 == 0 :
                if i in enique_numbers:
                    enique_numbers[i] +=1
                else:
                    enique_numbers[i] = 1

        for i in enique_numbers:
            if enique_numbers[i] == 1 :
                return i
            

        return -1
        
