# prarthana.py
from scheduler import PrayerScheduler

def main():
    """
    Main function to initialize and run the prayer scheduler.
    """
    # Initialize the PrayerScheduler instance
    scheduler = PrayerScheduler()
    
    # Schedule prayers based on the defined schedule
    scheduler.schedule_prayer()

if __name__ == "__main__":
    # Execute the main function if this script is run as the main program
    main()