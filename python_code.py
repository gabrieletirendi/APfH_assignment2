import re
import os
import pandas as pd


# ======================================================================================================================
# EXERCISE 1
# ======================================================================================================================

# create yelling text
yel_text = "THIS HOUSE IS A MESS AGAIN! You NEVER learned to CLEAN! START CLEANING NOW!"

# TASK 1 ---------------------------------------------------------------------------------------------------------------
# split the yelling text into sentences and remove white space at the beginning and end
yel_text_split = re.split(r'(?<=[.!?])\s+', yel_text.rstrip())

# TASK 2 ---------------------------------------------------------------------------------------------------------------
# create the no_yelling() function that takes a sentence as input
def no_yelling(sent):
    # turn all capital letters to small letters and convert string to a list
    sent_list = list(sent.lower())
    # turn some letters to capital letters
    for i in range(len(sent_list)):
        # turn first letter to capital letter
        if i == 0:
            sent_list[i] = sent_list[i].upper()
        # turn the word "I" to capital letter
        elif sent_list[i] == "i" and sent_list[i-1] == " " and (sent_list[i+1] == " " or sent_list[i+1] == "'"):
            sent_list[i] = sent_list[i].upper()
    # convert list to a new string
    sent_final = "".join(sent_list)
    # return new string
    return sent_final

# TASK 3 ---------------------------------------------------------------------------------------------------------------
# call no_yelling() on every sentence of the yelling text and store the outputs in a new list called modified_text_split
modified_text_split = [no_yelling(yel_text_split[n]) for n in range(len(yel_text_split))]

# TASK 4 ---------------------------------------------------------------------------------------------------------------
# convert modified_text_split into a new string called modified_text with white space between the sentences
modified_text = " ".join(modified_text_split)

# TASK 5 ---------------------------------------------------------------------------------------------------------------
# create a new folder called "output", if it does not exist
if not os.path.exists("output"):
    os.mkdir("output")
# create a new text file called "noYelling.txt", if it does not exist, and store modified_text into this file
with open(os.path.join(os.getcwd(), "output", "noYelling.txt"), "w") as f:
    f.write(modified_text)


# ======================================================================================================================
# EXERCISE 2
# ======================================================================================================================

# read the covid database "covid_countries.csv" from the data folder
covid = pd.read_csv(os.path.join("data", "covid_countries.csv"))
# create an index for the rows using the country/region names
covid.index = [i for i in covid["Country/Region"]]

# TASK 1 ---------------------------------------------------------------------------------------------------------------
# Get the entire rows about Switzerland, Germany, France, Italy, and Austria
covid_Ch_De_Fr_It_At = covid.loc[["Switzerland", "Germany", "France", "Italy", "Austria"],:]

# TASK 2 ---------------------------------------------------------------------------------------------------------------
# get the entire rows representing the countries with more than 800 thousands confirmed cases
covid_red_countries = covid.loc[covid["Confirmed"] > 800000]

# TASK 3 ---------------------------------------------------------------------------------------------------------------
# get the rows "Confirmed" to "New recovered" from these rows
covid_stats_red_countries = covid_red_countries.loc[:,"Confirmed":"New recovered"]
# store the slice as "covid_statistics_red_countries.csv" to the "output" folder
covid_stats_red_countries.to_csv(os.path.join("output", "covid_statistics_red_countries.csv"), index = False)


# ======================================================================================================================
# EXERCISE 3 & BONUS
# ======================================================================================================================

# read the xlsx file with Harry Potter characters called "harry_potter_characters.xlsx" from the data folder
potter = pd.read_excel(os.path.join("data", "harry_potter_characters.xlsx"))
# get the row with actual column names and assign the correct column names to the data frame
potter.columns = list(potter.iloc[0])
# delete the redundant row
potter = potter.drop(0, axis = 0)
# reset row index numbers to start from o
potter = potter.reset_index(drop = True)

# TASK 1-4 -------------------------------------------------------------------------------------------------------------
# find all students of Gryffindor
gryffindor_students = potter.loc[(potter["Job"] == "Student") & (potter["House"] == "Gryffindor")]
# find all female characters of Hufflepuff
hufflepuff_females = potter.loc[(potter["Gender"] == "Female") & (potter["House"] == "Hufflepuff")]
# find all male characters of Ravenclaw
ravenclaw_males = potter.loc[(potter["Gender"] == "Male") & (potter["House"] == "Ravenclaw")]
# find all Pure-blood students of Slytherin
slytherin_pureblood = potter.loc[(potter["Blood status"] == "Pure-blood") & (potter["House"] == "Slytherin")]
# store findings in different sheets in one EXCEL file
with pd.ExcelWriter("output/harry_potter_houses.xlsx") as writer:
    gryffindor_students.to_excel(writer, sheet_name = "gryffindor Students", index = False)
    hufflepuff_females.to_excel(writer, sheet_name = "Hufflepuff Females", index = False)
    ravenclaw_males.to_excel(writer, sheet_name = "ravenclaw Males", index = False)
    slytherin_pureblood.to_excel(writer, sheet_name = "slytherin Pureblood", index = False)