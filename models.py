class Teams:
    def __init__(self, team_no, team_id, password, team_name, team_color, players=None):
        self.team_no = team_no
        self.team_id = team_id
        self.password = password
        self.team_name = team_name
        self.team_color = team_color
        self.players = players or []
    
    
    
       

class Players:
    def __init__(self, player_name, team_name, goals=0):
        self.player_name = player_name
        self.team_name = team_name
        self.goals = goals
