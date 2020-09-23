"""
tg45° = 1 (45d = π/4)
tg π/4 = 1
arctg(1) = π/4
π = arctg * 4

arctg(x) = x - x^3/3 + x^5/5 - x^7/7 + x^9/9 - x^11/11 ...
arctg(1) = π/4 = 4 x (1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 ...)
"""
import time

def counter(q):
    a = 1
    iterations = int(q)

    for i in range(1, iterations + 1):
        onelink = 1 / (i + 2)               # 1/3, 1/5, 1/7 ...
        sign_link = (-1) ** i * onelink
        a = a + sign_link

        print(f"[INFO] ITER № = {i}")

    result = 4 * a
    print(f"[π] equals > {result}")


def main():
    quant = input("Type quantity of π counting > ")

    start_time = time.time()
    counter(q = quant)

    print("\nAll [%s] countings completed in: [%s sec.] ---\n" %
                    ((quant), (time.time() - start_time)))

main()