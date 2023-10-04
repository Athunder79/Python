from flask import Flask, render_template, request, redirect, url_for, session
from models import Teams, Users
from itertools import combinations
import random



app = Flask(__name__)


@app.context_processor
def inject_enumerate():
    return dict(enumerate=enumerate)

allteams=[]
users=[]
fixture=[]




@app.route('/', methods =['GET'])
def index():
     return render_template('index.html', allteams=allteams)


@app.route('/players/')
def players():
    return render_template('players.html')


@app.route('/fixtures/', methods=['GET','POST'])
def fixtures():
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
            week_fixtures.append((team1, team2))
        
        fixture.append(week_fixtures)
        team_name_list.insert(1, team_name_list.pop())
        print(fixture)
      
        
                              
    
    return render_template('fixtures.html', fixture=fixture)



@app.route('/results/', methods=['GET', 'POST'])
def results(): 
    print(fixture)
    return render_template('results.html', fixture=fixture)



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

  
    return render_template('register.html', team_id=team_id)

def user():
    users = {}
    for team in allteams: 
        users[team.team_id] = team.team_name
    return users



if __name__ == '__main__':
    app.run(debug=True, port=8080)