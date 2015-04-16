#Paulina Romo Villalobos
def triangles(size):
  for i in range(1, size +1):
    for x in range(i):
      print("T", end="")
    print()

  for i in range(1, size):
    for x in range(size-i):
      print("T", end="")
    print()

size=int(input("Size of the triangle: "))
triangles(size)
