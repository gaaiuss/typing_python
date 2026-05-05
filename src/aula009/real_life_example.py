# Real life example

# Imagine that you need to concatenate many videos of a playlist into a single
# big video

# lesson1.mp4 (120 seconds) lesson2.mp4 (60 seconds) lesson3.mp4 (120 seconds)
# big_lesson.mp4 (300 seconds)

# The problem was that I needed to convert the duration of the video from seconds
# to hours and from hours to seconds to create the youtube chapters. In resume
# sum the seconds, take the timestamp where a lesson ends and the other starts
# and finally convert seconds to hours to generate "HH:MM:SS - Chapter Title"

# lesson1.mp4 (00:02:00) lesson2.mp4 (00:01:00) lesson3.mp4 (00:02:00)
# big_lesson.mp4 (00:05:00)


from dataclasses import dataclass


class Duration:
    def __init__(self, value: str) -> None:
        self._value: str = value

    @property
    def value(self) -> str:
        return self._value

    def __repr__(self) -> str:
        return f"Duration({self._value!r})"


@dataclass
class VideoInfo:
    name: str
    duration: Duration

    @property
    def duration_time(self) -> str:
        return self.duration.value


def seconds_to_time(seconds: float) -> str: ...
