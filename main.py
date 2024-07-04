from src import Greeting


def change_readme_header() -> None:
    with open("README.md", "r", encoding="utf-8") as readme:
        lines = readme.readlines()
        
    index = next(index for index, line in enumerate(lines) if line.startswith("#"))
    lines[index] = f"# {Greeting.greeting()} {Greeting.WAVING_HAND}\n"

    print(lines[index])

    with open("README.md", "w", encoding="utf-8") as readme:
        readme.writelines(lines)


if __name__ == "__main__":
    change_readme_header()