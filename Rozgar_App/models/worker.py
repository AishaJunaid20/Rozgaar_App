class Worker:
    def __init__(self, name, skill, city, contact):
        self.name = name
        self.skill = skill
        self.city = city
        self.contact = contact

    def to_dict(self):
        return {
            "name": self.name,
            "skill": self.skill,
            "city": self.city,
            "contact": self.contact
        }
