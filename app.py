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