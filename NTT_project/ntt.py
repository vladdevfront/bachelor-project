from typing import List
import timeit
import random

#KONTROLA HODNOTY NA PRVOCISLO
def is_prime(p: int) -> bool:
    if p <= 1: return False
    if p <= 3: return True
    if p % 2 == 0 or p % 3 == 0: return False
    i = 5
    while i * i <= p:
        if p % i == 0 or p % (i + 2) == 0:
            return False
        i += 6
    return True
  
#VYBER MODULA
def choose_modulus(n: int) -> int:
    k = 1
    while True:
        p = n * k + 1
        if is_prime(p):
            return p
        k += 1

def is_primitive_root(omega, n, p):
    for k in range(1, n):
        if pow(omega, k, p) == 1:
            return False
    return pow(omega, n, p) == 1
  
#HLADANIE PRIMITVNEHO KORENA
def find_omega(n, p):
    required_order = (p - 1) // n
    for g in range(2, p):
        omega = pow(g, required_order, p)
        if is_primitive_root(omega, n, p):
            return omega
    raise Exception("No primitive root found")

#ALGORITMUS S ALGORITMICKOU ZLOZITOSTOU O(n^2)
def naive_ntt(a: List[int], omega: int, modulus: int) -> List[int]:
    n = len(a)
    out = [0] * n
    for i in range(n):
        for j in range(n):
            power = pow(omega, i * j, modulus)
            out[i] = (out[i] + a[j] * power) % modulus
    return out

#ALGORITMUS S ALGORITMICKOU ZLOZITOSTOU O(n log n)
def cooley_tukey_ntt(a: List[int], omega: int, modulus: int) -> List[int]:
    n = len(a)
    if n == 1:
        return a[:]
    
    omega_squared = pow(omega, 2, modulus)
    even = cooley_tukey_ntt(a[::2], omega_squared, modulus)
    odd = cooley_tukey_ntt(a[1::2], omega_squared, modulus)

    factor = 1
    out = [0] * n
    for i in range(n // 2):
        temp = (factor * odd[i]) % modulus
        out[i] = (even[i] + temp) % modulus
        out[i + n // 2] = (even[i] - temp) % modulus
        factor = (factor * omega) % modulus
    return out
  
#INVERZNA VERZIA NTT COOLEY-TUKEY
def inverse_ntt(a, omega, modulus):
    n = len(a)
    omega_inv = pow(omega, -1, modulus)
    raw = cooley_tukey_ntt(a, omega_inv, modulus)
    n_inv = pow(n, -1, modulus)
    return [(x * n_inv) % modulus for x in raw]


# ==== RUN ====
# N - DLZKA VEKTORA(POLYNOMU)
N = 4  

MODULUS = choose_modulus(N)
VECTOR = [random.randint(0, MODULUS - 1) for _ in range(N)]

omega = find_omega(N, MODULUS)
print("ω =", omega)
print("modulus =", MODULUS)
naive_result = naive_ntt(VECTOR, omega, MODULUS)
ct_result = cooley_tukey_ntt(VECTOR, omega, MODULUS)
print("Input vector:",VECTOR)
print("Naive NTT result:       ", naive_result)
print("Cooley-Tukey NTT result:", ct_result)
print("Equal?                  ", naive_result == ct_result)



print("\nCasova dlžka výpočtu:")
print("Naive NTT:", timeit.timeit(lambda: naive_ntt(VECTOR,omega,MODULUS), number=100))
print("Cooley-Tukey NTT:", timeit.timeit(lambda: cooley_tukey_ntt(VECTOR,omega,MODULUS), number=100))




res = inverse_ntt(ct_result, omega, MODULUS)
print("INV Cooley-Tukey NTT:", res)

