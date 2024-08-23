from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load your model
model = pickle.load(open('dermatology.pickle', 'rb'))

# Mapping of class numbers to disease names
disease_mapping = {
    1: "Psoriasis",
    2: "Seborrheic Dermatitis",
    3: "Lichen Planus",
    4: "Pityriasis Rosea",
    5: "Chronic Dermatitis",
    6: "Pityriasis Rubra Pilaris"
}


@app.route('/', methods=['GET', 'POST'])
def predict():
    features = [
        'follicular_horn_plug', 'PNL_infiltrate', 'elongation_rete_ridges',
        'polygonal_papules', 'inflammatory_mononuclear_infiltrate',
        'vacuolisation_damage_basal_layer', 'eosinophils_infiltrate',
        'itching', 'koebner_phenomenon', 'follicular_papules',
        'clubbing_rete_ridges', 'fibrosis_papillary_dermis',
        'definite_borders', 'parakeratosis', 'exocytosis',
        'focal_hypergranulosis'
    ]

    if request.method == 'POST':
        input_features = [int(request.form[feature]) for feature in features]
        prediction = model.predict([input_features])[0]
        disease_type = disease_mapping.get(prediction, "Unknown Disease")
        return f'<h2>Patient has disease type: <span>{disease_type}</span></h2>'

    return render_template('index.html', features=features)


if __name__ == "__main__":
    app.run(debug=True)
