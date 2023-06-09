import data_fetcher


def load_data():
    """ Retrieve data from the link provided

        Returns:
            response(list): nested dictionaries
    """
    valid_input = False
    while not valid_input:
        chosen_animal = input("Enter a name of an animal: ")
        data = data_fetcher.fetch_data(chosen_animal)
        response = data.json()
        if len(response) > 0:
            return response
        else:
            print(f"The animal {chosen_animal} does not exist.")


def read_html():
    """Load HTML file"""
    with open("animals_template.html", "r") as file_obj:
        data = file_obj.read()
        return data


def replace_animal_info():
    """Replace and write HTML file"""
    file_name = input("Enter a file name for your html file (do not include the extension): ")
    with open(file_name+".html", "w") as new_file:
        old_data = read_html()
        new_data = animal_info()
        new_content = old_data.replace("__REPLACE_ANIMALS_INFO__", new_data)
        new_file.write(new_content)
        print(f"Website was successfully generated to the file {file_name}")


def serialize_animal(animal_data):
    """ Structuring the animal data

     Args:
        animal_data(list): nested dictionaries

    Returns:
        HTML structure
    """
    output = ' '
    output += f'<li class="cards__item">'
    output += f'<div class="card__title">{animal_data["name"]}</div>\n'
    output += f'<p class="card__text">'
    output += f'<ul style="list-style-type:none;">'
    if 'characteristics' in animal_data and 'diet' in animal_data['characteristics']:
        output += f'<li style="padding: 0.5rem;"><strong> Diet: </strong> {animal_data["characteristics"]["diet"]}\n'
    if 'locations' in animal_data and animal_data['locations'] and len(animal_data['locations']) > 0:
        output += f'<li style="padding: 0.5rem;"><strong> Location: </strong> {animal_data["locations"][0]}\n'
    if 'characteristics' in animal_data and 'type' in animal_data['characteristics']:
        output += f'<li style="padding: 0.5rem;"><strong> Type: </strong> {animal_data["characteristics"]["type"]}\n'
    if 'characteristics' in animal_data and 'distinctive_feature' in animal_data['characteristics']:
        output += f'<li style="padding: 0.5rem;"><strong> Distinctive Feature: </strong> ' \
                  f'{animal_data["characteristics"]["distinctive_feature"]}<br/>\n'
    if 'characteristics' in animal_data and 'most_distinctive_feature' in animal_data['characteristics']:
        output += f'<li style="padding: 0.5rem;"><strong> Most Distinctive Feature: </strong> ' \
                  f'{animal_data["characteristics"]["most_distinctive_feature"]}<br/>\n'
    if 'locations' in animal_data and animal_data['locations'] and len(animal_data['locations']) > 1:
        output += f'<li style="padding: 0.5rem;"><strong>Other Locations</strong>'
        output += f'<ul style="list-style-type:square">'
        output += f'<li>{animal_data["locations"][1]}\n'
        if 'locations' in animal_data and animal_data['locations'] and len(animal_data['locations']) == 3:
            output += f'<li>{animal_data["locations"][2]}\n'
        elif 'locations' in animal_data and animal_data['locations'] and len(animal_data['locations']) == 4:
            output += f'<li>{animal_data["locations"][2]}\n'
            output += f'<li>{animal_data["locations"][3]}\n'
        elif 'locations' in animal_data and animal_data['locations'] and len(animal_data['locations']) == 5:
            output += f'<li>{animal_data["locations"][2]}\n'
            output += f'<li>{animal_data["locations"][3]}\n'
            output += f'<li>{animal_data["locations"][4]}\n'
        output += f'</ul>'
    if 'name' in animal_data or ('characteristics' in animal_data and 'diet' in animal_data['characteristics']) \
            or ('locations' in animal_data and animal_data['locations'] and len(animal_data['locations']) > 0)\
            or ('characteristics' in animal_data and 'type' in animal_data['characteristics'])\
            or ('characteristics' in animal_data and 'distinctive_feature' in animal_data['characteristics'])\
            or ('locations' in animal_data and animal_data['locations'] and len(animal_data['locations']) > 1)\
            or ('characteristics' in animal_data and 'most_distinctive_feature' in animal_data['characteristics']):
        output += f'</ul>'
        output += f'</p>'
    output += '</li>'
    return output


def animal_info():
    """ Creates HTML tags

    Returns:
        HTML Structure

    Raises:
        ValueError: If input is not in the list of options
    """
    data = load_data()
    output = ' '
    for animal_data in data:
        output += serialize_animal(animal_data)
    output += f'<label><em><strong>Notes/Comments: <br/></strong> </em></label>'
    output += f'<textarea style="background: linear-gradient(to right, white, pink);" rows="10" cols="75"></textarea>'
    return output


if __name__ == "__main__":
    replace_animal_info()
