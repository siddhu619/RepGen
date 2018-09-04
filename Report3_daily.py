"""
This report is executed daily
"""

import time, random#, #EmailSender

print "Daily Report Execution started.."
time.sleep(15)
status = random.randint(0, 1)
if status == 0:
    print "Daily Report Execution Failed.."
else:
    print "Daily Report Execution Succeeded.."
    #EmailSender.send_mail('Report3_daily.py', 'daily', 'Succeeded')




