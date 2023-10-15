# Import necessary libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, roc_curve, roc_auc_score
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Load the IMDb movie review dataset
data = pd.read_csv('path/to/imdb_dataset.csv')
data = data.sample(frac=1, random_state=42)  # Shuffle the dataset

# Preprocess the data
stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    words = word_tokenize(text)
    filtered_words = [word.lower() for word in words if word.isalnum() and word.lower() not in stop_words]
    return ' '.join(filtered_words)

data['review'] = data['review'].apply(preprocess_text)

# Split the data into training and testing sets
X = data['review']
y = data['sentiment']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Vectorize the text data using CountVectorizer
vectorizer = CountVectorizer()
X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)

# Train a Multinomial Naive Bayes classifier
nb_classifier = MultinomialNB()
nb_classifier.fit(X_train_vectorized, y_train)

# Make predictions on the test data
y_nb_pred = nb_classifier.predict(X_test_vectorized)

# Calculate accuracy
nb_accuracy = accuracy_score(y_test, y_nb_pred)
print("Multinomial Naive Bayes Accuracy:", nb_accuracy)

# Classification report
nb_classification_report = classification_report(y_test, y_nb_pred)
print("\nMultinomial Naive Bayes Classification Report:\n", nb_classification_report)

# Confusion matrix
nb_confusion_matrix = confusion_matrix(y_test, y_nb_pred)
print("\nMultinomial Naive Bayes Confusion Matrix:\n", nb_confusion_matrix)


# Import necessary libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense
from tensorflow.keras.optimizers import Adam
from sklearn.metrics import accuracy_score, classification_report

# Load the IMDb movie review dataset
# You can download it from: https://ai.stanford.edu/~amaas/data/sentiment/
data = pd.read_csv('path/to/imdb_dataset.csv')
data = data.sample(frac=1, random_state=42)  # Shuffle the dataset

# Preprocess the data
max_words = 5000
max_sequence_length = 300

tokenizer = Tokenizer(num_words=max_words)
tokenizer.fit_on_texts(data['review'])
X = tokenizer.texts_to_sequences(data['review'])
X = pad_sequences(X, maxlen=max_sequence_length)

label_encoder = LabelEncoder()
y = label_encoder.fit_transform(data['sentiment'])

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build an LSTM-based model
model = Sequential()
model.add(Embedding(input_dim=max_words, output_dim=128, input_length=max_sequence_length))
model.add(LSTM(128))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer=Adam(learning_rate=0.001), metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=5, batch_size=64, validation_split=0.2)

# Evaluate the model
y_pred = (model.predict(X_test) > 0.5).astype(int)
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred, target_names=label_encoder.classes_)

print("Accuracy:", accuracy)
print("\nClassification Report:\n", report)



# Predictions from the LSTM model
y_lstm_pred = (model.predict(X_test) > 0.5).astype(int)

# Calculate accuracy
lstm_accuracy = accuracy_score(y_test, y_lstm_pred)
print("\nLSTM-Based Deep Learning Model Accuracy:", lstm_accuracy)

# Classification report
lstm_classification_report = classification_report(y_test, y_lstm_pred, target_names=label_encoder.classes_)
print("\nLSTM-Based Deep Learning Model Classification Report:\n", lstm_classification_report)

# Confusion matrix
lstm_confusion_matrix = confusion_matrix(y_test, y_lstm_pred)
print("\nLSTM-Based Deep Learning Model Confusion Matrix:\n", lstm_confusion_matrix)



# Calculate ROC curve and ROC AUC score for Multinomial Naive Bayes
y_nb_prob = nb_classifier.predict_proba(X_test_vectorized)[:, 1]
fpr_nb, tpr_nb, _ = roc_curve(y_test, y_nb_prob)
roc_auc_nb = roc_auc_score(y_test, y_nb_prob)

# Calculate ROC curve and ROC AUC score for LSTM model
y_lstm_prob = model.predict(X_test)
fpr_lstm, tpr_lstm, _ = roc_curve(y_test, y_lstm_prob)
roc_auc_lstm = roc_auc_score(y_test, y_lstm_prob)

# Plot ROC curves
plt.figure(figsize=(8, 6))
plt.plot(fpr_nb, tpr_nb, label=f'Multinomial Naive Bayes (AUC = {roc_auc_nb:.2f})')
plt.plot(fpr_lstm, tpr_lstm, label=f'LSTM-Based Deep Learning (AUC = {roc_auc_lstm:.2f})')
plt.plot([0, 1], [0, 1], 'k--', color='gray')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC) Curve')
plt.legend(loc='lower right')
plt.show()
