from flask import Flask, render_template,request , redirect , url_for , flash 

app = Flask(__name__)
app.secret_key = 'clave_secreta'  # Cambia 'clave_secreta' por algo más seguro en un entorno de producción


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quienes-somos')
def quienes_somos():
    return render_template('quienes_somos.html')

@app.route('/servicios')
def servicios():
    return render_template('servicios.html')

@app.route('/servicio/<nombre>')
def servicio_detalle(nombre):
    # Puedes enviar el nombre del servicio a la plantilla para mostrar más detalles.
    return render_template('servicio_detalle.html', nombre=nombre)

@app.route('/noticias')
def noticias():
    return render_template('noticias.html')

@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        mensaje = request.form['mensaje']
        # Aquí puedes agregar lógica para guardar los datos o enviarlos por correo electrónico
        flash('Tu mensaje ha sido enviado con éxito.')
        return redirect(url_for('contacto'))
    return render_template('contacto.html')


if __name__ == '__main__':
    app.run(debug=True)
