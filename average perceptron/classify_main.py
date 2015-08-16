# -*- coding: gbk -*-  
'''
Created on 2015年8月13日

@author: zhuchenxi
'''
import sys, getopt
from perceptron import Perceptron
import random

class Example:
    def __init__(self, class_num, feature_list):
        self.class_num = class_num
        self.feature_list = feature_list

class Feature:
    def __init__(self, feature_num, value):
        self.feature_num = feature_num
        self.value = value

class Data:
    def __init__(self):
        self.num_class_list = []
        self.class_num_dict = {}
        self.num_feature_list = []
        self.feature_num_dict = {}
        self.train_example_list = []
        self.test_example_list = []
        random.seed(5288)  
               
    def shuffle_train(self):             
        random.shuffle(self.train_example_list)
    
    def get_class_num(self, class_name, isTrain):
        if class_name in self.class_num_dict:
            return self.class_num_dict[class_name]
        else:
            if isTrain:
                self.num_class_list.append(class_name)
                self.class_num_dict[class_name] = len(self.num_class_list)-1
                return self.class_num_dict[class_name]
            else:
                return -1
        
    def get_feature_num(self, feature_name, isTrain):
        if feature_name in self.feature_num_dict:
            return self.feature_num_dict[feature_name]
        else:
            if isTrain:
                self.num_feature_list.append(feature_name)
                self.feature_num_dict[feature_name] = len(self.num_feature_list)-1
                return self.feature_num_dict[feature_name]
            else:
                return -1
        
    def make_example(self, line, isTrain):
        splits = line.split()
        class_num = self.get_class_num(splits[0], isTrain)
        if class_num == -1:
            return None
        feature_list = []
        for i in range(1, len(splits)):
            small_splits = splits[i].split(":")
            feature_num = self.get_feature_num(small_splits[0], isTrain)
            if feature_num == -1:
                continue
            feature = Feature(feature_num, float(small_splits[1]))
            feature_list.append(feature)
        e = Example(class_num, feature_list)
        return e
        
    def read_train_file(self, train_file_path):
        f = open(train_file_path, "r")
        while True:
            line = f.readline().strip()
            if len(line) == 0:
                break            
            e = self.make_example(line, True)
            self.train_example_list.append(e)
    
    def read_test_file(self, test_file_path):
        f = open(test_file_path, "r")
        while True:
            line = f.readline().strip()
            if len(line) == 0:
                break
            e = self.make_example(line, False)
            if e is None:
                continue
            self.test_example_list.append(e)
        
def main(args):
    train_file_path = "./data/restaurant_train.txt"
    test_file_path = "./data/restaurant_test.txt"
    model_file_path = "./perc_mod.m"
    data = Data()
    data.read_train_file(train_file_path)
    data.read_test_file(test_file_path)
    model = Perceptron(data)
    model.train(data, 5)
    
    
if __name__ == '__main__':
    main(sys.argv[1:])
