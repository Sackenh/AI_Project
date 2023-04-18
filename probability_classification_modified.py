from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.linear_model import LogisticRegression
from sklearn import svm
from data_sanatizer import * 
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

data = create_correlation_matrix()

X = data
Y = data['num']

X_test, X_train, Y_test, Y_train = train_test_split(X, Y, test_size=.25, random_state=22)

C=10
kernel = 1.0 * RBF([1.0, 1.0])

print(f"--------------------  X Training Data ---------------\n{X_test}")
print(f"--------------------  X Test Data ---------------\n{X_train}") #showing the difference in amount of data
print(f"-------------------- Y Training Data ---------------\n{Y_test}")
print(f"--------------------  Y Test Data ---------------\n{Y_train}")     #<---- displaying the training sets, uncomment to see actual values

classifiers = {
    "L1 logistic": LogisticRegression(
        C=C, penalty="l1", solver="saga", multi_class="multinomial", max_iter=10000
    ),
    "L2 logistic (Multinomial)": LogisticRegression(
        C=C, penalty="l2", solver="saga", multi_class="multinomial", max_iter=10000
    ),
    "L2 logistic (OvR)": LogisticRegression(
        C=C, penalty="l2", solver="saga", multi_class="ovr", max_iter=10000
    )
}

n_classifiers = len(classifiers)

plt.figure(figsize=(3 * 2, n_classifiers * 2))
plt.subplots_adjust(bottom=0.2, top=0.95)

xx = np.linspace(3, 9, 100)
yy = np.linspace(1, 5, 100).T
xx, yy = np.meshgrid(xx, yy)
Xfull = np.c_[xx.ravel(), yy.ravel()]


for index, (name, classifier) in enumerate(classifiers.items()):
    classifier.fit(X, Y)

    y_pred = classifier.predict(X)
    accuracy = accuracy_score(Y, y_pred)
    print("Accuracy (train) for %s: %0.1f%% " % (name, accuracy * 100))

