"""
=== ASSIGNMENT OPERATORS (Operator Penugasan) ===

Operator     Contoh      Sama Dengan
=            a = 10      a = 10
+=           a += 10     a = a + 10
-=           a -= 10     a = a - 10
*=           a *= 10     a = a * 10
/=           a /= 10     a = a / 10
%=           a %= 10     a = a % 10
//=          a //= 10    a = a // 10
**=          a **= 10    a = a ** 10
&=           a &= 10     a = a & 10
|=           a |= 10     a = a | 10
^=           a ^= 10     a = a ^ 10
>>=          a >>= 10    a = a >> 10
<<=          a <<= 10    a = a << 10
"""

print("=== ASSIGNMENT OPERATORS ===")
print()

# = (Assignment)
a = 10
print(f"a = 10       -> a = {a}")

# += (Addition Assignment)
a += 10
print(f"a += 10      -> a = {a}")    # 20

# -= (Subtraction Assignment)
a -= 10
print(f"a -= 10      -> a = {a}")    # 10

# *= (Multiplication Assignment)
a *= 10
print(f"a *= 10      -> a = {a}")    # 100

# /= (Division Assignment)
a /= 10
print(f"a /= 10      -> a = {a}")    # 10.0

# Kembalikan ke integer
a = int(a)

# %= (Modulus Assignment)
a %= 3
print(f"a %= 3       -> a = {a}")    # 1

# Reset
a = 10

# //= (Floor Division Assignment)
a //= 3
print(f"a //= 3      -> a = {a}")    # 3

# Reset
a = 2

# **= (Exponentiation Assignment)
a **= 4
print(f"a **= 4      -> a = {a}")    # 16

print()
print("--- Bitwise Assignment ---")

# &= (Bitwise AND Assignment)
a = 12    # 1100
a &= 10   # 1010 -> 1000 = 8
print(f"a=12; a &= 10  -> a = {a}")

# |= (Bitwise OR Assignment)
a = 12    # 1100
a |= 10   # 1010 -> 1110 = 14
print(f"a=12; a |= 10  -> a = {a}")

# ^= (Bitwise XOR Assignment)
a = 12    # 1100
a ^= 10   # 1010 -> 0110 = 6
print(f"a=12; a ^= 10  -> a = {a}")

# >>= (Right Shift Assignment)
a = 16
a >>= 2   # 10000 -> 100 = 4
print(f"a=16; a >>= 2  -> a = {a}")

# <<= (Left Shift Assignment)
a = 3
a <<= 2   # 11 -> 1100 = 12
print(f"a=3;  a <<= 2  -> a = {a}")

print()

# --- Contoh penggunaan sehari-hari ---
print("=== CONTOH PENGGUNAAN ===")

saldo = 1000000
print(f"Saldo awal: Rp{saldo:,}")

saldo += 500000  # menabung
print(f"Menabung Rp500,000:  Saldo = Rp{saldo:,}")

saldo -= 200000  # belanja
print(f"Belanja Rp200,000:   Saldo = Rp{saldo:,}")

total = 0
for item_harga in [15000, 25000, 10000, 30000]:
    total += item_harga
print(f"Total belanja (15rb + 25rb + 10rb + 30rb) = Rp{total:,}")
