This project is an implementation of a custom K Nearest Neighbour (KNN) algorithm for classification using Python. Here's a brief summary of the project:

- Custom KNN Algorithm: The project focuses on creating a custom KNN classifier, named "MarvellousKNN." This classifier is designed to perform classification tasks using a KNN approach.

- Methods in MarvellousKNN Class:
  - `fit()`: This method initializes the training data and their corresponding target labels inside the MarvellousKNN class.
  - `predict()`: It creates a prediction array, storing the shortest distance between all test data and training data elements. It relies on the "closest" method.
  - `closest()`: This method calculates the shortest distance using the Euclidean distance algorithm.

- Characteristics:
  - Classifier: User-defined K Nearest Neighbour
  - DataSet: Iris Dataset
  - Features: Sepal width, Sepal Length, Petal Width, Petal Length
  - Labels: Versicolor, Setosa, Virginica
  - Training Dataset: 75 Entries
  - Testing Dataset: 75 Entries

The primary objecve of this project is to create a custom KNN classifier for the Iris dataset, demonstrating the core principles of KNN classification. The dataset consists of features related to iris flowers and their respective labels. By implementing a user-defined KNN algorithm, this project provides a hands-on understanding of how KNN works for classification tasks and is tailored to the Iris dataset with a training and testing split of 75 entries each.