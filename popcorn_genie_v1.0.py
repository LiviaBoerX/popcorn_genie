# importing pandas and numpy packages
import pandas as pd
import numpy as np

# Print welcome message
print('Welcome to Popcorn Genie v1.0. Initiating boot up procedure...')

# Reading the CSV file and storing it as a dataframe.
print('\nLoading CSV file.')
df = pd.read_csv('imdb_database.csv', dtype=object)
print('CSV file loaded.')

# Formatting the database. By default, all columns are treated as strings. The code below ensures that specific columns which we need for comparisons are treated as numerical values.
print('\nChanging data type of some columns.')
df['avg_vote'] = pd.to_numeric(df['avg_vote'])
df['year'] = pd.to_numeric(df['year'])
df['duration'] = pd.to_numeric(df['duration'])
print('Data types changed successfully.')

# Database with list of langauges only. Used later for filter check validity.
print("\nCreating dictionary of languages to be used later for filter validity checks.")
df_new = df["language"]  # we craete a database with only the languages
print("Language dictionary successfully created.")

# Create library that will be used for the "genre" request to avoid typos
print('\nLoading up genre dictionary.')
genre = {"A": "Action", "B": "Adult", "C": "Adventure", "D": "Animation", "E": "Biography", "F": "Comedy", "G": "Crime",
         "H": "Documentary", "I": "Drama", "J": "Family", "K": "Fantasy", "L": "Film-Noir", "M": "History",
         "N": "Horror", "O": "Music",
         "P": "Musical", "Q": "Mystery", "R": "Romance", "S": "Sci-Fi", "T": "Sport", "U": "Thriller", "V": "War",
         "W": "Western", "LEAVE BLANK": "NO FILTER"
         }
print('Genre dictionary successfully loaded.')

print('\nPopcorn Genie booted up correctly. Let\'s roll.\n')

# Allow input for YEAR preferences
while True:
    try:
        
        input_year_min = int(input("Input your lower limit for the year the movie was published in: "))
        input_year_max = int(input("Input your upper limit for the year the movie was published in: "))
    except:  # Check for wrong input
        print(
            "Your input is invalid. Ensure you are inputting a number. If you do not care about the movie publshing date, simply input a large max value like 9999 and a low input value like 0.")
        continue

    if input_year_max < input_year_min:  # Require input year miniumum to be smaller than the maximum year
        print("Lower year limit cannot be greater than upper year limit. Try again and invert your values!\n")
    else:
        break
print(
    f"The movies will be filtered in a year range from {input_year_min} to {input_year_max}")  # Confirm to user his selection

print("\n") #just formatting
# Allow input for DURATION preferences
while True:
    try:
        input_duration_min = int(input("Input the minimum movie duration in minutes: "))  # Max duration input
        input_duration_max = int(input("Input the maximum movie duration in minutes: "))  # Min duration input
    except:  # check for input mistakes
        print(
            "Your input is invalid. Ensure you are inputting a number. If you do not care about movie length, simply input a large max value like 9999 and a low min value like 0.")  # Provide explanation of what to do if input is wrong or no input is wanted
        continue

    if input_duration_max < input_duration_min:
        print(
            "Lower year limit cannot be greater than upper year limit. Try again and invert your values!\n")  # Provide explanation that max duration is smaller than minimum duration
    else:
        break

print("\n") #just formatting
# Allow input for LANGUAGE preferences
while True:
    input_language = input(
        "Input your language in English or simply leave blank if you do not wish to filter by language: ").capitalize()  # Require LANGUAGE input
    if input_language != "" and input_language != " ":  # Giving the possibility to skip the selection

        if input_language in df_new.values:  # Check if the language is in the database and provide confirmation
            print(f"Your choice of language is {input_language}. Great choice! I am contractually obliged to say that.")
            break
        else:
            print(
                "The language as written is not in the database. Try again. If you do not wish to filter by language, simply leave the input field blank.")  # Error message if input is not in database
            input_language = ""  # Cancel the value in the variable to avoid errors in filtering
    else:
        print("No langauge filter selected.")  # State that no language is selected
        break

print("\n") #just formatting
# Allow input for GENRE preferences
for key, value in genre.items():  # Print the dictionary
    print(key, ' : ', value)
try:
    input_genre_one = input(
        "\nSelect your first genre preference from the list above (Letter): ").upper()  # 1st GENRE input

    if input_genre_one != "" and input_genre_one != " ":
        if input_genre_one in genre:
            print("You have chosen %s" % genre.get(input_genre_one))  # Confirm choice
            input_genre_one = genre.get(input_genre_one)  # Converting the key to the dictionary value
        else:
            print("Invalid Key. Setting this filter input to BLANK.")  # Error message if wrong selection
            input_genre_one = ""  # Cancel the value in the variable to avoid errors in filtering


        input_genre_two = input(
            "\nSelect your second genre preference from the list above (Letter): ").upper()  # 2 GENRE input. Requested only if a first preference is expressed

        if input_genre_two != "" and input_genre_two != " ":  # Code = to genre 1
            if input_genre_two in genre:
                print("You have chosen %s" % genre.get(input_genre_two))  # Confirm choice of genre number 2
                input_genre_two = genre.get(input_genre_two)
            else:
                print("Invalid Key. Setting this filter input to BLANK.")  # Allow for a blank if wrong insertion
                input_genre_two = ""

    else:
        input_genre_two = "" #If filter 1 is skipped, filter 2 is defined as "", thus also skipped.
        
    input_genre_three = input(
        "\nSelect your a genre you want to EXCLUDE from the list above (Letter): ").upper()  # 3 GENRE input. Requested only if a second preference is expressed

    if input_genre_three != "" and input_genre_three != " ":  # Code = to genre 1
        if input_genre_three in genre:
            print("You have chosen %s" % genre.get(input_genre_three))  # Confirm choice of genre number 3
            input_genre_three = genre.get(input_genre_three)
        else:
            print("Invalid Key. Setting this filter input to BLANK.")  # Allow for a blank if wrong insertion
            input_genre_three = ""
except:
    print(
        "Unforeseen error. Genre filtering set to blank. This is not even possible to happen. How did you accomplish this, you maniac?")  # In case of mistake, genre filtering is reset
    input_genre_one = ""
    input_genre_two = ""
    input_genre_three = ""




print("\nPreparing results tailored to your interests...\n")

# FILTERING

# NUMERIC FILTER
# YEAR
df = df[df["year"] < input_year_max]
df = df[df["year"] > input_year_min]
print("Number of movies available in the year range you selected: %s" % len(
    df.index))  # checking how many movies correspond to the year range
# DURATION
df = df[df['duration'] < input_duration_max]
df = df[df['duration'] > input_duration_min]
print("Number of movies available with the desired year range and duration: %s" % len(df.index))




# STRING FILTER
# LANGUAGE
if input_language != "" and input_language != " ":  # print only if something is stored
    df = df[df['language'].str.contains(input_language)]
    print("Number of movies available with the desired year range, duration and language: %s" % len(df.index))


# GENRE
if input_genre_one != "" and input_genre_one != " ":  # filter only if something is stored
    df = df[df['genre'].str.contains(input_genre_one)]
print("Number of movies available with the desired year range, duration, language and genre preference 1: %s" % len(
    df.index))


if input_genre_two != "" and input_genre_two != " ":  # filter only if something is stored
    df = df[df['genre'].str.contains(input_genre_two)]
print("Number of movies available with the desired year range, duration, language and 2 genre preferences: %s" % len(
    df.index))

if input_genre_three != "" and input_genre_three != " ":  # filter only if something is stored
    df = df[~df['genre'].str.contains(input_genre_three)]
print("Number of movies available with the desired year range, duration, language and 3 genre preferences: %s" % len(
    df.index))
df = df.sort_values(['avg_vote'], ascending=False)  # sorting values by Rating
print("\nProcess complete.")



print("\n")
# OUTPUT
n = len(df.index)  # number of results matching user inputs
if len(df.index) == 0:  # control if the research has output
    print("Unfortunately, your movie taste is simply too exquisite. No results found matching your choices.")
    quit()

while True:
    try:
        x = int(input(
            "Please insert the NUMBER of results you would like to have presented: "))  # require input of desired number of results
        break
    except ValueError:
        print("Enter a number. Try again.")  # if error, require user to retry

if x > len(df.index):  # warning the user that the number of movies requested is higher than the results
    print("Only %s results are available " % len(df.index))

y = input(
    "Do you want to see detailed results? (yes/no): ")  # let user choose whether he wants a detailed or brief description of the movies that are suggested


print("\n")
if y.lower() == "yes":  # print complete results
    for i in range(0, min(x,
                          len(df.index))):  # if the results are less than the number requested, the program shows the results
        current_movie = df.iloc[i]
        print("\n\n####################################################")
        print("Title:", current_movie['title'])
        print("Average rating:", current_movie['avg_vote'])
        print("Genre:", current_movie['genre'])
        print("Languages supported:", current_movie['language'])
        print("Length of movie:", current_movie['duration'], "min")

        print("\nMovie description:\n", current_movie['description'], "\n")

        print("Release year:", current_movie['year'])

        print("\nMovie directors:", current_movie['director'], "\n")
        print("Movie writers:", current_movie['writer'], "\n")
        print("Actors in this movie:", current_movie['actors'], "\n")
        print("########################################################")
else:  # print short results
    for i in range(0, min(x, len(df.index))):
        current_movie = df.iloc[i]
        print("\n\n####################################################")
        print("Title:", current_movie['title'])
        print("Average rating:", current_movie['avg_vote'])
        print("Genre:", current_movie['genre'])
        print("Languages supported:", current_movie['language'])
        print("Length of movie:", current_movie['duration'], "min")
