import pandas as pd

# Load the dataset
train_data = pd.read_csv('train.csv')
test_data = pd.read_csv('test.csv')

# Display the first few rows of the training data
print(train_data.head())

# Display basic information about the dataset
print(train_data.info())

# Check for missing values
print(train_data.isnull().sum())

# Summary statistics
print(train_data.describe())

# Fill missing values for 'Age' with the median age
train_data['Age'].fillna(train_data['Age'].median(), inplace=True)

# Fill missing values for 'Embarked' with the most common port
train_data['Embarked'].fillna(train_data['Embarked'].mode()[0], inplace=True)

# Convert 'Sex' to numerical values (male = 0, female = 1)
train_data['Sex'] = train_data['Sex'].map({'male': 0, 'female': 1})

# Convert 'Embarked' to numerical values
train_data['Embarked'] = train_data['Embarked'].map({'C': 0, 'S': 1, 'Q': 2})

# Drop irrelevant features
train_data = train_data.drop(['Name', 'Ticket', 'Cabin'], axis=1)

# Prepare features and target variable
X = train_data.drop('Survived', axis=1)
y = train_data['Survived']

from sklearn.model_selection import train_test_split

X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Initialize the model
model = RandomForestClassifier(random_state=42)

# Train the model
model.fit(X_train, y_train)

# Predict on the validation set
y_val_pred = model.predict(X_val)

# Evaluate the model
accuracy = accuracy_score(y_val, y_val_pred)
print(f"Validation Accuracy: {accuracy:.2f}")
print(classification_report(y_val, y_val_pred))

# Preprocess the test data
test_data['Age'].fillna(test_data['Age'].median(), inplace=True)
test_data['Embarked'].fillna(test_data['Embarked'].mode()[0], inplace=True)
test_data['Sex'] = test_data['Sex'].map({'male': 0, 'female': 1})
test_data['Embarked'] = test_data['Embarked'].map({'C': 0, 'S': 1, 'Q': 2})
test_data = test_data.drop(['Name', 'Ticket', 'Cabin'], axis=1)

# Predict on test data
X_test = test_data.drop('PassengerId', axis=1)
predictions = model.predict(X_test)

# Create a submission DataFrame
submission = pd.DataFrame({
    'PassengerId': test_data['PassengerId'],
    'Survived': predictions
})

# Save the submission file
submission.to_csv('titanic_predictions.csv', index=False)
