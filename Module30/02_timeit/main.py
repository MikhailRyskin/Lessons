import timeit


def main():
    res: float = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
    print(res)

    # start_time = time.time()
    # [("-".join(str(n) for n in range(100))) for _ in range(10000)]
    # print(round(time.time() - start_time, 9))

    res_1: float = timeit.timeit('[("-".join(str(n) for n in range(100))) for _ in range(10000)]', number=1)
    print(res_1)

    # start_time = time.time()
    # list(map(lambda x: "-".join(str(n) for n in range(100)), [x for x in range(10000)]))
    # print(round(time.time() - start_time, 9))

    res_2: float = timeit.timeit('list(map(lambda x: "-".join(str(n) for n in range(100)), [x for x in range(10000)]))',
                                 number=1)
    print(res_2)

# пожалуйста, обратите внимание, в данном задании, все варианты стоит реализовать внутри метода timeit модуля timeit. =)


if __name__ == '__main__':
    main()
