from flask import Flask, render_template, request, redirect, url_for, session
from models import Teams, Results_list,Table
from itertools import combinations




app = Flask(__name__)


@app.context_processor
def inject_enumerate():
    return dict(enumerate=enumerate)

allteams=[]
fixture=[]
allresults=[]
table_results=[]


@app.route('/', methods =['GET'])
def index():
     print(allteams)    
     
     return render_template('index.html', allteams=allteams)


@app.route('/table/',methods=['GET'])
def table():
    def update_table(results):
        for game in results:
            team_1_name, team_1_score, team_2_name, team_2_score = game

            team_1= None
            for team in Table.all_stats:
                if team.team_name == team_1_name:
                    team_1 = team
                    break
                    
            team_2= None
            for team in Table.all_stats:
                if team.team_name == team_2_name:
                    team_2 = team
                    break

            if team_1 and team_2:   
                team_1.played += 1
                team_2.played += 1
                team_1.goals_for += team_1_score 
                team_2.goals_against += team_1_score
                team_2.goals_for += team_2_score 
                team_1.goals_against += team_2_score
            
                if team_1_score > team_2_score:
                    team_1.wins += 1
                    team_2.losses += 1
                    team_1.points += 3

                elif team_1_score < team_2_score: 
                    team_1.losses += 1 
                    team_2.wins += 1 
                    team_2.points += 3

                else: 
                    team_1.draws += 1 
                    team_2.draws += 1
                    team_1.points += 1 
                    team_2.points += 1
                
    # prevent duplicate instances of Table
    for team in allteams:
        if not any(team.team_name == existing_team.team_name for existing_team in Table.all_stats):
            Table(team.team_name)
        else:
            break
        
    print(table_results)
    update_table(table_results)
    table_results.clear()

    for team in Table.all_stats:
        print(f"Team: {team.team_name}, Played: {team.played}, Points: {team.points}, Goals For: {team.goals_for}, Goals Against: {team.goals_against}, Goals Difference: {team.goals_difference}, Wins: {team.wins}, Draws: {team.draws}, Losses: {team.losses}")
    
    return render_template('table.html', all_stats=Table.all_stats)


@app.route('/fixtures/', methods=['GET'])
def fixtures():

    return render_template('fixtures.html', fixture=fixture)

   

@app.route('/results/', methods=['GET','POST'])
def results(): 

    return render_template('results.html', allresults=allresults,fixture_flat=fixture_flat)


@app.route('/submit_results/', methods=['POST'])
def submit_results(): 
    
  
    if len(allteams) > 0:
        team_1 = request.form['team_1']
        team_2 = request.form['team_2']
        team_1_goals = request.form['team_1_goals']
        team_2_goals = request.form['team_2_goals']

        match_result = Results_list(team_1, team_1_goals, team_2, team_2_goals)
        
        global allresults
        allresults.append([match_result.team_1, int(match_result.team_1_goals), match_result.team_2, int(match_result.team_2_goals)])
        

        global table_results 
        table_results.append([match_result.team_1, int(match_result.team_1_goals), match_result.team_2, int(match_result.team_2_goals)])
        
        fixture_flat.pop(0)
        print(fixture_flat)
        print(allresults)
    
    

       
    return render_template('results.html',  allresults=allresults, fixture_flat=fixture_flat)


@app.route('/login/', methods=['POST'])
def login():
    return render_template('login.html')


@app.route('/register/')
def register():
    return render_template('register.html')

 
# Get team data from form and add to list allteams

@app.route('/submit', methods=['POST'])
def submit():
    team_no = allteams.__len__()+1
    team_id = request.form['team_id']
    password = request.form['password']
    team_name = request.form['team_name']
    team_color = request.form['team_color']
    players = request.form.getlist('player')

    team_id = Teams(team_no, team_id, password, team_name, team_color, players)
   
    allteams.append(team_id)

    print (len(allteams))

    # generate fixtures
    team_name_list = [team.team_name for team in allteams]
    if len(team_name_list)%2 !=0:   
        team_name_list.append('Bye')
    
    weeks =len(team_name_list)-1
    half = len(team_name_list) // 2

    global fixture   
    fixture= []

    for week in range(weeks):
        week_fixtures = []

        for i in range(half):
            team1 = team_name_list[i]
            team2 = team_name_list[len(team_name_list) - 1 - i]
            week_fixtures.append([team1, team2])
        
        fixture.append(week_fixtures)
        team_name_list.insert(1, team_name_list.pop())
        print(fixture) 

    # flatten fixture list for results page
    global fixture_flat
    fixture_flat=[item for sublist in fixture for item in sublist] 

  

    return render_template('register.html', team_id=team_id)


def user():
    users = []
    for team in allteams: 
        users[team.team_id] = team.team_name
    print(users)



if __name__ == '__main__':
    app.run(debug=True, port=8080)