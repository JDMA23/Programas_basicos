print("Este programa calcula el salario neto")
salario_bruto = float(input("Ingrese su salario bruto: "))
porcentaje_impuestos = float(input("Ingrese el porcentaje de impuestos : "))
deducciones = float(input("Ingrese las deducciones: "))
impuestos = salario_bruto * (porcentaje_impuestos / 100)
salario_neto = salario_bruto - impuestos - deducciones
print("Su salario neto es: ", salario_neto)

