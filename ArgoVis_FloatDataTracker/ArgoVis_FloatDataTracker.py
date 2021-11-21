import requests
import numpy as np
import math
import pandas as pd

from datetime import datetime, timedelta
import calendar

import matplotlib.pylab as plt
import matplotlib
##matplotlib.font_manager._rebuild()

import matplotlib.patches as mpatches
    
import warnings
warnings.filterwarnings('ignore')

def profile_req(float_no):
    site = 'https://argovis.colorado.edu/catalog/profiles/{}'.format(float_no)
    reply = requests.get(site)
    # Consider any status other than 2xx an error
    if not reply.status_code // 100 == 2:
        return "Error: Unexpected response {}".format(resp)
    profile = reply.json()
    return profile

profile_data = profile_req('7900211_266')

print(profile_data.keys)

profileDf = pd.DataFrame(profile_data['measurements'])
profileDf['cycle_number'] = profile_data['cycle_number']
profileDf['profile_id'] = profile_data['_id']
profileDf.head()

print(profileDf)