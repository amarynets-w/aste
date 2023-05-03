from example.example import format_data_for_display


def test_compare_people_data(example_people_data):
    people = [
        {
            "first_name": "Alfonsa",
            "second_name": "Ruiz",
            "title": "Senior Software Engineer",
        },
        {
            "first_name": "Sayid",
            "second_name": "Khan",
            "title": "Project Manager",
        },
    ]
    assert format_data_for_display(people) == [
        "Alfonsa Ruiz: Senior Software Engineer",
        "Sayid Khan: Project Manager",
    ]
    assert people == example_people_data


def test_format_data_for_display(example_people_data):

    assert format_data_for_display(example_people_data) == [
        "Alfonsa Ruiz: Senior Software Engineer",
        "Sayid Khan: Project Manager",
    ]
