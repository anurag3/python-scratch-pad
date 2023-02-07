class Solution:
    """
    Given an array of strings strs, group the anagrams together. You can return the answer in any order.
    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
    
    Best Case - 
    Time complexity is O(n*m). It will be O(n) since we have to traverse through all the elements of the string atleast once 
    to determine its an anagram and O(m) again since we have to traverse through the array of strings to group them.
    
    Soln 1 -
    Build hashmap where key=sorted_word and value=list of anagram words and then return values
    Sorting will be O(nlogn) and we would have to do it for m words so O(m)
    Time complexity is O(m*nlogn) and Space Complexity is O(m*n)
    
    Soln 2 -
    To improve on the sorting time we are going to skip sorting and we track occurance of each letter in an array
    We build this array of zeros from "a" to "z", we will be adding 1 for every occurance of character in the word. 
    To update every occurance correctly we will be updating based on the ASCII value of the character.
    To get the ASCII value between 0 to 25 we will subtract every char from ASCII value of "a". 
    (ASCII("a")- ASCII("a"))=0 
    (ASCII("b")- ASCII("a"))=1
    This array will be the key for hashmap and its value will be all the words that match the character frequency in the array.
    This is similar to how we used the sorted words as key in prev solution.
    Time complexity is O(m) for number of words we process, O(n) for length of word and O(26) for building character occurance array for every word
    Time complexity will be O(m*n*26) -> O(m*n)
    """
    def groupAnagrams_soln1(self, strs: List[str]) -> List[List[str]]:
        d = collections.defaultdict(list)
        for word in strs:
            key = ''.join(sorted(word))
            d[key].append(word)
        return d.values()
    
    def groupAnagrams_soln2(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        result = defaultdict(list) # Mapping character count to list of Anagrams
        
        for word in strs:
            count = [0] * 26 # Creating an array of zeros from a to z
            
            for char in word:
                # In order to map "a" to 0 and "z" to 25 we are going to subtract ASCII value of current char from ASCII value of "a"
                # Now we increment the value of current key (char) by 1 
                count[ord(char)- ord("a")] += 1
            #  we are converting char from list ot tuple since list can't be keys since lists are mutable and tuples are imutable 
            result[tuple(count)].append(word)
        
        return result.values()