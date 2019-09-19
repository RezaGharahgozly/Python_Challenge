import os
import csv

ByPass_csv = os.path.join('employee_data.csv')

# Lists to store data
EmpID = []
FirstName = []
LastName = []
DOB = []
SSN = []
State = []

with open(ByPass_csv, newline="", encoding='utf-8') as csvfile:
#with open(ByPass_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header=next(csvreader)
    
    for row in csvreader:
        # Add Emp ID
        EmpID.append(row[0])
        
        # Get First and Last names seperated
        new_Name = row[1].split(" ")
        FirstName.append(new_Name[0])
        LastName.append(new_Name[1])        


        # Add DOB
        words = row[2].replace('-','/')
        DOB.append(words)

        # Add SSN
        temp = list(row[3])
        temp[0]='#'
        temp[1]="#"
        temp[2]="#"
        temp[4]="#"
        temp[5]="#"
        temp = "".join( temp)
        row[3]=temp
        SSN.append(row[3])

        # Add Abbriviated state
        temp = list(row[4])
        temp2 = "".join(temp)
        temp3 = us_state_abbrev[temp2]
        row[4] = temp3
        State.append(row[4])


# Zip lists together
cleaned_csv = zip(EmpID, FirstName, LastName, DOB, SSN, State)

# Set variable for output file
output_file = os.path.join("New Employee Data.csv")

#  Open the output file
with open(output_file, "w", newline="", encoding = "utf-8") as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State"])

    # Write in zipped rows
    writer.writerows(cleaned_csv)    
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'District of Columbia': 'DC',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Northern Mariana Islands':'MP',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Palau': 'PW',
    'Pennsylvania': 'PA',
    'Puerto Rico': 'PR',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virgin Islands': 'VI',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}
 