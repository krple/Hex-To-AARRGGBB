def h2a(hex_code): return f'FF{int(hex_code,16):06X}'

while True:
    c = input("Enter a Hex Code (or 'exit'): ").lstrip('#').lower()
    if c == 'exit': break
    if len(c) == 6 and all(x in '0123456789ABCDEFabcdef' for x in c):
        print(f"AARRGGBB: {h2a(c)}")
    else:
        print("Invalid hex")