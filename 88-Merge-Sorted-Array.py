class Solution:
    """
    You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
    Merge nums1 and nums2 into a single array sorted in non-decreasing order.
    The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
    To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored.
    nums2 has a length of n.
    """

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # this is the pointer used to point to last element of nums1 and
        # we will use this pointer to update nums1
        update_pointer = m + n - 1

        # merge in reverse order
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[update_pointer] = nums1[m - 1]
                m -= -1
            else:
                nums1[update_pointer] = nums2[n - 1]
                n -= 1
            update_pointer -= 1

        # fill nums1 with leftover nums2 elements
        while n > 0:
            nums1[update_pointer] = nums2[n - 1]
            n -= 1
            update_pointer -= 1
