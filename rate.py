class Rate:
    def __init__(self, people):
        self.roles = self.read('roles.txt')
        self.countries = self.read('countries.txt')
        self.industries = self.read('industries.txt')
        self.people = people

    def read(self, file_name):
        with open(file_name) as file:
            return [line[:-1] for line in file.readlines()]
    
    def rate_all(self):
        for person in self.people:
            person.rate = self.rate(person)
        return self.people
    
    def rate(self, person):
        return (self.role_rate(person) + self.country_rate(person) + self.industry_rate(person) + self.recommendation_rate(person) + self.connections_rate(person))
    
    def role_rate(self, person):
        return (self.count_attr(person.current_role, self.roles)) * 20

    def country_rate(self, person):
        return (self.has_attr(person.country, self.countries) and 1 or 0) * 50

    def industry_rate(self, person):
        return (self.has_attr(person.industry, self.industries) and 1 or 0) * 100

    def recommendation_rate(self, person):
        return person.num_recommendations

    def connections_rate(self, person):
        return person.num_connections / 10

    def has_attr(self, word, list):
        for attr in list:
            return attr in word
        return False

    def count_attr(self, word, list):
        i = 0
        for attr in list:
            if attr in word:
                i += 1
        return i

    

