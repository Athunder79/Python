class Teams:
    def __init__(self, team_no, team_id, password, team_name, team_color, players=None):
        self.team_no = team_no
        self.team_id = team_id
        self.password = password
        self.team_name = team_name
        self.team_color = team_color
        self.players = players or []

class Fixture_list:
    def __init__(self, team_1, team_2):
        self.team_1 = team_1
        self.team_2 = team_2
    
class Results_list:
    def __init__(self, team_1, team_1_goals, team_2, team_2_goals):
        self.team_1 = team_1
        self.team_1_goals = team_1_goals
        self.team_2 = team_2
        self.team_2_goals = team_2_goals

class Table:
    all_stats=[]
    
    def __init__(self, team_name, played=0, points=0, goals_for=0, goals_against=0, goals_difference=0, wins=0, losses=0, draws=0):
        self.team_name = team_name
        self.played = played
        self.points = points
        self.goals_for = goals_for
        self.goals_against = goals_against
        self.goals_difference = goals_difference
        self.wins = wins
        self.losses = losses
        self.draws = draws
        Table.all_stats.append(self)
    
   

       

class Players:
    def __init__(self, player_name, team_name, goals=0):
        self.player_name = player_name
        self.team_name = team_name
        self.goals = goals
