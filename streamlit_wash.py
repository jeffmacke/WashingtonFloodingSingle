# Monte Carlo simulation for flood damages in Washington, Illinois
# For loop to run for the number of simulations desired

# Importing Packages
import streamlit as st
import matplotlib.pyplot as plt
import random
import altair as alt
import numpy as np
import pandas as pd



# Creating Roll Dice Function
def sim_year():
    year_chance = random.randint(1, 500)

    # Determining if the dice are the same number
    if year_chance < 51:
        storm = '10-Year'
    elif year_chance > 50 and year_chance < 71:
        storm = '25-Year'
    elif year_chance > 80 and year_chance < 86:
        storm = '100-Year'
    elif year_chance == 86:
        storm = '500-Year'
    else:
        storm = False
    return storm

# Inputs
if st.button('Run 1 sim'):
    num_simulations = 1
else: 
    num_simulations = 1
max_year = 2072

# Tracking# Monte Carlo simulation for flood damages in Washington, Illinois
# For loop to run for the number of simulations desired

# Importing Packages
import streamlit as st
#import matplotlib.pyplot as plt
import random
import altair as alt
import numpy as np
import pandas as pd

st.title('Flood Damages from 2022 to 2072')
st.write('Damage to buildings in Washington, Illinois due to urban flooding.')


# Creating storm frequency function
def sim_year():
    year_chance = random.randint(1, 500)

    # Determining if the dice are the same number
    if year_chance < 51:
        storm = '10-Year'
    elif year_chance > 50 and year_chance < 71:
        storm = '25-Year'
    elif year_chance > 80 and year_chance < 86:
        storm = '100-Year'
    elif year_chance == 86:
        storm = '500-Year'
    else:
        storm = False
    return storm


# Tracking
flood_probability = []
end_balance = []

#graph
#fig,ax= plt.subplots()

for i in range(num_simulations):
    balance = [0]
    year = [2022]
    num_floods = 0
    # Run until max years is exceeded
    floods10 = []
    floods25 = []
    floods100 = []
    floods500 = []
    damages10 = [0]
    damages25 = [0]
    damages100 = [0]
    damages500 = [0]
    while year[-1] < max_year:
        flood = sim_year()
        # Result if 500-year flood occurs
        if flood == '500-Year':
            balance.append(balance[-1] + 16000000)
            num_floods += 1
            floods500.append(year[-1])
            damages500.append(16000000)
        # Result if 100-year flood occurs
        elif flood == '100-Year':
            balance.append(balance[-1] + 10000000)
            num_floods += 1
            floods100.append(year[-1])
            damages100.append(10000000)
        # Result if 25-year flood occurs
        elif flood == '25-Year':
            balance.append(balance[-1] + 7000000)
            num_floods += 1
            floods25.append(year[-1])
            damages25.append(7000000)
        # Result if 10-year flood occurs
        elif flood == '10-Year':
            balance.append(balance[-1] + 5000000)
            num_floods += 1
            floods10.append(year[-1])
            damages10.append(5000000)
        else:
            balance.append(balance[-1])
        year.append(year[-1] + 1)
    
# Store tracking variables and add line to figure
    flood_probability.append(num_floods/(year[-1]-2022))
    end_balance.append(balance[-1])
    #ax.plot(year, balance)
    source = pd.DataFrame({'Year':year,'Damages':balance})
    altchart = alt.Chart(source).mark_line().encode(x='Year',y='Damages')

# Print the flooding years and total damages for each flood frequency
    string10 = [str(int) for int in floods10]
    st.subheader('10-year floods: ' + ', '.join(string10))
    st.write('10-year damages ' + str("${:,}".format(sum(damages10))))
    string25 = [str(int) for int in floods25]
    st.subheader('25-year floods: ' + ', '.join(string25))
    st.write('25-year damages ' + str("${:,}".format(sum(damages25))))
    string100 = [str(int) for int in floods100]
    st.subheader('100-year floods: ' + ', '.join(string100))
    st.write('100-year damages ' + str("${:,}".format(sum(damages100))))
    string500 = [str(int) for int in floods500]
    st.subheader('500-year floods: ' + ', '.join(string500))
    st.write('500-year damages ' + str("${:,}".format(sum(damages500))))

# Showing the plot after the simulations are finished
#st.pyplot(fig)
# Averaging win probability and end balance
overall_flood_probability = sum(flood_probability)/len(flood_probability)
overall_end_balance = sum(end_balance)/len(end_balance)
# Displaying the averages
#st.write("Average flood probability after " + str(num_simulations) + " sims: " + str(overall_flood_probability))
st.header("Total damages "+ str("${:,}".format(overall_end_balance)))


st.altair_chart(altchart,use_container_width=True)

# Averaging win probability and end balance
#overall_flood_probability = sum(flood_probability)/len(flood_probability)
#overall_end_balance = sum(end_balance)/len(end_balance)
# Displaying the averages
#st.write("Average flood probability after " + str(num_simulations) + " sims: " + str(overall_flood_probability))
#st.write("Average damages after " + str(num_simulations) + " sims: $" + str(overall_end_balance))
