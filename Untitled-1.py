import readchar

laberinto = [
    ['#', '#', '#', '#', '#', '#', '#'],
    ['#', 'P', '.', '.', '.', '.', '#'],
    ['#', '.', '#', '#', '#', '.', '#'],
    ['#', '.', '#', '.', '.', '.', '#'],
    ['#', '.', '#', '#', '#', '#', '#'],
    ['#', '.', '.', '.', '.', '.', '#'],
    ['#', '#', '#', '#', '#', '#', '#']
]

posicion_jugador = [1, 1]

def mostrar_laberinto():
    for fila in laberinto:
        print(' '.join(fila))
    print()

def mover_jugador(direccion):
    x, y = posicion_jugador
    if direccion == 'W' and laberinto[x-1][y] == '.':
        laberinto[x][y], laberinto[x-1][y] = '.', 'P'
        posicion_jugador[0] -= 1
    elif direccion == 'S' and laberinto[x+1][y] == '.':
        laberinto[x][y], laberinto[x+1][y] = '.', 'P'
        posicion_jugador[0] += 1
    elif direccion == 'A' and laberinto[x][y-1] == '.':
        laberinto[x][y], laberinto[x][y-1] = '.', 'P'
        posicion_jugador[1] -= 1
    elif direccion == 'D' and laberinto[x][y+1] == '.':
        laberinto[x][y], laberinto[x][y+1] = '.', 'P'
        posicion_jugador[1] += 1

def main():
    print("Presiona W, A, S, D para moverte por el laberinto. Para salir, presiona ↑.")
    mostrar_laberinto()

    while True:
        tecla = readchar.readchar().upper()
        if tecla == readchar.key.UP:
            print("¡Has presionado la tecla ↑! Saliendo del programa.")
            break
        elif tecla in ['W', 'A', 'S', 'D']:
            mover_jugador(tecla)
            mostrar_laberinto()

if __name__ == "__main__":
    main()



