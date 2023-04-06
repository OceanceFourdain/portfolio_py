from flask import Flask, render_template
from requests import get
from json import loads
from http import HTTPStatus
#from flask_mysqldb import MySQL

app = Flask(__name__)
#db = mysql.connector.connect(
 # host = "db5011726151.hosting-data.io",
  #user = "dbu121730",
  #password = "Shooter@7017",
  #database = "dbs9879762"
#)

#cur = db.cursor()

@app.route('/')
def index():
    return render_template ('home.jinja')
@app.route('/profil')
def profil():
    return render_template ('profil.jinja', pagecss='profil')
@app.route('/projet')
def project():
    return render_template ('project.jinja', pagecss='project')
@app.route('/contact')
def contact():
    return render_template ('contact.jinja', pagecss='contact')  
@app.route('/project/pokemons')
def pokemons():
    pokemons = get('https://studies.delpech.info/pbi/pokemons/dataset/json').json()
    return render_template ('pokedex/pokedex.jinja', pokemons=pokemons, pagecss='pokemon')
@app.route('/project/pokemon/<id>')
def pokemon(id): 
    pokemon = get('https://studies.delpech.info/pbi/pokemons/dataset/{}/json'.format(id)).json()
    return render_template ('pokedex/pokemon.jinja', pokemon=pokemon, pagecss='pokemon')
# Partie E-boutique

#@app.route('/boutique/home')
#def boutique_home():
#s   return render_template ('boutique/home-boutique.jinja', boutiquecss='boutique_home')
#
#@app.route('/boutique/product')
#def boutique_product():
 #   cur.execute("""SELECT * FROM product""")
  #  productAll = cur.fetchall()
   # return render_template ('boutique/product/boutique-product.jinja', products=productAll)

if __name__ == '__main__':
  app.run(debug=True)