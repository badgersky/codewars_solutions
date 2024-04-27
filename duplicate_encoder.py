def duplicate_encode(word):
    word_c = word.lower()
    res = [')' if word_c.count(char) > 1 else '(' for char in word_c]     
            
    return ''.join(res)


if __name__ == '__main__':
    print(duplicate_encode('murica fuck yea'))
