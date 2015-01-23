#helper methods for main.py

#import
from datetime import datetime
import pickle as pickle 

#global variable
valid_ints= [0,1,2,3,4,5,6,7,8,9]  

def calculate_days_remaining (due_date): 
    #Calculates days between current date and due_date
    difference= 0
    index= []

    for i in range (0, len(due_date)):
        if due_date[i]=='/' or due_date[i]== '-':
                index.append(i)
        else:
            try:
                int (due_date[i])
            except:
                return False

    try: 
        month= int (due_date[0:index[0]])
        day= int (due_date [index[0]+1:index[1]])
        year= int (due_date [index[1]+1:])
    except: 
        return False

    current_date= datetime.now()
    current_month= int (current_date.month)
    current_day= int (current_date.day)
    current_year= int (current_date.year)

    year_difference= year-current_year
    month_difference= month- current_month
    day_difference= day- current_day

    #checks if earlier date than current
    if month_difference==0:
        if year_difference==0:
            if day_difference<0: 
                return "5000"
            elif day_difference==0:
                return 0
    elif year_difference==0:
        if month_difference<0:
            return "5000"
    if year_difference<0:
        return "5000"

    #main calculation
    if year_difference==0:
        pass
    elif year_difference==1:
        difference+= end_the_year(current_day, current_month, current_year, difference)
        current_month=1
        current_day= 1
        current_year+= 1
        month_difference= month-current_month
        day_difference= day-current_day
    else:
        difference+= end_the_year(current_day, current_month, current_year, difference)
        difference+= (year_difference-1)*365
        #for leap year
        difference+= 1
        current_year= year
        current_month=1
        current_day= 1
        day_difference= day-current_day
        month_difference= month-current_month

    if month_difference==0:
        if day_difference <0:
            return False
        else:
            difference+= day-current_day
            return difference
    else:
        difference= find_difference_month(day, current_day, month, current_month, difference)
        difference+= (day-1)
        return difference




def find_difference_month(day, current_day, month, current_month, difference):
    #helper method for calculate_days_remaining, adds days until due_date month
    days_in_each_month= [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days_left= days_in_each_month[current_month]-current_day
    difference+= days_left
    current_month+=1
    while (current_month!= month):
        difference+=days_in_each_month[current_month]
        current_month+=1
    return difference

def end_the_year (current_day, current_month, current_year, difference):
    #helper method for calculate_days_remaining, ends the current year and adds amount to difference
    days_in_each_month= [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days_left= days_in_each_month[current_month]-current_day
    difference += days_left
    current_month+=1
    while (current_month!=13):
        difference+= days_in_each_month[current_month]
        current_month+=1
    return difference


def check_date_valid(due_date):
    #Checks to see if user entered date is valid
    index= []
    if len(due_date)>10 or len(due_date)<8:
        return False

    for i in range (0, len(due_date)):
        if due_date[i]=='/' or due_date[i]== '-':
                index.append(i)
        else:
            try:
                int (due_date[i])
            except:
                return False

    if len(index)!=2:
        return False

    try: 
        month= int (due_date[0:index[0]])
        day= int (due_date [index[0]+1:index[1]])
        year= int (due_date [index[1]+1:])
    except: 
        return False

    if month ==0 or month >12:
        return False
    if day==0 or day>31:
        return False

    try:
        a= int(calculate_days_remaining(due_date))
        if a==0:
            pass
        elif a== False:
            return False
        elif a== 5000:
            return "earlier date"
    except:
        return False

    return True

def check_days_needed_valid (days_needed):
     #Checks to see if user entered days_needed is valid
    for i in range (0, len(days_needed)):
        try: 
            int (days_needed[i])
        except:
            return False

    try:
        if int(days_needed)>0:
            pass
        else:
            return False
    except:
        return False


def check_name_valid (name):
     #Checks to see if user entered item_name is valid
    if len (name)==0:
        return False

    any_characters= False

    for i in name:
        if i== " ":
            pass
        else:
            any_characters= True

    return any_characters


def append_days_left(to_do_list):
     #appends days left to to_do_list item as 3rd index
    for i in range (0, len(to_do_list)):
        a= calculate_days_remaining(to_do_list[i][1])
        try: 
            to_do_list[i][3]= a
        except:
            to_do_list[i].append(a)
    return to_do_list

def organize_list (to_do_list):
    #organizes to_do list into now, soon, and eventually  lists
    organized_list= []
    now= []
    soon= []
    eventually= []

    for i in range (0, len(to_do_list)):
        if to_do_list[i][3]<= to_do_list[i][2]:
            now.append(to_do_list[i])
        elif to_do_list[i][2]==1:
            if to_do_list[i][3]>1 and to_do_list[i][3]<=4:
                soon.append(to_do_list[i])
            else:
                eventually.append(to_do_list[i])
        elif to_do_list[i][2]>1 and to_do_list[i][2]<=4:
            if to_do_list[i][3]>to_do_list[i][2] and to_do_list[i][3]<=5+(to_do_list[i][2]):
                soon.append(to_do_list[i])
            else:
                eventually.append(to_do_list[i])
        else:
            if to_do_list[i][3]>to_do_list[i][2] and to_do_list[i][3]<=15:
                soon.append(to_do_list[i])
            else:
                eventually.append(to_do_list[i])


    #sort the list by days until due

    now= sorted(now, key=lambda x:x[3])
    soon= sorted(soon, key=lambda x:x[3])
    eventually= sorted (eventually, key=lambda x:x[3])

    organized_list.append(now)
    organized_list.append(soon)
    organized_list.append(eventually)


    return organized_list

def formatting_display (name, days_till_due):
    #formats the item for proper display. 
    #formatting= [spaces_needed, days_till_due]

    a= len(name)
    b= int(34-a)
    less_than_ten= int(b-1)
    less_than_hundred= int(b-2)
    less_than_thousand= int(b-3)


    if days_till_due==0:
        formatting= [b* " ", "Today"]
    elif days_till_due==1:
        formatting= [b* " " , "1 day"]
    elif days_till_due<10:
        formatting= [less_than_ten* " ", str(days_till_due)+ " days"]
    elif days_till_due<100:
        formatting= [less_than_hundred * " ", str(days_till_due)+ " days"]
    else:
        formatting= [less_than_thousand * " ", str(days_till_due )+ " days"]
    return formatting
        



def save_to_do(to_do_list): 
    #saves to_do_list
    pickle.dump(to_do_list, open("user_data.txt", "wb"))

def unsave_to_do():
    #loads to_do_list
    try: 
        return pickle.load(open("user_data.txt", "rb"))
    except:
        pass


def save_specfile(slist, filename):
    pickle.dump(slist, open(filename, "wb"))

def unsave_specfile(filename):
    try:
        return pickle.load(open(filename, "rb"))
    except: 
        pass

