class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        res = 0
        size_limit = 2 ** 31 // 10
        if x < 0:
            sign = -1 #save the sign
        
        x = x * sign #make it a positive number

        while x > 0:
            digit = x % 10
            #make sure the value is signed 32 bit int
            res += digit  # last digit saved to result

            x = x // 10     # remove last digit from original number
            #make sure the value is signed 32 bit int
            if res > size_limit and x > 0:
                print(size_limit, x)
                return 0
            res *= 10       # multiply by 10 before repeating the loop
        res = res // 10     # reverse the last mult before exiting loop

        return res * sign
