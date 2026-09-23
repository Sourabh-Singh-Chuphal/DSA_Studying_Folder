class Solution:
    def sum(self,arr, n): 
        return sum(arr)

if __name__ == "__main__":
    n = int(input("Enter the number of elements in the array: "))
    arr = []
    for i in range(n):
        element = int(input(f"Enter element {i + 1}: "))
        arr.append(element)

    solution = Solution()
    total_sum = solution.sum(arr, n)
    print(f"The sum of the array is: {total_sum}")