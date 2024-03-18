# primer ejercicio

texto = input("Escribe un texto: ").lower()
letras_elegidas= []
letras_elegidas.append(input("ingrese la primera letra: " .lower()))
letras_elegidas.append(input("ingrese la segunda letra: " .lower()))
letras_elegidas.append(input("ingrese la tercera letra: " .lower()))
conteo_l1= texto.count(letras_elegidas[0])
conteo_l2= texto.count(letras_elegidas[1])
conteo_l3= texto.count(letras_elegidas[2])
print("----------------------------------------------------------------------")
print("Conteo de letras ingresadas:")
print(f"primera letra: {conteo_l1}\nsegunda letra : {conteo_l2} \ntercera letra: {conteo_l3}")

# segundo ejercicio 
print("----------------------------------------------------------------------")
print (f"El conteo de las palabras es: {len(texto.split())}")
print("----------------------------------------------------------------------")

# el tercer ejercicio
print("----------------------------------------------------------------------")
print((f"la primera letras del texto es : {texto[0]} y la ultima es: {texto[-1]}"))
print("----------------------------------------------------------------------")


# el cuarto ejercicio
print("Texto invertido: ")
print(texto[::-1])
print("----------------------------------------------------------------------")
# el quinto ejercicio
buscador= "python" in texto.lower()

buscar_palabra={
    "True": "La palabra python se encuentra en el texto",
    "False":"La palabra python No se encuentra en el texto"
}
if buscador == True:
    print(buscar_palabra["True"])
else:
    print(buscar_palabra["False"])

