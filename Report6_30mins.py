"""
This report is executed every 5mins
"""

import time, random
import subprocess,os

#import #EmailSender




print "30min Report Execution started.."
time.sleep(5)
status = random.randint(0,1)
if status == 0:
    print "30min Report Execution Failed.."
    stat = "Failed"
    #os.system('kill %d' % os.getpid())
else:
    print "30min Report Execution Succeeded.."
    stat = "Succeeded"
    #EmailSender.send_mail('Report6_30mins.py', '30mins', stat)






