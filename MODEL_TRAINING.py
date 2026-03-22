# 5. TRAIN-TEST SPLIT
# ================================
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

# ================================
# 6. MODEL TRAINING
# ================================
model = LinearRegression()
model.fit(X_train, y_train)