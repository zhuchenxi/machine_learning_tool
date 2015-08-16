# -*- coding: gbk -*-  
'''
Created on 2015年8月13日

@author: zhuchenxi
'''

class Perceptron:
    def __init__(self, data):
        self.num_updates = 0
        self.feature_sum = len(data.num_feature_list)
        self.label_sum = len(data.num_class_list)
        self.W = [0] * (self.feature_sum * self.label_sum)
        self.avg_W = [0] * (self.feature_sum * self.label_sum)
    
    def train(self, data, iters):
        for iter in range(iters):
            for example in data.train_example_list:
                pred_label = self.pred(example)
                gold_label = example.class_num
                if pred_label != gold_label:
                    self.update(example, gold_label, pred_label)
                self.num_updates += 1
            print "this is %i iter:" %(iter+1)
            print "train accuracy is: %.2f" %(self.accuracy(data.train_example_list)*100)
            print "test accuracy is: %.2f" %(self.accuracy(data.test_example_list)*100) 
            print "*" * 10
        self.adjust_avg_w()
        #print "*" * 10
        print "final train accuracy is: %.2f" %(self.accuracy(data.train_example_list)*100)
        print "final test accuracy is: %.2f" %(self.accuracy(data.test_example_list)*100) 
        
    def adjust_avg_w(self):
        for i in range(self.feature_sum * self.label_sum):
            self.W[i] -= self.avg_W[i] / self.num_updates
    
    def accuracy(self, example_list):
        right_sum = 0.0
        all_sum = 0.0
        for example in example_list:
            all_sum += 1
            pred_label = self.pred(example)
            gold_label = example.class_num
            if pred_label == gold_label:
                right_sum += 1
        return right_sum / all_sum
            
    
    def pred(self, example):
        max_score = float("-inf")
        max_label = -1
        for label in range(self.label_sum):
            score = self.score(example, label)
            if score > max_score:
                max_score = score
                max_label = label
        return max_label
    
    def score(self, example, label):
        score = 0.0
        for feature in example.feature_list:
            index = feature.feature_num + label * self.feature_sum
            score += self.W[index] * feature.value
        return score
        
    def update(self, example, gold_label, pred_label):
        for feature in example.feature_list: 
            gold_index = feature.feature_num + gold_label * self.feature_sum
            pred_index = feature.feature_num + pred_label * self.feature_sum
            self.W[gold_index] += feature.value
            self.W[pred_index] -= feature.value
            self.avg_W[gold_index] += feature.value * self.num_updates
            self.avg_W[pred_index] -= feature.value * self.num_updates