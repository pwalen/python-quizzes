a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

li = [a, b, c]
li_min = min(li)
li_max = max(li)
li.remove(li_min)
li.remove(li_max)
li_mid = li[0]

if li_min ** 2 + li_mid ** 2 == li_max ** 2:
    print("It is a triangle with a right angle (90°) in it")
else:
    print("It is NOT a triangle with a right angle (90°) in it")

