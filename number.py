import re


class Number:
    def __init__(self, value: int):
        self.value = value


    def get_number(self):
        """
        Returns the number.

        returns: int
        """
        return self.value

    def is_odd(self):
        """
        Returns True if the number is odd, otherwise False.

        returns: bool

        """
        return self.value % 2 !=0

    def is_even(self):
        """
        Returns True if the number is even, otherwise False. 

        returns: bool
        """
        return self.value % 2 ==0

    def is_prime(self):
        """
        Returns True if the number is prime, otherwise False.

        returns: bool
        """
        p = self.value
        c = 0
        for i in range(2, p // 2 + 1):
            if p % 2 == 0:
                c += 1
        return c == 0

    def get_divisors(self):
        """
        Returns a list of all the divisors of the number.

        returns: list
        """
        n = self.value
        return [d for d in range(1, n) if not n % d]

    def get_length(self):
        """
        Returns the number of digits in the number.

        returns: int
        """
        return len(str(self.value))

    def get_sum(self):
        """
        Returns the sum of all the digits in the number.

        returns: int
        """
        p = str(self.value)
        sum = 0
        for i in p:
            sum += int(i)
        return sum


    def get_reverse(self):
        """
        Returns the number in reverse.

        returns: int
        """
        p = str(self.value)
        return int(p[::-1])

    def is_palindrome(self):
        """
        Returns True if the number is a palindrome, otherwise False.

        returns: bool
        """
        p = str(self.value)
        l = len(p)
        if l % 2:
            return p[:l//2] == p[:l//2:-1]
        else:
            return p[:l//2] == p[:l//2-1:-1]

    def get_digits(self):
        """
        Returns a list of all the digits in the number.

        returns: list
        """
        p = str(self.value)
        return [int(i) for i in p]

    def get_max(self):
        """
        Returns the largest digit in the number.

        returns: int
        """
        p = str(self.value)
        m = 0
        for i in p:
            if m <= int(i):
                m = int(i)
        return m

    def get_min(self):
        """
        Returns the smallest digit in the number.

        returns: int
        """
        p = str(self.value)
        m = 0
        for i in p:
            if m >= int(i):
                m = int(i)
        return m

    def get_average(self):
        """
        Returns the average of all the digits in the number.

        returns: float
        """
        p = str(self.value)
        sum = 0
        for i in p:
            sum += int(i)
        return sum / len(p)

    def get_median(self):
        """
        Returns the median of all the digits in the number.

        returns: float
        """
        med = 0
        p = list(str(self.value))
        l = len(p)
        if l % 2:
            return float(p[l // 2])
        else:
            return (int(p[l//2-1])+int(p[l//2]))/2        

    def get_range(self):
        """
        Returns the range of all the digits in the number.

        returns: list
        """
        

    def get_frequency(self):
        """
        Returns a dictionary of the frequency of each digit in the number.

        returns: dict
        """
        s = str(self.value)
        l = [int(i) for i in s]
        return {i:l[i] for i in range(1,len(l))}
    

# Create a new instance of Number
number = Number(3)
