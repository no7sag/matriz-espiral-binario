def makeFigure(size):
    
    # Matriz bidimensional de dimensiones iguales compuesta de ceros
    figure = [[0] * size for i in range(size)]
    
    # Límites de la matriz
    start_row = 0
    start_col = 0
    end_row = size-1
    end_col = size-1
    
    # Número que define en qué dirección se recorre la matriz
    # Derecha = 0   | Abajo = 1
    # Izquierda = 2 | Arriba = 3
    dir = 0
    
    while (start_row <= end_row or start_col <= end_col):
        
        # Derecha
        if dir == 0:
            for i in range(start_col-1, end_col+1):
                figure[start_row][i] = 1
                
            start_row +=2
            
            dir = 1
            
        # Abajo
        elif dir == 1:
            for i in range(start_row-1, end_row+1):
                figure[i][end_col] = 1
                
            end_col -= 2
            
            dir = 2
        
        # Izquierda
        elif dir == 2:
            for i in range(end_col+1, start_col-1, -1):
                figure[end_row][i] = 1
                
            end_row -= 2
                
            dir = 3
            
        # Arriba
        elif dir == 3:
            for i in range(end_row+1, start_row-1, -1):
                figure[i][start_col] = 1
                
            start_col += 2
            
            dir = 0  # Dirección inicial
    
    # Visualización de la figura
    for row in figure:
        for n in row:
            if n == 0: print(".", end=" ")
            if n == 1: print("0", end=" ")
        print("")
    print("")
    
    return figure