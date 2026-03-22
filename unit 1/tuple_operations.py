t1 = (10, 20, 30)

print("Tuple:", t1)

t2 = (1, 2, (3, 4, 5))
print("Nested Tuple:", t2)
print("Access nested element:", t2[2][1])  # 4

t_repeat = t1 * 2
print("Repeated Tuple:", t_repeat)

t3 = (40, 50)
t_concat = t1 + t3
print("Concatenated Tuple:", t_concat)