#
# Fibonacci 
#

class Fibo:
    
    def fib(self, n): #재귀
        if n <= 1:
            return n
        else:
            return (self.fib(n-1) + self.fib(n-2))

    def fib_memo(self, n): #DP 1
        a, b = 1, 0
        for i in range(n):
            a, b = b, a + b
        return b

    def fib_memo_2(self, n): #DP 2
        c = [0 for i in range(n+1)]
        c[0] = 0
        c[1] = 1

        for i in range(2, n+1):
            c[i] = c[i-1] + c[i-2]
        
        return c[n]
    
if __name__ == '__main__':
    f = Fibo()

    print(f.fib(10))
    print(f.fib_memo(10))
    print(f.fib_memo_2(10))