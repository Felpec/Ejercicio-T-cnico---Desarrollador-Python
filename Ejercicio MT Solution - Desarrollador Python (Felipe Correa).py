#Importe de la librería fileinput para la lectura de múltiples logs
import fileinput

#Definición del método de ordenamiento
def orden(e):
    i = e.split(';')
    return i[2]

#Definición de funcion para la lectura de logs (La función fileinput permite la lectura de una cantidad n de logs)
with fileinput.input(files=('Directorio_log_1\nombre_log', 'Directorio_log_2\nombre_log')) as f:
    #Definición ubicación y nombre del log a generar
    nuevo = open("Directorio_log_de_la_union\nombre_log", "w")
    datos = []
    #Generación lista con los valores extraidos de los logs
    for line in f:
        datos.append(line.strip('\n'))
    datos.sort(key=orden)
    #Registro de los valores ordenados en el log especificado anteriormente
    nuevo.write("\n".join(datos))
    nuevo.close()
