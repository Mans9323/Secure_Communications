from Crypto.Util.number import inverse, long_to_bytes
from functools import reduce
from gmpy2 import iroot
from itertools import combinations

moduli = []
ciphertexts = []
with open("output_0ef6d6343784e59e2f44f61d2d29896f.txt") as file:
    for line in file:
        if line.strip() == '':
            continue
        if "n" in line:
            moduli.append(int(line[4:])) #get moduli
        elif "c" in line:
            ciphertexts.append(int(line[4:])) #get ciphertexts

def hastad_attack(ciphertexts, moduli):
	N = reduce(lambda x, y: x*y, moduli) # N = n1*n2*n3*n4*n5*n6*n7
	Mi = [N//moduli[i] for i in range(len(moduli))]
	Mi_inv = [ inverse(Mi[i],moduli[i]) for i in range(len(moduli))]
	c = sum(ciphertexts[i] * Mi[i] * Mi_inv[i] for i in range(len(ciphertexts))) % N # unique solution x % N according to CRT 
	return c

def solve(e=3):
	for comb_moduli in combinations(moduli, e):
		for comb_ciphertexts in combinations(ciphertexts, e):
			m, bool = iroot(hastad_attack(comb_ciphertexts,comb_moduli),e) #m = c^(1/e) [N] = c ^(1/e)
			if bool:
				return(m) 

m = solve(); print(long_to_bytes(m))