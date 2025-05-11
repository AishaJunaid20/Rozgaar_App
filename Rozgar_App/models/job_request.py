# Not used yet, but for future: clients requesting specific jobs
class JobRequest:
    def __init__(self, client_name, city, required_skill, details):
        self.client_name = client_name
        self.city = city
        self.required_skill = required_skill
        self.details = details

    def to_dict(self):
        return {
            "client_name": self.client_name,
            "city": self.city,
            "required_skill": self.required_skill,
            "details": self.details
        }
