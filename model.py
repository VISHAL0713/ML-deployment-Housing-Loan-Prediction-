import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier

loan_data = pd.read_csv('home_loan_assignment.csv')

X=loan_data.drop("Loan_Status",axis=1)
X = X.values
y=loan_data[["Loan_Status"]]
y = y.values
x_train,x_test,y_train,y_test=train_test_split(X,y,test_size=.60)
classifier = DecisionTreeClassifier()
classifier.fit(x_train,y_train)
pred_cv_forest=classifier.predict(x_test)
#export the model
pickle.dump(classifier, open('model.pkl','wb'))
#load the model and test with a custom input
model = pickle.load( open('model.pkl','rb'))
x = [[1,0,0,0,0,141.0,360.0,1.0,5849.0]]
predict = model.predict(x)
print("Hello Worlds")
print(predict[0])