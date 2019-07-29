def pluralize(word):
    if word[-3:] == "ife":
        return word[:-3] + "ives"
    elif word [-2:] == "ch":
        return word[:-1] + "hes"
    elif word [-2:] == "us":
        return word[:-2] + "i"
    elif word[-1:] == "y":
        return word[:-1] + "ies"
    else:
        return word+'s'

number = int(raw_input("#: "))
the_word = raw_input("word:")

if number == 1:
    print ((str(number))+(" ")+(the_word))
else:
    print ((str(number))+(" ")+pluralize(the_word))



import webapp2
import jinja2
import os


the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


# the handler section
class EnterInfoHandler(webapp2.RequestHandler):
    def get(self):  # for a get request
        welcome_template = the_jinja_env.get_template('templates/welcome.html')
        a_variable_dict = {
            "greeting": "Salutations",
            "adjective": "dank"
        }
        self.response.write(welcome_template.render(a_variable_dict))

], debug=True)
