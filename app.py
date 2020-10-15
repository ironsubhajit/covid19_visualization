import os

import pandas as pd
import folium
import webbrowser


def clean_coordinates_data(coordinates):
    """cleaning coordinates data (removing degree etc.)"""
    print('Cleaning coordinates Data...')
    coordinates['Latitude'] = coordinates['Latitude'].apply(lambda cord: cord[0:5]).astype('float')
    coordinates['Longitude'] = coordinates['Longitude'].apply(lambda cord: cord[0:5]).astype('float')
    return coordinates


def clean_covid19_data(covid19):
    """cleaning covid19 data for easy to use"""
    print('Cleaning covid19 Data...')
    covid19 = covid19.iloc[:-2, :-4]
    covid19.columns = ['State', 'Total cases', 'Deaths', 'Recoveries', 'Active cases']
    return covid19


def merged_data(coordinates, covid19):
    """merging two DataFrames"""
    print("Merging coordinates and covid19 data...")
    final_data = pd.merge(coordinates, covid19, how='inner', on='State')
    return final_data


if __name__ == '__main__':

    # get coordinates of states
    print("scraping coordinates data... ")
    info = pd.read_html(
        'http://www.quickgs.com/latitudinal-and-longitudinal-extents-of-india-indian-states-and-cities/')

    # creates a df from that table data
    coordinates = pd.DataFrame(info[0])

    # get corona statistics for the States
    print("scraping covid19 data... ")
    corona_stats = pd.read_html('https://en.wikipedia.org/wiki/COVID-19_pandemic_in_India#covid19-container',
                                match='State/Union Territory')
    # creates df from corona statistics data
    covid19 = pd.DataFrame(corona_stats[0])

    # new & cleaned coordinates data
    coordinates = clean_coordinates_data(coordinates)

    # new & cleaned covid19 data
    covid19 = clean_covid19_data(covid19)

    # joining two Dataframes
    final_data = merged_data(coordinates, covid19)