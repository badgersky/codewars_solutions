def get_pins(observed):
    pos = {
        '1': '124',
        '2': '1235',
        '3': '236',
        '4': '1457',
        '5': '24568',
        '6': '3569',
        '7': '478',
        '8': '57890',
        '9': '869',
        '0': '08',
    }
    
    prev = []
    for num in observed:
        curr = []
        if not prev:
            curr = list(pos[num])
        else:
            for pin in prev:
                for n in pos[num]:
                    new_pin = pin + n
                    curr.append(new_pin)
                    
        prev = curr
        
    return prev
