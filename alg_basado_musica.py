import random

# Función objetivo: minimizar la suma de cuadrados
def objetivo(x): #Funcion que queremos minimizar
    return sum([xi ** 2 for xi in x]) #Suma de los cuadrados de cada elemento en X

# Algoritmo de Búsqueda de Armonía (HS)
#(funcion que queremos minimizar, numero de variables en el vector solucion, rango de valores permitidos para cada variable, numero total de iteraciones, tamaño de la memoria de armonía, Probabilidad de considerar la memoria al crear una nueva armonía, Probabilidad de ajustar el tono de un valor seleccionado de la memoria)
def harmony_search(funcion_objetivo, dimension, limites, iteraciones, tam_memoria, hmcr, par): 
    # Inicialización de la memoria de armonía (HM)
    memoria_armonia = [#Lista que almacenara las soluciones actuales (armonias)
        [random.uniform(limites[0], limites[1]) for _ in range(dimension)] #Genera un vector de valores aleatorios dentro de los límites para cada variable de la solución.
        for _ in range(tam_memoria) #Repite el proceso para crear tam_memoria soluciones iniciales.
    ]
    
    # Evaluar la memoria inicial
    #Lista que almacena los valores de la función objetivo para cada armonía en la memoria=(Evalúa cada armonía usando la función objetivo.)
    valores_memoria = [funcion_objetivo(armonía) for armonía in memoria_armonia]

    for iteracion in range(iteraciones):
        # Improvisar una nueva armonía
        nueva_armonia = []
        for i in range(dimension): #recorrer cada variable en el vector solucion
            if random.random() < hmcr:  # Memoria de armonía
                valor = random.choice([memoria_armonia[j][i] for j in range(tam_memoria)])
                if random.random() < par:  # Ajuste de tono
                    valor += random.uniform(-0.01, 0.01)  # Ajuste pequeño
            else:  # Aleatorización
                valor = random.uniform(limites[0], limites[1])
            nueva_armonia.append(valor)
        
        # Evaluar la nueva armonía
        valor_nuevo = funcion_objetivo(nueva_armonia)
        
        # Actualizar la memoria de armonía si es mejor
        peor_valor_idx = valores_memoria.index(max(valores_memoria))
        if valor_nuevo < valores_memoria[peor_valor_idx]:
            memoria_armonia[peor_valor_idx] = nueva_armonia
            valores_memoria[peor_valor_idx] = valor_nuevo
        
        # Imprimir progreso (opcional)
        if iteracion % 10 == 0:
            print(f"Iteración {iteracion}: Mejor valor = {min(valores_memoria):.5f}")

    # Devolver el mejor resultado encontrado
    mejor_idx = valores_memoria.index(min(valores_memoria))
    return memoria_armonia[mejor_idx], min(valores_memoria)

# Parámetros del algoritmo
dimension = 5                # Dimensión del problema
limites = [-10, 10]          # Límites para las variables
iteraciones = 100            # Número de iteraciones
tam_memoria = 10             # Tamaño de la memoria de armonía (HM)
hmcr = 0.9                   # Probabilidad de considerar la memoria (Harmony Memory Considering Rate)
par = 0.3                    # Probabilidad de ajuste de tono (Pitch Adjusting Rate)

# Ejecución del algoritmo
mejor_solucion, mejor_valor = harmony_search(
    funcion_objetivo=objetivo,
    dimension=dimension,
    limites=limites,
    iteraciones=iteraciones,
    tam_memoria=tam_memoria,
    hmcr=hmcr,
    par=par
)

print("\nMejor solución encontrada:", mejor_solucion)
print("Valor de la función objetivo:", mejor_valor)
