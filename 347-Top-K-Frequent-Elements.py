class Solution:
    """
    Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

    Best Case - 
    Time complexity of O(nlogn) as we have to traverse the given array atleast once and sort it for freq
    
    Soln 1 - 
    Use collections.counter and return most_common. This returns a list of most common tuples as (element, frequency). 
    We can use zip to convert them to list of most common elements
    We can also use a for loop to get list 
    
    Soln 2 -
    Use Modified Bucket Sort. Create dict with k=element and v=freq of element. Create a freq_array with len(input_array) 
    where index of array is the freq of the element and values in the array are the list of elements. 
    Use the dict to list all the items and use those tuples to populate the freq_array.
    This freq_array will have elements sorted based on freq with most freq element in highest index value
    We scan this freq_array from highest to lowest index and return when we have k elements in result array
    
    """
    def topKFrequent_soln1(self, nums: List[int], k: int) -> List[int]:
        import collections
        most_freq_k_tuples = collections.Counter(nums).most_common(k)
        return [x for x, y in most_freq_k_tuples]
        # return list(zip(*most_freq_k_tuples))[0]
    
    def topKFrequent_soln2(self, nums: List[int], k: int) -> List[int]:
        count_dict = {}
        freq = [[] for i in range(len(nums)+1)]
        
        # Create dict with k=element and v=freq of element
        for num in nums:
            count_dict[num] = 1 + count_dict.get(num, 0)
        # Add to the freq array 
        for num, count in count_dict.items():
            freq[count].append(num)
        
        res =[]
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        
            