# coding=UTF-8
'''
Created on 2015年8月17日

@author: zhu
'''

#This model just ignore the value of feature.
#If someone want to use the value of feature, he may use the Gaussian NB or Multinomal NB
class NaiveBayes:
    def __init__(self, data):
        self.feature_sum = len(data.num_feature_list)
        self.label_sum = len(data.num_class_list)
        #just like a[feature_sum][label_sum]
        self.prob_x_given_y = [[0.0 for col in range(self.label_sum)] for row in range(self.feature_sum)]
        self.prob_y = [0.0 for i in range(self.label_sum)]
        
    def train(self, data):
        y_sum = 0
        x_given_y_sum = 0
        for example in data.train_example_list:
            self.prob_y[example.class_num] += 1
            y_sum += 1
            for feature in example.feature_list:
                self.prob_x_given_y[feature.feature_num][example.class_num] += 1
                x_given_y_sum += 1
        #number divide the sum of number
        for i in range(self.label_sum):
            self.prob_y[i] /= y_sum
        for i in range(self.feature_sum):
            for j in range(self.label_sum):
                self.prob_x_given_y[i][j] /= x_given_y_sum
        print "final train accuracy is: %.2f" %(self.accuracy(data.train_example_list)*100)
        print "final test accuracy is: %.2f" %(self.accuracy(data.test_example_list)*100) 
    
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
        score = 1.0        
        for feature in example.feature_list:
            score *= self.prob_x_given_y[feature.feature_num][label] * \
                    self.prob_y[label]
        return score
                         
        
if __name__ == '__main__':
    pass