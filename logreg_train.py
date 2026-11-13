import sys
from data_analysis import data_analysis
from ft_dslr import LogisticRegression

import numpy as np
import pandas as pd

def main():
    args = sys.argv[1:]
    if len(args) != 1:
        print("Usage: python logreg_train.py <dataset.csv>")
        exit(1)
    # Cargo los datos y los separo en Y (classes) y X (features)
    data = data_analysis(sys.argv[1])
    #data.describe()
    data.clean_nan_data()
    data.describe()
    
    list_features = [6,7,8,9,10,11,12,13,14,15,16,17,18]
    list_category = 1  
    y_train = data.get_column_by_index(list_category)
    X_train = data.get_columns_by_index_list(list_features)
    print(len(X_train), len(y_train))
    model = LogisticRegression(learning_rate=0.0005)  
    # Entreno el Modelo
    model.fit(X_train, y_train, epochs=1500)
    model.save_model("model.json")
    print(model.get_weights())
    print(model.get_bias())

    exit()

    # Testing prediction
    #model.load_model("model.json")
    #print(X_train)

    test_sample = [41642.0,696.0960714808824,3.0201723778093963,-6.960960714808824,7.996,-365.1518504531068,393.13818539298967,4.207690767250213,1046.7427360602487,3.6689832316813447,0.3738525472517433,-244.48172,-13.62]
    test_sample3 = [41907.0,470.65375662672136,-5.518263685781008,-4.7065375662672135,4.425,-434.2932661222959,596.6100889263835,-4.1618229744065465,967.2239116973597,5.027414761055882,-1.135957011752296,-252.27344,174.27]
    #Ravenclaw
    test_sample1= [58384.0,-487.88608595139016,5.727180298550763,4.8788608595139005,4.7219999999999995,272.0358314131986,532.4842261151226,5.231058287281048,1039.7882807428462,3.7903690663529614,0.7159391270136213,-232.79405,-26.89]
    #Slycerin
    test_sample2 = [67239.0,-552.0605073421984,-5.987445780050746,5.520605073421985,-5.612,-487.3405572673422,367.7603030171392,4.107170286816076,1058.9445920642218,7.248741976146588,0.091674183916857,-252.18425,-113.45]
    print("Predicted class:", model.predict(test_sample1))
    print("Predicted probabilities:", model.predict_proba(test_sample1))
    print("Predicted class:", model.predict(test_sample2))
    print("Predicted probabilities:", model.predict_proba(test_sample2))
    
    print("Predicted class:", model.predict(test_sample3))
    print("Predicted probabilities:", model.predict_proba(test_sample3))
    exit(1)

    
##
    df = pd.read_csv(sys.argv[1])
    df.drop(
        columns=["Index", "First Name", "Last Name", "Birthday", "Best Hand"],
        inplace=True,
    )
    X_1 = df.drop(columns=["Hogwarts House"])
    X_1 = X_1.fillna(X_1.mean())
    X_1 = (X_1 - X_1.mean()) / X_1.std()
    y_1 = df["Hogwarts House"]
##
    #print("l",len(load_data.get_data()))
    #print("l",len(load_data.get_data()[0]))
    #print(load_data.get_data())
    #print((load_data.get_data()[1]))
    #print(len(load_data.get_data()))
    #print("celanind")


    load_data.clean_nan_data()
    
    # Other 
    # rellena los nulos con la media
    # cambia los valores con (x-X.mean())/X.std()

    #print((load_data.get_data()[0]))
    #print(len(load_data.get_data()))
    #print(load_data.get_columns_type())
    load_data.describe()
    

    # standarize de data
 
    list_features = [6,7,8,9,10,11,12,13,14,15,16,17,18]
    list_category = 1  
    y_train = load_data.get_column_by_index(list_category)
    X_train = load_data.get_columns_by_index_list(list_features)
    
    #print(y_train)
    #print(y_1)
    #exit()
    #print(X_train[0])
    print(X_train[1])
    print(X_1)
    exit()
    
    
    
    
    exit()
    model1 = logistic_regression(learning_rate=0.01)
    model1.fit(X_train, y_train, epochs=1500)
    exit()
    
    # save results


    test_sample = [41642.0,696.0960714808824,3.0201723778093963,-6.960960714808824,7.996,-365.1518504531068,393.13818539298967,4.207690767250213,1046.7427360602487,3.6689832316813447,0.3738525472517433,-244.48172,-13.62]
    test_sample = [45352.0,-370.8446553065122,2.9652261693057698,3.708446553065121,6.349,522.5804860261724,602.8530505526203,6.460017331082373,1048.0538781192083,8.51462223474569,0.5774322733924575,-231.292,-26.26]
    test_sample = [58384.0,-487.88608595139016,5.727180298550763,4.8788608595139005,4.7219999999999995,272.0358314131986,532.4842261151226,5.231058287281048,1039.7882807428462,3.7903690663529614,0.7159391270136213,-232.79405,-26.89]
    test_sample = [67239.0,-552.0605073421984,-5.987445780050746,5.520605073421985,-5.612,-487.3405572673422,367.7603030171392,4.107170286816076,1058.9445920642218,7.248741976146588,0.091674183916857,-252.18425,-113.45]
    print("Predicted class:", model1.predict(test_sample))
    print("Predicted probabilities:", model1.predict_proba(test_sample))
    print("This is the model")
    print(model1.get_weights())
    print(model1.get_bias())
    #print(X_train)
    print("save model")
    model1.save_model("model.json")
    #exit()
    # test load model
    print("Loading model:")
    model2 = logistic_regression(learning_rate=0.01)
    model2.load_model("model.json")
    print(model2.get_weights())
    print(model2.get_bias())
    print("Predicted class:", model2.predict(test_sample))
    print("Predicted probabilities:", model2.predict_proba(test_sample))
    #exit()

    # get csv to predict
    # predict each
    # add csv results

    #print(test)
    X_train = [
        [1.0, 2.0],
        [1.5, 1.8],
        [5.0, 8.0],
        [6.0, 9.0],
        [1.0, 0.6],
        [9.0, 11.0]
    ]
    #y_train = [0, 0, 1, 1, 0, 2]  # class labels
    
    
    
    
    y_train = ['a0', 'a0', 'a1', 'a1', 'a0', 'a2']  # class labels
    model = logistic_regression( learning_rate=0.01)
    model.fit(X_train, y_train, epochs=1500)
    print("Trainning done.")
    # Predictions
    test_sample = [5.5, 9.0]
    test_sample = [9.0, 11.0]
    print("Predicted class:", model.predict(test_sample))
    print("Predicted probabilities:", model.predict_proba(test_sample))
    #print(logistic.predict())

if __name__=="__main__":
    main()