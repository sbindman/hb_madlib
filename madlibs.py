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
        
@app.route('/madlib')
def show_madlib():
    person = request.args.get("person")
    color = request.args.get("fave_color")
    noun = request.args.get("noun")
    adjective = request.args.get("adjective")
# TODO would be cool to change the bg-color based on which color the person chooses for the madlib
    return render_template("madlib.html", person=person, color=color, noun=noun, adjective=adjective)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
