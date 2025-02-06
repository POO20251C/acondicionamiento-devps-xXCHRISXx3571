def suma_digitos(numero: int) -> int:
    return sum(int(digito) for digito in str(abs(numero)))

def contar_vocales(cadena: str) -> int:
    vocales = "aeiou"
    return sum(1 for c in cadena.lower() if c in vocales)

def es_palindromo(cadena: str) -> str:
    cadena_limpia = "".join(c for c in cadena.lower() if c.isalnum())
    return "Si" if cadena_limpia == cadena_limpia[::-1] else "No"

def invertir_lista(lista: str) -> str:
    return " ".join(lista.split()[::-1])

def contar_palabras(cadena: str) -> int:
    return len(cadena.split())

def max_min(lista: str) -> str:
    numeros = list(map(int, lista.split()))
    return f"{max(numeros)} {min(numeros)}"

def main():
    entrada = input()
    if entrada.isdigit() or (entrada[0] == '-' and entrada[1:].isdigit()):
        print(suma_digitos(int(entrada)))
    elif " " in entrada:
        if all(c.isdigit() or c.isspace() for c in entrada):
            print(max_min(entrada))
            print(invertir_lista(entrada))
        else:
            print(contar_palabras(entrada))
            print(contar_vocales(entrada))
            print(es_palindromo(entrada))
    else:
        print(es_palindromo(entrada))
        print(contar_vocales(entrada))

if __name__ == "__main__":
    main()
