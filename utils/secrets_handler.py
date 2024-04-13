# data file to represent a secret storage service like hashicorp vault
# secrets are typically provisioned in test run time from a trusted external source, and stored as env variable. 

import json
import random

_data = None

def load_secrets_data():
    with open("../data/data.json", "r") as f: #note hardcoded source, could be a URI or an env var. 
        _data = json.load(f)
    
def get_test_account():
    """
        Gets an admin acciunt
    """
    if _data is None:
        load_secrets_data()
    
    try:
        
        valid_items = [item for item in _data if item["account_type"] == "test"]
        random_choice = random.choices(valid_items)
        return random_choice
        # TODO : case for missing data, generalize funciton, users provisioning for test parameter building, etc
    except IndexError:
        raise IndexError("can't find a test account")
