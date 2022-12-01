with open("input.txt", "r") as input:
  a = []
  b = []
  white = 0
  while input.readline():
    inpu = input.readlines()
    for inp in inpu:
      if "\n" in inp:
        white += 1
        if white == 1 and inp == "\n":
          a.append(sum(b))
          white = 0
          b = []
        else:
          white = 0
          b.append(int(inp.replace("\n", "")))
      else:
        b.append(int(inp.replace("\n", "")))
        a.append(sum(b))
top1 = 0
top2 = 0
top3 = 0
print(a)
for i in a:
  if i > top1:
    a.append(top1)
    top1 = i
  elif i > top2:
    a.append(top2)
    top2 = i
  elif i > top3:
    top3 = i
print(top1 + top2 + top3)