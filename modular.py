"""Ejemplo de modularización"""
# print("    *")
# print("   **")
# print("  ***")
# print(" ****")
# print("*****")

# ###################

# n = 5
# for i in range(1, n + 1):
#     for j in range(1, n - i):
#         print(" ", sep = "")
#     for j in range(1, i):
#         print("*", sep = "")
#     print("\n")

# n = 8
# for i in range(1, n + 1):
#     for j in range(1, n - i):
#         print(" ", sep = "")
#     for j in range(1, i):
#         print("*", sep = "")
#     print("\n")

# n = 10
# for i in range(1, n + 1):
#     for j in range(1, n - i):
#         print(" ", sep = "")
#     for j in range(1, i):
#         print("*", sep = "")
#     print("\n")

# ########################

# def imprimir_piramide(n):
#     for i in range(1, n + 1):
#         for j in range(1, n - i):
#             print(" ", sep = "")
#         for j in range(1, i):
#             print("*", sep = "")
#         print("\n")

# imprimir_piramide(5)
# imprimir_piramide(8)
# imprimir_piramide(10)

########################


def imprimir_piramide(altura):
    """
    Imprime una pirámide de asteriscos
    alineada a la derecha, de tamaño
    altura x altura.
    """
    for i in range(1, altura + 1):
        print(" " * (altura - i) + "*" * i)


imprimir_piramide(5)
imprimir_piramide(8)
imprimir_piramide(10)
