class Teams:
    def __init__(self, team_id, team_name, team_color):
        self.team_id = team_id
        self.team_name = team_name
        self.team_color = team_color

 
    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

    def __repr__(self):
        return str(self.__class__) + ": " + str(self.__dict__)
       

class Players:
    def __init__(self, player_name, team_name, goals=0):
        self.player_name = player_name
        self.team_name = team_name
        self.goals = goals
