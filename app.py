from flask_mysqldb import MySQL
from flask import Flask, render_template, request

app  = Flask(__name__, template_folder='template')

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'beta_expert_system'

mysql = MySQL(app)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/egg")
def egg_page() :
    main_ingridient = 'egg'
    return render_template('question.html', value=main_ingridient)

@app.route("/meat")
def meat_page() :
    main_ingridient = 'meat'
    return render_template('question.html', value=main_ingridient)

@app.route("/vegetable")
def vegetable_page() :
    main_ingridient = 'vegetable'
    return render_template('question.html', value=main_ingridient)

@app.route("/flour")
def flour_page() :
    main_ingridient = 'flour'
    return render_template('question.html', value=main_ingridient)


@app.route("/<main_ingridient>/result",  methods=['GET', 'POST'])
def result_page(main_ingridient):
    result = "ERROR"
    if  request.method == "POST" :
        food_type = request.form['food-type'] 
        calories_type = request.form['calories-type']
        flavor_type = request.form['flavor-type']
        
        query = """
            SELECT dish_name FROM recipe WHERE food_type = %s AND calories_type = %s AND flavor_type = %s AND main_ingridient = %s;
        """
        var = food_type, calories_type, flavor_type, main_ingridient
        
        cursor = mysql.connection.cursor()        
        cursor.execute(query, var)
        mysql.connection.commit()
        
        food = str(cursor.fetchall())
        
        result = food[3:-5]

    return render_template('result.html', value=result)

if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.debug = True
    app.run()