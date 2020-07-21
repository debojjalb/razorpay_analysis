
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json
from plotly.offline import download_plotlyjs,plot, iplot
import plotly.express as px
#import cufflinks as cf
import streamlit as st

#cf.go_offline()

st.markdown("# Fee Managment System")
st.markdown("### Find the record of each student payment status")
st.markdown(" #### © CoachIO")



filename = st.file_uploader("Choose a CSV file of data of payment till date", type="csv")
currentMonth = st.selectbox('Which Month data you want to check?', ['June 2020', 'July 2020','Sep 2020','Oct 2020', 'Nov 2020', 'Dec 2020', 'Jan 2021','Feb 2021', 'Mar 2021' ])

master = st.file_uploader("Choose a CSV file of list of people in the coachiing", type="csv")
           



class fee:
    
    
    
   
    #Initialising dummy list and month dataframes
    
    #self.master_list=pd.read_csv('master_list')
    #del below code when you use a sample master list as csv import
    

    
    #change this hard code as suitable in streamlit
    ##currentMonth='June 20'
    
    #samehere
    ##month='Jul 20'

#Initialising input csv and month
    def __init__(self):
        
        
        self.df=pd.read_csv(filename)  ##change the csv as required
        
        self.month=currentMonth
        self.sel_mon=self.df[self.df['fee_month']== currentMonth] #change this to currentMonth
        print (self.sel_mon)  #for testing
        self.cd=pd.DataFrame()
    
        #self.master_list=np.array([['Ram','Shayam','Hari', 'Radha','Ramesh', 'Suresh', 'Sayan', 'Debojjal'],[12,13,78,98,54,67,83,'SampleRoll123'],['JEE','JEE','JEE','JEE','JEE','JEE','JEE','JEE']]).transpose()
        self.master_list= pd.read_csv('master')
    
    def selectMonth(self): 
        
        
        
        #change input param as suitable
        
        if (self.month=='June 20'):
            
            self.sel_mon=self.df[self.df['fee_month']=='June 2020']
        elif (self.month==' July 20'):
            self.sel_mon=self.df[self.df['fee_month']=='July 2020']
        elif (self.month=='Aug 20'):
            self.sel_mon=self.df[self.df['fee_month']=='Aug 2020']
        elif (self.month=='Sep 20'):
            self.sel_mon=self.df[self.df['fee_month']=='Sep 2020']   
        elif (self.month=='Oct 20'):
            self.sel_mon=self.df[self.df['fee_month']=='Oct 2020']          
        elif (self.month=='Nov 20'):
            self.sel_mon=self.df[self.df['fee_month']=='Nov 2020']
        elif (self.month=='Dec 20'):
            self.sel_mon=self.df[self.df['fee_month']=='Dec 2020'] 
        elif (self.month=='Jan 21'):
            self.sel_mon=self.df[self.df['fee_month']=='Jan 2021']
        elif (self.month=='Feb 21'):
            self.sel_mon=self.df[self.df['fee_month']=='Feb 2021']
        elif (self.month=='Mar 21'):
            self.sel_mon=self.df[self.df['fee_month']=='Mar 2021']
            
        

        
   
       
       
       
       

#Making the final dataframe for each month
    def makechart(self):
    
    #change the input param as required
        e=self.sel_mon.values
        bp=[]
        amt=[]
        for i in range(0,len(self.master_list)):
            flag=False
         
            for j in range(0,len(e)):
                if e[j,12]==self.master_list[i,1]:
                   flag=True
                else:
                    flag=False
            if flag==True:
                bp.append('Paid')
                amt.append(e[j,8])
            else:
                bp.append('Un-Paid')
                amt.append(0)
        
        amt=np.array(amt).reshape(-1,1,)
        bp=np.array(bp).reshape(-1,1,)
        ''''c=np.append(self.master_list,bp,axis=1)'''
        c=np.concatenate((self.master_list,bp,amt),axis=1)
        self.cd=pd.DataFrame(c)
        self.cd.rename(columns={0:'Name',1:'Roll Number', 2:'Course',3:'Status', 4:'Amount'},inplace=True)
        
        st.markdown("### Database of students whether Payment Status")

        st.write(self.cd)
        
        #Generating Pie-Chart  #If you want make a separate def for this
        
        win=0
        lose=0
        for i in range(0,len(self.cd)):
            if(self.cd.iloc[i,3]=='Paid'):
                win=win+1
            else:
                lose=lose+1
        list1=['Paid','Un-Paid']
        list2=[win,lose]
        
        '''
        def make_autopct(values):
            def my_autopct(pct):
                total=sum(values)
                val=int(round(pct*total/100.0))
                return '{p:.2f}%  ({v:d})'.format(p=pct,v=val)
            return my_autopct
        '''
        st.markdown("### A pie Chart showing monthly Paid- Unpaid Ratio")

        fig = px.pie(list1, values=list2,names=['Paid','Unpaid'], color_discrete_sequence=px.colors.sequential.RdBu)
        st.write(fig)
        #End of PieChart
       
                
            




    #Calling the functions
pay=fee()
pay.selectMonth()
pay.makechart()

#Plotting no. of paid and unpaid as count plot using seaborn and plotly

##cd1=cd.groupby('Payment Status').count()['Name'].reset_index()
##cd1.iplot(x='Payment Status', y='Name', kind='bar')


            
            
            
        
            
            
    
