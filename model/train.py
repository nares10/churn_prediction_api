import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score

# Load data
df = pd.read_csv("data/churn_100k.csv")

# Target
df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0})

X = df[["Tenure", "MonthlyCharges", "Contract", "PaymentMethod", "TotalCharges" ]]
y = df["Churn"]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Preprocessing
categorical_features = ["Contract", "PaymentMethod"]
numerical_features = ["Tenure", "MonthlyCharges", "TotalCharges" ]

preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features),
        ("num", "passthrough", numerical_features),
    ]
)

# Model
model = LogisticRegression(max_iter=1000)

pipeline = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("model", model),
    ]
)

# Train
pipeline.fit(X_train, y_train)

# Evaluate
y_pred_proba = pipeline.predict_proba(X_test)[:, 1]
auc = roc_auc_score(y_test, y_pred_proba)

print(f"ROC-AUC: {auc:.8f}")

# Save model
with open("model/churn_model.pkl", "wb") as f:
    pickle.dump(pipeline, f)

