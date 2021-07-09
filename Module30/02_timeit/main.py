import time
import timeit


def main():
    res: float = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
    print(res)

    start_time = time.time()
    [("-".join(str(n) for n in range(100))) for _ in range(10000)]
    print(round(time.time() - start_time, 9))

    start_time = time.time()
    list(map(lambda x: "-".join(str(n) for n in range(100)), [x for x in range(10000)]))
    print(round(time.time() - start_time, 9))


if __name__ == '__main__':
    main()
