# -*- coding: gbk -*-  
'''
Created on 2015年8月13日

@author: zhuchenxi
'''
import sys, getopt
from perceptron import Perceptron
from naive_bayes import NaiveBayes
from data import Data
import random
        
def main(args):
    train_file_path = "./data/restaurant_train.txt"
    test_file_path = "./data/restaurant_test.txt"
    model_file_path = "./perc_mod.m"
    data = Data()
    data.read_train_file(train_file_path)
    data.read_test_file(test_file_path)
    model = NaiveBayes(data)
    model.train(data)
    model = Perceptron(data)
    model.train(data, 5)
       
if __name__ == '__main__':
    main(sys.argv[1:])
