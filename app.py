from flask import Flask, request, render_template, json, redirect

app = Flask(__name__)
jsnfile = 'data.json'



@app.route('/', methods=['GET', "POST"])
def index():
    with open(jsnfile, 'r') as ps:
        usuarios = json.load(ps)
    return render_template("index.html",  usuarios=usuarios)

@app.route("/add_usuario", methods = ['GET', 'POST'])
def addFilm():
    if request.method == 'GET':
        return render_template('add_usuario.html', usuario={})
    if request.method == 'POST':
        id_usuario = request.form["id_usuario"]
        nombre_usuario = request.form["nombre_usuario"]
        apellido_1_usuario = request.form["apellido_1_usuario"]
        apellido_2_usuario = request.form["apellido_2_usuario"]
        telefono_usuario = request.form["telefono_usuario"]
        email_usuario= request.form["email_usuario"]
        horas_semanales_usuario = request.form["horas_semanales_usuario"]
        coste_hora_usuario = request.form["coste_hora_usuario"]
        puesto_trabajo_usuario = request.form["puesto_trabajo_usuario"]
        usuario_usuario = request.form["usuario_usuario"]
        contrasena_usuario = request.form["contrasena_usuario¡"]
        tipo_usuario = request.form["tipo_usuario"]
        contador_tareas_usuario = 0
        contador_proyectos_usuario = 0
        with open(jsnfile, 'r+') as us:
            usuarios = json.load(us)
        usuarios.append({"id_usuario": id_usuario, "nombre_usuario": nombre_usuario, "apellido_1_usuario": apellido_1_usuario,
                              "apellido_2_usuario": apellido_2_usuario, "telefono_usuario": telefono_usuario, "email_usuario": email_usuario,
                              "horas_semanales_usuario": horas_semanales_usuario, "coste_hora_usuario": coste_hora_usuario,
                              "puesto_trabajo_usuario": puesto_trabajo_usuario, "contador_tareas_usuario": contador_tareas_usuario, "contador_proyectos_usuario": contador_proyectos_usuario,
                              "usuario_usuario": usuario_usuario, "contrasena_usuario": contrasena_usuario, "tipo_usuario": tipo_usuario})
        with open(jsnfile, 'w') as us:
            json.dump(usuarios, us)
        return redirect('/')
    

@app.route('/update_usuario/<string:id_usuario>',methods = ['GET','POST'])
def update_usuario(id_usuario):
    with open(jsnfile) as ps:
        usuarios = json.load(ps)
    if request.method == 'GET':
        usuario = [x for x in usuarios if x['id_usuario'] == id_usuario][0]
        return render_template("add_usuario.html", usuario=usuario)
    if request.method == 'POST':
        for usuario in usuarios:
            if(usuario['id_usuario'] == id_usuario):
                usuario['nombre_usuario'] = request.form["nombre_usuario"]
                usuario['apellido_1_usuario'] = request.form["apellido_1_usuario"]
                usuario['apellido_2_usuario'] = request.form["apellido_2_usuario"]
                usuario['telefono_usuario'] = request.form["telefono_usuario"]
                usuario['email_usuario'] = request.form["email_usuario"]
                usuario['horas_semanales_usuario'] = request.form["horas_semanales_usuario"]
                usuario['coste_hora_usuario'] = request.form["coste_hora_usuario"]
                usuario['puesto_trabajo_usuario'] = request.form["puesto_trabajo_usuario"]
                usuario['contador_tareas_usuario'] = request.form["contador_tareas_usuario"]
                usuario['contador_proyectos_usuario'] = request.form["contador_proyectos_usuario"]
                usuario['usuario_usuario'] = request.form["usuario_usuario"]
                usuario['contrasena_usuario'] = request.form["contrasena_usuario"]
                usuario['tipo_usuario'] = request.form["tipo_usuario"]
                break
        with open(jsnfile, 'w') as ps:
            json.dump(usuarios, ps)
        return redirect('/')


@app.route('/delete_usuario/<string:id_usuario>')
def delete_usuaario(id_usuario):
    with open(jsnfile) as ps:
        usuarios = json.load(ps)
    new_user_list = []
    for usuario in usuarios:
        if(usuario['id_usuario'] != id_usuario):
            new_user_list.append(usuario)
    with open(jsnfile, 'w') as uw:
        json.dump(new_user_list, uw)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True, port=5001)