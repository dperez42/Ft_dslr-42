import sys
from data_analysis import data_analysis
from ft_dslr import LogisticRegression
import matplotlib.pyplot as plt
import sys
import numpy as np
import pandas as pd
import argparse

def parse_args():
    parser = argparse.ArgumentParser(
      description=("Entrena modelo de regresión logística del dataset y compara metodos de optimización"),
      usage="python logreg_train.py <dataset.csv> [opciones]",
    )
    # obligatorio
    parser.add_argument("dataset", type=str, help="Ruta al archivo CSV del dataset to train")
    # opcionales
    parser.add_argument("-e","--epochs",type=int,default=1500,help="Número de épocas de entrenamiento (default: 1500)")
    parser.add_argument("-l","--lr",type=float,default=0.01,help="Tasa de aprendizaje / learning rate (default: 0.01)")
    parser.add_argument("-b","--batch_size",type=int,default=32,help="Tamaño del lote solo para Mini-Batch (default: 32)")
    #parser.add_argument("-o","--output",type=bool,default=False,help="Guarda modelo en archivo JSON con nombre: model_XXX.json (XXX metodo de entrenamiento)")
    # elige metodos para comparar
    methods_group = parser.add_argument_group("Métodos de optimización")
    methods_group.add_argument("--batch", action="store_true", help="Usa Batch Gradient Descent completo")
    methods_group.add_argument("--mini-batch",action="store_true",help="Usa Mini-Batch Gradient Descent (por defecto)")
    methods_group.add_argument("--sgd",default=True, action="store_true",help="Usa Stochastic Gradient Descent (batch_size = 1)")
    methods_group.add_argument("-o","--output",default=False, action="store_true",help="Guarda modelo en archivo JSON con nombre: model_XXX.json (XXX metodo de entrenamiento)")
    return parser.parse_args()

def main():
    args = parse_args()
    print(args)
    
    # Cargo los datos y los separo en Y (classes) y X (features)
    data = data_analysis(sys.argv[1])
    data.clean_nan_data()
    #data.describe()
    
    # Creo lista de methodos a entrenar
    methods_list=[] # nombre, abreviatura, batch size, learning rate
    muestra = len(data.get_data())-1 # quito encabezados
    if args.batch:
       methods_list.append(("BATCH", "BGD", muestra, args.lr))
    if args.mini_batch:
       methods_list.append((f"MINI-BATCH ({args.batch_size})", "MGD", args.batch_size, args.lr))
    if args.sgd:
       methods_list.append(("STOCHASTIC", "SGD", 1, args.lr))

    list_features = [6,7,8,9,10,11,12,13,14,15,16,17,18]
    list_category = 1  
    y_train = data.get_column_by_index(list_category)
    X_train = data.get_columns_by_index_list(list_features)
    
    plt.figure(figsize=(10, 6))
    main_title =""
    for name, method, batch, learning_rate in methods_list:
        print(f"\n\033[1;36m[INFO]\033[0m Ejecutando método: {name} {method} {batch} {learning_rate}")
        # Entreno el Modelo
        model = LogisticRegression(learning_rate=learning_rate)  
        model.fit(X_train, y_train, epochs=args.epochs, batch_size=batch)
        # salva modelo si parameter
        if args.output:
            nombre_fichero = "model_" + method +".json"
            model.save_model(nombre_fichero)
        plt.plot(
            range(1, len(model.cost_history) + 1),
            model.cost_history,
            label=f"{name}",
            linewidth=2,
        )
        main_title += name + "-"

    # Configurar el gráfico
    plt.title(
        "Comparación de Convergencia:" + main_title,
        fontsize=14,
        fontweight="bold",
    )
    plt.xlabel("Épocas (Epochs)", fontsize=11)
    plt.ylabel("Coste (Cross-Entropy Loss)", fontsize=11)
    plt.legend(fontsize=10, frameon=True)
    plt.grid(True, linestyle="--", alpha=0.4)
    plt.tight_layout()
    plt.show()    
    sys.exit(0)

if __name__=="__main__":
    main()