from data_analysis import data_analysis
from ft_dslr import LogisticRegression
import argparse

def parse_args():
    parser = argparse.ArgumentParser(
      description=("Testeado un dataset con un modelo ya entrenado y muestra los resulados en un fichero"),
      usage="python logreg_train.py <dataset.csv> <model.json>",
    )
    # obligatorio
    parser.add_argument("dataset", type=str, help="Ruta al archivo CSV del dataset to train")
    parser.add_argument("model", type=str, help="Ruta al archivo Json del modelo")
    return parser.parse_args()

def main():
    args = parse_args()
    print(args)
        
    # Cargo los datos y los separo en Y (classes) y X (features)
    data = data_analysis(args.dataset)        #data.describe()
    #data.describe()
    # Elijo las columnas de features y la de categorias
    list_features = [6,7,8,9,10,11,12,13,14,15,16,17,18]
    list_category = 1  

    y_train = data.get_column_by_index(list_category)
    X_train = data.get_columns_by_index_list(list_features)

    model = LogisticRegression()
    model.load_model(args.model)  
    model.test(X_train, y_train)
    model.compare("houses.csv", "dataset_truth.csv", col_index=1, header= True)

if __name__=="__main__":
    main()