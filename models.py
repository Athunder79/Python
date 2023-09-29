class Teams:
    def __init__(self, team_no, team_id, password, team_name, team_color, players=None):
        self.team_no = team_no
        self.team_id = team_id
        self.password = password
        self.team_name = team_name
        self.team_color = team_color
        self.players = players or []
    
    def submit():
        team_no = allteams.__len__()+1
        team_id = request.form['team_id']
        password = request.form['password']
        team_name = request.form['team_name']
        team_color = request.form['team_color']
        players = request.form.getlist('player')

        team_id = Teams(team_no, team_id, password, team_name, team_color, players)
        allteams.append(team_id)
  

    
    
    
    
       

class Players:
    def __init__(self, player_name, team_name, goals=0):
        self.player_name = player_name
        self.team_name = team_name
        self.goals = goals
