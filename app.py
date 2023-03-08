from flask import Flask, jsonify, request, render_template
import joblib

app = Flask(__name__, template_folder='templates')

# 0 - hate speech 1 - offensive language 2 - neither

Labels = ['setosa', 'versicolor', 'virginica']
clf = joblib.load("model/irisclass.joblib.z")

@app.route('/')
def hello():
    return render_template('index.html')

# Route pour prédire la classe d'une texte de plusieurs mots
@app.route('/prediction', methods=['POST'])
def predict_specie():
    length = float(request.form['pet_len'])
    width = float(request.form['pet_wid'])
    pred = clf.predict([[length, width]])
    return render_template('index.html', response = Labels[pred[0]])
    #return jsonify(Labels[clf.predict_proba([request.json.get('texte')]).argmax()])

# Lancement de l'application Flask
if __name__ == '__main__':
    app.run(debug=True)

