d = {}
for x in range(10):
    y = x * 2
    d["string{0}and{1}".format(x,y)] = "Hello", "test"

print(d)