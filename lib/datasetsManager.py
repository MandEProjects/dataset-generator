import json


class DatasetsManager:

    def __init__(self):
        with open("datasets/firstName.txt") as f:
            self.first_names = f.read().split('\n')
        with open("datasets/lastName.txt") as f:
            self.lastName = f.read().split('\n')
        with open("datasets/subjects.json") as f:
            self.subjects = json.load(f)
            self.list_of_subjects = [subject for subject in self.subjects]





