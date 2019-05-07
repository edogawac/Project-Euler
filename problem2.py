from runtime import proRuntime as runtime

a = 0
ad = 1
n = 0

n = a + ad
sum = 0

while True:
    a = ad
    ad = n
    n = a + ad
    if n <= 4000000:
        if n % 2 == 0:
            sum += n
    else:
        break

print(sum)
runtime()
