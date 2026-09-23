class Solution:
    def isPalindrome(self, n) -> bool:
        if n < 0:
            return False
        reversed_num = 0
        original = n

        while n > 0:
            reversed_num = (reversed_num * 10) + (n % 10 )
            n = n // 10
        return original == reversed_num

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    solution = Solution()
    if solution.isPalindrome(n):
        print(f"{n} is a palindrome.")
    else:
        print(f"{n} is not a palindrome.")