from random import choice
from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module; Flask wants
# to know this to know what any imported things are relative to.
app = Flask(__name__)

# user_name = "this is not a name"

# route to handle the landing page of a website.
@app.route('/')
def start_here():
    return "Hi! This is the home page."

# route to display a simple web page
@app.route('/home')
def say_hello():
    return render_template("hello.html")
# This gets called in the HTML tag for the submit button on hello.html



@app.route('/greet')
def greet_person():
    user_name = request.args.get("person")

    AWESOMENESS = [
        'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
        'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html", person=user_name, compliment=compliment)


@app.route('/game')
def show_game_form():
    user_choice = request.args.get("play_choice")

    if user_choice == "false":
        return render_template("goodbye.html")
    else:
        return render_template("game.html")
        

@app.route('/madlib', methods=['POST'])
def show_madlib():
# Need to look up ways of specifying the HTTP method type
    print request
    person = request.form("person")
    color = request.form("fave_color")
    noun = request.form("noun")
    adjective = request.form("adjective")
    swallow_type = request.form("swallow_type")
    verb = request.form("verb")

    POSSIBLE_TEMPLATES = ["madlib.html", "madlib1.html", "madlib2.html", "madlib3.html"]
    template_to_load = choice(POSSIBLE_TEMPLATES)

# TODO would be cool to change the bg-color based on which color the person chooses for the madlib
    return render_template(template_to_load, person=person, color=color, noun=noun, adjective=adjective, swallow_type=swallow_type, verb=verb)



if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
