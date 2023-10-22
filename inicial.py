import sys

def main(archivo, n: int) -> None :
    try:
        # Abrir el archivo
        with open(archivo, "r") as archivo:
            # Recuperamos las líneas en un arreglo
            contenido = archivo.readlines()
            
            if n <= len(contenido):                
                # Imprimir las primeras n líneas
                for i in range(n):
                    print(contenido[i])
            else:
                print(f"El archivo contiene solo {len(contenido)} líneas. No se pueden imprimir {n} líneas.")

    except FileNotFoundError:
        print(f"El archivo {archivo} no se encontró.")
        
# Validación ejecución desde terminal
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Debe pasar el numero correcto de argumentos")
    else:
        archivo = sys.argv[1]
        n = int(sys.argv[2])
        main(archivo, n)