from datetime import datetime

announcements = []
announced = []
announcements.append(datetime(2017, 12, 15, 4)) #14th, 10pm
announcements.append(datetime(2017, 12, 15, 3, 30)) #14th, 9:30pm
announcements.append(datetime(2017, 12, 15, 3)) #14th, 9pm

checker = datetime.utcnow()
for announce in announcements:
    datePassed = announce < checker #true if the time has passed
    if(datePassed):
        #this announcement is the last one to occur
        #announce it if it has not been
        if(announce not in announced):
            print(announce)
            announced.append(announce)
        break
