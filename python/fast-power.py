class Solution:
    """
    @param a, b, n: 32bit integers
    @return: An integer
    """
    # (X*Y) mod P = (X*(Y mod P)) mod P = ((X mod P)*(Y mod P)) mod P
    # (X^N) mod P = (X mod P)^N mod P

    # square first and then recursion
    # even:
    #   f(n) = a^n % b = (a^2)^(n/2) % b
    #        = (a^2 % b)^(n/2) % b
    #        = f(a^2 % b,b,n/2)
    #        = 1*f(a^2 % b,b,n/2) % b
    # odd:
    #   f(n) = a^n % b = a*(a^2)^(n/2) % b
    #        = a*((a^2)^(n/2) % b) % b
    #        = a*((a^2 % b)^(n/2) % b) % b
    #        = a*f(a^2 % b,b,n/2) % b
    def fastPower2(self, a, b, n):
        if n == 0:
            return 1 % b
        product = self.fastPower(a * a % b, b, n / 2)
        return (a if n % 2 else 1) * product % b

    # bottom-up
    # doubling trick
    # odd:
    #   f(n) = a^n % b = a*(a^2)^(n/2) % b
    #        = a*((a^2)^(n/2) % b) % b
    #        = a*((a^2 % b)^(n/2) % b) % b
    #        = a*f(a^2 % b,b,n/2) % b
    #        = (a % b) * (f(a^2 % b,b,n/2) % b) % b
    #        = (a % b) * f(a^2 % b,b,n/2) % b
    def fastPower(self, a, b, n):
        ans = 1
        while n > 0:
            ans = ans * (a if n % 2 else 1) % b
            a = a * a % b
            n /= 2
        return ans % b

    # recursion first and then square
    # even:
    #   f(a,b,n) = a^n % b = a^(n/2)*a^(n/2) % b
    #        = (a^(n/2) % b)*(a^(n/2) % b) % b
    #        = f(a,b,n/2)*f(a,b,n/2) % b
    # odd:
    #   f(a,b,n) = a^n % b = a*a^(n/2)*a^(n/2) % b
    #        = a*(a^(n/2) % b)*(a^(n/2) % b) % b
    #        = a*f(a,b,n/2)*f(a,b,n/2) % b
    #        = a*(  f(a,b,n/2)*f(a,b,n/2) % b  ) % b
    def fastPower1(self, a, b, n):
        if n == 0:
            return 1 % b
        product = self.fastPower(a, b, n / 2)
        product = (product * product) % b
        if n % 2 == 1:
            product = (a * product) % b
        return product




