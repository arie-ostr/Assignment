import json
"""
Extremely rudimentary store of baseline jsons
I would use a DB for real life cases 
I would also fine tune the areas I want to compare against the baseline
this reduces the false negative rate

"""


record_mode = True
fname = "../data/baseline_data.json"
json_baselines = {}


def read_data():
    global json_baselines    
    with open(fname,"r") as f:
        json_baselines = json.load(f)



def record_data(update_dict):
    global json_baselines 
    read_data()
    json_baselines.update(update_dict)
    with open(fname,"w") as f:
        f = json.dump(json_baselines)