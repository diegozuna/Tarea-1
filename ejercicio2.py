#tarea 2

peso = input("hola. ingresa tu peso en kg porfavor:")
peso = float(peso)
estatura = input("ahora tu estatura en metros:" )
estatura = float(estatura)
imc = peso/estatura**2
imc = round(imc,2)
imc = str(imc)
print("tu indice de masa corporal es de:"+imc)