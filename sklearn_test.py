# https://www.datacamp.com/es/tutorial/understanding-logistic-regression-python
# https://prasunmaity.medium.com/logistic-regression-unlocked-practical-guide-with-data-cleaning-feature-engineering-and-more-bd4b725d4f3f
# https://medium.com/@jshaik2452/multi-class-logistic-regression-a-friendly-guide-to-classifying-the-many-4a590c2e6c26
# https://www.datacamp.com/tutorial/understanding-logistic-regression-python

import pandas as pd

from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import normalize

#col_names = ['pregnant', 'glucose', 'bp', 'skin', 'insulin', 'bmi', 'pedigree', 'age', 'label']
df = pd.read_csv("dataset_train.csv", header=0)
print(df.head())

print(df.columns)

#### 3. Data Preprocessing:

# Take a look at the first few rows
print(df.info())

# Check for any missing values
print(df.isnull().sum())
# Handle missing values (if any)
df = df.dropna()  # Example of dropping rows with missing values
# 
df.drop(columns=['Index','First Name','Last Name','Birthday','Best Hand'], inplace=True)

# Encode categorical variables (if applicable)
#df = pd.get_dummies(df, drop_first=True)  # Convert categorical variables to dummy/indicator variables
print(df.head())

#### 4. Define features and target
X = df[['Arithmancy','Astronomy','Herbology','Defense Against the Dark Arts','Divination','Muggle Studies','Ancient Runes','History of Magic','Transfiguration','Potions','Care of Magical Creatures','Charms','Flying']]
y = df['Hogwarts House']

# Normalize data https://scikit-learn.org/stable/modules/preprocessing.html
X_scale = normalize(X,norm='l2')
print(X_scale)
#exit()

#### 5. Split the Data into Training and Test Sets:
# Split the data into training and testing sets
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
X_train = X_scale
y_train = y

# Check the shapes of the resulting datasets
#print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)
print(X_train.shape, y_train.shape)

#### 6. Train the Logistic Regression Model:
# instantiate the model (using the default parameters)
# We set multi_class='multinomial' for softmax, and solver='lbfgs' for efficiency
model = LogisticRegression(multi_class='multinomial', solver='lbfgs',max_iter=1000)

# fit the model with training data
model.fit(X_train, y_train)

# Output the coefficients
print('Intercept:', model.intercept_)
print('Coefficients:', model.coef_)

#### 7. Make Predictions:
#y_pred = logreg.predict(X_test)

#### 8. Evaluate the Model:
# Evaluate the model
# accuracy = accuracy_score(y_test, y_pred)
# conf_matrix = confusion_matrix(y_test, y_pred)
# class_report = classification_report(y_test, y_pred)

# print(f'Accuracy: {accuracy:.2f}')
# print(f'Confusion Matrix:\n{conf_matrix}')
#print(f'Classification Report:\n{class_report}')