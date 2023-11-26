from flask import Flask
from flask import render_template
#from tabulate import tabulate 
import pandas as pd


app = Flask(__name__)

@app.route('/students/')
def fill_table ():
    people = [
           {"imya": "Ivan", "Familya": "Ivanovic","Vozrast": 29, "Sredniy": 34},
          {"imya": "senya", "Familya": "Anovic","Vozrast": 34, "Sredniy": 54},
          {"imya": "Masa", "Familya": "wenovic","Vozrast": 18, "Sredniy": 44}]
    
    html_table = pd.DataFrame(people).to_html()
    return render_template(template_name_or_list='students.html', people=html_table)
    print(html_table)



if __name__ == '__main__': 
    app.run()