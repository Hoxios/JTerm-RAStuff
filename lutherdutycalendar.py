#Ryan Ehrhardt
#Janurary Term 2017 Independent Study Project
#Luther College Resident Assistant Scheduler
#Take input of conflicts from a text file and from that information create a calendar that schedules people around their conflicts
import calendar
class RA:
    def __init__(self, name):
        self.name = name
    def get_conflicts(self):
        return Conflicts(self.name)




class Conflicts:
    def __init__(self):
        self.infile = open('conflicts.txt', 'r')

    def make_conflicts(self):
        #makes a dictionary for each RA
        #ex.) Ryan: 1 3 5
        RA_dict= {}
        self.infile.split()
        for item in self.infile:
            if "0123456789" in item:
                RA_dict[RA] = int(item)
            else:
                RA = item






def scheduling:
    duty = Conflicts()
    duty.make_conflicts()
    #determine how many days are in the month from there assign points(I know a basic way to do this however eventually it'll need to do this on its own).
    #numbers pulled from current month for testing purposes
    weekday_points = 23 *1
    #weekdays * 1

    weekend_points = 8 * 2

    points = weekday_points + weekend_points


    #determine a max point value for staff
    max_points = len(RA_dict)/points
    # iterate through RA_dict and schedule people one at a time
    days_remaining = []
    days_scheduled = []
    #fills list up with days of month (temp)
    for days in range(1,32):
        days_remaining.append(days)
    while len(days_remaining) != 0:
        #scheduling code goes here
        #thinking of for loop of the dictionary from there getting the conflicts of the RA and then scheduling the RA
        # only if the conflicts are seperated by seven days ideally






def make_calendar:
    #use information from scheduling to then make output of a calendar.. may or may not be necessary.

