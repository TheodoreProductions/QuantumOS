def run(screen, x, y):
    text = []

    if screen == 'debug':
        text = appendLists(text, [{
            'text': [['''A BCDEFGHIJKLMNOPQRSTUVWXYZ
abcdefghijklmnopqrstuvwxyz
0123456789
.,!?()[]{-}_=+@#$%^&*/\\|<>:;'"

�
Hello, this is some test thing.
The quick brown fox jumps over the lazy dog.
            ''', (0, 0, 0)]],
            'x': 1,
            'y': 1,
            'size': 1
        }, {
            'text': [['Text', (0, 0, 0)], 
                     ['redtext', (255, 0, 0)], 
                     ['bluetext', (0, 0, 255)]],
            'x': 1,
            'y': 89,
            'size': 1
        }])
    else:
        text = appendLists(text, [{
            'text': [['E0000: screen number wrong', (255, 0, 255)]],
            'x': 1,
            'y': 1,
            'size': 1
        }])
    
    for t in text:
        t['x'] += x
        t['y'] += y
    
    return text

def appendLists(list1, list2):
    for l in list2:
        list1.append(l)
    
    return list1