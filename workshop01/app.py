import flask
import random
app = flask.Flask(__name__)


@app.route('/')
def index():
    list_of_words = [
        "Logic will get you from A to B. Imagination will take you everywhere.",
        "There are 10 kinds of people. Those who know binary and those who don't.",
        "There are two ways of constructing a software design. One way is to make it \
            so simple that there are obviously no deficiencies and the other is to make \
            it so complicated that there are no obvious deficiencies.",
        "It's not that I'm so smart, it's just that I stay with problems longer.",
        "It is pitch dark. You are likely to be eaten by a grue."]
    random_index = random.randint(0, 4)
    return flask.render_template('index.html', e=list_of_words[random_index])


if __name__ == '__main__':
    app.debug = True
    app.run()
