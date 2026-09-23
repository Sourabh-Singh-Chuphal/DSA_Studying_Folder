class Solution:
    def reverseNumber(self, n):
        reverseNumber = 0
        while n > 0:
            reverseNumber = (reverseNumber * 10 ) + (n % 10)
            n = n // 10
        
        return reverseNumber


class Solution_1:
    def reverseNumber_2(self, n):
        return int(str(n)[::-1])

if __name__ == "__main__":
        n = int(input("Enter a number: "))
        solution = Solution()
        reversed_number = solution.reverseNumber(n)
        print(f"The reverse of {n} is: {reversed_number}")

        n = int(input("Enter a number: "))
        solution_1 = Solution_1()
        reversed_number_1 = solution_1.reverseNumber_2(n)
        print(f"The reverse of 2 class {n} is: {reversed_number_1}")


