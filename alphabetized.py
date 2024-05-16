from string import ascii_lowercase


def alphabetized(s):
    characters = {char: '' for char in ascii_lowercase}
    
    for char in s:
        if char.lower() in characters:
            characters[char.lower()] += char
        
    return ''.join(characters.values())


if __name__ == '__main__':
    print(alphabetized('Curus moja dziecie moje co u ciebie szepcze, pani matko dobrodziejko kotek mleko chlepcze'))
