def run(screen):
    if screen == 'debug':
        return [{
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
            'y': 78,
            'size': 1
        }]
    else:
        return [{
            'text': [['E0000: screen number wrong', (255, 0, 255)]],
            'x': 1,
            'y': 1,
            'size': 1
        }]