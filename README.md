# Telegram Group Contacts Exporter

Un script Python pour exporter les membres d’un groupe Telegram dans un fichier CSV, facilement et rapidement !

## Installation

1. Clonez le repo  
2. `pip install -r requirements.txt`
3. Copiez `.env.example` en `.env` et remplissez vos identifiants Telegram :
   - `API_ID`, `API_HASH` : [Créez-les ici](https://my.telegram.org/auth)
   - `PHONE_NUMBER` : Votre numéro au format international
4. Lancez le script avec :  
   `python main.py`

## Utilisation

Le script va :
- Vous demander un code (envoyé par Telegram la première fois)
- Lister vos groupes
- Exporter tous les membres du groupe choisi dans `contacts.csv`

## Auteur

Projet réalisé par **[Claude Ndanda]**  

## Licence

MIT
