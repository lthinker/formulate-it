class primeIterator:
    '''
        Iterator that generates prime numbers on the fly!
        :D
    '''

    def __init__(self):
        # Creates the prime list
        self.primes_list = [2, 3]
        self.counter = 0

    def __iter__(self):
        # Set the first prime candidate
        self.prime_candidate = self.primes_list[-1] + 2
        return self

    def __next__(self):
        # Return the first two primes
        if self.counter < 2:
            self.counter = self.counter + 1
            return self.primes_list[self.counter-1]

        while True:
            for p in self.primes_list[1:]:
                # Is it divisible by p?
                if self.prime_candidate % p == 0:
                    break;

            # Have we exhausted the primes list? and haven't we found \\
            # any number which can devide our prime candidate?
            # Therefore we've found a new prime number
            if self.prime_candidate % p != 0:
                self.primes_list.append(self.prime_candidate)
                return self.prime_candidate

            # Generate a new prime candidate
            self.prime_candidate = self.prime_candidate + 2

    # Return primes list
    def primeList(self):
        return self.primes_list

def is_palindromic(number):
    '''
        Syntax: is_palindromic(arg1)

        Returns True if arg1 is a palindromic number.
    '''

    number = str(number)

    if number == number[::-1]:
        return True
    else:
        return False

def primeFact(number):
    '''
        Syntax: prime_fact(arg)

        If the arg is a composed number returns the factorization within a dictionary.
        Otherwise if the number is prime, then it returns the number itself.
    '''
    # The argument must be an integer.
    if not type(number) is int:
        print('Number must be an integer.')
        return None

    # If the integer is negative gets its absolute number.
    number = abs(number)

    # Number must not be zero and It must be > |1|.
    if number == 0 or number == 1:
        return None

    primes_baby = primeIterator()

    factors_dic = dict()

    for factor_candidate in primes_baby:
        # Gets the next prime number
        # Checks if our number is divisible for the last retreived prime
        if number % factor_candidate == 0:
            factors_dic[factor_candidate] = 0
            # Hm, It is, bitch! Therefore, let's see how many times it is divisible
            while number % factor_candidate == 0:
                number = number / factor_candidate
                factors_dic[factor_candidate] = factors_dic[factor_candidate] + 1

        # Have we finished our factorization?
        if number == 1:
            return factors_dic

if __name__ == "__main__":
    print('Never gonna give... you... up!')
    n = int(input('Type a number to see its factorization --> '))

    print(prime_fact(n))
    print(is_palindromic(90066019))