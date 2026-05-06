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
from datetime import UTC, datetime, timedelta
from resource.utils import cyan_print, sep_print

type StrIntFloat = str | int | float


class Duration[T: StrIntFloat]:
    def __init__(self, value: T) -> None:
        self._value: T = value

    @property
    def value(self) -> T:
        return self._value

    def __repr__(self) -> str:
        return f"Duration({self._value!r})"


@dataclass
class VideoInfo[T: StrIntFloat]:
    name: str
    duration_seconds: Duration[T]

    @property
    def duration_time(self) -> str:
        if isinstance(self.duration_seconds.value, int | float):
            return seconds_to_time(self.duration_seconds.value)
        return self.duration_seconds.value


def seconds_to_time(seconds: float) -> str:
    delta = datetime(1, 1, 1, 0, 0, 0, tzinfo=UTC) + timedelta(seconds=seconds)
    return f"{delta:%H:%M:%S}"


if __name__ == "__main__":
    sep_print()

    d1 = Duration(60)
    d2 = Duration("00:10:00")

    v1 = VideoInfo("lesson1.mp4", d1)
    v2 = VideoInfo("lesson2.mp4", d2)

    cyan_print(v1, v1.duration_time)
    cyan_print(v2, v2.duration_time)
    cyan_print(v2, v2.duration_seconds)

    sep_print()
