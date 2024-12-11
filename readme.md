# Ejemplo Bokeh

Este repositorio contiene un ejemplo práctico de cómo graficar series de tiempo utilizando **Bokeh**, una biblioteca de visualización interactiva en Python.

## Contenido del Repositorio

- **`grafica.py`**: Script principal en Python que realiza la lectura del archivo de datos y genera la gráfica interactiva utilizando Bokeh.
- **`database.xlsx`**: Archivo de datos en formato Excel que contiene las series de tiempo a graficar.
- **`page.html`**: Archivo HTML que muestra la gráfica generada.
- **`bokeh_plot.png`**: Imagen de ejemplo de la salida gráfica con variables independientes.
- **`readme.txt`**: Archivo con una breve descripción del proyecto.

## Requisitos

Para ejecutar el script, es necesario tener instaladas las siguientes bibliotecas de Python:

- `pandas`
- `bokeh`

Estas pueden instalarse utilizando `pip`:

```bash
pip install pandas bokeh
```

## Uso

1. Asegúrate de que el archivo de datos (`database.xlsx`) esté en el mismo directorio que el script `grafica.py`.
2. Ejecuta el script `grafica.py`:

   ```bash
   python grafica.py
   ```

3. El script generará un archivo HTML (`page.html`) que contiene la gráfica interactiva. Abre este archivo en tu navegador para visualizarla.

## Notas

- Puedes modificar el script `grafica.py` para leer otros formatos de archivo como `.csv` o `.json`, ajustando la función de lectura de `pandas` correspondiente.
- La imagen `bokeh_plot.png` proporciona un ejemplo de la salida gráfica esperada con variables independientes.

## Más Información

Para más detalles sobre Bokeh y sus funcionalidades, visita la [documentación oficial de Bokeh](https://docs.bokeh.org/en/latest/).
