#name: ibrahim johar farooqi
#date: 25 september 2024
#lab: 06
#task: 5

import pandas as pd

my_data = {
    'Year': [1986, 1986, 1985, 1987, 1985, 1988, 1989, 1990, 1987, 1991,
             1986, 1988, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999],
    'WHO Region': ['Western Pacific', 'Americas', 'Africa', 'Western Pacific', 'Africa', 'Americas', 'Western Pacific', 'Africa',
                   'Western Pacific', 'Americas', 'Western Pacific', 'Americas', 'Africa', 'Western Pacific', 'Americas',
                   'Africa', 'Western Pacific', 'Americas', 'Africa', 'Western Pacific'],
    'Country': ['Viet Nam', 'Uruguay', "Cte d'Ivoire", 'Japan', "Cte d'Ivoire", 'Brazil', 'China', 'Nigeria',
                'Korea', 'Argentina', 'Australia', 'Mexico', 'South Africa', 'Malaysia', 'Canada', 'Egypt',
                'New Zealand', 'Chile', 'Kenya', 'Philippines'],
    'Beverage Types': ['Wine', 'Other', 'Wine', 'Beer', 'Wine', 'Beer', 'Wine', 'Other',
                       'Beer', 'Wine', 'Other', 'Wine', 'Beer', 'Wine', 'Other', 'Wine',
                       'Beer', 'Wine', 'Beer', 'Wine'],
    'Display Value': [0, 0.5, 1.62, 2.1, 1.25, 3.0, 0.8, 1.0, 2.5, 0.9,
                      0, 0.45, 1.75, 0.6, 0.85, 1.5, 2.0, 0.7, 1.95, 1.1]
}

data = pd.DataFrame(data=my_data)
print("dimensions: ", data.shape)
print("columns: ", data.columns)
