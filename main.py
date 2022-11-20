(tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18),[MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

#https://www.niehs.nih.gov/health/topics/agents/air-pollution/index.cfm#:~:text=Respiratory%20Disease,are%20linked%20to%20chronic%20bronchitis.
import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
from PIL import Image
df = pd.DataFrame({'Years':[2020,2015,2010,2005,2000,1995,1990]
                   ,'AVG Global Temp':[1.02,.9,.72,.68,.39,.45,.45]})





import geocoder
airqualdict = {'0-50':'Good','51-100':'Moderate','101-150':'Unhealthy for sensitive groups','151-200':'Unhealthy','201-300':'Very unhealthy','301 or higher':'Hazardous'}
dictionary = {'Alabama':'30','Alaska':'24','Arizona':'50', 'Arkansas':'25', 'California':'63', 'Colorado':'52', 'Connecticut':'26', 'Delaware':'27', 'Florida':'38', 'Georgia':'42', 'Hawaii':'18', 'Idaho':'15', 'Illinois':'50', 'Indiana':'23', 'Iowa':'12', 'Kansas':'30', 'Kentucky':'39', 'Louisiana':'28', 'Maine':'34', 'Maryland':'24', 'Massachusetts':'22', 'Michigan':'50', 'Minnesota':'40', 'Mississippi':'26', 'Missouri':'21', 'Montana':'45', 'Nebraska':'28', 'Nevada':'28', 'New Hampshire':'26', 'New Jersey':'32', 'New Mexico':'27', 'New York':'30', 'North Carolina':'31', 'North Dakota':'29', 'Ohio':'26', 'Oklahoma':'27', 'Oregon':'39', 'Pennsylvania':'33', 'Rhode Island':'16', 'South Carolina':'30', 'South Dakota':'22', 'Tennessee':'17', 'Texas':'26', 'Utah':'37', 'Vermont':'23', 'Virginia':'22', 'Washington':'39', 'West Virginia':'22', 'Wisconsin':'23', 'Wyoming':'33'}



userlocation = geocoder.ip('Me')
ip = open('ipaddress.txt', 'a')
strip = str(userlocation)
ip.writelines(strip)
ip.close()


def pagelayout():
  #Title
  st.title("How Pollution Effects Our Health")

  #Names below title
  st.caption("Andrew G, Hayden W, William W, Brock Ş, Erick")

  #Info beneath title
  column1, column2 = st.columns(2)
  with column1:
    st.write(
      "ㅤㅤIn today's world, environmental safety is an ever-present concern. Using this program, you will be able to search levels of pollution within the United States by state, learn how to combat pollution on a small scale within your own life, and learn the effects that pollution can have on those who live in affected areas."
    )
    #Main image (trees)
  image = Image.open('image.jpg')
  with column2:
    st.image(image, caption='')

  #Sidebar
  st.sidebar.header("Who we are")
  with st.sidebar:
    st.write("We are a team of highschool students in Northern AL that created this web tool to help inform people of health risks caused by pollution.")
    st.write("For more information, please visit the links below.")
    st.write("Global Warming Data: [link](https://climate.nasa.gov/vital-signs/global-temperature/)")
    st.write("Air Pollution: [link](https://www.niehs.nih.gov/health/topics/agents/air-pollution/index.cfm#:~:text=Respiratory%20Disease,are%20linked%20to%20chronic%20bronchitis.)")
    st.write("Health Effects: [link](https://www.sureshotayurveda.com/blog/effect-of-pollution-on-the-environment-human-health/#:~:text=Health%20effects%20of%20air%20pollution%20on%20human%20beings%3A,air%20are%20prone%20to%20develop%20cancer.%20More%20items)")
    
    
  tab1, Htab, tab2, tab3 = st.tabs(
    ["What is Pollution?", "Health Risks Caused by Pollution", "How You Can Help", "Local AQI"])
  with tab1:  #What is Pollution
    clm1, clm2=st.columns(2)
    with clm1:
      st.write(
      "ㅤㅤPollution is the introduction of harmful substances into the environment. This happens on a massive scale every day by people around the world. Carbon dioxide, or CO2, is a greenhouse gas, meaning that, in small amounts, it helps keeps the Earth insulated. However, the amount of CO2 in our atmosphere is increasing at an alarming rate— 37.12 billion tonnes of carbon dioxide were released into the atmosphere in 2021 alone. This process is known as global warning. Global warming will lead to innumerable climate refugees, as nations such as Kiribati and the Maldives are at risk of going underwater."
      )
    with clm2:
      chartdata = pd.DataFrame(data=df,
        columns=['Years','AVG Global Temp'])
      st.bar_chart(chartdata, x= 'Years', y = 'AVG Global Temp')
      

  with Htab:  #Health risks
    st.header("What You Need to Know to Stay Safe")
    clm1,clm2=st.columns(2)
    with clm1:
      st.write(    
      "ㅤㅤIn terms of health-related consequences, pollution causes a variety of issues, lung damage, respiratory conditions, increased fatigue, and illnesses due to contaminated water supplies. A common method of measuring air quality is the AQI (Air Quality Index), which assigns a numerical value to the air in a given area; the lower the number, the better. In the chart below is information regarding what to do, depending on the air quality present:")
    def load_data():
      return pd.DataFrame(
        {'AQI':[50,100,150,200,300]
                    ,'Severeness':['Good','Moderate','Unhealthy for sensitive groups','unhealthy','very unhealthy']}
  )

    st.checkbox('Use container width', value = False, key = 'use_container_width')
    dfs = load_data()
  
    st.dataframe(dfs, use_container_width=st.session_state.use_container_width)
  with tab2:  #How You can Help
    st.header('Be Active In the Fight Against Climate Change and Find Out How You Can Help')
    st.write(
      "ㅤㅤAlthough it is difficult to reverse climate change without widespread action, some things you can do to reduce pollution is to use your car less, instead using public transportation; not burning your garbage and instead using trash hauling services provided by your county; planting and take care of trees, as trees are a natural filter for pollutants; switching to electric lawncare products, as gas-powered products produce chemicals that are harmful to the environment.   "
    )

  with tab3:  #Local AQI
    st.header('Air Quality (AQI)')
    userinput = st.text_input('Enter a state in the U.S')
    st.caption('The average AQI for your requested state is: ')
    if userinput in dictionary:
      st.write(dictionary[userinput])
    else:
      st.write('Enter a valid state.')
      

pagelayout()
