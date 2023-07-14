#from itertools import permutations
class Solution:
    def countAnagrams(self, s: str) -> int:
        mod= 10**9 + 7
        #splitting the words of string s in list w
        w=s.split(" ")
        a=[]
        #then iterating the words in list and appending the permutation of the word to list a
        for i in w:
            a.append(Solution.perm(i))
        #multiplying the elements of list to return the total count of Anagrams
        result = 1
        for num in a:
            result *= num
        return result % mod

    #function to calculate the permutation of a given string 
    def perm(inputt):
        char_counts = Counter(inputt)
        total_permutations = factorial(len(inputt))
        denominator = 1
        for i in char_counts.values():
            denominator *= factorial(i)
        return total_permutations // denominator
