from runtime import proRuntime as runtime

lt = rt = lb = rb = 0
sum = 0
oddnum = 3

while oddnum <= 1001:
    rt = oddnum * oddnum
    lt = rt - (oddnum - 1)
    lb = lt - (oddnum - 1)
    rb = lb - (oddnum - 1)
    sum += rt + lt + lb + rb

    oddnum += 2

print(sum + 1)
runtime()
