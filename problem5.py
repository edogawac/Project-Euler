from runtime import proRuntime as runtime

def smallestMultiple(a, b):
    num = 1
    result = 0
    j = 0

    while True:
        for i in range(a, b+1, 1):
            if num % i == 0:
                result = num if i == b else i
                j = i
                continue
            else:
                break

        num += 1
        if j == b:
            break

    print(result)

smallestMultiple(1, 20)

runtime()
# --- 320.50462222099304 seconds ---