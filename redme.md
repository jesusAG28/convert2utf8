# Conversor de Encoding a UTF-8

Este programa de Python permite convertir archivos de texto con diferentes encodings al formato UTF-8. Utiliza la biblioteca `chardet` para detectar automáticamente el encoding de cada archivo antes de realizar la conversión.

## Requisitos

Asegúrate de tener los siguientes requisitos previos antes de ejecutar el programa:

-   Python 3.x instalado en tu sistema. Puedes descargarlo desde [el sitio oficial de Python](https://www.python.org/downloads/).

## Instalación de dependencias

Antes de ejecutar el programa, debes asegurarte de que la biblioteca `chardet` esté instalada. Puedes instalarla utilizando `pip`:

```bash
pip install chardet
```

# Cómo usar el programa

Sigue estos pasos para utilizar el programa:

-   Descarga el código fuente del programa o clona este repositorio en tu sistema.

-   Abre una terminal o línea de comandos en el directorio donde se encuentra el código fuente del programa.

-   Ejecuta el programa con el siguiente comando, proporcionando la carpeta de origen y la carpeta de salida como argumentos:

```bash
python convert_to_utf8.py <directorio_de_origen> <directorio_de_salida>
```

-   El programa detectará automáticamente el encoding de cada archivo en el directorio de origen y los convertirá a UTF-8 en el directorio de salida.

-   Una vez completada la conversión, el programa mostrará un mensaje de éxito.

# Notas adicionales

-   Asegúrate de tener permisos de escritura en el directorio de salida especificado.

-   El programa se adapta automáticamente al encoding de los archivos de entrada utilizando la biblioteca chardet.

-   Si los archivos de entrada utilizan un encoding diferente a ISO-8859-1, modifica el valor de encoding en el código para adaptarlo a tus necesidades.
