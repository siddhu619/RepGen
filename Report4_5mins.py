"""
This report is executed every 5mins
"""

import time, random
import subprocess,os
#import #EmailSender






print "5min Report Execution started.."
time.sleep(10)
status = random.randint(0,1)
if status == 0:
    print "5min Report Execution Failed.."
    #os.system('kill %d' % os.getpid())
else:
    print "5min Report Execution Succeeded.."
    #EmailSender.send_mail('Report4_5mins.py', '5mins', "Succeeded")



