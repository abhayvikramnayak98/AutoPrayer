# scheduler.py
import pygame as pyg
import schedule
import time
from progress_bar import ConsoleProgBar
from prayer_abstract import PrayerComponent, ProgressBar

class PrayerScheduler(PrayerComponent):
    """
    Concrete implementation of PrayerComponent that handles scheduling and playing prayers.
    """

    def __init__(self) -> None:
        """
        Initializes the scheduler with prayer data.
        """
        self.prayer_list = [
            {'prayer_name' : 'Sheja Aarti', 'file_path': 'prayerAudio\Saibaba\Shej Aarti.mp3', 'prayer_time': '22:05'}
        ]
        self.progress_bar = ConsoleProgBar()

    def play_prayer(self, prayer_name, file_path, prayer_time):
        '''
        Plays the prayer audio and displays progress.

        Args:
            prayer_name (str): Name of the prayer.
            file_path (str): Path of the audio file.
            prayer_time (str): Scheduled time for the prayer.
        '''
        print(f"At {prayer_time}, time for {prayer_name}! Preparing to play the audio...")
        print(f"Playing prayer from file: {file_path}")

        pyg.mixer.init()
        pyg.mixer.music.load(file_path)
        pyg.mixer.music.play()

        self.progress_bar.show_progress(file_path)

    def schedule_prayer(self):
        '''
        Schedules prayers based on the defined prayer times.
        '''
        for prayer in self.prayer_list:
            prayer_name = prayer['prayer_name']
            file_path = prayer['file_path']
            prayer_time = prayer['prayer_time']

            schedule.every().day.at(prayer_time).do(self.play_prayer, prayer_name, file_path, prayer_time)

        while True:
            schedule.run_pending()
            time.sleep(1)
