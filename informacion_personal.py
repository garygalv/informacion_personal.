# Crear un diccionario con información ficticia
informacion_personal = {
    "nombre": "Carlos Pérez",
    "edad": 30,
    "ciudad": "Quito",
    "profesion": "Ingeniero"
}

# Acceder y modificar el valor de la clave "ciudad"
informacion_personal["ciudad"] = "Guayaquil"

# Agregar una nueva clave-valor "profesion" (si se requiere actualizar)
informacion_personal["profesion"] = "Desarrollador de Software"

# Verificar si existe la clave "telefono", si no existe, agregarla
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0999999999"

# Eliminar la clave "edad"
informacion_personal.pop("edad")

# Imprimir el diccionario final
print("Diccionario final:", informacion_personal)
