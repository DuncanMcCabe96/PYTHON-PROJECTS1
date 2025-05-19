# Parent Class 
class Team:
    def __init__(self, name, sport, state, conference, rank):
        # Initialize attributes when a Team object is created
        self.name = name
        self.sport = sport
        self.state = state
        self.conference = conference
        self.rank = rank

    def information(self):
        msg = "\nThe {} {} are a {} team in the {} conference.".format(
            self.state, self.name, self.sport, self.conference
        )
        return msg

    def ranking(self):
        msg = "\n{} is my number {} favorite sport.".format(self.sport, self.rank)
        return msg


# Child Class
class Avs(Team):
    def __init__(self):
        # Provide all required arguments, including rank
        Team.__init__(self, "Avalanche", "Hockey", "Colorado", "Western", 1)

    def performance(self):
        msg = "\nThe Avalanche were eliminated in the first round of the playoffs by the Dallas Stars."
        return msg


# Second Child Class
class Stars(Team):
    def __init__(self):
        Team.__init__(self, "Stars", "Hockey", "Dallas", "Western", 1)

    def performance(self):
        msg = "\nThe Stars defeated the Colorado Avalanche in the first round of the playoffs."
        return msg

# Third Child Class
class Broncos(Team):
    def __init__(self):
        Team.__init__(self, "Broncos", "Football", "Denver", "AFC", 2)

    def information(self):
        msg = "\nThe broncos were founded in 1959"
        return msg



# Main program
if __name__ == "__main__":
    teams = [Avs(), Stars(), Broncos()]  # Polymorphic collection

    for team in teams:
        print(team.information())  # Polymorphic call (different behavior for Broncos)
        print(team.ranking())      # Inherited method behaves the same
        # Only call performance if it exists
        if hasattr(team, 'performance'):
            print(team.performance())

