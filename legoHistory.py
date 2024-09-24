import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# Datasets
colors = pd.read_csv("D:\\Downloads\\noBorrar\\colors.csv")
sets = pd.read_csv("D:\\Downloads\\noBorrar\\sets.csv")

# Count number of colors
num_colors = colors['name'].count()
print(f"Count of colors: {num_colors}")

# Count number of colors grouped by 'is_trans'
colors_summary = colors.groupby('is_trans').size()
print(colors_summary)

colors_summary.plot(
    kind='bar',
    color=["Red", "Orange"],
    edgecolor='black',
    width=0.6
)

#
plt.xticks(
    np.arange(2),
    ['Not Transparent', 'Transparent'],
    rotation=15,
    fontsize=12,
    ha='right'
)


plt.ylabel("Number", fontsize=12)
plt.title("Summary of Colors by Transparency", fontsize=14, fontweight='bold')
plt.show()

# Calculation mean number of parts by year
parts_by_year = sets[sets['year'] != 2025][['year', 'num_parts']].groupby('year').mean()
print(parts_by_year)


# Plot parts by year
parts_by_year.plot(title='Average Number of Parts by Year')
plt.xlabel('Year')
plt.ylabel('Average Number of Parts')
plt.show()

# Number of unique themes by year
themes_by_year = sets.groupby('year')[['theme_id']].nunique()
print(themes_by_year)

lowest_themes = themes_by_year.sort_values(by='theme_id').head(5)
lowest_themes.plot(
    kind='bar',
    color=["#6FA3EF", "#F4A261", "#A890D3", "#66C2A5", "#FF6F61"],
    edgecolor='black',
    width=0.6
)


plt.xticks(rotation=15, fontsize=12)
plt.ylabel("Number of Unique Theme IDs", fontsize=12)
plt.title("Lowest Unique Themes by Year", fontsize=14, fontweight='bold')

plt.show()


# Number of themes in 1999
if 1999 in themes_by_year.index:
    num_themes = themes_by_year.loc[1999]
    print(f"Number of themes in 1999: {num_themes}")
else:
    print("Data for the year 1999 is not available.")

