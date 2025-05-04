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
    
    def isValid(self, s : str) -> bool: 
        """
        string containing: (,),{,},[,]
        the string is valid if: 
            - open brackets must be closed by the same type
            - open brackets must be closed in the correct order 
            - 

        solution: 
        - number of brackets needs to be divisible by 2 

        open yes
        next has to be same closed different open 
        otherwise false

        ( { [ ] )}

        rules: 
        if its open it needs to be followed by an open 
        unless its the same type 
        we can create a list or maybe just be smart about a bool 
        a for loop and if output is false then we return false otherwise true?

        """
    def isValid(self, s: str) -> bool:
        open : list = ['(', '{', '[']
        close : list = [')', '}', ']']
        lst : list = []
        if len(s) == 1: 
            return False 
        for char in s:
            if char in open: 
                lst.append(char)
            elif lst and lst[-1] == open[close.index(char)]:  
                lst.pop()
            else:
                return False  
        return True if not lst else False 


    def mergeTwoLists(self, list1, list2):
        # check which is longer 
        # loop through the longer one and remove elements 
        # pop removes the last element so we start backwards loop the other way and pop 
        lst : list = list1 + list2
        return lst.sort()
        

    def numEquivDominoPairs(self, dominoes: list[list[int]]) -> int:
        from collections import Counter 
        cnt = Counter()
        ans = 0

        for a,b in dominoes: 
            if a <= b: 
               key = a,b
            else: 
               key = b, a
            cnt[key] += 1 

        for add in cnt.values(): 
            ans += add * (add - 1) // 2
        return ans  