import pandas as pd
mydata = pd.read_csv("Covid-Dataset-with-numbers-and-restricted-columns.csv", sep=";")

myfeatures = mydata.iloc[:, 0:-1]

mytargets = mydata.iloc[:, -1]

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(myfeatures, mytargets, test_size=0.25, random_state=0)

from sklearn.linear_model import LogisticRegression
logisticRegr = LogisticRegression()
logisticRegr.fit(x_train, y_train)

def result():
    return "hi"

for sample_id in range(0, 20):
    print("id: {}".format(sample_id))
    mytest = x_test.iloc[sample_id, :]
    type(x_test)
    print(mytest)
    predicted_value = logisticRegr.predict(mytest.values.reshape(1, -1))
    predicted_probs = logisticRegr.predict_proba(mytest.values.reshape(1,-1))
    print(predicted_probs)
    print("predicted_value: {}".format(predicted_value))
    print(predicted_probs[0][predicted_value])
    print("actual value: {}".format(y_test.iloc[sample_id]))


def result2(mytest):
    predicted_value = logisticRegr.predict(mytest)
    predicted_probs = logisticRegr.predict_proba(mytest)
    return predicted_probs

