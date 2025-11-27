#!/usr/bin/env python3
"""
Juego de Michi (Tic-Tac-Toe)
Un juego clásico para dos jugadores en la consola.
"""

class Michi:
    def __init__(self):
        self.tablero = [[' ' for _ in range(3)] for _ in range(3)]
        self.jugador_actual = 'X'
    
    def mostrar_tablero(self):
        """Muestra el tablero actual del juego"""
        print("\n   0   1   2")
        for i in range(3):
            print(f"{i}  {self.tablero[i][0]} | {self.tablero[i][1]} | {self.tablero[i][2]}")
            if i < 2:
                print("  -----------")
    
    def hacer_movimiento(self, fila, columna):
        """Realiza un movimiento en la posición especificada"""
        if self.tablero[fila][columna] == ' ':
            self.tablero[fila][columna] = self.jugador_actual
            return True
        return False
    
    def verificar_ganador(self):
        """Verifica si hay un ganador"""
        # Verificar filas
        for fila in self.tablero:
            if fila[0] == fila[1] == fila[2] != ' ':
                return fila[0]
        
        # Verificar columnas
        for col in range(3):
            if self.tablero[0][col] == self.tablero[1][col] == self.tablero[2][col] != ' ':
                return self.tablero[0][col]
        
        # Verificar diagonales
        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] != ' ':
            return self.tablero[0][0]
        
        if self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] != ' ':
            return self.tablero[0][2]
        
        return None
    
    def tablero_lleno(self):
        """Verifica si el tablero está lleno"""
        for fila in self.tablero:
            if ' ' in fila:
                return False
        return True
    
    def cambiar_jugador(self):
        """Cambia al siguiente jugador"""
        self.jugador_actual = 'O' if self.jugador_actual == 'X' else 'X'
    
    def reiniciar_juego(self):
        """Reinicia el juego"""
        self.tablero = [[' ' for _ in range(3)] for _ in range(3)]
        self.jugador_actual = 'X'
    
    def obtener_movimiento_valido(self):
        """Obtiene un movimiento válido del jugador"""
        while True:
            try:
                entrada = input(f"\nJugador {self.jugador_actual}, ingresa tu movimiento (fila,columna): ")
                fila, columna = map(int, entrada.split(','))
                
                if 0 <= fila <= 2 and 0 <= columna <= 2:
                    if self.tablero[fila][columna] == ' ':
                        return fila, columna
                    else:
                        print("¡Esa posición ya está ocupada! Intenta otra.")
                else:
                    print("¡Coordenadas inválidas! Usa números del 0 al 2.")
            except ValueError:
                print("¡Formato inválido! Usa el formato: fila,columna (ejemplo: 1,2)")
            except KeyboardInterrupt:
                print("\n¡Juego interrumpido!")
                return None, None
    
    def jugar(self):
        """Función principal del juego"""
        print("¡Bienvenido al juego de Michi!")
        print("Instrucciones:")
        print("- Los jugadores se turnan para colocar X y O")
        print("- Ingresa las coordenadas como: fila,columna (ejemplo: 1,2)")
        print("- Las coordenadas van del 0 al 2")
        print("- Gana el primer jugador que logre 3 en línea")
        
        while True:
            self.mostrar_tablero()
            
            # Obtener movimiento del jugador
            fila, columna = self.obtener_movimiento_valido()
            
            # Verificar si el juego fue interrumpido
            if fila is None:
                break
            
            # Realizar el movimiento
            self.hacer_movimiento(fila, columna)
            
            # Verificar si hay ganador
            ganador = self.verificar_ganador()
            if ganador:
                self.mostrar_tablero()
                print(f"\n¡Felicidades! ¡El jugador {ganador} ha ganado!")
                break
            
            # Verificar empate
            if self.tablero_lleno():
                self.mostrar_tablero()
                print("\n¡Es un empate! El tablero está lleno.")
                break
            
            # Cambiar jugador
            self.cambiar_jugador()
        
        # Preguntar si quieren jugar otra vez
        while True:
            jugar_otra_vez = input("\n¿Quieren jugar otra vez? (s/n): ").lower().strip()
            if jugar_otra_vez in ['s', 'si', 'sí', 'y', 'yes']:
                self.reiniciar_juego()
                self.jugar()
                break
            elif jugar_otra_vez in ['n', 'no']:
                print("¡Gracias por jugar!")
                break
            else:
                print("Por favor, responde 's' para sí o 'n' para no.")


def main():
    """Función principal para ejecutar el juego"""
    juego = Michi()
    try:
        juego.jugar()
    except KeyboardInterrupt:
        print("\n\n¡Gracias por jugar!")


if __name__ == "__main__":
    main()