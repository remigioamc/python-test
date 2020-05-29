class Person:
    def __init__(self, args):
        self.id = args[0]
        self.first_name = args[1]
        self.last_name = args[2]
        self.current_role = args[3]
        self.country = args[4]
        self.industry = args[5]
        self.num_recommendations = int(args[6])
        self.num_connections = int(args[7])
        self.rate = 0
