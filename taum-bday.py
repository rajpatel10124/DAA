def taumBday(b, w, bc, wc, z):
    eff_bc = min(bc, wc + z)
    eff_wc = min(wc, bc + z)
    return b * eff_bc + w * eff_wc

if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        b, w = map(int, input().split())
        bc, wc, z = map(int, input().split())
        print(taumBday(b, w, bc, wc, z))
