from datetime import datetime
import messages

announcementTimes = []
announcedTimes = []
announcementTimes.append(datetime(2017, 12, 18, 18, 53)) # 11:00pm
announcementTimes.append(datetime(2017, 12, 18, 18, 50)) # 10:30pm
announcementTimes.append(datetime(2017, 12, 18, 18, 47)) # 10:15pm
announcementTimes.append(datetime(2017, 12, 18, 18, 43)) # 10:00pm
announcementTimes.append(datetime(2017, 12, 18, 18, 40)) # 9:30pm
counter = 5

checker = datetime.utcnow()
print(checker)
for announce in announcementTimes:
    






    #print(announce)
    datePassed = announce < checker #true if the time has passed
    #print(datePassed)
    if(datePassed):
        #this announcement is the last one to occur, announce it if it hasn't been
        if(announce not in announcedTimes):
            announcedTimes.append(announce)
            counter -= 1
            print(announce)
            print(messages.announcements[counter])
