from flask import Flask, render_template, request
import os
import pickle
import pandas as pd
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['DEBUG'] = True
bootstrap = Bootstrap(app)

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Obtener datos del formulario
        city = request.form['city']
        area = request.form['area']
        rooms = int(request.form['rooms'])
        bathroom = int(request.form['bathroom'])
        parking_spaces = int(request.form['parking_spaces'])
        floor = int(request.form['floor'])
        animal = int(request.form['animal'])
        furniture = int(request.form['furniture'])
        hoa = float(request.form['hoa'])
        rent_amount = float(request.form['rent_amount'])
        property_tax = float(request.form['property_tax'])
        fire_insurance = float(request.form['fire_insurance'])

        # Crear un DataFrame con los datos del formulario
        input_data = pd.DataFrame({
            'city': [city],
            'area': [area],
            'rooms': [rooms],
            'bathroom': [bathroom],
            'parking spaces': [parking_spaces],
            'floor': [floor],
            'animal': [animal],
            'furniture': [furniture],
            'hoa (R$)': [hoa],
            'rent amount (R$)': [rent_amount],
            'property tax (R$)': [property_tax],
            'fire insurance (R$)': [fire_insurance]
        })

        # Cargar el modelo
        with open('mejor_modelo.pkl', 'rb') as archivo_entrada:
            mejor_modelo = pickle.load(archivo_entrada)

        # Predecir el valor de alquiler
        valor_renta = mejor_modelo.predict(input_data)

        # Redirigir a la página de resultados
        return render_template('results.html', valor_renta=valor_renta[0])

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
