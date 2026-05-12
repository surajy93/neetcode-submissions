class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(nums, l, m, r):
            left, right = nums[l : m + 1], nums[m + 1 : r + 1]
            i, j, k = l, 0, 0
            # Merge back into nums
            while j < len(left) and k < len(right):
                if left[j] <= right[k]:
                    nums[i] = left[j]
                    j += 1
                else:
                    nums[i] = right[k]
                    k += 1
                i += 1

            while j < len(left):
                nums[i] = left[j]
                j += 1
                i += 1

            while k < len(right):
                nums[i] = right[k]
                k += 1
                i += 1

        def mergeSort(arr, l, r):
            if l >= r:
                return arr
            m = (l + r) // 2
            mergeSort(arr, l, m)
            mergeSort(arr, m + 1, r)
            merge(arr, l, m, r)
            return arr

        mergeSort(nums, 0, len(nums) - 1)
        return nums
