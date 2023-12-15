# 指定した素数リストを作成するクラス、メソッドを作成
# 個数が1以下の場合は空のリスト作成してください。クラス名はPrimeNumber  メソッドはgenerate(number)
# 以下は、指定された素数リストを作成するPrimeNumberクラスの実装例です。
# generate(number)メソッドは、与えられた数以下の素数をすべて格納したリストを返します。
# この実装では、is_prime(n)メソッドを使って、指定された数が素数かどうかを判定しています。
# is_prime(n)メソッドは、渡された数が1以下の場合はFalseを返します。
# 渡された数が2以上の場合は、2から平方根までのすべての数で割り切れるかどうかを判定しています。
# 割り切れる場合はFalseを返します。すべての数で割り切れない場合は、素数と判定してTrueを返します。
# generate(number)メソッドは、指定された数以下の素数をすべて格納したリストを返します。
# 個数が1以下の場合は空のリストを返します。
# generate(number)メソッドでは、2から指定された数までのすべての数について、
# is_prime(n)メソッドを呼び出し、素数の場合はリストに追加しています。最終的に、素数リストを返しています。
class PrimeNumber:
    @staticmethod
    def is_prime(n):
        """Check if a number is prime"""
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    @staticmethod
    def generate(number):
        """Generate prime numbers up to the given number"""
        primes = []
        if number > 1:
            for i in range(2, number+1):
                if PrimeNumber.is_prime(i):
                    primes.append(i)
        return primes