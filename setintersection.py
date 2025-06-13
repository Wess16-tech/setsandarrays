setx = {"green","blue"}
sety = {"blue","yellow"}
print('Original set elements: ')
print(setx)
print(sety)
print("\nIntersection of two said sets:")
setz = setx.intersection(sety)
print(setz)

print("\n union of two said sets:")
setz = setx.union(sety)
print(setz)

print("\nDifference of two said sets:")
setz = setx.difference(sety)
print(setz)

print("\nSymmetric difference of two said sets:")
setz = setx.symmetric_difference(sety)
print(setz)