# Generate-Password

Esta basado en el framework flet y tambien utiliza el paquete randon 

Seleccion de varias opciones de caracteres a la hora de armar la contraseña (Minusculas, Mayusculas, Simbolos, Numeros)

Elección del largo de la contraseña siempre y cuando no superando los caracteres maximos de cada grupo de caracteres

Copiado al portapapeles de la contraseña generada.

Por ultimo un boton de limpieza de contraseña para generar nuevas

![demo_video](https://user-images.githubusercontent.com/55749965/232059065-d05b2cda-094c-4cc8-99a0-68207680be87.gif)

# Generate_Password

Este código genera contraseñas seguras.

## Argumentos

* `length` (int): La longitud de la contraseña.
* `symbols` (list): La lista de símbolos que se pueden usar en la contraseña.

## Retorno

* str: La contraseña generada.

## Ejemplo

```python
>>> generate_password(12, ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])
'abcdefghij'


## Notas

* La contraseña se genera aleatoriamente.
* La contraseña es segura porque utiliza una combinación de letras, números y símbolos.


