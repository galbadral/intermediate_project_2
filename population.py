import streamlit as st
import numpy as np
import pandas as pd
import time

df = pd.read_csv("countries.csv")

st.title("World's next 100 year population projection based on fertility")
st.caption("This projection does not count immigration")

tab1, tab2 = st.tabs(["Countries","World"])

with tab1:

    coll1, coll2, coll3= st.columns([1,2,1])

    option1 = coll2.selectbox(
        'Select your country',
        (df['Country Name']))


    for i in range(len(df)):
        if df['Country Name'][i]== option1:
            index1=i

    link1= 'https://countryflagsapi.com/png/'+df['Country Code'][index1].lower()

    coll2.image(link1,caption=df['Country Name'][index1],use_column_width='always')
    
    
    df1 = pd.read_csv(str(df['Country Code'][index1])+'.csv')
    
    
    
    col1, col2, col3 = st.columns([3,1,3])


    #chart_data = pd.df(
        #columns=['', 'b', 'c'])
    st.markdown("<h4 style='text-align: center; color: #414b56;'><b>"+df['Country Name'][index1]+"'s fertility projection till 2121"+"</b></h4>", unsafe_allow_html=True)
    
    #df1.rename(columns = {'10_years_fert':'Used last 10 years mean fertility change'}, inplace = True)
    #df1.rename(columns = {'20_years_fert':'Used last 20 years mean fertility change'}, inplace = True)
    #df1.rename(columns = {'60_years_fert':'Used last 60 years mean fertility change'}, inplace = True)
    #df1.rename(columns = {'no_growth_fert':'Fertility rate that population remains the same 2.1'}, inplace = True)
    #df1.rename(columns = {'1_years_fert':'Last years fertility'}, inplace = True)
    
    #st.line_chart(df1[['Used last 10 years mean fertility change', 'Used last 20 years mean fertility change', 'Used last 60 years mean fertility change','Last years fertility', 'Fertility rate that population remains the same 2.1','year']],x='year', y= ['Used last 10 years mean fertility change', 'Used last 20 years mean fertility change', 'Used last 60 years mean fertility change', 'Fertility rate that population remains the same 2.1','Last years fertility'])
   
    #for i in range(len(df1)):
        #df1['year'][i]=str(df1['year'][i])
    
    st.line_chart(df1[['1_years_fert','10_years_fert', '20_years_fert', '60_years_fert', 'no_growth_fert','year']],x='year', y= ['1_years_fert','10_years_fert', '20_years_fert', '60_years_fert', 'no_growth_fert'])
   
    #st.area_chart(chart_data)
    st.caption("1_years_fert: Last years fertility")
    st.caption("10_years_fert: Used last 10 years mean fertility change")
    st.caption("20_years_fert: Used last 20 years mean fertility change")
    st.caption("60_years_fert: Used last 60 years mean fertility change")
    st.caption("no_growth_fert: Fertility rate that population remains the same which is 2.1")
    
    
    st.markdown("<h4 style='text-align: center; color: #414b56;'><b>"+df['Country Name'][index1]+"'s population projection till 2121"+"</b></h4>", unsafe_allow_html=True)
    
    
    st.line_chart(df1[['1_years_popu','10_years_popu', '20_years_popu', '60_years_popu', 'current_popu','year']],x='year', y= ['1_years_popu','10_years_popu', '20_years_popu', '60_years_popu', 'current_popu'])
    
    st.caption("1_years_popu: Used last years fertility rate")
    st.caption("10_years_popu: Used last 10 years mean fertility  change")
    st.caption("20_years_popu: Used last 20 years mean fertility change")
    st.caption("60_years_popu: Used last 60 years mean fertility change")
    st.caption("current_popu: Current population of the country")
    
    st.markdown("<h4 style='text-align: center; color: #414b56;'><b>"+df['Country Name'][index1]+"'s population in 2122"+"</b></h4>", unsafe_allow_html=True)
    
    col_1, col_2= st.columns([3,1])
    
    col_1.markdown("<h6 style='text-align: center; color: #414b56;'><b>If "+df['Country Name'][index1]+" keeps its last year's fertility rate:</b></h4>", unsafe_allow_html=True)
    col_2.markdown("<h6 style='text-align: center; color: #414b56;'><b>"+str(round(df1['1_years_popu'][161],0))+"</b></h4>", unsafe_allow_html=True)
    
    col_1.markdown("<h6 style='text-align: center; color: #414b56;'><b>If "+df['Country Name'][index1]+" keeps its last 10 years' fertility rate change:</b></h4>", unsafe_allow_html=True)
    col_2.markdown("<h6 style='text-align: center; color: #414b56;'><b>"+str(round(df1['10_years_popu'][161],0))+"</b></h4>", unsafe_allow_html=True)
                            

    col_1.markdown("<h6 style='text-align: center; color: #414b56;'><b>If "+df['Country Name'][index1]+" keeps its last 20 years' fertility rate change:</b></h4>", unsafe_allow_html=True)
    col_2.markdown("<h6 style='text-align: center; color: #414b56;'><b>"+str(round(df1['20_years_popu'][161],0))+"</b></h4>", unsafe_allow_html=True)
    
    
    col_1.markdown("<h6 style='text-align: center; color: #414b56;'><b>If "+df['Country Name'][index1]+" keeps its last 60 years' fertility rate change:</b></h4>", unsafe_allow_html=True)
    col_2.markdown("<h6 style='text-align: center; color: #414b56;'><b>"+str(round(df1['60_years_popu'][161],0))+"</b></h4>", unsafe_allow_html=True)
    

    col_1.markdown("<h6 style='text-align: center; color: #414b56;'><b>"+df['Country Name'][index1]+"'s current population:</b></h4>", unsafe_allow_html=True)
    col_2.markdown("<h6 style='text-align: center; color: #414b56;'><b>"+str(round(df1['current_popu'][161],0))+"</b></h4>", unsafe_allow_html=True)
    
    
    
    st.image("crowd.png")
    
    st.caption("Calcuation: If the fertility is 2.1 ther will be no growth. If it is 0 there will be mean decrease of population by that years population divided by their current mean life expectancy. And I porportioned the each change of population based on this and their changing fertility. And from America's charts we can see impact of immigration")
    
with tab2:
    
    
    coll1, coll2, coll3= st.columns([1,2,1])
    
    st.caption("I tried a lot to sum up the datas and make world data but my computer gives me nothing just nan values I don't know why it is giving me nan, maybe my computer memory was reaching its limit. You can see the attempts at add_dataframes_into_one.ipynb's 45th line")

    coll2.image("world.png",use_column_width='always')
    
    col1, col2, col3 = st.columns([3,1,3])
    
    
    df1 = pd.read_csv('world.csv')


    #chart_data = pd.df(
        #columns=['', 'b', 'c'])
    st.markdown("<h4 style='text-align: center; color: #414b56;'><b>World's fertility projection till 2121"+"</b></h4>", unsafe_allow_html=True)
    
    #df1.rename(columns = {'10_years_fert':'Used last 10 years mean fertility change'}, inplace = True)
    #df1.rename(columns = {'20_years_fert':'Used last 20 years mean fertility change'}, inplace = True)
    #df1.rename(columns = {'60_years_fert':'Used last 60 years mean fertility change'}, inplace = True)
    #df1.rename(columns = {'no_growth_fert':'Fertility rate that population remains the same 2.1'}, inplace = True)
    #df1.rename(columns = {'1_years_fert':'Last years fertility'}, inplace = True)
    
    #st.line_chart(df1[['Used last 10 years mean fertility change', 'Used last 20 years mean fertility change', 'Used last 60 years mean fertility change','Last years fertility', 'Fertility rate that population remains the same 2.1','year']],x='year', y= ['Used last 10 years mean fertility change', 'Used last 20 years mean fertility change', 'Used last 60 years mean fertility change', 'Fertility rate that population remains the same 2.1','Last years fertility'])
   
    #for i in range(len(df1)):
        #df1['year'][i]=str(df1['year'][i])
    
    st.line_chart(df1[['1_years_fert','10_years_fert', '20_years_fert', '60_years_fert', 'no_growth_fert','year']],x='year', y= ['1_years_fert','10_years_fert', '20_years_fert', '60_years_fert', 'no_growth_fert'])
   
    #st.area_chart(chart_data)
    st.caption("1_years_fert: Last years fertility")
    st.caption("10_years_fert: Used last 10 years mean fertility change")
    st.caption("20_years_fert: Used last 20 years mean fertility change")
    st.caption("60_years_fert: Used last 60 years mean fertility change")
    st.caption("no_growth_fert: Fertility rate that population remains the same which is 2.1")
    
    
    st.markdown("<h4 style='text-align: center; color: #414b56;'><b>World's population projection till 2121"+"</b></h4>", unsafe_allow_html=True)
    
    
    st.line_chart(df1[['1_years_popu','10_years_popu', '20_years_popu', '60_years_popu', 'current_popu','year']],x='year', y= ['1_years_popu','10_years_popu', '20_years_popu', '60_years_popu', 'current_popu'])
    
    st.caption("1_years_popu: Used last years fertility rate")
    st.caption("10_years_popu: Used last 10 years mean fertility  change")
    st.caption("20_years_popu: Used last 20 years mean fertility change")
    st.caption("60_years_popu: Used last 60 years mean fertility change")
    st.caption("current_popu: Current population of the country")
    
    st.markdown("<h4 style='text-align: center; color: #414b56;'><b>World's population in 2121"+"</b></h4>", unsafe_allow_html=True)
    
    col_1, col_2= st.columns([3,1])
    
    col_1.markdown("<h6 style='text-align: center; color: #414b56;'><b>If World keeps its last year's fertility rate:</b></h4>", unsafe_allow_html=True)
    col_2.markdown("<h6 style='text-align: center; color: #414b56;'><b>"+str(round(df1['1_years_popu'][161],0))+"</b></h4>", unsafe_allow_html=True)
    
    col_1.markdown("<h6 style='text-align: center; color: #414b56;'><b>If World keeps its last 10 years' fertility rate change:</b></h4>", unsafe_allow_html=True)
    col_2.markdown("<h6 style='text-align: center; color: #414b56;'><b>"+str(round(df1['10_years_popu'][161],0))+"</b></h4>", unsafe_allow_html=True)
                            

    col_1.markdown("<h6 style='text-align: center; color: #414b56;'><b>If World keeps its last 20 years' fertility rate change:</b></h4>", unsafe_allow_html=True)
    col_2.markdown("<h6 style='text-align: center; color: #414b56;'><b>"+str(round(df1['20_years_popu'][161],0))+"</b></h4>", unsafe_allow_html=True)
    
    
    col_1.markdown("<h6 style='text-align: center; color: #414b56;'><b>If World keeps its last 60 years' fertility rate change:</b></h4>", unsafe_allow_html=True)
    col_2.markdown("<h6 style='text-align: center; color: #414b56;'><b>"+str(round(df1['60_years_popu'][161],0))+"</b></h4>", unsafe_allow_html=True)
    

    col_1.markdown("<h6 style='text-align: center; color: #414b56;'><b>World's current population:</b></h4>", unsafe_allow_html=True)
    col_2.markdown("<h6 style='text-align: center; color: #414b56;'><b>"+str(round(df1['current_popu'][161],0))+"</b></h4>", unsafe_allow_html=True)
    
    
    
    st.image("crowd.png")
    