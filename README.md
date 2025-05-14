# Number Theoretic Transform (NTT) in Python
# Number Theoretic Transform (NTT) 

This project implements the **Number Theoretic Transform (NTT)** in Python — an analog of the Fast Fourier Transform (FFT) that works over finite fields. The implementation includes both a naive O(n²) algorithm and an efficient **Cooley-Tukey O(n log n)** recursive algorithm, as well as the inverse transform.

## Features

- ✅ Prime modulus selection ensuring the existence of an n-th root of unity
- ✅ Primitive root search
- ✅ Naive NTT (brute-force approach)
- ✅ Fast NTT using Cooley-Tukey divide-and-conquer strategy
- ✅ Inverse NTT using modular inverses
- ✅ Performance comparison with `timeit`

## Usage

1. **Configure input length**:
   Inside the script, set the desired length `N` of your input vector:
   ```python
   N = 8  # Must be a power of two
