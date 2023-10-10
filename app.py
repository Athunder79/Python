from flask import Flask, render_template, request, redirect, url_for, session
from models import Teams, Results_list,Table
from itertools import combinations

app = Flask(__name__)
app.secret_key = 'fiveaside'


@app.context_processor
def inject_enumerate():
    return dict(enumerate=enumerate)


allteams=[]
fixture=[]
all_results=[]
table_results=[]
users=[]


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
                team_1.goal_difference = team_1.goals_for - team_1.goals_against 
                team_2.goal_difference = team_2.goals_for - team_2.goals_against
            
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

    sorted_table = sorted(Table.all_stats, key=lambda x: (x.points, x.goal_difference), reverse=True)


    table_results.clear()

    
    return render_template('table.html', sorted_table=sorted_table)


@app.route('/fixtures/', methods=['GET'])
def fixtures():

    return render_template('fixtures.html', fixture=fixture)

   

@app.route('/results/', methods=['GET','POST'])
def results(): 

    return render_template('results.html', all_results=all_results, fixture_flat=fixture_flat)


@app.route('/submit_results/', methods=['POST'])
def submit_results(): 
    
  
    if len(allteams) > 0:
        team_1 = request.form['team_1']
        team_2 = request.form['team_2']
        team_1_goals = request.form['team_1_goals']
        team_2_goals = request.form['team_2_goals']

        match_result = Results_list(team_1, team_1_goals, team_2, team_2_goals)
        
        global all_results
        all_results.append([match_result.team_1, int(match_result.team_1_goals), match_result.team_2, int(match_result.team_2_goals)])
        

        global table_results 
        table_results.append([match_result.team_1, int(match_result.team_1_goals), match_result.team_2, int(match_result.team_2_goals)])
        
        fixture_flat.pop(0)
        print(fixture_flat)
        print(all_results)
    
    

       
    return render_template('results.html',  all_results=all_results, fixture_flat=fixture_flat)


@app.route('/login/', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        if username in users:
            session['username'] = username
            return redirect(url_for('index'))
        else:
            return 'Invalid username. <a href="/login">Try Again</a>'
    return render_template('login.html')


@app.route('/logout/')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


@app.route('/register/')
def register():
    return render_template('register.html')

 
# Get team data from form and add to list allteams

@app.route('/submit', methods=['POST'])
def submit():
    team_no = allteams.__len__()+1
    team_id = request.form['team_id']
    team_name = request.form['team_name']
    team_color = request.form['team_color']
    players = request.form.getlist('player')

    if team_id in users:
        raise ValueError('A very specific bad thing happened.')

    team_id = Teams(team_no, team_id, team_name, team_color, players)
   
    allteams.append(team_id)

    users.append(team_id.team_id)

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





if __name__ == '__main__':
    app.run(debug=True, port=8080)