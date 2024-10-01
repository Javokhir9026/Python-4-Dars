s1 = {1,2,3,4}
s3 = {1,2,3,4}
s2 = {3,45,6,7,8}

print(s1)
print(s2)
print()

print("DIFFERENCE")
natija = s1.difference(s2)
print(natija)

print("INTERSECTION")
borlari = s1.intersection(s2)
print(borlari)

print("DIFFERENCE_UPDATE")
s1.difference_update(s2)
print(s1)

print("INTERSECTION_UPDATE")
s1.intersection_update(s2)
print(s1)

n = s1.symmetric_difference(s2)
print(n)

s1.symmetric_difference_update(s2)
print(s1)

n = s1.issubset(s3)
print(n)