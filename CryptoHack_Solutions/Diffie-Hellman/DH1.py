def multiplicative_inverse(g, p):
    def extended_gcd(a, b):
        if a == 0:
            return b, 0, 1
        else:
            gcd, x, y = extended_gcd(b % a, a)
            return gcd, y - (b // a) * x, x

    gcd, x, _ = extended_gcd(g, p)
    if gcd == 1:
        return x % p
    else:
        return None

g = 209
p = 991
d = multiplicative_inverse(g, p)
print(d)