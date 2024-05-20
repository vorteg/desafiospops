# Tetris

Este es el primer desafío de Desafios Pops: una implementación del juego Tetris con controles de teclado.

## Requisitos

- Python 3.x
- Librería `keyboard`
- Sistema operativo macOS o Linux (se requieren permisos de superusuario)

## Instrucciones

Sigue estos pasos para configurar y ejecutar el desafío Tetris:

1. Navega a la carpeta del desafío Tetris:
    ```bash
    cd Tetris
    ```

2. Crea un entorno virtual en Python:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

4. Ejecuta el archivo `pops.py` como superusuario:
    ```bash
    sudo python pops.py
    ```

## Notas Adicionales

- Es importante ejecutar el script con permisos de superusuario (`sudo`) en macOS o Linux, ya que el script hace uso de la librería `keyboard` que requiere permisos elevados para capturar eventos del teclado globalmente.
- Asegúrate de tener los permisos de `sudo` correctamente configurados en tu sistema.

## Controles del Juego

- `Left Arrow`: Mover la pieza a la izquierda
- `Right Arrow`: Mover la pieza a la derecha
- `Down Arrow`: Mover la pieza hacia abajo
- `Esc`: Salir del juego

## Contribuciones

Si encuentras algún problema o tienes alguna mejora, siéntete libre de abrir un issue o un pull request.

## Licencia

Este proyecto está bajo la Licencia MIT. Para más detalles, consulta el archivo [LICENSE](../LICENSE).
