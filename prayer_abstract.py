# prayer_abstract.py
from abc import ABC, abstractmethod

class PrayerComponent(ABC):
    """
    An abstract base class for components involved in the prayer system, defining a blueprint for all prayer-related components.
    """
    
    @abstractmethod
    def play_prayer(self, prayer_name, file_path, prayer_time):
        """
        Play the specified prayer.

        Args:
            prayer_name (str): Name of the prayer.
            file_path (str): Path of the audio file.
            prayer_time (str): Scheduled time for the prayer.
        """
        pass

    @abstractmethod
    def schedule_prayer(self):
        """
        Schedule prayers based on predefined terms.
        """
        pass

class ProgressBar(ABC):
    """
    Abstract base class for progress bar components, defining the blueprint for all progress bar implementations.
    """

    @abstractmethod
    def show_progress(self, file_path):
        """
        Show the progress of an ongoing process.

        Args:
            file_path (str): Path to the file for which progress is being shown.
        """
        pass