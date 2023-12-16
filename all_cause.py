import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("NCHS_-_Leading_Causes_of_Death__United_States.csv")
all_causes = list(set(data["Cause Name"].to_list()))
response = "Default"
years = [1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008,
         2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017]

intro = "Welcome to all_cause. Type in the name of a state you want \n"
intro += "to get the top 10 leading causes of death from 1999-2007. \n"
intro += "To get the data for America as a whole, type \"America\". \n"
intro += "When you're done using the program, type \"Quit\". \n"
print(intro)

while True:
    response = input("Please type your input: ")
    response = response.lower().capitalize()
    if response == "America":
        response = "United States"

    elif response == "Quit":
        break

    elif response not in set(data.State):
        print("Not a valid input. Defaulting to \"America\"")
        response = "United States"

    data_for_state = data[data["State"] == response]
    for cause in all_causes:
        data_for_cause = data_for_state[data_for_state["Cause Name"] == cause]
        death_rate = data_for_cause["Age-adjusted Death Rate"].to_list()
        plt.plot(years, death_rate)

    title = "Age-Adjusted Death Rates For Top 10 Causes Of Death In "
    title += response + ", 1999-2017"
    plt.title(title)
    plt.legend(all_causes)
    plt.show()
