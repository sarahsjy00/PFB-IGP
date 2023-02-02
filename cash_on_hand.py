# importing the cash on hand csv from the project group folder to be read
from pathlib import Path
import csv
filepath = Path.cwd()/"C:/project_group/csv_reports/cash-on-hand-usd.csv"

def coh_difference():
    '''
    This function has no parameters and will check all rows and data in the csv file to see if there are cash deficits the following days
    and display them in a txt file
    '''
    # opening the csv file with mode "r" to access the data in the file
    with filepath.open(mode="r", encoding="UTF-8", newline="") as file:
      
        reader = csv.reader(file)
        # skipping the header
        next(reader)

        # assigning an empty list for day and cash on hand data
        coh_day = []
                
        # using a for loop to run through all rows in the file
        for row in reader:

            # appending the day and cash on hand data to the empty list
            coh_day.append([row[0], row[1]])
            
            # assigning an empty list to store days where there is a deficit and its respective amount
            coh_deficit = []

            # using a for loop to run through all the data assigned to the list starting from 1
            for day in range(1 , len(coh_day)):

                # assigning a variable for the difference between 2 separate amounts on 2 days
                coh_difference = int(coh_day[day-1][1]) - int(coh_day[day][1])

                # setting a condition if the amount on the current day is lower than the amount on the previous day,
                # it will append that day of the deficit and the calculated amount into the above empty list
                if float(coh_day[day][1]) < float(coh_day[day-1][1]):

                    deficit_day = float(coh_day[day][0])

                    coh_deficit.append([deficit_day,coh_difference])

               
