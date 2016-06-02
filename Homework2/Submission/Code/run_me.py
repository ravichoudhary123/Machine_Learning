import kaggle

# Assuming you are running run_me.py from the Submission/Code
# directory, otherwise the path variable will be different for you
#Import Packages
import numpy as np
from sklearn import tree, grid_search

from time import time
from sklearn import svm, datasets, feature_selection
#from sklearn.feature_selection import SelectFromModel
from plotting import plot_score_linechart

from sklearn.pipeline import Pipeline
from sklearn import ensemble
from sklearn.linear_model import *

def choose_regression_model(problem_instance):
    if problem_instance == 1:
        #Load the Computer Activity Data
        path = '../../Data/ComputerActivity/'
    elif problem_instance == 2:
        #Load the Housing Data
        path = '../../Data/Housing/'

    data = np.load(path + 'Data.npz')
    features_train = data['X_train']
    labels_train = data['y_train']
    features_test = data['X_test']
    labels_test = data['y_test']
    n_estimator = []
    print("Computer Activity:", features_train.shape, labels_train.shape, features_test.shape, labels_test.shape)

    #Regression Method
    if problem_instance == 1:
        print("Executing Computer Activity problem")
        #transform = feature_selection.SelectKBest(feature_selection.f_regression)
        transform = feature_selection.RFECV(estimator = RidgeCV())
        pipeline = Pipeline([('anova', transform), ('adr', ensemble.GradientBoostingRegressor(random_state=404))])
        n_estimator = np.arange(75, 86, 1)
        depth = range(6, 8)
        #n_estimator = np.arange(10, 100, 10)
        parameters = {'anova__cv': [5,10],
                      #'anova__k': np.arange(15, 22, 1),
                      'adr__n_estimators': n_estimator,
                      'adr__max_depth': depth
                      }
    elif problem_instance == 2:
        print("Executing Housing problem")
        transform = feature_selection.SelectKBest(feature_selection.f_regression)
        #transform = feature_selection.RFECV(estimator = RidgeCV())
        n_estimator = np.arange(130, 160, 10)
        #n_estimator = np.arange(10, 100, 1)
        depth = range(6,8)
        pipeline = Pipeline([('anova', transform), ('adr', ensemble.GradientBoostingRegressor(random_state=404))])
        parameters = {'anova__k': np.arange(5, 9, 1),
                      #'anova__cv': [5,10],
                      'adr__n_estimators': n_estimator, #50
                      'adr__max_depth': depth
                      }
    grid = grid_search.GridSearchCV(pipeline, parameters, n_jobs=-1, verbose=1)
    grid.fit(features_train, labels_train)
    predictions = grid.predict(features_test)
    print(grid.best_params_, grid.best_score_, grid.best_estimator_, grid.grid_scores_)
    scores = grid.grid_scores_
    #print(type(scores), len(scores))
    mean_score_list = []
    parameters_list = []
    for x in range(0, len(scores)):
        mean_score_list.append(scores[x][1])
        parameters_list.append(scores[x][0])
    print(mean_score_list)
    #print(parameters_list)
    scores_list = np.array(mean_score_list)
    plot_score_linechart(scores_list, problem_instance)
    if problem_instance ==1:
        kaggle.kaggleize(predictions, "../Predictions/ComputerActivity/test.csv")
    else:
        kaggle.kaggleize(predictions, "../Predictions/Housing/test.csv")


for problem in range(1,3):
    t1 = time()
    choose_regression_model(problem)
    t2 = time()
    print("Time taken in seconds: %f" % (t2-t1))
