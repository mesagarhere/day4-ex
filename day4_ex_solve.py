#write a program to calculate how many days and hours are there in a given number of seconds:
# seconds = int(input("Enter the number of seconds: "))
# days = seconds // 86400
# hours = (seconds % 86400) // 3600
# print(f"{seconds} seconds is equal to {days} days and {hours} hours")

from datetime import date, datetime

def age_in_days_and_seconds(birth_date_str):
    """Calculates a person's age in days and seconds."""
    try:
        # Assuming input format YYYY-MM-DD for simplicity
        birth_date = datetime.strptime(birth_date_str, '%Y-%m-%d').date()
        today = date.today()

        # Calculate difference
        time_difference = today - birth_date

        # Result
        days_old = time_difference.days
        seconds_old = time_difference.total_seconds()

        print(f"Born on: {birth_date_str}")
        print(f"Today's date: {today}")
        print("-" * 30)
        print(f"You are approximately **{days_old}** days old.")
        print(f"You are approximately **{int(seconds_old)}** seconds old.")

    except ValueError:
        print("Error: Invalid date format. Please use 'YYYY-MM-DD'.")

# Example Usage
age_in_days_and_seconds("1990-08-15")

from datetime import datetime

def event_countdown(event_date_str, event_name="Event"):
    """Calculates the time remaining until a future event."""
    try:
        # Assuming input format YYYY-MM-DD HH:MM
        event_datetime = datetime.strptime(event_date_str, '%Y-%m-%d %H:%M')
        now = datetime.now()

        if event_datetime < now:
            print("Error: The event date must be in the future.")
            return

        time_left = event_datetime - now

        # Convert total seconds to days, hours, and minutes
        total_minutes = int(time_left.total_seconds() / 60)
        days = total_minutes // (24 * 60)
        minutes_remaining = total_minutes % (24 * 60)
        hours = minutes_remaining // 60
        minutes = minutes_remaining % 60

        print(f"Time left until **{event_name}** ({event_date_str}):")
        print(f"**{days}** days, **{hours}** hours, and **{minutes}** minutes.")

    except ValueError:
        print("Error: Invalid date/time format. Please use 'YYYY-MM-DD HH:MM'.")

# Example Usage
event_countdown("2026-01-01 00:00", "New Year's Day")

from datetime import datetime

def date_format_converter(date_str):
    """Converts a date string to the format 'Dayth Month, Year'."""
    try:
        # 1. Parse the original date string (e.g., 2025-10-20)
        dt_object = datetime.strptime(date_str, '%Y-%m-%d')
        
        # 2. Get the day number and apply the correct suffix
        day = dt_object.day
        if 11 <= day <= 13:
            suffix = 'th'
        else:
            suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(day % 10, 'th')
            
        # 3. Format the rest of the string
        formatted_date = dt_object.strftime(f"%%d{suffix} %%B, %%Y").replace(f"%%d{suffix}", str(day) + suffix)
        
        print(f"Input: {date_str}")
        print(f"Output: **{formatted_date}**")

    except ValueError:
        print("Error: Invalid date format. Please use 'YYYY-MM-DD'.")

# Example Usage (20th, 1st, 2nd, 11th)
date_format_converter("2025-10-20")
date_format_converter("2025-01-01")
date_format_converter("2025-07-22")
date_format_converter("2025-12-11")

from datetime import date, datetime

def validate_date_of_birth(birth_date_str):
    """Calculates age and validates that the birth date is not in the future."""
    try:
        birth_date = datetime.strptime(birth_date_str, '%Y-%m-%d').date()
        today = date.today()

        if birth_date > today:
            # VALIDATION: Error for future date
            print(f"🚫 **Error:** The date of birth '{birth_date_str}' is in the future. Please enter a valid past date.")
            return

        # Calculate age (rest of the age calculator logic)
        time_difference = today - birth_date
        days_old = time_difference.days

        print(f"✅ Validation successful: Date of birth is **{birth_date_str}**.")
        print(f"You are approximately {days_old} days old.")

    except ValueError:
        print("Error: Invalid date format. Please use 'YYYY-MM-DD'.")

# Example Usage
print("--- Test Case 1 (Valid Past Date) ---")
validate_date_of_birth("1995-05-30")

print("\n--- Test Case 2 (Future Date) ---")
# Use a future date for the test (e.g., tomorrow's date)
import timedelta # Using the current time to generate a future date
tomorrow = (date.today() + timedelta(days=1)).strftime('%Y-%m-%d')
validate_date_of_birth(tomorrow)

from datetime import datetime

def time_difference_calculator(time1_str, time2_str):
    """Calculates the difference between two times (HH:MM:SS)."""
    
    # Use an arbitrary common date to compare only the time part
    DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
    base_date = '2000-01-01 ' # Anchor date

    try:
        # Combine date and time to create datetime objects for comparison
        dt1 = datetime.strptime(base_date + time1_str, DATE_FORMAT)
        dt2 = datetime.strptime(base_date + time2_str, DATE_FORMAT)

        # Calculate the absolute difference
        difference = abs(dt1 - dt2)

        # Extract components
        total_seconds = int(difference.total_seconds())
        
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60

        print(f"Time 1: {time1_str}")
        print(f"Time 2: {time2_str}")
        print("-" * 30)
        print(f"The difference is: **{hours}** hours, **{minutes}** minutes, and **{seconds}** seconds.")

    except ValueError:
        print("Error: Invalid time format. Please use 'HH:MM:SS'.")

# Example Usage
time_difference_calculator("14:30:00", "10:00:15")

import pytz
from datetime import datetime

def timezone_converter():
    """Displays the current time in different timezones."""
    
    # Define the target timezones
    timezones = {
        "Pakistan": 'Asia/Karachi', # Example 1
        "USA (New York)": 'America/New_York' # Example 2
    }
    
    now_utc = datetime.now(pytz.utc) # Get the current time in Coordinated Universal Time (UTC)

    print("Current Timezone Display:")
    print("-" * 30)

    for country, tz_name in timezones.items():
        try:
            # Get the timezone object
            tz = pytz.timezone(tz_name)
            
            # Convert the UTC time to the target timezone
            current_time_tz = now_utc.astimezone(tz)
            
            # Format and print
            time_str = current_time_tz.strftime('%I:%M:%S %p %Z')
            print(f"Current Time in **{country}** ({tz_name}): **{time_str}**")
            
        except pytz.exceptions.UnknownTimeZoneError:
            print(f"Error: Unknown timezone name for {country}.")

from datetime import datetime

def display_current_datetime():
    """Prints the current date and time in the specified format."""
    now = datetime.now()
    
    # Python's strftime codes:
    # %A: Full weekday name (Monday)
    # %d: Day of the month (20)
    # %B: Full month name (October)
    # %Y: Full year (2025)
    # %I: Hour (12-hour clock) (09)
    # %M: Minute (45)
    # %S: Second (00)
    # %p: AM/PM (AM)
    
    formatted_string = now.strftime("Today is %A, %d %B %Y - %I:%M:%S %p")
    
    print(f"The current date and time is: **{formatted_string}**")

# Example Usage
display_current_datetime()

from datetime import datetime

def display_current_datetime():
    """Prints the current date and time in the specified format."""
    now = datetime.now()
    
    # Python's strftime codes:
    # %A: Full weekday name (Monday)
    # %d: Day of the month (20)
    # %B: Full month name (October)
    # %Y: Full year (2025)
    # %I: Hour (12-hour clock) (09)
    # %M: Minute (45)
    # %S: Second (00)
    # %p: AM/PM (AM)
    
    formatted_string = now.strftime("Today is %A, %d %B %Y - %I:%M:%S %p")
    
    print(f"The current date and time is: **{formatted_string}**")

# Example Usage
display_current_datetime()

from datetime import datetime

def days_between_dates(date1_str, date2_str):
    """Calculates the number of days between two input dates."""
    DATE_FORMAT = '%Y-%m-%d'
    try:
        dt1 = datetime.strptime(date1_str, DATE_FORMAT)
        dt2 = datetime.strptime(date2_str, DATE_FORMAT)
        
        # The result of subtraction is a timedelta object
        difference = abs(dt1 - dt2)
        
        total_days = difference.days
        
        print(f"Date 1: {date1_str}")
        print(f"Date 2: {date2_str}")
        print("-" * 30)
        print(f"The total number of days between them is **{total_days}** days.")

    except ValueError:
        print("Error: Invalid date format. Please use 'YYYY-MM-DD'.")

# Example Usage
days_between_dates("2025-01-01", "2025-10-23")

from datetime import datetime, timedelta

def add_subtract_days(start_date_str, num_days):
    """Calculates the date before and after a specified number of days."""
    DATE_FORMAT = '%Y-%m-%d'
    try:
        # Convert the number of days to an integer
        days_delta = int(num_days)
        
        # Parse the starting date
        start_date = datetime.strptime(start_date_str, DATE_FORMAT)
        
        # Create a timedelta object
        delta = timedelta(days=days_delta)
        
        # Calculate the resulting dates
        date_after = (start_date + delta).strftime(DATE_FORMAT)
        date_before = (start_date - delta).strftime(DATE_FORMAT)
        
        print(f"Starting Date: {start_date_str}")
        print(f"Days to add/subtract: {days_delta}")
        print("-" * 30)
        print(f"The date **{days_delta} days after** is: **{date_after}**")
        print(f"The date **{days_delta} days before** is: **{date_before}**")

    except ValueError:
        print("Error: Invalid date or number of days format.")

# Example Usage
add_subtract_days("2025-10-23", 90)

from datetime import date, datetime

def simple_age_calculator(birth_date_str):
    """Calculates age in years only."""
    try:
        birth_date = datetime.strptime(birth_date_str, '%Y-%m-%d').date()
        today = date.today()

        # Calculate difference in years
        age_in_years = today.year - birth_date.year
        
        # Adjustment: Subtract 1 if the birthday hasn't occurred yet this year
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age_in_years -= 1

        print(f"Date of Birth: {birth_date_str}")
        print(f"Current Age: **{age_in_years}** years old.")

    except ValueError:
        print("Error: Invalid date format. Please use 'YYYY-MM-DD'.")

# Example Usage
# If today is Oct 23, 2025:
# For 1990-11-05 (Birthday hasn't passed) -> 34 years
simple_age_calculator("1990-11-05")
# For 1990-09-01 (Birthday has passed) -> 35 years
simple_age_calculator("1990-09-01")

from datetime import date, datetime

def full_age_calculator(birth_date_str):
    """Calculates age in years, months, and days."""
    try:
        birth_date = datetime.strptime(birth_date_str, '%Y-%m-%d').date()
        today = date.today()

        # 1. Calculate Years
        years = today.year - birth_date.year
        
        # Adjust for months and days
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            years -= 1
            
        # 2. Calculate Months (from last birthday)
        # Find the date of the last birthday
        last_birthday = date(today.year, birth_date.month, birth_date.day)
        if last_birthday > today:
            last_birthday = date(today.year - 1, birth_date.month, birth_date.day)

        # Calculate total months difference
        months = today.month - last_birthday.month
        
        # Adjustment for year-end crossing
        if months < 0:
            months += 12

        # 3. Calculate Days (from start of current month/last birthday)
        days = today.day - last_birthday.day
        
        # Adjustment for day difference
        if days < 0:
            # Go back one month to get the number of days in the *previous* month
            months -= 1
            if months < 0:
                months += 12 # Adjusting month count if needed
            
            # Find the date of the day before the current one
            temp_date = today.replace(day=1) - timedelta(days=1)
            days += temp_date.day # Add days in the previous month

        print(f"Date of Birth: {birth_date_str}")
        print("-" * 30)
        print(f"Your full age is: **{years}** years, **{months}** months, and **{days}** days.")

    except ValueError:
        print("Error: Invalid date format. Please use 'YYYY-MM-DD'.")

# Example Usage (Calculated using current time Oct 23, 2025)
# 1990-05-15: Age is 35 years, 5 months, 8 days
full_age_calculator("1990-05-15")

from datetime import date, datetime, timedelta

def next_birthday_countdown(birth_date_str):
    """Calculates the date and days remaining until the next birthday."""
    try:
        birth_date = datetime.strptime(birth_date_str, '%Y-%m-%d').date()
        today = date.today()
        this_year = today.year

        # 1. Determine the next birthday date
        
        # Set the birthday for the current year
        next_birthday = date(this_year, birth_date.month, birth_date.day)

        # Check if the current year's birthday has passed
        if next_birthday < today:
            # If it passed, set the birthday for next year
            next_birthday = date(this_year + 1, birth_date.month, birth_date.day)

        # 2. Calculate the days left
        days_left = (next_birthday - today).days

        print(f"Date of Birth: {birth_date_str}")
        print("-" * 30)
        print(f"The next birthday date is: **{next_birthday.strftime('%A, %B %d, %Y')}**")
        print(f"How many days left until it arrives: **{days_left}** days.")

    except ValueError:
        print("Error: Invalid date format. Please use 'YYYY-MM-DD'.")

# Example Usage (using a date that's close to today)
next_birthday_countdown("1995-10-30")