import kaggle

# Assuming you are running run_me.py from the Submission/Code
# directory, otherwise the path variable will be different for you
import numpy as np
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.cross_validation import cross_val_score
#Load the Advertisements Data
path = '../../Data/Advertisements/'
data = np.load(path + 'Data.npz')
features_train = data['X_train']
labels_train = data['y_train']
features_test = data['X_test']
labels_test = data['y_test']
print "Advertisements:", features_train.shape, labels_train.shape, features_test.shape, labels_test.shape 

datasets = np.concatenate(features_train,labels_train)

def:
    
training_set = datasets[]
validation_set = datasets[]
test_set = datasets[]

#clf = SVC()
for i in (1,2,3,4,5,6,7,8,9):
   clf = KNeighborsClassifier(n_neighbors=i)
   clf.fit(features_train, labels_train)
   score_svm = cross_val_score(clf,features_train, labels_train)
   print score_svm.mean()
   pred = clf.predict(features_test)
   #print pred
   #print '\n'


"""
   a=0
   for x,y in zip(pred,labels_test):
      #print x,y
      a=a+(x==y).sum()

   print a
"""
   #Save prediction file in Kaggle format
   #predictions = np.zeros(labels_test.shape)
   #kaggle.kaggleize(predictions, "../Predictions/Advertisements/test.csv")




#Load the FirstOrderLogic Data
path = '../../Data/FirstOrderLogic/'
data = np.load(path + 'Data.npz')
features_train = data['X_train']
labels_train = data['y_train']
features_test = data['X_test']
labels_test = data['y_test']
print "FirstOrderLogic:", features_train.shape, labels_train.shape, features_test.shape, labels_test.shape 

#Save prediction file in Kaggle format
predictions = np.zeros(labels_test.shape)
kaggle.kaggleize(predictions, "../Predictions/FirstOrderLogic/test.csv")


#Load the Income Data
path = '../../Data/Income/'
data = np.load(path + 'Data.npz')
features_train = data['X_train']
labels_train = data['y_train']
features_test = data['X_test']
labels_test = data['y_test']
print "Income:", features_train.shape, labels_train.shape, features_test.shape, labels_test.shape 

#Save prediction file in Kaggle format
predictions = np.zeros(labels_test.shape)
kaggle.kaggleize(predictions, "../Predictions/Income/test.csv")


#Map features values for Income Data set
#For details see http://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html}{sklearn LabelEncoder documentation} for more information.
les = np.load(path + 'labelencoders.npy').item()
# Print the indices of the features that were originally transformed from strings
print(les.keys())
# The workclass feature is at index 1 in the feature set
idx = 1
# Transform workclass values to string representation
workclass_string = les[idx].inverse_transform(features_train[:,idx].astype(int))
print workclass_string
