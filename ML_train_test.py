# Import train_test_split function
# Import Gaussian Naive Bayes model
# Import LabelEncoder
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from joblib import dump

csv_file = 'ML_data/Publication.csv'
bin_width = 1000
no_of_intervals = 3

# Load dataset
FoR_df = pd.read_csv(csv_file)
max_val = bin_width * no_of_intervals


def value_to_label(val):
    if val * bin_width == max_val:
        return 'greater than ' + str(max_val)
    else:
        return '[' + str(val * bin_width) + '-' + str(val * bin_width + bin_width) + ')'


labels = list(map(value_to_label, range(no_of_intervals + 1)))

# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(FoR_df[['year']].values, FoR_df['label'].values,
                                                    test_size=0.3)  # 70% training and 30% test

# Create a Decision Tree Classifier
clf = DecisionTreeClassifier()

# Train Decision Tree Classifer
clf.fit(X_train,y_train)

# Create a Gaussian Classifier
gnb = GaussianNB()

# Train the model using the training sets
gnb.fit(X_train, y_train)

# Model Accuracy, how often is the classifier correct?
print("Accuracy on Decision Tree Test: ", clf.score(X_test, y_test))
print("Accuracy on Decision Tree Train: ", clf.score(X_train, y_train))

print("Accuracy on Naive Bayes Test: ", gnb.score(X_test, y_test))
print("Accuracy on Naive Bayes Train: ", gnb.score(X_train, y_train))

y_pred_clf = clf.predict(X_test)
y_pred_gnb = gnb.predict(X_test)

mat_clf = confusion_matrix(y_test, y_pred_clf)
mat_gnb = confusion_matrix(y_test, y_pred_gnb)

fig, ax = plt.subplots(figsize=(8, 8))  # Sample fig size in inches
sns.heatmap(mat_clf.T, square=True, annot=True, fmt='d', cbar=False, xticklabels=labels, yticklabels=labels, ax=ax)
plt.xlabel('true label')
plt.ylabel('predicted label')
plt.show()

fig1, ax1 = plt.subplots(figsize=(8, 8))  # Sample fig size in inches
sns.heatmap(mat_gnb.T, square=True, annot=True, fmt='d', cbar=False, xticklabels=labels, yticklabels=labels, ax=ax1)
plt.xlabel('true label')
plt.ylabel('predicted label')
plt.show()

dump(gnb, 'ML_data/Naive_Publication.joblib')
dump(clf, 'ML_data/Decision_Publication.joblib')
