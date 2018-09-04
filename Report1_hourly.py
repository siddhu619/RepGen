"""
This report is executed hourly
"""

import time, random
import subprocess
#import #EmailSender






print "Hourly Report Execution started.."
time.sleep(5)
status = random.randint(0,1)
if status == 0:
    print "Hourly Report Execution Failed.."
    stat = "Failed"
else:
    print "Hourly Report Execution Succeeded.."
    stat = "Succeeded"



