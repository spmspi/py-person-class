class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result = []
    for person in people:
        obj = Person(person["name"], person["age"])
        result.append(obj)
    for i in range(len(result)):
        one_dict = people[i]
        p_obj = result[i]
        if one_dict.get("wife"):
            wife_name = one_dict["wife"]
            p_obj.wife = Person.people[wife_name]

        if dict.get("husband"):
            husband_name = dict["husband"]
            p_obj.husband = Person.people[husband_name]
    return result
