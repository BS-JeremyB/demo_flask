
from flask import Flask
from config import SECRET_KEY, DB
from flask_wtf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialiser l'application Flask
app = Flask(__name__)

# Configurations
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialisation des extensions
csrf = CSRFProtect(app)
db = SQLAlchemy(app)

from app.models.film_model import Film, Realisateur

# Créer un contexte d'application pour exécuter db.create_all()
try:
    with app.app_context():
        db.create_all()  # Création de toutes les tables
        print("----------------------")
        print("Connexion db établie et tables créées !")
        print("----------------------")
except SQLAlchemyError as error:
    print(f"Erreur de connexion à la base de données : {error}")
except Exception as e:
    print(f"Erreur inattendue : {e}")

from app.routes import presentation, film
