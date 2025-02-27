import joblib
from sklearn.linear_model import LogisticRegression
import numpy as np

X_train = np.random.rand(100, 2)
y_train = (X_train[:, 0] + X_train[:, 1] > 1).astype(int)

model = LogisticRegression()
model.fit(X_train, y_train)

joblib.dump(model, "model.pkl")
