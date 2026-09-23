class Solution:
    def largestDigit(self, n):
        largestDigit = 0
        while n > 0:
            num = n % 10 
            if num > largestDigit:
                largestDigit = num
            
            n = n // 10
        return largestDigit

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    solution = Solution()
    largest_digit = solution.largestDigit(n)
    print(f"The largest digit in {n} is: {largest_digit}")