# How to run
python classify_main.py

It will read the train and test data in ./data and then 
invoke perceptron.py to train the model and test.

I think it is very efficient because it will only update the weight W where the feature is 1 instead of update all the element of weight W including both base perceptron and average perceptron.

# Reference #
The structure references the Nivre's exercise:
http://stp.lingfil.uu.se/~nivre/master/ml2.html

The optimization of perfomance references the Liang Huang's slides for average perceptron, which I think may be found in his homepage:
http://acl.cs.qc.edu/~lhuang/