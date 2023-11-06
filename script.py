import os
import sys
import shutil
import codecs
import chardet
import re
from colorama import init, Fore

init(autoreset=True)

def detectar_encoding(archivo):
    try:
        with open(archivo, 'rb') as f:
            resultado = chardet.detect(f.read())
        return resultado['encoding']
    except Exception as e:
        return None

def convertir_archivo_a_utf8(archivo, encoding_original, ruta_destino, exitosos, errores):
    try:
        with codecs.open(archivo, 'r', encoding=encoding_original, errors='replace') as f:
            contenido = f.read()

        contenido = re.sub(r'(<\?(?!=|php|xml))', '<?php ', contenido)

        ruta_destino_completa = os.path.join(ruta_destino, os.path.relpath(archivo, start=ruta_origen))
        os.makedirs(os.path.dirname(ruta_destino_completa), exist_ok=True)

        with codecs.open(ruta_destino_completa, 'w', encoding='utf-8') as f:
            f.write(contenido)
        print(Fore.GREEN + f'{archivo} convertido a UTF-8 y guardado en {ruta_destino_completa}')
        exitosos += 1
    except Exception as e:
        error_msg = f'Error al convertir {archivo}: {str(e)}'
        print(Fore.RED + error_msg)
        errores += 1

        # Si ocurre un error, copiamos el archivo directamente a destino
        ruta_destino_completa = os.path.join(ruta_destino, os.path.relpath(archivo, start=ruta_origen))
        os.makedirs(os.path.dirname(ruta_destino_completa), exist_ok=True)
        shutil.copy2(archivo, ruta_destino_completa)
        print(Fore.GREEN + f'{archivo} copiado a {ruta_destino_completa}')
        exitosos += 1

def contar_archivos_en_directorio(ruta):
    archivos = [f for f in os.listdir(ruta) if os.path.isfile(os.path.join(ruta, f))]
    return len(archivos)

def convertir_proyecto_a_utf8(ruta_origen, ruta_destino):
    exitosos = 0
    errores = 0

    archivos_origen = contar_archivos_en_directorio(ruta_origen)
    archivos_destino = 0

    for ruta_actual, directorios, archivos in os.walk(ruta_origen):
        for archivo in archivos:
            ruta_completa_origen = os.path.join(ruta_actual, archivo)
            if archivo.endswith(('.html', '.css', '.js', '.php', '.py')):
                encoding_original = detectar_encoding(ruta_completa_origen)
                if encoding_original:
                    convertir_archivo_a_utf8(ruta_completa_origen, encoding_original, ruta_destino, exitosos, errores)
                    archivos_destino += 1
            else:
                ruta_destino_completa = os.path.join(ruta_destino, os.path.relpath(ruta_completa_origen, start=ruta_origen))
                os.makedirs(os.path.dirname(ruta_destino_completa), exist_ok=True)
                shutil.copy2(ruta_completa_origen, ruta_destino_completa)
                print(Fore.GREEN + f'{archivo} copiado a {ruta_destino_completa}')
                exitosos += 1
                archivos_destino += 1

    return exitosos, errores, archivos_origen, archivos_destino

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python script.py <ruta_origen> <ruta_destino>")
        sys.exit(1)

    ruta_origen = sys.argv[1]
    ruta_destino = sys.argv[2]

    exitosos, errores, archivos_origen, archivos_destino = convertir_proyecto_a_utf8(ruta_origen, ruta_destino)
    print(f'Archivos OK: {exitosos}')
    print(f'Archivos ERROR: {errores}')
    print(f'Archivos en origen: {archivos_origen}')
    print(f'Archivos en destino: {archivos_destino}')

    if archivos_origen == archivos_destino:
        print("Todos los archivos han sido procesados.")
    else:
        print("No se han procesado todos los archivos.")
