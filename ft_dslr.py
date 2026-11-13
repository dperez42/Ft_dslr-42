# https://github.com/LahlouS/ft_dslr/blob/main/submission/dataloader.py
# https://github.com/rutgercap/ft_dslr/blob/main/src/describe.py

# https://www.datacamp.com/es/tutorial/softmax-activation-function-in-python


import  csv
import  sys
import  os.path
import  matplotlib.pyplot as plt
from pathlib import Path
import math
import random
import json

class LogisticRegression :

    def __init__(self, learning_rate=0.01) :
        self.model_load = False
        self.lr = learning_rate
        self.num_features = 0
        self.features_names = []
        self.features = []
        self.classes = []
        self.num_classes = 0
        # Initialize 
        self.means = []
        self.stds = []
        self.weights = []
        self.bias = []
        # To plot de evolution of cost when training
        self.cost_history = []       

    # z-score normalization 
    def z_normalize(self, data):
        num_rows = len(data)
        num_cols = len(data[0])
        means = []
        stds = []
        # 1. Calcular media y std por cada columna
        for j in range(num_cols):
            col = [data[i][j] for i in range(num_rows)]
            mean = sum(col) / num_rows
            variance = sum((v - mean) ** 2 for v in col) / num_rows
            std = math.sqrt(variance) if variance > 0 else 1.0
            means.append(mean)
            stds.append(std)

        # 2. Crear nueva matriz normalizada
        normalized_data = [
            [(data[i][j] - means[j]) / stds[j] for j in range(num_cols)]
            for i in range(num_rows)
        ]
        self.means = means
        self.stds = stds
        print(" Data has been normalized")
        return normalized_data
    
    # Convert class index to one-hot vector.
    def one_hot_encode(self,y):
        i = 0
        encode = []
        while i < self.num_classes:
            if y == self.classes_names[i]:
                encode.append(1)
            else:
                encode.append(0)
            i = i + 1
        return encode
    
    # Compute cross-entropy loss for one sample.
    def cross_entropy_loss(self,y_true, y_pred):
        epsilon = 1e-15      # Avoid log(0) by adding a small epsilon
        return -sum(y_true[i] * math.log(y_pred[i] + epsilon) for i in range(len(y_true)))
    
    # Compute softmax values for a list of scores
    def softmax(self,z):
        max_z = max(z)  # for numerical stability
        exp_vals = [math.exp(v - max_z) for v in z]
        total = sum(exp_vals)
        return [ev / total for ev in exp_vals]
    
    # Optimizes weights and bias by minimizing the cost function
    def fit(self, X, y, epochs=1000):
        # Init variables Ordenamos las clases para garantizar comsistencia --------------------
        # Clases
        self.classes_names = sorted(list(set(y[1:])))
        self.classes = y[1:]
        self.num_classes = len(set(y[1:]))
        # Features
        self.features_names  = X[0] 
        self.features  = X[1:]
        self.num_features = len(X[0])
        
        #print(self.num_classes ,self.classes, len(self.classes))
        #print(self.num_features, self.features)
        print(self.features[0])
         # Z-score to normalize feature data
        self.features = self.z_normalize(self.features)
        print(self.num_classes ,self.classes_names)
        print(self.num_features, self.features_names)
        print(self.features[0])
        #exit()
        # Initializar weights and bias
        self.weights = [[random.uniform(-0.01, 0.01) for _ in range(self.num_features)] 
                        for _ in range(self.num_classes)]
        self.bias = [0.0 for _ in range(self.num_classes)]
        self.cost_history = []
        m = len(self.features)
        step = max(1, epochs // 10)  # Evita ZeroDivisionError si epochs < 10
        # Train model------------------------
        # # Gradient descent: empezamos iteraciones
        for epoch in range(epochs):
            total_loss = 0.0     # inicializa loss en cada epoch           
            # Creo los indices
            indices = list(range(m))
            random.shuffle(indices)     # mezclar índices en cada epoch 
            for i in indices:
                ######### FORWARD PASS ##############################
                # probilidad = (w1*F1 + w2*F2 +..+ b1) x cada clase -> luego aplica soft para dejarlo [1, 0, ...]
                probs = self.predict_proba(self.features[i])
                y_true = self.one_hot_encode(self.classes[i]) # -> [0, 1, ]
                total_loss += self.cross_entropy_loss(y_true, probs)
                ########## BACKPROPAGATION ###########################
                for c in range(self.num_classes):
                    error = probs[c] - y_true[c]
                    for j in range(self.num_features):
                        self.weights[c][j] -= self.lr * error * self.features[i][j]
                    self.bias[c] -= self.lr * error

            if (epoch + 1) % step == 0:
                print(f"Epoch {epoch+1}/{epochs} - Loss: {total_loss/len(self.features):.4f}")
                self.cost_history.append(total_loss/len(self.features))
        self.model_load = True
    
    # Test data
    def test(self, X_test, y_test, output_file="house.csv"):
        # 1. Verificar que el modelo esté entrenado o cargado
        if not self.model_load:
          print("\n\033[1;31m┌──────────────────────────────────────────────────┐")
          print("│  ❌ ERROR: No model loaded                       │")
          print("│  👉 Please train or load a model first           │")
          print("└──────────────────────────────────────────────────┘\033[0m\n")
          sys.exit(1)

        # 2. Verificar que X_test no esté vacío y coincida en número de columnas
        if not X_test or len(X_test[0]) != self.num_features:
          actual_features = len(X_test[0]) if X_test else 0
          print("\n\033[1;31m┌──────────────────────────────────────────────────┐")
          print("│  ❌ ERROR: Feature dimension mismatch            │")
          print(
              f"│  Expected: {self.num_features} features | Got:"
              f" {actual_features:<15} │"
          )
          print("└──────────────────────────────────────────────────┘\033[0m\n")
          sys.exit(1)
        # Comprobamos X_test[0][0] para detectar si la fila 0 es encabezado
        start_idx = (
            1 if (len(X_test) > 0 and isinstance(X_test[0][0], str)) else 0
        )
        correct = 0
        total = 0
        with open(output_file, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Index", "Hogwarts House"])
            for i in range(start_idx, len(X_test)):
                row = X_test[i]
                true_label = y_test[i]

                # Reemplazar cualquier NaN por la media en el modelo entrenamiento antes de predecir
                clean_row = [
                    self.means[j]
                    if (isinstance(row[j], float) and math.isnan(row[j]))
                    else float(row[j])
                    for j in range(self.num_features)
                ]
                # normalize row
                normalize_row = [
                    (clean_row[j] - self.means[j]) / self.stds[j]
                    for j in range(self.num_features)
                ]             
                pred_label = self.predict(normalize_row)
                if pred_label == true_label:
                    correct += 1
                total += 1
                # Escribir en CSV (índice empieza en 0)
                writer.writerow([total, pred_label])
        accuracy = (correct / total) * 100 if total > 0 else 0.0
        print(f"Accuracy: {accuracy:.2f}% ({correct}/{total} aciertos)")
        return accuracy
  
    #Predict class probabilities for a single sample. Use in Train
    def predict_proba(self, x):
        z = []
        for c in range(self.num_classes):
            z_c = sum(self.weights[c][j] * x[j] for j in range(self.num_features)) + self.bias[c]
            z.append(z_c)
        return self.softmax(z)
    
    #predict class label for a single sample
    def predict(self, x):
        probs = self.predict_proba(x)
        #return probs.index(max(probs))
        return self.classes[probs.index(max(probs))]
    
    # Save Model
    def save_model(self,file_path):
        model_data = {
            "means": self.means,
            "stds": self.stds,
            "num_classes": self.num_classes,
            "classes": self.classes_names,
            "num_features": self.num_features,
            "features": self.features_names,
            "weights": self.weights,
            "bias": self.bias,
            "learning_rate": self.lr
        }
        with open(file_path, "w") as f:
            json.dump(model_data, f, indent=4)

    # Load Model
    def load_model(self,file_path):
        with open(file_path, "r") as f:
            model_data = json.load(f)
        self.means = model_data["means"]
        self.stds = model_data["stds"]
        self.num_classes = model_data["num_classes"]
        self.classes = model_data["classes"]
        self.num_features = model_data["num_features"]
        self.features = model_data["features"]
        self.weights = model_data["weights"]
        self.bias = model_data["bias"]
        self.lr = model_data["learning_rate"]
        self.model_load = True
        return 
        
    
    # GETTERS
    def get_weights(self):
        return self.weights   
     
    def get_bias(self):
        return self.bias
    
    # get the index number of a class
    def get_index_class(self, y):
        i = 0
        while i < self.num_classes:
            if y == self.classes[i]:
                return i    
            i = i +1
        return
   
    # SETTERS
    def set_weights(self, weights):
        self.weights = weights
        return
    def set_bias(self, bias):
        self.weights = bias
        return