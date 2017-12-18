from datetime import datetime
import messages

announcementTimes = []
announcedTimes = []
announcementTimes.append(datetime(2017, 12, 18, 4, 30)) #14th, 10:30pm
announcementTimes.append(datetime(2017, 12, 18, 4)) #14th, 10:00pm
announcementTimes.append(datetime(2017, 12, 18, 3, 45)) #14th, 9:45pm
announcementTimes.append(datetime(2017, 12, 18, 3, 30)) #14th, 9:30pm
announcementTimes.append(datetime(2017, 12, 18, 3)) #14th, 9:00pm

checker = datetime.utcnow()
print(checker)
counter = 5
for announce in announcementTimes:
    #print(announce)
    datePassed = announce < checker #true if the time has passed
    #print(datePassed)
    if(datePassed):
        #this announcement is the last one to occur, announce it if it hasn't been
        if(announce not in announcedTimes):
            announcedTimes.append(announce)
            counter -= 1
            print(messages.announcements[counter])
