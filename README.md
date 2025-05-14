# Number Theoretic Transform (NTT) in Python

This project implements the **Number Theoretic Transform (NTT)** and its inverse in Python, using both a **naive O(n²)** method and the optimized **Cooley-Tukey O(n log n)** algorithm. It also includes utility functions to find a suitable prime modulus and a primitive root of unity.

---

## 📘 What is NTT?

NTT is the modular arithmetic counterpart of the Fast Fourier Transform (FFT). It's commonly used for **fast polynomial multiplication** in fields such as:

- Cryptography (e.g. lattice-based schemes)
- Signal processing in modular arithmetic
- Competitive programming for large integer convolutions

Instead of working with complex numbers like FFT, NTT operates entirely in finite fields defined by a prime modulus.

---

## 📂 Project Structure

- `is_prime(p)`  
  Checks if a given number `p` is a prime number.

- `choose_modulus(n)`  
  Finds a prime modulus of the form `p = k * n + 1` that works with an NTT of size `n`.

- `is_primitive_root(omega, n, p)`  
  Validates that `omega` is an n-th primitive root of unity modulo `p`.

- `find_omega(n, p)`  
  Finds an appropriate primitive root of unity for a given `n` and `p`.

- `naive_ntt(a, omega, modulus)`  
  Computes the NTT of vector `a` using the naive O(n²) algorithm.

- `cooley_tukey_ntt(a, omega, modulus)`  
  Efficient implementation of NTT using the Cooley-Tukey divide-and-conquer method.

- `inverse_ntt(a, omega, modulus)`  
  Computes the inverse NTT (used to recover the original polynomial from its transformed form).

---

## ▶️ Example Run

This script runs a demonstration with:

- A random input vector `a` of length `N = 8`
- Automatically selected modulus `p`
- Automatically found primitive root `ω`
- Comparison of naive and fast NTT results
- Timing benchmark
- Inverse NTT verification

**Sample Output:**

```
ω = 8
modulus = 97
Input vector: [73, 45, 30, 21, 46, 89, 64, 12]
Naive NTT result:        [...]
Cooley-Tukey NTT result: [...]
Equal?                   True

Execution time:
Naive NTT:        0.0102 seconds
Cooley-Tukey NTT: 0.0013 seconds

INV Cooley-Tukey NTT: [73, 45, 30, 21, 46, 89, 64, 12]
```

---

## 🧪 Dependencies

No external dependencies are required. This project runs on standard Python 3.

---

## 🚀 How to Run

1. Save the code to a Python file, e.g., `ntt_demo.py`.
2. Run it with:

```bash
python ntt_demo.py
```

---

## 📈 Performance

- **Naive NTT:** O(n²) — slower, educational purpose
- **Cooley-Tukey NTT:** O(n log n) — recommended for large input sizes

---

## 🛠️ Applications

- Polynomial multiplication in cryptography (e.g., NTRU, RLWE)
- Error-correcting codes
- Fast convolution in modular arithmetic settings



