# importing the overheads csv from the project group folder to be read
from pathlib import Path
import csv
filepath = Path.cwd()/"C:/project_group/csv_reports/overheads-day-90.csv"

def overheads_highest():
    '''
    This function has no parameters and will check all rows and data in the csv file to see if there are cash deficits the following days
    and display them in a txt file
    '''
    # opening the csv file with mode "r" to access the data in the file
    with filepath.open(mode="r", encoding="UTF-8", newline="") as file:

        reader = csv.reader(file)
        # skipping the header
        next(reader)

        # assigning variables for the category with the highest overhead and starting them from 0
        highest_cat = ""
        overhead = 0
        
       