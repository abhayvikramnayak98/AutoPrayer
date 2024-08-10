# progress_bar.py
import time
import sys
from mutagen.mp3 import MP3
import pygame as pyg
from prayer_abstract import ProgressBar

class ConsoleProgBar(ProgressBar):
    """
    Concrete implementation of ProgressBar abstract class that shows progress in the console.
    """

    def show_progress(self, file_path):
        """
        Displays a progress bar for the playing audio file in the console.

        Args:
            file_path (str): Path to the audio file.
        """
        # Get the length of the audio in seconds
        audio = MP3(file_path)
        length = audio.info.length

        # Display the progress bar
        while pyg.mixer.music.get_busy():
            elapsed = pyg.mixer.music.get_pos() / 1000  # Converting milliseconds to seconds
            elapsed_display = time.strftime("%M:%S", time.gmtime(elapsed))
            total_display = time.strftime("%M:%S", time.gmtime(length))
            progress = int((elapsed / length) * 100)  # Calculate progress percentage

            # Print progress bar with elapsed time, percentage, and total duration
            sys.stdout.write(f"\r[{ '=' * (progress // 2) }{' ' * (50 - progress // 2) }] {elapsed_display}/{total_display} ({progress}%)")
            sys.stdout.flush()
            time.sleep(0.5)  # Update every half second
        
        