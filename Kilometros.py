def conver(kil):
    millaconv = 0.622
    return kil * millaconv

print("**********Conversor de Km a Mi**********\n")

try:
    km = float(input("Ingresar km: "))
    res = round(conver(km),2)
    print(km, "kilometro son", res, "millas")
except ValueError:
    print("Error: Ingrese un valor numérico para los kilómetros.")

