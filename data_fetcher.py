import requests


API_KEY = "RRhRnIM0DDVn6BbmwULBzQ==n9DVxWtNtkN2nwH5"


def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary:
    {
      'name': ...,
      'taxonomy': {
        ...
      },
      'locations': [
        ...
      ],
      'characteristics': {
        ...
      }
    },
    """
    url = "https://api.api-ninjas.com/v1/animals?name={}".format(animal_name)
    animal_data = requests.get(url, headers={'X-Api-Key': API_KEY})
    return animal_data
