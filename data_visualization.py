import  matplotlib.pyplot as plt
import numpy as np

class data_visualization:

    def __init__(self) :

        # init parameters
        self.size = {0, 0}
        self.data = []
        self.nb_features = 0
        
    def histogram(self):
            x = np.random.normal(170, 10, 250)
            plt.hist(x)
            #plt.title('Real values')
            #plt.xlabel('Mileage')
            #plt.ylabel('Price')
 
            plt.show()

    def scatter(self, x, y):
            print("scatter")
           # x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
           # y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

            plt.scatter(x, y)
            plt.show()

    def pair(self):
            print("pair")



        