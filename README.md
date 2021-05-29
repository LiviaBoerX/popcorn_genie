# popcorn_genie
IMDb filtering script that suggests movies based on user preferences

Popcorn Genie v1.0
 
Project Description
This group project – created by students at the University of St. Gallen – focuses on the design, implementation and testing of Python programs to process data files and extract meaningful information from them.
 
Since almost everyone likes movies and it can be quite lengthy sometimes to find the right one, we chose to do a project that helps you speed up the process of finding your perfect movie. The Internet Movie Database (IMDb) is a well-known rating review platform for movies. In this project, you will be able to make use of the database provided by the platform to automatically get suggested movies not only based on their ranking, but also based on other criteria, such as language, genre, and duration. 

Data will be read from a CSV (comma-separated values) file called IMDB_database.csv
Each row in the file contains the following information on each movie in the database. 
imdb_title_id
title 
original_title
year
date_published
genre 
duration
country
language 
Director
Writer
Production_company
Actors
Description
Avg_vote
Votes
Budget
Usa_gross_income
Worlwide_gross_income
Metascore
Reviews_from_users
Reviews_from_critics
 
Criteria are split by commas.
 
Note that Python uses zero-based indexing, meaning that when data is put in a list the first value (State) will be found by taking the 0th index of the list.
 
The database is uploaded together with the document on github. 
  
Project Deliverable
The deliverable for this project is the following files:
            
python.py – the source code for your Python program
Imdb_database.csv - the database used to run the program 

 
Project Specifications
Provide the following functions – you get to choose the name and the parameters.  
 
1. Function that opens the file and stores it as a dataframe
This is done automatically.

2. Formatting the database 
Transform the average vote, year, duration variables from strings to numeric values. 

3. Function that requires user to choose their movie characteristics preferences from a list of options for string values or insert their preferences for numeric values       
Create the variables that can store the user preferences for the following movie characteristics.
Language 
Genre 
Maximum release year
Minimum release year 
Maximum movie duration
Minimum movie duration

Require the user to input their preferences for each of the variables.
When doing so you should take into account that the user may not want to input any preferences for some criteria. 

4. Select the best movie offers based on the input 
Filter criteria
Order by movie rating, the highest rating being selected first





5. Present results 
Let user determine number of results to be shown 
Let user determine whether they want a detailed or brief summary of movie characteristics of the presented movies 
Print results 
If detailed version desired, print: title, average rating, genre, language supported, length of movie, movie description, release year, movie directors, movie writers, actors
If short version desired, print: title, average rating, genre, language supported, length of movie

 Project Notes
We provide a file popcorn_genie_v1.0.py
The script imports the pandas and numpy packages.
Some user preference inputs are optional. 
The following function may prove useful in creating the filter for string value criteria: str.contains()
For further assistance, please consult: https://www.programiz.com/python-programming


Tests and Output
 
Test 1

Welcome to Popcorn Genie v1.0. Initiating boot up procedure...

Loading CSV file.
CSV file loaded.

Changing data type of some columns.
Data types changed successfully.

Creating dictionary of languages to be used later for filter validity checks.
Language dictionary successfully created.

Loading up genre dictionary.
Genre dictionary successfully loaded.

Popcorn Genie booted up correctly. Let's roll.

Input your lower limit for the year the movie was published in: 1970
Input your upper limit for the year the movie was published in: 2000
The movies will be filtered in a year range from 1970 to 2000


Input the minimum movie duration in minutes: 120
Input the maximum movie duration in minutes: 180


Input your language in English or simply leave blank if you do not r by language: Russian
Your choice of language is Russian. Great choice! I am contractually obliged to say that.


A  :  Action
B  :  Adult
C  :  Adventure
D  :  Animation
E  :  Biography
F  :  Comedy
G  :  Crime
H  :  Documentary
I  :  Drama
J  :  Family
K  :  Fantasy
L  :  Film-Noir
M  :  History
N  :  Horror
O  :  Music
P  :  Musical
Q  :  Mystery
R  :  Romance
S  :  Sci-Fi
T  :  Sport
U  :  Thriller
V  :  War
W  :  Western
LEAVE BLANK  :  NO FILTER

Select your first genre preference from the list above (Letter): S
You have chosen Sci-Fi

Select your second genre preference from the list above (Letter): I
You have chosen Drama

Select your a genre you want to EXCLUDE from the list above (Letter): C
You have chosen Adventure

Preparing results tailored to your interests...

Number of movies available in the year range you selected: 22502
Number of movies available with the desired year range and duration: 2795
Number of movies available with the desired year range, duration and language: 141
Number of movies available with the desired year range, duration, language and genre preference 1: 13
Number of movies available with the desired year range, duration, language and 2 genre preferences: 7
Number of movies available with the desired year range, duration, language and 3 genre preferences: 7

Process complete.


Please insert the NUMBER of results you would like to have presented: 8
Only 7 results are available 
Do you want to see detailed results? (yes/no): yes




####################################################
Title: Stalker
Average rating: 8.2
Genre: Drama, Sci-Fi
Languages supported: Russian
Length of movie: 162 min

Movie description:
 A guide leads two men through an area known as the Zone to find a room that grants wishes. 

Release year: 1979

Movie directors: Andrei Tarkovsky 

Movie writers: Arkadiy Strugatskiy, Boris Strugatskiy 

Actors in this movie: Alisa Freyndlikh, Aleksandr Kaydanovskiy, Anatoliy Solonitsyn, Nikolay Grinko, Natalya Abramova, Faime Jurno, E. Kostin, Raymo Rendi 

########################################################


####################################################
Title: Solaris
Average rating: 8.1
Genre: Drama, Mystery, Sci-Fi
Languages supported: Russian, German
Length of movie: 167 min

Movie description:
 A psychologist is sent to a station orbiting a distant planet in order to discover what has caused the crew to go insane. 

Release year: 1972

Movie directors: Andrei Tarkovsky 

Movie writers: Stanislaw Lem, Fridrikh Gorenshteyn 

Actors in this movie: Natalya Bondarchuk, Donatas Banionis, Jüri Järvet, Vladislav Dvorzhetskiy, Nikolay Grinko, Anatoliy Solonitsyn, Olga Barnet, Vitalik Kerdimun, Olga Kizilova, Tatyana Malykh, Aleksandr Misharin, Bagrat Oganesyan, Tamara Ogorodnikova, Sos Sargsyan, Yulian Semyonov 

########################################################


####################################################
Title: Kin-dza-dza!
Average rating: 8.1
Genre: Comedy, Drama, Sci-Fi
Languages supported: Georgian, Russian
Length of movie: 135 min

Movie description:
 Two Russians push the wrong button on a strange device and end up on the telepathic planet Pluke with its strange societal norms. 

Release year: 1986

Movie directors: Georgiy Daneliya 

Movie writers: Georgiy Daneliya, Revaz Gabriadze 

Actors in this movie: Stanislav Lyubshin, Evgeniy Leonov, Yuriy Yakovlev, Levan Gabriadze, Olga Mashnaya, Irina Shmeleva, Lev Perfilov, Anatoliy Serenko, Aleksandra Dorokhina, Olesya Ivanova, Tatyana Novitskaya, Tatyana Perfileva, Lyudmila Solodenko, Galina Daneliya-Yurkova, Igor Bogolyubov 

########################################################


####################################################
Title: Zerkalo dlya geroya
Average rating: 7.5
Genre: Drama, Fantasy, Sci-Fi
Languages supported: Russian
Length of movie: 139 min

Movie description:
 Two not quite similar men, our contemporaries, psychologist-linguist Sergey Pshenichny and former mining engineer Andrew Nemchinov, are walking in the street in their native miners town and... 

Release year: 1987

Movie directors: Vladimir Khotinenko, Violetta Sedova 

Movie writers: Nadezhda Kozhushanaya, Svyatoslav Rybas 

Actors in this movie: Sergey Koltakov, Ivan Bortnik, Boris Galkin, Feliks Stepun, Natalya Akimova, Elena Golyanova, Yakov Stepanov, Viktor Smirnov, Nikolay Stotskiy, Sergei Parshin, Valentin Aronyan, Aleksandr Peskov, Yelena Kozlitina, Denis Tsys, Mikhail Chernobrovkin 

########################################################


####################################################
Title: Contact
Average rating: 7.4
Genre: Drama, Mystery, Sci-Fi
Languages supported: English, Spanish, German, Russian
Length of movie: 150 min

Movie description:
 Dr. Ellie Arroway, after years of searching, finds conclusive radio proof of extraterrestrial intelligence, sending plans for a mysterious machine. 

Release year: 1997

Movie directors: Robert Zemeckis 

Movie writers: James V. Hart, Michael Goldenberg 

Actors in this movie: Jena Malone, David Morse, Jodie Foster, Geoffrey Blake, William Fichtner, Sami Chester, Timothy McNeil, Laura Elena Surillo, Matthew McConaughey, Tom Skerritt, Henry Strozier, Max Martini, Larry King, Thomas Garner, Conroy Chino 

########################################################


####################################################
Title: Posetitel muzeya
Average rating: 7.3
Genre: Drama, Sci-Fi
Languages supported: Russian
Length of movie: 136 min

Movie description:
 In a post-apocalyptic world, in which a large part of the population consists of demented and deformed mutants being kept in reservations, a man embarks upon visiting the ruins of a museum ... 

Release year: 1989

Movie directors: Konstantin Lopushanskiy 

Movie writers: Konstantin Lopushanskiy 

Actors in this movie: Viktor Mikhaylov, Vera Mayorova, Vadim Lobanov, Irina Rakshina, Aleksandr Rasinsky, Iosif Ryklin, Yu. Sobolev, Vladimir Firsov 

########################################################


####################################################
Title: I giorni dell'eclisse
Average rating: 7.1
Genre: Drama, Sci-Fi
Languages supported: Russian, Armenian, Turkmen, Azerbaijani, Italian
Length of movie: 139 min

Movie description:
 Days of Eclipse is filmed in a psychedelic manner close to stream of consciousness using unusual cinematographic techniques. The action is set in Middle Asia. 

Release year: 1988

Movie directors: Aleksandr Sokurov 

Movie writers: Arkadiy Strugatskiy, Boris Strugatskiy 

Actors in this movie: Aleksei Ananishnov, Eskender Umarov, Irina Sokolova, Vladimir Zamanskiy, Kirill Dudkin, Aleksey Yankovskiy, Viktor Belovolskiy, Sergei Krylov 

########################################################
 
 
Test 2

Welcome to Popcorn Genie v1.0. Initiating boot up procedure...

Loading CSV file.
CSV file loaded.

Changing data type of some columns.
Data types changed successfully.

Creating dictionary of languages to be used later for filter validity checks.
Language dictionary successfully created.

Loading up genre dictionary.
Genre dictionary successfully loaded.

Popcorn Genie booted up correctly. Let's roll.

Input your lower limit for the year the movie was published in: 1980
Input your upper limit for the year the movie was published in: 2025
The movies will be filtered in a year range from 1980 to 2025


Input the minimum movie duration in minutes: 1
Input the maximum movie duration in minutes: 999


Input your language in English or simply leave blank if you do not r by language: Italian
Your choice of language is Italian. Great choice! I am contractually obliged to say that.


A  :  Action
B  :  Adult
C  :  Adventure
D  :  Animation
E  :  Biography
F  :  Comedy
G  :  Crime
H  :  Documentary
I  :  Drama
J  :  Family
K  :  Fantasy
L  :  Film-Noir
M  :  History
N  :  Horror
O  :  Music
P  :  Musical
Q  :  Mystery
R  :  Romance
S  :  Sci-Fi
T  :  Sport
U  :  Thriller
V  :  War
W  :  Western
LEAVE BLANK  :  NO FILTER

Select your first genre preference from the list above (Letter): R
You have chosen Romance

Select your second genre preference from the list above (Letter): 

Select your a genre you want to EXCLUDE from the list above (Letter): Q
You have chosen Mystery

Preparing results tailored to your interests...

Number of movies available in the year range you selected: 63432
Number of movies available with the desired year range and duration: 63432
Number of movies available with the desired year range, duration and language: 2587
Number of movies available with the desired year range, duration, language and genre preference 1: 400
Number of movies available with the desired year range, duration, language and 2 genre preferences: 400
Number of movies available with the desired year range, duration, language and 3 genre preferences: 387

Process complete.


Please insert the NUMBER of results you would like to have presented: 4
Do you want to see detailed results? (yes/no): no




####################################################
Title: La vita è bella
Average rating: 8.6
Genre: Comedy, Drama, Romance
Languages supported: Italian, German, English
Length of movie: 116 min


####################################################
Title: La meglio gioventù
Average rating: 8.5
Genre: Drama, Romance
Languages supported: Italian, English, Norwegian
Length of movie: 366 min


####################################################
Title: Ritratto della giovane in fiamme
Average rating: 8.1
Genre: Drama, Romance
Languages supported: French, Italian
Length of movie: 122 min


####################################################
Title: La leggenda del pianista sull'oceano
Average rating: 8.1
Genre: Drama, Music, Romance
Languages supported: English, French, Italian
Length of movie: 169 min


