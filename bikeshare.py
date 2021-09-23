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
    print("hi,I am sarah and i hope you enjoy using my program")
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']

    days = ['all', 'monday', 'tuesday', 'wednesday', 'friday', 'saturday', 'sunday']

    while(True):
        try:
            city=input("Would you like to see data for Chicago, New York, or Washington?").lower()
            if city in CITY_DATA :
                break
            else:
                print("invalid input,try again")
        except:
             print("invalid input,try again")


    # TO DO: get user input for month (all, january, february, ... , june)

    while(True):
        try:
            month=input("Which month - January, February, March, April, May, or June?  ").lower()
            if month in months :
                break
            else:
                print("invalid input,try again")
        except:
             print("invalid ,try again")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while(True):
            try:
                day=input("Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?").lower()
                if day in days :
                    break
                else:
                    print("invalid input,try again")
            except:
                print("invalid input,try again")

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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    if month != 'all': #filter by month
      months = ['january', 'february', 'march', 'april', 'may', 'june']
      month = months.index(month) + 1
      df = df[df['month'] == month]

    if day != 'all': #filter by day
        df = df[df['day_of_week'] == day.title()]



    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    popular_month = df['month'].mode()[0]
    print('most common start month:', popular_month)

    # TO DO: display the most common day of week

    popular_day = df['day_of_week'].mode()[0]
    print('most common start day of week:', popular_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('most common start hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    srart_station = df['Start Station'].mode()[0]
    print('most commonly used start station :', srart_station)

    # TO DO: display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print('most commonly used end station :', end_station)

    # TO DO: display most frequent combination of start station and end station trip

    start_end_sta= (df[['Start Station','End Station']].mode())
    print('most frequent combination of start station and end station trip:/n', start_end_sta.iloc[[0]])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time=df['Trip Duration'].sum()
    print('total travel time:\n',total_time)
    # TO DO: display mean travel time
    mean_time=df['Trip Duration'].mean()
    print('mean travel time:\n',mean_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    num_tybe=df['User Type'].value_counts()
    print('counts of user types: \n',num_tybe)
    # TO DO: Display counts of gender
    if city !='washington':
        num_gender=df['Gender'].value_counts()
        print('counts of gender\n:',num_gender)
    # TO DO: Display earliest, most recent, and most common year of birth
        earliest_birth=df['Birth Year'].min()
        recent_birth=df['Birth Year'].max()
        common_birth=df['Birth Year'].mode().iloc[[0]]
        print('earliest, most recent, and most common year of birth:\n',earliest_birth,'\n',recent_birth,'\n',common_birth[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(df):
    start_loc = 0
    while (True):
        view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?").lower()
        if view_data != 'yes':
            break

        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5



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
            print("goodbye *_*")
            break


if __name__ == "__main__":
	main()
