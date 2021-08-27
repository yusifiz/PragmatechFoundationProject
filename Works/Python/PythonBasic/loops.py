# ----while loops----
i = 1
while i < 6:
  print(i)
  i += 1

# break

b = 1
while b < 6:
  print(b)
  if b == 3:
    break
  b += 1

# continue

a = 0
while a < 6:
  a += 1
  if a == 3:
    continue
  print(a)

# else

c = 1
while c < 6:
  print(c)
  c += 1
else:
  print(c)

# ----for loop----

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

# break

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

# continue

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

# range()

for x in range(2, 6):
  print(x) # 2-den 6-ya qeder ededleri cap edir

for x in range(2, 30, 3):
  print(x) # 2-den 30-a qeder ededleri 3 vahid artirib cap edir

# else

for x in range(6):
  print(x)
else:
  print("Finally finished!")