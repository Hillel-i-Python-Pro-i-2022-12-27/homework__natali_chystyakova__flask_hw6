import json

from application.config.path import FILES_OUTPUT_PATH


# astronauts_api = "http://api.open-notify.org/astros.json"


def number_of_astro(name_file: str = "output") -> None:
    path_to_file = FILES_OUTPUT_PATH.joinpath(f"{name_file}.json")
    with open(path_to_file) as file:
        response_dict = json.load(file)
    number_of_astro_ = response_dict["number"]
    answer = f"The number of people in space at this moment: {number_of_astro_} astronauts"
    print(answer)
    return f"The number of people in space at this moment: {number_of_astro_} astronauts"


if __name__ == "__main__":
    number_of_astro()
