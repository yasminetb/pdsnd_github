import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def main():
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    run = True
    while (run):
        city=' '
        while city!='chicago' and city!='new_york' and city!='washington':
                print('Enter name of city:')
                city = input().lower()
        filres = ''
        while(filres != 'y' and filres != 'n'):
            print ('Do you want to filter by day ? Y/N')
            filres = input().lower()
        dayFilter= filres == 'y'
        filres = ''
        while(filres != 'y' and filres != 'n'):
            print ('Do you want to filter by month ? Y/N')
            filres = input().lower()
        monthFilter= filres == 'y'
        df=pd.read_csv(CITY_DATA[city])
        df['Start Time']=pd.to_datetime(df['Start Time'])
        if (dayFilter):
            day = int(input('Enter day '))
            df = df[df['Start Time'].dt.day == day]
        if (monthFilter):
            month = int(input('Enter Month '))
            df = df[df['Start Time'].dt.month == month]
        if (df.empty):
            print('Your result is empty')
            continue
        showres = ''
        while(showres != 'y' and showres != 'n'):
            print ('Show 5 rows of data Y/N')
            showres = input().lower()
        show = (showres == 'y')
        key = 0
        if (show == True):
            for i, row in enumerate(df.index):
                key = i
                if (i % 5 == 0 and i != 0):
                    print(df.head(i))
                    showres = ''
                    while(showres != 'y' and showres != 'n'):
                        print ('Show 5 more rows of data Y/N')
                        showres = input().lower()
                    if(showres == 'n'):
                        break
            if (key % 5 != 0):
                print(df.head(key))
        df['month']=df['Start Time'].dt.month
        popular_month=df['month'].mode()[0]
        print('most popular start month: ', popular_month)
        df=pd.read_csv(CITY_DATA[city])
        df['Start Time']=pd.to_datetime(df['Start Time'])
        df['hour']=df['Start Time'].dt.hour
        popular_hour=df['hour'].mode()[0]
        print('most popular start hour: ',popular_hour)
        df['day']=df['Start Time'].dt.day
        popular_day=df['day'].mode()[0]
        print('most popular start day: ', popular_day)

    #popular stations and trip
        popular_station=df['Start Station'].mode()[0]
        print('most popular start station: ', popular_station)
        popular_stations=df['End Station'].mode()[0]
        print('most popular end station: ', popular_stations)
        comn_station=df.groupby(['Start Station','End Station']).size().idxmax()
        print('most popular trip: ', comn_station)
        sum=0
        for time in df['Trip Duration'] :
            total=sum +time
        print('the total travel time  is:' ,total)
        avrg=df['Trip Duration'].mean()
        print('avrg is :',avrg)

        cpt=0
        for types in df['User Type']:
              if types=='Customer':
                cpt=cpt+1
        print('number of customer is :',cpt)
        cpt1=0
        for types in df['User Type']:
             if types=='Subscriber':
                cpt1=cpt1+1
        print('number of subscriber is :',cpt1) 
        if city=='chicago' or city=='new york city':
            nb1=0 
            for genders in df['Gender']:
                if genders=='Female':
                    nb1=nb1+1
            print('number of female is:',nb1)
            nb2=0
            for genders in df['Gender']:
                if genders=='Male':
                    nb2=nb2+1
            print('number of male is:',nb2)
            nb3=0
            for genders in df['Gender']:
                if genders=='NaN':
                    nb3=nb3+1
            print('number of nan is:',nb3)
            x=min(df['Birth Year'])
            print('the erliest is :',x)    
            y=max(df['Birth Year'])
            print('the most recent is:',y)
            birth_year=df['Birth Year'].mode()[0]
            print('most recent: ', birth_year)
        res = ''
        while(res != 'y' and res != 'n'):
            print('Do you want to stop the program ? Y/N')
            res = input().lower()
        run = (res == 'n')
   

if __name__ == "__main__":
	main()
