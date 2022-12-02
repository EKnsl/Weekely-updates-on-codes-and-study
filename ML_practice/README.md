Index:

``` bash
.
├── README.md
├── week1_ML_ Intro_and_supervised_learing
│   ├── data
│   │   ├── 50_Startups.csv
│   │   ├── headbrain.csv
│   │   └── titanic.csv
│   ├── Linear Regression
│   │   ├── Multiple_Linear_Regression_with_startup_data.ipynb
│   │   └── Simple_Linear_Regression.ipynb
│   └── Logistic Regression
│       └── Logistic_Regression.ipynb
├── week2_Supervised_Learning
│   ├── data
│   │   └── credit_data.csv
│   ├── K Nearest Neighbour
│   │   ├── 05.KNN.pdf
│   │   └── K_Nearest_Neighbors.ipynb
│   ├── Naive Bayes
│   │   ├── Conditional Probability.pdf
│   │   ├── cs188 lecture 20 -- naive bayes 6PP.pdf
│   │   └── Naive_Bayes.ipynb
│   └── Support Vector Machine
│       └── Support_Vector_Machines.ipynb
├── week3_part1
│   └── Regularization
│       └── regularization.ipynb
├── week3_part2
│   ├── Decison_Tree
│   │   ├── data
│   │   │   └── pima_indians_diabetes.csv
│   │   ├── Decision_Tree_Classifier.ipynb
│   │   └── diabetes.png
│   └── Ensemble
│       ├── AdaBoost.ipynb
│       └── XGBoost_Regression.ipynb
└── week4_Unsupervised_Learning
    ├── Anomaly_Detection
    │   ├──  Credit Card Fraud Detection.ipynb
    │   └── data
    ├── Clustering
    │   ├── 01_K_Means_Clustering.ipynb
    │   ├── 02_DBSCAN_Clustering.ipynb
    │   ├── 03_Hierarchical_Clustering.ipynb
    │   └── data
    │       └── Quotes.csv
    └── Dimensionality Reduction
        └── Principal Component Analysis
            └── Principal Component Analysis.ipynb

```

# Week1

Date : 19/05/2022

https://ml.howtocode.dev/

[ML basics(Lec 1.1 to 2.3 of the playlist)](https://www.youtube.com/playlist?list=PLLssT5z_DsK-h9vYZkQkYNWcItqhlRJLN)

---------------------------------------------------------------------------------------------------------
Date : 20/05/2022

[Linear Regression](https://github.com/mhuzaifadev/mlzero_to_hero/tree/main/04_Simple%20_Linear_Regression)

-----------------------------------------------------------------------------------------------------------
Date : 23/05/2022

[lec 2.4 to 3.4 (Linear Regression with one variable and Linear Algebra upto matrix matrix multiplication)](https://www.youtube.com/playlist?list=PLLssT5z_DsK-h9vYZkQkYNWcItqhlRJLN)

Additional : 

[ML intro](https://ml.howtocode.dev/)

[why matrix multiplication is not commutative i.e order matters](https://www.quora.com/Why-is-the-multiplication-of-matrices-not-a-commutative-property-so-that-AB-neq-BA)

----------------------------------------------------------------------------------------------------------

Date : 24/05/2022

[Linear Algebra review](https://towardsdatascience.com/linear-algebra-for-machine-learning-22f1d8aea83c)

[Lec 3.4 to 3.6(Linear Algebra) and Lecture 4.1 — Linear Regression With Multiple Variables-(Multiple Features)](https://www.youtube.com/playlist?list=PLLssT5z_DsK-h9vYZkQkYNWcItqhlRJLN)

[Multiple Linear Regreassion notebook with startup data](https://github.com/mhuzaifadev/mlzero_to_hero/tree/main/05%20Multiple%20Linear%20Regression)

additional resources : 

Example of using categorical features : [Multiple Linear Regression: A quick Introduction](https://www.askpython.com/python/examples/multiple-linear-regression)

------------------------------------------------------------------------------------------------------------------------------------------

Date : 25/05/2022

Linear Regression with Multiple Variable: [Lecture 4.1 - 4.7 of this playlist.](https://www.youtube.com/watch?v=PPLop4L2eGk&list=PLLssT5z_DsK-h9vYZkQkYNWcItqhlRJLN)

additional resources :
[Why One-Hot Encode Data in Machine Learning?](https://machinelearningmastery.com/why-one-hot-encode-data-in-machine-learning)

[Use ColumnTransformer to apply different preprocessing to different columns](https://www.youtube.com/watch?v=NGq8wnH5VSo)

[How column Transformers work](https://www.analyticsvidhya.com/blog/2021/05/understanding-column-transformer-and-machine-learning-pipelines/)

------------------------------------------------------------------------------------------------------------------------------------------------------

Date : 26/05/2022

* ## Practise Logistic Regression

    [My Logistic Regression Notebook](https://github.com/EKnsl/Weekely-updates-on-codes-and-study/blob/main/ML_practice/week1_ML_%20Intro_and_supervised_learing/code/Logistic_Regression.ipynb)

    * Prediction of survival with titanic dataset using Logistic regression 

    * Performance evaluation using accuracy precison, recall and f1 score

    related resources : 

    https://datascienceplus.com/logistic-regression-with-python-using-titanic-data/

    [kaggle notenook](https://www.kaggle.com/code/mnassrib/titanic-logistic-regression-with-python/notebook)

    [Feature Selection Techniques for regression](https://machinelearningmastery.com/feature-selection-for-regression-data/)

    -------------------------------------------------------------------------------------------------------------------------------------

Date : 30/05/2022

* ## Logistic Regression Basic concepts

    * Learnt about

        * Logistic function  
        
        * non-linear decision boundaries

        * A better cost function than sqaured error for classification with non linear decision boundary
         
        * Some optimization algorithms that often converge faster than Gradiant descent (according to Andrew N.G):
            * [Conjugate Gradient Descent](https://ikuz.eu/machine-learning-and-computer-science/the-concept-of-conjugate-gradient-descent-in-python/)
            
            * [BFGS](https://machinelearningmastery.com/bfgs-optimization-in-python/)
            
            * L-BFGS : 
            [How L-BFGS works](https://stats.stackexchange.com/questions/284712/how-does-the-l-bfgs-work),
            [L-BFGS method basics with python code](https://www.earthinversion.com/techniques/the-L-BFGS-optimization-method/)

        * One vs rest or One vs all for multiclass classification (choose 1 class from k classes)
            
            [One-vs-Rest and One-vs-One for Multi-Class Classification](https://machinelearningmastery.com/one-vs-rest-and-one-vs-one-for-multi-class-classification/ )
            
            [Logistic regression  Multiclass - One-vs-rest classification](https://www.youtube.com/watch?v=EYXSve6T5BU)
            
            [Logistic Regression Mutliclass Classification(OneVsRest)](https://www.youtube.com/watch?v=V8fS0T_ktn4)

    * Completed [Lecture 6.1 - 6.7 of this playlist.](https://www.youtube.com/playlist?list=PLLssT5z_DsK-h9vYZkQkYNWcItqhlRJLN)

------------------------------------------------------------------------------------------------------------------------------------

# Week2


Date : 02/06/2022

* ## Study conditional probability , Naive Bayes and K Nearest Neighbour
    
    [Naive Bayes practice](https://github.com/EKnsl/Weekely-updates-on-codes-and-study/tree/main/ML_practice/week2_Supervised_Learning/Naive%20Bayes)

    [K Nearest Neighbour practice](https://github.com/EKnsl/Weekely-updates-on-codes-and-study/tree/main/ML_practice/week2_Supervised_Learning/K%20Nearest%20Neighbour)


Date : 13/06/2022

* ## Study and practice support vector machine (SVM)
    
    * completed lecture 12.1 to 12.6 of  [this playlist](https://www.youtube.com/watch?v=FCUBwP-JTsA&list=PLLssT5z_DsK-h9vYZkQkYNWcItqhlRJLN&index=75) 

    * [SVM practice notebook](https://github.com/EKnsl/Weekely-updates-on-codes-and-study/blob/main/ML_practice/week2_Supervised_Learning/Support%20Vector%20Machine/Support_Vector_Machines.ipynb)

---------------------------------------------------------------------------------------------------------------------------------------------------

# Week 03 | Part 1: Tuning and Performance Metrics of ML Model

Date : 13/06/2022

* ## Learnt basics of regularization and bias variance tradeoff

    * Completed Regularization in Traditional ML | Part 1: lecture [7.1 to 7.4 of this playlist](https://www.youtube.com/watch?v=u73PU6Qwl1I&list=PLLssT5z_DsK-h9vYZkQkYNWcItqhlRJLN&index=39)

    * Completed Regularization in Traditional ML | Part 2: lecture [10.1 to 10.7 of this playlist](https://www.youtube.com/watch?v=sZSKGNbrwus&list=PLLssT5z_DsK-h9vYZkQkYNWcItqhlRJLN&index=58)

Date : 21/06/20222

* Completed Performance Metrics: [Lecture 11.1 - 11.5 of this playlist.](https://www.youtube.com/playlist?list=PLLssT5z_DsK-h9vYZkQkYNWcItqhlRJLN)


Date : 22/06/2022


* study [Regularization for Simplicity](https://developers.google.com/machine-learning/crash-course/regularization-for-simplicity/video-lecture) 

* read [Regularization for Simplicity: L₂ Regularization](https://developers.google.com/machine-learning/crash-course/regularization-for-simplicity/l2-regularization), [Lambda](https://developers.google.com/machine-learning/crash-course/regularization-for-simplicity/lambda), [Generalization: Peril of Overfitting](https://developers.google.com/machine-learning/crash-course/generalization/peril-of-overfitting#ockham)

Date : 23/06/2022

* study [Regularization in Traditional ML](http://ethen8181.github.io/machine-learning/regularization/regularization.html) 

* [regularization pratice notebook](https://github.com/EKnsl/Weekely-updates-on-codes-and-study/blob/main/ML_practice/week3_part1/Regularization/regularization.ipynb)

# Week 03 | Part 2: Ensemble Learning

Date : 26/06/2022

* studied Decison Tree : [Decision Tree Explained](https://www.youtube.com/watch?v=7VeUPuFGJHk) ,
          [Decision Tree Summary.](https://www.youtube.com/watch?v=tNa99PG8hR8)  
          
* studied Random Forest : [part1](https://www.youtube.com/watch?v=J4Wdy0Wc_xQ) ,
          [part2](https://www.youtube.com/watch?v=nyxTdL_4Q-Q)


Date : 28/06/2022

* ## Practice Decision tree using a diabetes dataset
    
    * learnt tuning some of the hyperparametes of decison tree
    
    * [decision tree practice notebook](https://github.com/EKnsl/Weekely-updates-on-codes-and-study/blob/main/ML_practice/week3_part2/Decison_Tree/Decision_Tree_Classifier.ipynb)

* ## Study Regression tree 
    Regression Tree: [Regression Tree Explained](https://www.youtube.com/watch?v=g9c66TUylZ4).
    
    Summary :
    
    * each leaf node has a numeric value

    * we determine how to divide the observations by trying different 
    thresholds and calculating the sum of squared residuals at each step 
    and pick the candidate with smallest sum of squared residuals 
    to be the root

    * when we have some minimum number of observations in a node then that node becomes leaf.
    (usually 20, but for smaller datasets, it can be less than 20)
    otherwise, we repeat the process to split the remaining 
    observations untill we can no longer split the observations into smaller groups
     
Date : 01/07/2022

* ## Studied Adaboost: [AdaBoost Explained](https://www.youtube.com/watch?v=LsK-xG1cLYA).
    
    important points :
    
    * adaboost are made with stumps(tree with one node and two leaves)
    * weighted voting is used, larger stumps weight more than smaller ones
    * errors in making previous stumps influence erros in the next ones
    * initially all stumps has weight = 1/(number of samples)
    * total error = sum of the weights for the incorrectly classified samples
    * for a stump, amount of say = 0.5 * log2((1-total error)/total error)
    * amount of say is reciprocal to total error. i.e., when total error is small, the
    amount of say is a relatively large positive value
    * after the initial step, sample weights for the incorrectly 
    classified samples are increased and decreased for correctly classified samples.
    * for incorrectly classified samples, 
    new sample weight = previous sample weight * exp(amount of say)
    * for correctly classified samples, 
    new sample weight = previous sample weight * exp(-1.0 * amount of say) 
    * when the amount of say is relatively large, new sample weight is close to 0
    and when the amount of say is relatively small, new sample weight is close to 1.
    * New sample weights are normalized so that they add upto 1.
    * weighted gini index can be used to determine which feature variable should split the next stump


Date : 02/07/2022

* ## Studied [Decision Trees and Ensemble Methods](https://www.youtube.com/watch?v=wr9gUr-eWdA&list=PLoROMvodv4rMiGQp3WXShtMGgzqpfVfbU&index=11)
    
    * learnt about splits in decision tree, pros and cons of DTs, different kind of ensemble techniques


Date : 03/07/2022

* ## Studied Gradient Boost: 
    [Part 1](https://www.youtube.com/watch?v=3CC4N4z3GJc), 
    [Part 2](https://www.youtube.com/watch?v=2xudPOBz-vs), 
    [Part 3](https://www.youtube.com/watch?v=jxuNLH5dXCs), 
    [Part 4](https://www.youtube.com/watch?v=StWY5QWMXCw).


Date : 04/07/2022

* ## Studied Xtreme Gradient Boost: 
    [Part 1](https://www.youtube.com/watch?v=OtD8wVaFm6E), 

Date : 08/07/2022

* ## Studied Xtreme Gradient Boost: 
    [Part 2](https://www.youtube.com/watch?v=2xudPOBz-vs), 
    [Part 3](https://www.youtube.com/watch?v=jxuNLH5dXCs), 
    [Part 4](https://www.youtube.com/watch?v=StWY5QWMXCw).

Date : 09/07/2022

* ## Ensemble related problem solving :
    
    * [Adaboost Practice Norebook](https://github.com/EKnsl/Weekely-updates-on-codes-and-study/blob/main/ML_practice/week3_part2/Ensemble/AdaBoost.ipynb)

    * [Xtreme Gradiant Boosting Practice Notebook](https://github.com/EKnsl/Weekely-updates-on-codes-and-study/blob/main/ML_practice/week3_part2/Ensemble/XGBoost_Regression.ipynb)


Date : 12/07/2022

* ## Studied clustering 
    Lec 13.1 - 13.5 of [this playlist](https://www.youtube.com/watch?v=Ev8YbxPu_bQ&list=PLLssT5z_DsK-h9vYZkQkYNWcItqhlRJLN&index=77)

Date : 13/07/2022
* ## Studied Dimensionality reduction
    Lec 14.1 - 14.5 of [this playlist](https://www.youtube.com/watch?v=Zbr5hyJNGCs&list=PLLssT5z_DsK-h9vYZkQkYNWcItqhlRJLN&index=81)

Date : 14/07/2022

* ## Studied Dimensionality reduction
    Lec 14.6 - 14.7 of [this playlist](https://www.youtube.com/watch?v=Zbr5hyJNGCs&list=PLLssT5z_DsK-h9vYZkQkYNWcItqhlRJLN&index=81)

Date : 15/07/2022

* ## Studied Anomaly detection
    Lec 15.1 - 15.4 of [this playlist](https://www.youtube.com/watch?v=086OcT-5DYI&list=PLLssT5z_DsK-h9vYZkQkYNWcItqhlRJLN&index=88)

Date : 16/07/2022

* ## Studied Anomaly detection
    Lec 15.5 - 15.8 of [this playlist](https://www.youtube.com/watch?v=086OcT-5DYI&list=PLLssT5z_DsK-h9vYZkQkYNWcItqhlRJLN&index=88)

Date : 17/07/2022

* ## Studied Recommendation Systems
    Lec 16.1 - 16.2 of [this playlist](https://www.youtube.com/watch?v=giIXNoiqO_U&list=PLLssT5z_DsK-h9vYZkQkYNWcItqhlRJLN&index=96)

Date : 18/07/2022

* ## Studied Recommendation Systems
    Lec 16.3 - 16.6 of [this playlist](https://www.youtube.com/watch?v=giIXNoiqO_U&list=PLLssT5z_DsK-h9vYZkQkYNWcItqhlRJLN&index=96)

Date : 19/07/2022

* ## Kmeans clustering : 

[Kmeans clustering practice notebook](https://github.com/EKnsl/Weekely-updates-on-codes-and-study/blob/main/ML_practice/week4_Unsupervised_Learning/Clustering/K_Means_Clustering.ipynb)

* ## DBSCAN clustering : 

[DBSCAN clustering practice notebook](https://github.com/EKnsl/Weekely-updates-on-codes-and-study/blob/main/ML_practice/week4_Unsupervised_Learning/Clustering/DBSCAN_Clustering.ipynb)

* ## Principal Component Analysis : 

[Principal Component Analysis](https://github.com/EKnsl/Weekely-updates-on-codes-and-study/blob/main/ML_practice/week4_Unsupervised_Learning/Dimensionality%20Reduction/Principal%20Component%20Analysis/Principal%20Component%20Analysis.ipynb)

Date : 21/07/2022

* ## Practice Anomaly Detection with credit card data
    [Credit Card Fraud Detection.ipynb](https://github.com/EKnsl/Weekely-updates-on-codes-and-study/blob/main/ML_practice/week4_Unsupervised_Learning/Anomaly_Detection/%20Credit%20Card%20Fraud%20Detection.ipynb)




    

