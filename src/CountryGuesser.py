#!/usr/bin/python3

import os
import time
import datetime

s_time = time.perf_counter()

europe = ['Albania','Andorra','Armenia','Austria','Azerbaijan','Belarus','Belgium','Bosnia And Herzegovina','Bulgaria','Croatia','Cyprus','Czech Republic','Denmark','England','Estonia','Finland','France','Georgia','Germany','Greece','Hungary','Iceland','Ireland','Italy','Latvia','Liechtenstein','Lithuania','Luxembourg','Malta','Moldova','Monaco','Montenegro','Netherlands','North Macedonia','Norway','Poland','Portugal','Romania','Russia','San Marino','Scotland','Serbia','Slovakia','Slovenia','Spain','Sweden','Switzerland','Ukraine','Wales']
south_america = ['Argentina','Bolivia','Brazil','Chile','Colombia','Ecuador','Falkland Islands','French Guiana','Guyana','Paraguay','Peru','Suriname','Uruguay','Venezuela']
north_america = ['Bermuda','Canada','Greenland','Saint Pierre And Miquelon','United States Of America']
central_america = ['Belize','Costa Rica','El Salvador','Guatemala','Honduras','Nicaragua','Panama']
oceania = ['Australia','Fiji','Kiribati','Marshall Islands','Micronesia','Nauru','New Zealand','Palau','Papua New Guinea','Samoa','Solomon Islands','Tonga','Tuvalu','Vanuatu','Cook Islands','Niue']
africa = ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cabo Verde", "Cameroon", "Central African Republic", "Chad", "Comoros", "Ivory Coast", "Djibouti", "Democratic Republic of the Congo", "Egypt", "Equatorial Guinea", "Eritrea", "Eswatini", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", "Republic of the Congo", "Rwanda", "Sao Tome & Principe", "Senegal", "Seychelles", "Sierra Leone", "Somalia", "South Africa", "South Sudan", "Sudan", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"]
asia = ['Afghanistan','Armenia','Azerbaijan','Bahrain','Bangladesh','Bhutan','Cambodia','China','East Timor','India','Indonesia','Iran','Iraq','Israel','Japan','Jordan','Kazakhstan','Kuwait','Kyrgyzstan','Lebanon','Malaysia','Maldives','Mongolia','Myanmar','Nepal','North Korea','Oman','Pakistan','Palestine Brunei','Philippines','Qatar','Saudi Arabia','Singapore','South Korea','Sri Lanka','Syria','Taiwan','Tajikistan','Thailand','Turkey','Turkmenistan','United Arab Emirates','Uzbekistan','Vietnam','Yemen']

cont_null = []
cont_dict = {'South America':south_america,'North America':north_america,'Central America':central_america,'Asia':asia,'Europe':europe,'Africa':africa,'Oceania':oceania}

overall_score = 0

def __banner__():

    os.system('clear')
    print('''\nPython Game:\n\n     __   __            ___  __          __        ___  __   __   ___  __  
    /    /  \ |  | |\ |  |  |__) \ /    / __ |  | |__  /__` /__` |__  |__) 
    \__/ \__/ \__/ | \|  |  |  \  |     \__/ \__/ |___ .__/ .__/ |___ |  \ 
                                                                            ''')
    print(f"\nMade by https://github.com/0xSickb0y)\nLast Modified: 13-02-2024 14:57:00\nGlobal Score: {overall_score}\n")

def __timer__():

    global time_played
    e_time = time.perf_counter()
    elapsed_time = e_time - s_time
    time_played = str(datetime.timedelta(seconds=elapsed_time)).split('.', 1)[0]

def __game__():

    global overall_hits, overall_errors, overall_score

    overall_hits = 0
    overall_errors = 0
    score = 0
    user_input = input('\n\nContinent:\n>>> ').title()

    if user_input in cont_dict:
        cont_size = len(cont_dict[user_input])
        cont_choice = cont_dict[user_input]
        __banner__()
        print(f"Chosen continent: {user_input}",f"\nNumber of countries to guess: {cont_size}",f'\nLocal Score: {score}')
        
        while cont_size > 0:
            user_choice = input("\nCountry Guess:\n>>> ").title()

            if user_choice in cont_choice:
                __banner__()
                score = score + 1
                print(f"Chosen continent: {user_input}",f"\nNumber of countries to guess: {cont_size}",f'\nLocal Score: {score}')
                print(f"\nGood Guess!")
                cont_choice.remove(user_choice)
                overall_hits += 1
                
                if score == cont_size:
                    overall_score += 1
                    cont_null.append(user_input)
                    del cont_dict[user_input]
                    __banner__()
                    print(f"Chosen continent: {user_input}",f"\nNumber of countries to guess: {cont_size}",f'\nLocal Score: {score}')
                    print(f"\nYou finished the Continent!!!")

                    if overall_score == 7:
                        __timer__()
                        __banner__()
                        print(f"Congratulations, You finished the Game! Thank you for playing!!!\n\nNumber of Hits: {overall_hits}. Number of Errors: {overall_errors}.\n"+f"Time spent while playing: {time_played}\n")
                        exit()

                    else:    
                        __win__()

            elif user_choice not in cont_choice:
                overall_errors += 1
                __banner__()
                print(f"Chosen continent: {user_input}",f"\nNumber of countries to guess: {cont_size}",f'\nLocal Score: {score}')
                print(f"\nBad Guess!")

    elif user_input in cont_null:
        __banner__()
        print("Error! (Continent already completed). Continents available:")
        for i in cont_dict:
            print(i, end = ". ")
        __game__()

    else:
        __banner__()
        print("Error! (Invalid user input). Continents available:")        
        for i in cont_dict:
            print(i, end = ". ")
        __game__()

def __win__():

    sec_choice = input("\nDo you want to play another one? [Y/n] ").lower()

    if sec_choice == 'y':
        __banner__()
        print(f"Continents available:")
        for i in cont_dict:
            print(i, end = ". ")
        __game__()

    elif sec_choice == '':
        __banner__()
        print(f"Continents available:")
        for i in cont_dict:
            print(i, end = ". ")
        __game__()    

    elif sec_choice == 'n':
        __timer__()
        print(f"\nGoodbye...\n\nNumber of Hits: {overall_hits}. Number of Errors: {overall_errors}.\n"+f"Time spent while playing: {time_played}\n")
        exit()

    else:   
        __banner__()
        print('Error (Invalid user input). Continents available:')
        for i in cont_dict:
            print(i, end = ". ")
        print('')
        __win__()

__banner__()

print(f'Welcome to Country Guesser! To start the game, first select one of the 7 continents:')

for i in cont_dict:
    print(i, end = ". ")

__game__()
