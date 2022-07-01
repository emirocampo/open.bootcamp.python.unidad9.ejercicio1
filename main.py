def main():
    cadena = input("digite nombres de paises separados por comas: ")
    cad = cadena.split(",")
    setPaises = set(cad)
    limpiarPaises = map(lambda x: x.strip(), setPaises)
    ordenPaises = sorted(list(limpiarPaises))
    print(",".join(ordenPaises))

if __name__ == "__main__":
    main()