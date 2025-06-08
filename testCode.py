def main():
    a = 'sdf'
    print(a[0])
    print(a[1])
    print(a[2])
    b = 'a\ng'
    print(b[0])
    if b[1] == '\n':
        print('\\n')
    else:
        print(b[1])
    print(b[2])
if __name__ == "__main__":
    main()