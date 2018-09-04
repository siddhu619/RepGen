"""
This report is executed every 5mins
"""

import datetime,time, random
#import #EmailSender

msg = \
"""
Name    : Report5_15mins.py
Frequecy: 15mins
Status  : %s
Time    : %s"""





print "15min Report Execution started.."
time.sleep(10)
status = random.randint(0,1)
if status == 0:
    print "15min Report Execution Failed.."
    mail=msg, "Failed\n", "time   : "+str(datetime.datetime.now())
    mail = str(mail)
    stat = "Failed"
    #os.system('kill %d' % os.getpid())
else:
    print "15min Report Execution Succeeded.."
    mail =  msg, "Succeeded\n", "time    : " +str(datetime.datetime.now())
    mail = str(mail)
    stat = 'Succeeded'
    #EmailSender.send_mail('Report5_15mins.py', '15mins', stat)




