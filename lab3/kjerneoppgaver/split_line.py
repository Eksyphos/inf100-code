def get_endpoints(i,n,x_lo,x_hi):
    lengde = abs(x_hi-x_lo)
    partering = lengde/n
    segmentstart = i*partering+x_lo
    segmentslutt = (i+1)*partering+x_lo
    return f"{segmentstart} {segmentslutt}"

if __name__ == '__main__':
    x_lo = float(input("x_lo = "))
    x_hi = float(input("x_hi = "))
    n = int(input("n = "))
    for i in range(n):
        result = get_endpoints(i,n,x_lo,x_hi)
        print(result)
