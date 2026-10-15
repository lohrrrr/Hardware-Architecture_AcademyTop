def truth_table(expression):
    print("a b c f")
    for a in [0, 1]:
        for b in [0, 1]:
            for c in [0, 1]:
                f = expression(a, b, c)
                print(f"{a} {b} {c} {int(f)}")


# ¬(A ∧ B) ∨ ¬(A ∨ C)
truth_table(lambda a, b, c: (not (a and b)) or (not (a or c)))
print(f"\n")

# Вывод
# a b c f
# 0 0 0 1
# 0 0 1 1
# 0 1 0 1
# 0 1 1 1
# 1 0 0 1
# 1 0 1 1
# 1 1 0 0
# 1 1 1 0

# (A ∧ B) ∨ (¬B ∧ C)
truth_table(lambda a, b, c: (a and b) or ((not b) and c))
print(f"\n")

# Вывод
# a b c f
# 0 0 0 0
# 0 0 1 1
# 0 1 0 0
# 0 1 1 0
# 1 0 0 0
# 1 0 1 1
# 1 1 0 1
# 1 1 1 1

# (A ∧ B) ∨ ¬C
truth_table(lambda a, b, c: ((a and b) or not c))
print(f"\n")
# Вывод
# a b c f
# 0 0 0 1
# 0 0 1 0
# 0 1 0 1
# 0 1 1 0
# 1 0 0 1
# 1 0 1 0
# 1 1 0 1
# 1 1 1 1

# Мини-эксперимент с числами и побитовыми операциями
a = 12  # 00001100
b = 10  # 00001010


def show_operation(name, value):
    print(f"{name:<8} = {value:3} = {value:08b}")


print("Числа и битовые операции:")
show_operation("a", a)
show_operation("b", b)
show_operation("a & b", a & b)
show_operation("a | b", a | b)
show_operation("a ^ b", a ^ b)
show_operation("~a", ~a & 0xFF)
show_operation("a << 1", a << 1)
show_operation("a >> 1", a >> 1)

# Вывод
# Числа и битовые операции:
# a        =  12 = 00001100
# b        =  10 = 00001010
# a & b    =   8 = 00001000
# a | b    =  14 = 00001110
# a ^ b    =   6 = 00000110
# ~a       = 243 = 11110011
# a << 1   =  24 = 00011000
# a >> 1   =   6 = 00000110
