# 8-misol: Toq sonlar va ularning soni
a = [1, 2, 3, 4, 5, 6, 7, 8]
toq = [x for x in a if x % 2 != 0]
print(f"Toqlar: {toq}, Soni: {len(toq)}")

# 9-misol: Juft sonlar (teskari tartibda)
a = [1, 2, 3, 4, 5, 6, 7, 8]
juft = [x for x in a if x % 2 == 0]
print(f"Juftlar: {juft[::-1]}, Soni: {len(juft)}")

# 10-misol: Avval juft, keyin toqlar
a = [1, 2, 3, 4, 5, 6]
natija = [x for x in a if x % 2 == 0] + [x for x in a if x % 2 != 0]
print(natija)

# 11-misol: K ga karrali indekslar
n, k = 10, 2
a = list(range(n))
print(a[k::k])

# 12-misol: Juft indekslar
a = [10, 20, 30, 40, 50, 60]
print(a[::2])

# 13-misol: Toq indekslar (teskari)
a = [10, 20, 30, 40, 50, 60]
toq_indeks = a[1::2]
print(toq_indeks[::-1])
