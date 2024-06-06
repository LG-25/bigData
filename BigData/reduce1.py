import sys

current_marca = None
current_total = 0

for linea in sys.stdin:
    marca, nasientos = linea.strip().split('\t')
    nasientos = int(nasientos)

    if current_marca == marca:
        current_total += nasientos
    else:
        if current_marca:
            print(f"{current_marca}\t{current_total}")
        current_marca = marca
        current_total = nasientos

if current_marca:
    print(f"{current_marca}\t{current_total}")
