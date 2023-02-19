import math


class Solution:
    """
    Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas.
    The guards have gone and will come back in h hours.

    Koko can decide her bananas-per-hour eating speed of k.
    Each hour, she chooses some pile of bananas and eats k bananas from that pile.
    If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

    Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

    Return the minimum integer k such that she can eat all the bananas within h hours.
    """

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        leftPointer, rightPointer = 1, max(piles)
        result = rightPointer

        while leftPointer <= rightPointer:
            k = (leftPointer + rightPointer) // 2
            hours = 0
            for pile in piles:
                # computing total hours needed to finish all the piles with the current `k`
                hours += math.ceil(pile / k)

            # if hours taken to finish the piles is less than `h` then we can update
            # current result to `k` as we know that we can finish the piles at `k` speed
            if hours <= h:
                result = min(k, result)
                # now we can try to see if there is any value lower than `k`
                rightPointer = k - 1
            else:
                leftPointer = k + 1

        return result
