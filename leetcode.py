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

        we use two pointers: i and j. 

        We start from the back and sort the biggest number using indexes or "pointers" 
        """
        i = m -1 
        j = n -1 
        p = n + m -1 
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[p] = nums1[i]
                i -= 1
            else: 
                nums1[p] = nums2[j]
                j -= 1 
            p -= 1 
        while j >= 0: 
            nums1[p] = nums2[j]
            p -=1
            j -= 1
    