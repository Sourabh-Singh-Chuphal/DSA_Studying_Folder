class Solution:
    def countOddDigit(self, n):
        if n == 0:
            return 0

        count = 0
        while n > 0:
            m = n % 10
            if (m % 2 != 0):
                count += 1
            n = n // 10
        return count     

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    solution = Solution()
    odd_digit_count = solution.countOddDigit(n)
    print(f"The number of odd digits in {n} is: {odd_digit_count}")