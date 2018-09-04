"""
This report is executed weekly
"""

import time, random#, #EmailSender

print "Weekly Report Execution started.."
time.sleep(10)
status = random.randint(0, 1)
if status == 0:
    print "Weekly Report Execution Failed.."
else:
    print "Weekly Report Execution Succeeded.."
    #EmailSender.send_mail('Report2_weekly.py', 'weekly', 'Succeeded')

