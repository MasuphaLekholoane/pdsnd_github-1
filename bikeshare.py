import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    city = input( "which City do you need (chicago,new_york_city,washington\n\n) :")
    while city not in CITY_DATA.keys():
        print ('wrong city,enter the correct one')
        city = input("which city do you need(chicago,new_york_city,washington\n\n:")



    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['january','february', 'march', 'april','may','june','all']
    while True:
        month = input('what month do you need?:(january,february,march,april,may,june,all):')
        if month in months:
            break
        else:
            print('please enter the correct month')


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday', 'Saturday', 'Sunday','all']

    while True:
        day = input ('mention any day you need:(Monday,Tuesday,Wednesday,Thursday,Friday,Saturday,Sunday,all):')
        if day in days:
                break
        else:
                print('please enter the correct day:')



    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])


    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour


    # filter by month if applicable
    if month != 'all':

        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1


        df = df[df['month'] == month]


    if day != 'all':

        df = df[df['day_of_week'] == day.title()]

    return df


# filter by day of week to create the new dataframe




def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month=df['month'].mode()[0]
    print('most common month is:',common_month)


    # TO DO: display the most common day of week
    common_day=df['day_of_week'].mode()[0]
    print('most common day is:',common_day)

    # TO DO: display the most common start hour
    most_common_hour = df['hour'].mode()[0]
    print(' frequent Start Hour',most_common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('most common start station is:',common_start_station)


    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print ('most common end station:', common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    combination_group=df.groupby(['Start Station','End Station'])
    frequent_combination_station = combination_group.size().sort_values(ascending=False).head(1)
    print('Most frequent combination of Start Station and End Station trip is: ',frequent_combination_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('total travel time is:',total_travel_time)


    # TO DO: display mean travel time
    AVG_travel_time= df['Trip Duration'].mean()
    print('Average Travel Time is: ', AVG_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()




    # TO DO: Display counts of user types
    print('user types are:',df['User Type'].value_counts())


    # TO DO: Display counts of gender

    try:
        Gender_types=df['Gender'].value_counts()
        print('counts of gender types are:',Gender_types)
    except KeyError:
        print('counts of gender are:\nNo data found for this month')



    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_year= earliest_year = df['Birth Year'].min()
        print('Earliest Year is: ',earliest_year)
    except KeyError:
        print('Earliest year:no data available for this month')

    try:
        most_recent_year = df['Birth Year'].max()
        print('Most Recent Year is: ',most_recent_year)
    except KeyError:
        print('Frequent recent year:no data available for this month')

    try:
        most_common_year = df['Birth Year'].mode()[0]
        print('Most Common Year is: ',most_common_year)
    except KeyError:
        print('Most common year:no data available for this month')



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(df):
    row=0
    while True:
        view_data = input("Would you like to view 5 rows of individual trip data? for 'Yes' enter 'YES' and for 'No' enter 'NO'.\n").lower()
        #row = 0
        if view_data == "yes":
            print(df.iloc[row : row + 6])
            row += 6
        elif view_data == "no":
            break
        else:
            print("Sorry! You entered Wrong Input, Kindly try Again!")





def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_data(df)


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
            	main()
