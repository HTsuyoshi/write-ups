if __name__ == '__main__':
    n = 510143758735509025530880200653196460532653147
    primes = qsieve(n)
    p, q = primes[0][0], primes[0][1]

    print(f'p = {p}')
    print(f'q = {q}')

    answer = p if p < q else q

    print(f'answer = {answer}')
