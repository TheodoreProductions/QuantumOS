def square(x, y, length, size, color):
    return [x * size, y * size, length * size, length * size, color]

def fSquare(x, y, length, color):
    return [x, y, length, color]

def rect(x, y, length, height, size, color):
    return [x * size, y * size, length * size, height * size, color]

def fRect(x, y, width, height, color):
    return [x, y, width, height, color]