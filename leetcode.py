class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """
        We get two strings, we're supposed to add the letters in alt order starting with word 1
        basic idea could be to check which word is longer: 
        loop through the shorter word and then finish with the longer word

        Optimization ideas: 


        """
        first : bool = False 
        output : str = ""
        if len(word1) > len(word2): 
            first = True 

        if first: # word 1 is longer 
            for i in range(len(word2)): 
                output += word1[i]
                output += word2[i]
            
            for j in range(len(word2), len(word1)): 
                output += word1[j]

        
        else: # word2 is longer
            for i in range(len(word1)):
                output += word1[i]
                output += word2[i]

            for j in range(len(word1), len(word2)):
                output += word2[j]
        return output 

    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.

        we use two pointers: ptr1 and ptr2. 

        We 
        """
        ptr1 = m -1 
        ptr2 = n -1 
        p = n + m -1 
        while ptr1 >= 0 and ptr2 >= 0:
            if nums1[ptr1] > nums2[ptr2]:
                nums1[p] = nums1[ptr1]
                ptr1 -= 1
            else: 
                nums1[p] = nums2[ptr2]
                ptr2 -= 1 
            p -= 1 
        while ptr2 >= 0: 
            nums1[p] = nums2[ptr2]
            p -=1
            ptr2 -= 1
        return nums1
sol = Solution()
print(sol.merge([1,2,3,0,0,0],3,[2,5,6], 3 ))
