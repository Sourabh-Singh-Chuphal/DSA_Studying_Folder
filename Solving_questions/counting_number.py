class Solution:
    def countDigit(self, n):
        
        if n == 0:
            return 1

        count = 0
        while n > 0:
            n = n // 10
            count += 1

        return count    

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    solution = Solution()
    digit_count = solution.countDigit(n)
    print(f"The number of digits in {n} is: {digit_count}")