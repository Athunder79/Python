from flask import Flask, render_template, request, redirect, url_for,session

app = Flask(__name__)

class Teams:
    def __init__(self, team_id, team_name, team_color):
        self.team_id = team_id
        self.team_name = team_name
        self.team_color = team_color
       


@app.route('/')
def index():    
     return render_template('index.html')
   

@app.route('/fixtures/')
def fixtures():
    return render_template('fixtures.html')

@app.route('/results/')
def results(): 
    return render_template('results.html')

@app.route('/login/')
def login():
    return render_template('login.html')

@app.route('/register/')
def register():
    return render_template('register.html')

 




@app.route('/submit', methods=['POST'])
def submit():
     team_id = request.form.get('team_id')
     team_name = request.form.get('team_name')
     team_color = request.form.get('team_color')
     team = Teams(team_id, team_name, team_color)
     return render_template('register.html', team=team)    




if __name__ == '__main__':
    app.run(debug=True, port=8080)