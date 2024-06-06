import sys

for linea in sys.stdin:
    claves = linea.strip().split(';')
    if len(claves) > 3 and claves[3].isdigit():
        marca = claves[0]
        nasientos = int(claves[3])
        print(f"{marca}\t{nasientos}")
