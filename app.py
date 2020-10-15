import os

import pandas as pd
import folium
import webbrowser

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
