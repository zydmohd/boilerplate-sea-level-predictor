import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df=pd.read_csv("epa-sea-level.csv")


    # Create scatter plot
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])


    # Create first line of best fit
    m = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    xn = np.arange(df["Year"].min(),2051,1)
    yn=xn*(m.slope)+(m.intercept)
    plt.plot(xn,yn)

    # Create second line of best fit
    df2000=df[df["Year"]>=2000]
    m2000=linregress(df2000['Year'], df2000['CSIRO Adjusted Sea Level'])
    xn2000 = np.arange(2000,2051,1)
    yn2000=xn2000*(m2000.slope)+(m2000.intercept)
    plt.plot(xn2000,yn2000)

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()