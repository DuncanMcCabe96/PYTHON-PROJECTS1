# Parent class: Athlete
class Athlete:
    def __init__(self, name, sport, age):
        # Common attributes for all athletes
        self.name = name
        self.sport = sport
        self.age = age

    def display_info(self):
        # Display basic athlete information using string concatenation
        print("Name: " + self.name)
        print("Sport: " + self.sport)
        print("Age: " + str(self.age))


# Child class: FootballPlayer inherits from Athlete
class FootballPlayer(Athlete):
    def __init__(self, name, sport, age, position, touchdowns):
        # Call the parent class constructor
        Athlete.__init__(self, name, sport, age)
        # Football-specific attributes
        self.position = position
        self.touchdowns = touchdowns

    def player_info(self):
        # Display football player specific info
        print("Position: " + self.position)
        print("Touchdowns scored: " + str(self.touchdowns))


# Child class: BasketballPlayer inherits from Athlete
class BasketballPlayer(Athlete):
    def __init__(self, name, sport, age, points_per_game, team):
        # Call the parent class constructor
        Athlete.__init__(self, name, sport, age)
        # Basketball-specific attributes
        self.points_per_game = points_per_game
        self.team = team

    def player_info(self):
        # Display basketball player specific info
        print("Team: " + self.team)
        print("Points per game: " + str(self.points_per_game))


# Example usage:

# Create a FootballPlayer object
player1 = FootballPlayer("Tom Brady", "Football", 45, "Quarterback", 624)
player1.display_info()    # Inherited from Athlete
player1.player_info()     # Specific to FootballPlayer

print()  # Blank line for readability

# Create a BasketballPlayer object
player2 = BasketballPlayer("LeBron James", "Basketball", 39, 27.2, "Lakers")
player2.display_info()    # Inherited from Athlete
player2.player_info()     # Specific to BasketballPlayer
