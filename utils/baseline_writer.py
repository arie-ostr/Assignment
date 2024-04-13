import json
import os
"""
Extremely rudimentary store of baseline jsons
I would use a DB for real life cases 
I would also fine tune the areas I want to compare against the baseline
this reduces the false negative rate

"""


base_path = os.getcwd()
str_fname = "data/baseline_data.json"
abs_path  = os.path.join(base_path,str_fname)
norm_path = os.path.normpath(abs_path)

json_baselines = {}


def read_data():
    global json_baselines    
    with open(norm_path,"r") as f:
        json_baselines = json.load(f)

def get_data(key):
    return json_baselines[key]

def record_data(baseline_key,baseline_value):
    update_dict = {baseline_key:baseline_value}
    global json_baselines 
    read_data()
    json_baselines.update(update_dict)
    with open(norm_path,"w") as f:
        f = json.dump(json_baselines,f)

#if this file is imported : read the data!
#we can also put this as a fixture 
read_data()