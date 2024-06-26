from datetime import date


def coffee_limits(year, month, day):
    h = int(str(date(year, month, day)).replace('-', ''))
    hc, hd = h, h
    
    cafe, decaf = int('CAFE', 16), int('DECAF', 16)
    found = [False, False]
    cc = 0
    
    while not all(found):
        if cc != 0:
            if 'dead' in hex(hc) and not found[0]:
                c_limit = cc if cc < 5000 else 0
                found[0] = True
            if 'dead' in hex(hd) and not found[1]:
                d_limit = cc if cc < 5000 else 0
                found[1] = True
        
        hc += cafe
        hd += decaf
        cc += 1

    return [c_limit, d_limit]
        


if __name__ == '__main__':
    print(coffee_limits(1880, 3, 1))
