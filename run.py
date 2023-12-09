from flask import Flask, render_template, request
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html', title="index")

@app.route('/form01')
def mostrar_form01():
    return render_template('form/form_send01.html', title="index")

@app.route('/resultado-form-example01', methods=['GET', 'POST'])
def form_resultados01():
    # handle the POST request
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        apellido = request.form.get('apellido')
        return '''
                  <h1>Nombre: {}</h1>
                  <h1>Apellido: {}</h1>
                  <br>
                  <a href="/">Home</a>'''.format(nombre, apellido)
    
@app.route('/form02')
def mostrar_form02():
    return render_template('form/form_send02.html', title="index")

@app.route('/resultado-form-example02', methods=['GET', 'POST'])
def form_resultados02():
    # handle the POST request
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        apellido = request.form.get('apellido')
        return render_template('form/resultado_form02.html', nombre=nombre, apellido=apellido)
    
@app.route('/mostrar_lista_datos')
def mostrar_lista_datos():
    # Pasa una lista de valores a la plantilla
    lista_de_valores = ['Valor 1', 'Valor 2', 'Valor 3', 'Valor 4', 'Valor 5']

    # Renderiza la plantilla y pasa la lista de valores
    return render_template('datos/mostrar-lista-datos.html', lista_de_valores=lista_de_valores)

@app.route('/mostrar_dataframe')
def mostrar_dataframe():
    # Crea un DataFrame de ejemplo
    data = {'Nombre': ['Alice', 'Bob', 'Charlie'],
            'Edad': [25, 30, 22],
            'Ciudad': ['Ciudad A', 'Ciudad B', 'Ciudad C']}
    df = pd.DataFrame(data)

    # Convierte el DataFrame a una lista de diccionarios
    lista_de_diccionarios = df.to_dict('records')

    # Renderiza la plantilla y pasa la lista de diccionarios
    return render_template('datos/mostrar-dataframe.html', datos=lista_de_diccionarios)

@app.route('/mostrar_grafico')
def mostrar_grafico():
    # Crea un DataFrame de ejemplo
    data = {'Nombre': ['Alice', 'Bob', 'Charlie'],
            'Edad': [25, 30, 22],
            'Ciudad': ['Ciudad A', 'Ciudad B', 'Ciudad C']}
    df = pd.DataFrame(data)

    # Crea un gráfico de barras
    plt.bar(df['Nombre'], df['Edad'])
    plt.xlabel('Nombre')
    plt.ylabel('Edad')
    plt.title('Gráfico de Barras')

    # Convierte el gráfico a una imagen en formato base64
    img_data = BytesIO()
    plt.savefig(img_data, format='png')
    img_data.seek(0)
    img_base64 = base64.b64encode(img_data.read()).decode('utf-8')

    # Renderiza la plantilla y pasa la imagen base64
    return render_template('graficos/mostrar-grafico.html', imagen_base64=img_base64)


if __name__ == '__main__':
    app.run(debug=True)