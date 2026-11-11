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

class logistic_regression :

    def __init__(self, learning_rate=0.01) :
        self.lr = learning_rate
        self.num_features = 0
        self.features = []
        self.classes = []
        self.num_classes = 0
        # Initialize 
        self.weights = []
        self.bias = []
        # To plot de evolution of cost when training
        self.cost_history = []       

    #def z_normalize(data):
	#    mean = custom_mean(data, axis=0)
	#   std = custom_std(data, axis=0)  # Use ddof=1 for sample standard deviation
	#   normalized_data = (data - mean) / std
    #   return normalized_data, mean, std

    # Convert class index to one-hot vector.
    def one_hot_encode(self,y):
        i = 0
        encode = []
        while i < self.num_classes:
            if y == self.classes[i]:
                encode.append(1)
            else:
                encode.append(0)
            i = i + 1
        return encode
        #return [1 if i == y else 0 for i in range(num_classes)]
    
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
    
    #Predict class probabilities for a single sample.
    def predict_proba(self, x):
        z = []
        for c in range(self.num_classes):
            z_c = sum(self.weights[c][j] * x[j] for j in range(self.num_features)) + self.bias[c]
            z.append(z_c)
        #print("predict:",z)
        #print("softmax:",self.softmax(z))
        return self.softmax(z)
    
    #predict class label for a single sample
    def predict(self, x):
        probs = self.predict_proba(x)
        #return probs.index(max(probs))
        return self.classes[probs.index(max(probs))]
    
    # Optimizes weights and bias by minimizing the cost function
    def fit(self, X, y, epochs=1000):
        # Init variables --------------------
        self.classes = list(set(y[1:]))
        self.num_classes = len(set(y[1:]))
        self.features  = X[0]
        self.num_features = len(X[0])
        
        print(self.num_classes ,self.classes, len(self.classes))
        print(self.num_features, self.features)

        # Initialize weights and bias
        self.weights = [[random.uniform(-0.01, 0.01) for _ in range(self.num_features)] 
                        for _ in range(self.num_classes)]
        self.bias = [0.0 for _ in range(self.num_classes)]
        
        #print("Aqui",self.weights, self.bias)
        #return()
        # Train model------------------------
        # # Gradient descent: start iterations
        for epoch in range(epochs):
            total_loss = 0.0
            i = 1
            total_X = len(X)
            while i < total_X:
                # Forward pass
                # probilidad = (w1*F1 + w2*F2 +..+ b1) x cada clase -> luego aplica soft para dejarlo [1, 0, ...]
                probs = self.predict_proba(X[i])
                #y_true = self.one_hot_encode(self.get_index_class(y[i]), self.num_classes)
                y_true = self.one_hot_encode(y[i]) # -> [0, 1, ]
                #print(self.classes)
                #print(y[i],self.get_index_class(y[i]))
                #print("Features:",X[i])
                #print("y_true:",y_true, "probs:",probs)
                loss = self.cross_entropy_loss(y_true, probs)
                total_loss += loss
            
                # Backpropagation
                for c in range(self.num_classes):
                    error = probs[c] - y_true[c]
                    for j in range(self.num_features):
                        self.weights[c][j] -= self.lr * error * X[i][j]
                    self.bias[c] -= self.lr * error
                i = i + 1
            if (epoch + 1) % (epochs // 10) == 0:
                print(f"Epoch {epoch+1}/{epochs} - Loss: {total_loss/len(X):.4f}")
                self.cost_history.append(total_loss/len(X))
            # make array 
            #z = self.mydot(X, self.weights) + self.bias
            # make a array prediction
            #h = self.sigmoid(z)
            #iter = iter + 1
            
            # calculate error
            #dw = (1/m) * self.mydot(X.T, (h - y))
            #db = (1/m) * np.sum(h - y)

            # change weights and bias by learning rate 
            #self.weights -= self.lr * dw 
            #self.bias -= self.lr * db

            #self.cost_history.append(self.cost(h, y))
    
    def save_model(self,file_path):
        model_data = {
            "weights": self.weights,
            "bias": self.bias,
            "classes": self.classes,
            "features": self.features,
            "learning_rate": self.lr
            #"normalization_parameters": norm_params.tolist()
        }
        
        with open(file_path, "w") as f:
            json.dump(model_data, f, indent=4)
 
    def load_model(self,file_path):
        with open(file_path, "r") as f:
            model_data = json.load(f)
        
        self.weights = model_data["weights"]
        self.bias = model_data["bias"]
        self.classes = model_data["classes"]
        self.features = model_data["features"]
        self.num_classes = len(self.classes )
        self.num_features = len(self.features)
        self.lr = model_data["learning_rate"]
        #norm_params = np.array(model_data["normalization_parameters"])
        #class_name = list(model_data["class_order"])
        return 
        #return weights, bias, class_name, norm_params
    
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