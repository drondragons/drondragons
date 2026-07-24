from __future__ import annotations

import datetime as dt
from dataclasses import dataclass
from pathlib import Path


README_PATH = Path("README.md")

MOSCOW_TIME = dt.timezone(
    dt.timedelta(hours=3), 
    name="Europe/Moscow",
)

START_MARKER = "<!-- GREETING:START -->"
END_MARKER = "<!-- GREETING:END -->"

EMOJI_BASE_URL = (
    "https://raw.githubusercontent.com/Tarikul-Islam-Anik/"
    "Animated-Fluent-Emojis/master/Emojis"
)

IMAGE_ATTRIBUTES = 'width="40" height="40" align="center"'


@dataclass(frozen=True)
class Greeting:
    text: str
    emoji_file: str
    emoji_alt: str


def greeting_for_hour(hour: int) -> Greeting:
    if not 0 <= hour <= 23:
        raise ValueError(f"Hour must be between 0 and 23, got {hour}")

    if hour < 5:
        return Greeting(
            text="Доброй ночи",
            emoji_file="Night%20with%20Stars.png",
            emoji_alt="Night",
        )

    if hour < 12:
        return Greeting(
            text="Доброе утро",
            emoji_file="Sunset.png",
            emoji_alt="Morning",
        )

    if hour < 18:
        return Greeting(
            text="Добрый день",
            emoji_file="Cityscape.png",
            emoji_alt="Afternoon",
        )

    return Greeting(
        text="Добрый вечер",
        emoji_file="Cityscape%20at%20Dusk.png",
        emoji_alt="Evening",
    )


def render_image(src: str, alt: str) -> str:
    return f'<img src="{src}" alt="{alt}" {IMAGE_ATTRIBUTES} />'


def render_greeting(greeting: Greeting) -> str:
    time_emoji = render_image(
        src=f"{EMOJI_BASE_URL}/Travel%20and%20places/{greeting.emoji_file}",
        alt=greeting.emoji_alt,
    )

    waving_hand = render_image(
        src=f"{EMOJI_BASE_URL}/Hand%20gestures/Waving%20Hand.png",
        alt='Waving Hand',
    )

    return f"# {time_emoji} {greeting.text} {waving_hand}"


def replace_greeting_block(readme: str, rendered_greeting: str) -> str:
    if START_MARKER not in readme:
        raise ValueError(f"Start marker not found: {START_MARKER}")

    if END_MARKER not in readme:
        raise ValueError(f"End marker not found: {END_MARKER}")
    
    before, rest = readme.split(START_MARKER, 1)
    _, after = rest.split(END_MARKER, 1)

    return (
        f"{before}"
        f"{START_MARKER}\n"
        f"{rendered_greeting}\n"
        f"{END_MARKER}"
        f"{after}"
    )


def update_readme(readme_path: Path, now: dt.datetime) -> bool:
    greeting = greeting_for_hour(now.hour)

    current_readme = readme_path.read_text(encoding="utf-8")
    updated_readme = replace_greeting_block(
        readme=current_readme,
        rendered_greeting=render_greeting(greeting),
    )

    if updated_readme == current_readme:
        return False

    readme_path.write_text(
        updated_readme,
        encoding="utf-8",
    )

    return True


def main() -> None:
    if not README_PATH.is_file():
        raise FileNotFoundError(f"README not found: {README_PATH}")

    now = dt.datetime.now(MOSCOW_TIME)
    changed = update_readme(
        readme_path=README_PATH,
        now=now,
    )

    if changed:
        print("README greeting was updated.")
    else:
        print("README greeting is already up to date.")


if __name__ == "__main__":
    main()
