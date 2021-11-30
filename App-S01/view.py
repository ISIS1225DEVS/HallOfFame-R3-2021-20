"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import folium as fl
import config as cf
import controller
import sys
assert cf

default_limit = 1000
sys.setrecursionlimit(default_limit*10)
###############################################################################################################
# Exposición de resultados
###############################################################################################################

def PrintTable1(first_events_list, last_events_list):
    print('+' + 22*'-' + '+' + 50*'-' + '+' + 10*'-'+ '+' + 10*'-' + '+' + 11*'-' + '+' + 16*'-' + '+')
    print('| {:<21}| {:<49}| {:<9}| {:<9}| {:<10}|{:>15} |'.format('datetime', 'city', 'state', 'country',
                                                                        'shape', 'duration (seg)'))
    print('+' + 22*'=' + '+' + 50*'=' + '+' + 10*'=' + '+' + 10*'=' + '+' + 11*'=' + '+' + 16*'=' + '+')
    for event in first_events_list:
        datetime = event['datetime']
        city = event['city']
        state = event['state']
        country = event['country']
        shape = event['shape']
        duration = int(float(event['duration (seconds)']))
        print('| {:<21}| {:<49}| {:<9}| {:<9}| {:<10}|{:>15} |'.format(datetime, city, state, country,
                                                                                        shape, duration))
        print('+' + 22*'=' + '+' + 50*'=' + '+' + 10*'=' + '+' + 10*'=' + '+' + 11*'=' + '+' + 16*'=' + '+')
    for event in last_events_list:
        datetime = event['datetime']
        city = event['city']
        state = event['state']
        country = event['country']
        shape = event['shape']
        duration = int(float(event['duration (seconds)']))
        print('| {:<21}| {:<49}| {:<9}| {:<9}| {:<10}|{:>15} |'.format(datetime, city, state, country,
                                                                                        shape, duration))
        print('+' + 22*'=' + '+' + 50*'=' + '+' + 10*'=' + '+' + 10*'=' + '+' + 11*'=' + '+' + 16*'=' + '+')

###############################################################################################################

def PrintTable2(first_events_list, last_events_list):
    print('+' + 22*'-' + '+' + 50*'-' + '+' + 10*'-'+ '+' + 10*'-' + '+' + 11*'-' + '+' + 16*'-' + '+' + 12*'-' + '+' + 12*'-' + '+')
    print('| {:<21}| {:<49}| {:<9}| {:<9}| {:<10}|{:>15} |{:>11} |{:>11} |'.format('datetime', 'city', 'state', 'country',
                                                                        'shape', 'duration (seg)', 'latitude', 'longitude'))
    print('+' + 22*'=' + '+' + 50*'=' + '+' + 10*'=' + '+' + 10*'=' + '+' + 11*'=' + '+' + 16*'=' + '+' + 12*'=' + '+' + 12*'=' + '+')
    for event in first_events_list:
        datetime = event['datetime']
        city = event['city']
        state = event['state']
        country = event['country']
        shape = event['shape']
        duration = int(float(event['duration (seconds)']))
        latitude = round(float(event['latitude']), 2)
        longitude = round(float(event['longitude']), 2)
        print('| {:<21}| {:<49}| {:<9}| {:<9}| {:<10}|{:>15} |{:>11} |{:>11} |'.format(datetime, city, state, country,shape, duration,
                                                                               latitude, longitude))
        print('+' + 22*'=' + '+' + 50*'=' + '+' + 10*'=' + '+' + 10*'=' + '+' + 11*'=' + '+' + 16*'=' + '+' + 12*'=' + '+' + 12*'=' + '+')
    for event in last_events_list:
        datetime = event['datetime']
        city = event['city']
        state = event['state']
        country = event['country']
        shape = event['shape']
        duration = int(float(event['duration (seconds)']))
        latitude = round(float(event['latitude']), 2)
        longitude = round(float(event['longitude']), 2)
        print('| {:<21}| {:<49}| {:<9}| {:<9}| {:<10}|{:>15} |{:>11} |{:>11} |'.format(datetime, city, state, country,shape, duration,
                                                                               latitude, longitude))
        print('+' + 22*'=' + '+' + 50*'=' + '+' + 10*'=' + '+' + 10*'=' + '+' + 11*'=' + '+' + 16*'=' + '+' + 12*'=' + '+' + 12*'=' + '+')  

###############################################################################################################

def PrintRequirement1(city, first_events_list, last_events_list, 
                                                        num_cities, most_events_city, num_events_city):
    print('=============== Req No. 1 Inputs ===============')
    print('UFO Sightings in the city of:', city)
    print('')
    print('=============== Req No. 1 Answer ===============')
    print('There are', num_cities, 'different cities with UFO sightings...')
    print('The city with most UFO sightings is:', most_events_city)
    print('')
    print('There are', num_events_city, 'sightings at the:', city, 'city.')
    print('The first 3 and last 3 UFO sightings in the city are:')
    PrintTable1(first_events_list, last_events_list)

###############################################################################################################

def PrintRequirement2(initial_duration, end_duration, first_events_list, last_events_list, 
                    num_durations, longest_duration, num_events_longest_duration, num_events_duration_interval):
    print('=============== Req No. 2 Inputs ===============')
    print('UFO Sightings between', initial_duration, 'and', end_duration, 'seg')
    print('')
    print('=============== Req No. 2 Answer ===============')
    print('There are', num_durations, 'different durations of UFO sightings...')
    print('The longest UFO sightings are:')
    print('+' + 21*'-' + '+' + 8*'-' + '+')
    print('|{:>20} |{:>7} |'.format('duration (seconds)', 'count'))
    print('+' + 21*'=' + '+' + 8*'=' + '+')
    print('|{:>20} |{:>7} |'.format(int(longest_duration), num_events_longest_duration))
    print('+' + 21*'-' + '+' + 8*'-' + '+')
    print('')
    print('There are', num_events_duration_interval, 'sightings between:', float(initial_duration), 'and', 
                                                                    float(end_duration), 'seg of duration')
    print('The first 3 and last 3 UFO sightings in the duration time are:')
    PrintTable1(first_events_list, last_events_list)

###############################################################################################################

def PrintRequirement3(initial_time, end_time, first_events_list, last_events_list, 
                                    num_times, latest_time, num_events_latest_time, num_events_time_interval):
    print('=============== Req No. 3 Inputs ===============')
    print('UFO Sightings between', initial_time, 'and', end_time)
    print('')
    print('=============== Req No. 3 Answer ===============')
    print('There are', num_times, 'UFO sightings with different times [hh:mm:ss]...')
    print('The latest UFO sightings time is:')
    print('+' + 10*'-' + '+' + 8*'-' + '+')
    print('|{:^9} |{:>7} |'.format('time', 'count'))
    print('+' + 10*'=' + '+' + 8*'=' + '+')
    print('|{:>9} |{:>7} |'.format(str(latest_time)[11:], num_events_latest_time))
    print('+' + 10*'-' + '+' + 8*'-' + '+')
    print('')
    print('There are', num_events_time_interval, 'sightings between:', initial_time, 'and', end_time)
    print('The first 3 and last 3 UFO sightings in this time are:')
    PrintTable1(first_events_list, last_events_list)
    
###############################################################################################################

def PrintRequirement4(initial_date, end_date, first_events_list, last_events_list, 
                                    num_dates, oldest_date, num_events_oldest_date, num_events_date_interval):
    print('=============== Req No. 4 Inputs ===============')
    print('UFO Sightings between', initial_date, 'and', end_date)
    print('')
    print('=============== Req No. 4 Answer ===============')
    print('There are', num_dates, 'UFO sightings with different times [YYYY-MM-DD]...')
    print('The oldest UFO sightings date is:')
    print('+' + 12*'-' + '+' + 8*'-' + '+')
    print('|{:^11} |{:>7} |'.format('date', 'count'))
    print('+' + 12*'=' + '+' + 8*'=' + '+')
    print('|{:>11} |{:>7} |'.format(str(oldest_date)[:10], num_events_oldest_date))
    print('+' + 12*'-' + '+' + 8*'-' + '+')
    print('')
    print('There are', num_events_date_interval, 'sightings between:', initial_date, 'and', end_date)
    print('The first 3 and last 3 UFO sightings in this time are:')
    PrintTable1(first_events_list, last_events_list)

###############################################################################################################

def PrintRequirement5(initial_longitude, end_longitude,initial_latitude, end_latitude, 
                                                        first_events_list, last_events_list, num_events_area):
    print('=============== Req No. 5 Inputs ===============')
    print('UFO Sightings between latitude range of', initial_latitude, 'and', end_latitude)
    print('plus longitude range of', initial_longitude, 'and', end_longitude)
    print('')
    print('=============== Req No. 5 Answer ===============')
    print('There are', num_events_area, 'different UFO sightings in the current area')
    print('The first 5 and last 5 UFO sightings in this time are:')
    PrintTable2(first_events_list, last_events_list)                         


############################################################################################################### 

def PrintRequirement6(area_events_list, initial_longitude, end_longitude, initial_latitude, end_latitude):
    middle_longitude = (initial_longitude + end_longitude)/2
    middle_latitude = (initial_latitude + end_latitude)/2

    events_map = fl.Map(location=[middle_latitude, middle_longitude])

    for event in area_events_list:
        event_latitude = event['latitude']
        event_longitude = event['longitude']
        fl.Marker([event_latitude, event_longitude]).add_to(events_map)
    
    events_map.fit_bounds([(end_latitude, end_longitude), (initial_latitude, initial_longitude)])
    events_map.save('events_map.html')
    print('The map generated by the program can be consulted in the main folder of the proyect as an HTML file.')
    print("The name of the HTML file is 'events_map.html'.")

###############################################################################################################
# Menu principal
###############################################################################################################

catalog = None

def Menu():
    print('')
    print('Welcome')
    print('0- Load information')
    print('1- Requirement 1')
    print('2- Requirement 2')
    print('3- Requirement 3')
    print('4- Requirement 4')
    print('5- Requirement 5')
    print('6- Requirement 6')
    print('7- Finish program')
    option = int(input('Choose an option: '))
    return option

def UserProgram(test, option, catalog, input_1, input_2, input_3, input_4):
    if not test:
        option = Menu()
        while option != 7:
            if option == 0:
                print('There exist 80332 sightings registred in UFOS-utf8-large.csv')
                sample_size = int(input('Enter the number of sightings to load: '))
                print('Loading Information from UFOS-utf8-large.csv...')
                catalog = controller.initialization()
                controller.loadData(catalog, sample_size)
                                                            
            elif option == 1:
                city = input('Enter a City: ')
                print('')
                print('Loading...')
                information = controller.Requirement1(catalog, city)
                time_elapsed = information[0]
                first_events_list = information[1]
                last_events_list = information[2]
                num_cities = information[3]
                most_events_city = information[4]
                num_events_city = information[5]
                print('')
                print('The requirement took', time_elapsed, 'mseg to execute')
                print('')
                PrintRequirement1(city, first_events_list, last_events_list, 
                                                        num_cities, most_events_city, num_events_city)

            elif option == 2:
                initial_duration = int(input('Enter the first duration of the interval: '))
                end_duration = int(input('Enter the last duration of the interval: ')) 
                print('')
                print('Loading...')
                information = controller.Requirement2(catalog, initial_duration, end_duration)
                time_elapsed = information[0]
                first_events_list = information[1]
                last_events_list = information[2]
                num_durations = information[3]
                longest_duration = information[4]
                num_events_longest_duration = information[5]
                num_events_duration_interval = information[6]
                print('')
                print('The requirement took', time_elapsed, 'mseg to execute')
                print('')
                PrintRequirement2(initial_duration, end_duration, first_events_list, last_events_list, 
                    num_durations, longest_duration, num_events_longest_duration, num_events_duration_interval)

            elif option == 3:
                initial_time = input('Enter the first time of the interval [hh:mm:ss]: ')
                end_time = input('Enter the last time of the interval [hh:mm:ss]: ')
                print('')
                print('Loading...')
                information = controller.Requirement3(catalog, initial_time, end_time)
                time_elapsed = information[0]
                first_events_list = information[1]
                last_events_list = information[2]
                num_times = information[3]
                latest_time = information[4]
                num_events_latest_time = information[5]
                num_events_time_interval = information[6]
                print('')
                print('The requirement took', time_elapsed, 'mseg to execute')
                print('')
                PrintRequirement3(initial_time, end_time, first_events_list, last_events_list, 
                                        num_times, latest_time, num_events_latest_time, num_events_time_interval)

            elif option == 4:
                initial_date = input('Enter the first date of the interval [YYYY-MM-DD]: ')
                end_date = input('Enter the last date of the interval [YYYY-MM-DD]: ')
                print('')
                print('Loading...')
                information = controller.Requirement4(catalog, initial_date, end_date)
                time_elapsed = information[0]
                first_events_list = information[1]
                last_events_list = information[2]
                num_dates = information[3]
                oldest_date = information[4]
                num_events_oldest_date = information[5]
                num_events_date_interval = information[6]
                print('')
                print('The requirement took', time_elapsed, 'mseg to execute')
                print('')
                PrintRequirement4(initial_date, end_date, first_events_list, last_events_list, 
                                        num_dates, oldest_date, num_events_oldest_date, num_events_date_interval)

            elif option == 5:
                initial_longitude = round(float(input('Enter the first longitude of the interval: ')), 2)
                end_longitude = round(float(input('Enter the last longitude of the interval: ')), 2)
                initial_latitude = round(float(input('Enter the first latitude of the interval: ')), 2)
                end_latitude = round(float(input('Enter the last latitude of the interval: ')), 2)
                print('')
                print('Loading...')
                information = controller.Requirement5(catalog, initial_longitude, end_longitude,
                                                                                    initial_latitude, end_latitude)
                time_elapsed = information[0]
                first_events_list = information[1]
                last_events_list = information[2]
                num_events_area = information[3]      
                print('')
                print('The requirement took', time_elapsed, 'mseg to execute')
                print('')
                PrintRequirement5(initial_longitude, end_longitude,initial_latitude, end_latitude, 
                                                            first_events_list, last_events_list, num_events_area)                                                         

            elif option == 6:
                initial_longitude = round(float(input('Enter the first longitude of the interval: ')), 2)
                end_longitude = round(float(input('Enter the last longitude of the interval: ')), 2)
                initial_latitude = round(float(input('Enter the first latitude of the interval: ')), 2)
                end_latitude = round(float(input('Enter the last latitude of the interval: ')), 2)
                print('')
                print('Loading...')
                information = controller.Requirement5(catalog, initial_longitude, end_longitude,
                                                                                    initial_latitude, end_latitude) 
                time_elapsed = information[0]
                area_events_list = information[1]                                                
                print('')
                print('The requirement took', time_elapsed, 'mseg to execute')
                print('')
                PrintRequirement6(area_events_list, initial_longitude, end_longitude, initial_latitude, end_latitude)

            else:
                print('Please choose a valid option')
                
            option = Menu()

        print('Finishing program...')

    else:
        if option == 0:
           catalog = controller.initialization()
           controller.loadData(catalog, input_1)
           return  catalog
        elif option == 1:
            return controller.Requirement1(catalog, input_1)[0]
        elif option == 2:
            return controller.Requirement2(catalog, input_1, input_2)[0]
        elif option == 3:
            return controller.Requirement3(catalog, input_1, input_2)[0]
        elif option == 4:
            return controller.Requirement4(catalog, input_1, input_2)[0]  
        elif option == 5:
            return controller.Requirement5(catalog, input_1, input_2, input_3, input_4)[0]
        elif option == 6:
            return controller.Requirement6(catalog, input_1, input_2, input_3, input_4)[0]
    
UserProgram(False, 0, catalog, 0, 0, 0, 0)