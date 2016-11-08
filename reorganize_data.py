########################################################
# python 2.7
#
# Tess Jeffers
# 11/07/2016
#
########################################################
import subprocess
import os

def reorganize_data(id_list,data_type):
    base = '/Users/tess/Desktop/kaggle-leaves/images/'
    ext = '.jpg'
    location = base + data_type + '/'
    cmd = 'mkdir ' + location
    os.system(cmd)
    
    for id in id_list:
        filename = base + str(id) + ext
        cmd = 'mv ' + filename + " " + location
        os.system(cmd)
        
        
train_ids = list(leaves_train['id'])
test_ids = list(leaves_test['id'])

reorganize_data(train_ids, 'train')
reorganize_data(test_ids, 'test')