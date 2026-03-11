"""
=== BITWISE OPERATORS (Operator Bitwise) ===

Operator bitwise bekerja pada level bit (binary) dari bilangan.
"""

a = 12   # binary: 1100
b = 10   # binary: 1010

print("=== BITWISE OPERATORS ===")
print(f"a = {a} (binary: {bin(a)})")
print(f"b = {b} (binary: {bin(b)})")
print()

# AND (&) - bit 1 jika kedua bit 1
hasil_and = a & b    # 1100 & 1010 = 1000 = 8
print(f"a & b  = {hasil_and}  (binary: {bin(hasil_and)})")

# OR (|) - bit 1 jika salah satu bit 1
hasil_or = a | b     # 1100 | 1010 = 1110 = 14
print(f"a | b  = {hasil_or}  (binary: {bin(hasil_or)})")

# XOR (^) - bit 1 jika hanya salah satu bit 1
hasil_xor = a ^ b    # 1100 ^ 1010 = 0110 = 6
print(f"a ^ b  = {hasil_xor}   (binary: {bin(hasil_xor)})")

# NOT (~) - membalik semua bit
hasil_not = ~a        # ~1100 = ...0011 = -13
print(f"~a     = {hasil_not}  (binary: {bin(hasil_not)})")

# Left Shift (<<) - geser bit ke kiri
hasil_left = a << 2  # 1100 << 2 = 110000 = 48
print(f"a << 2 = {hasil_left}  (binary: {bin(hasil_left)})")

# Right Shift (>>) - geser bit ke kanan
hasil_right = a >> 2  # 1100 >> 2 = 11 = 3
print(f"a >> 2 = {hasil_right}   (binary: {bin(hasil_right)})")

print()

# --- Visualisasi operasi bitwise ---
print("=== VISUALISASI ===")
print(f"  a     = {a:>4d} = {a:04b}")
print(f"  b     = {b:>4d} = {b:04b}")
print(f"  a & b = {a & b:>4d} = {a & b:04b}  (AND)")
print(f"  a | b = {a | b:>4d} = {a | b:04b}  (OR)")
print(f"  a ^ b = {a ^ b:>4d} = {a ^ b:04b}  (XOR)")
