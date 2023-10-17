# Diebetes Predictor application using Descision Tree algorithm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

def Diabetes_Decision_Tree():
    diabetes = pd.read_csv(r'C:\backup\Python\ML\Datasets\diabetes.csv')

    print("Columns of Dataset")
    print(diabetes.columns)

    print("First 5 records of Dataset")
    print(diabetes.head())

    print("Dimension of diabetes data: {}".format(diabetes.shape))

    X_train, X_test, Y_train, Y_test = train_test_split(diabetes.loc[:, diabetes.columns != 'Outcome'], diabetes['Outcome'], stratify=diabetes['Outcome'],random_state=66)

    tree = DecisionTreeClassifier(random_state=0)
    tree.fit(X_train, Y_train)

    print("Accuracy on Training set: {:.3f}".format(tree.score(X_train, Y_train)))
    print("Accuracy on test set: {:.3f}".format(tree.score(X_test, Y_test)))

    tree = DecisionTreeClassifier(max_depth=3, random_state=0)
    tree.fit(X_train, Y_train)

    print("Accuracy on training set: {:.3f}".format(tree.score(X_train, Y_train)))
    print("Accuracy on test set: {:.3f}".format(tree.score(X_test, Y_test)))

    print("Feature importances: \n{}".format(tree.feature_importances_))

    plt.figure(figsize=(8,6))
    n_features = 8
    plt.barh(range(n_features), tree.feature_importances_, align='center')
    diabetes_features = []
    for i,x in enumerate(diabetes.columns):
        if i != 8:
            diabetes_features.append(x)
    plt.yticks(np.arange(n_features), diabetes_features)
    plt.xlabel("Feature importance")
    plt.ylabel("Feature")
    plt.ylim(-1, n_features)
    plt.show()




def main():
    print("----- Diabetes predictor using Decision Tree -----")
    Diabetes_Decision_Tree()

if __name__ == "__main__":
    main()
