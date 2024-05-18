from flask import Flask, request, render_template, json, redirect

app = Flask(__name__)
jsnfile_usuarios = 'usuarios.json'
jsnfile_tareas = 'tareas.json'


@app.route('/', methods=['GET', "POST"])
def mostrar_usuarios():
    with open(jsnfile_usuarios, 'r') as ps:
        usuarios = json.load(ps)
    return render_template("mostrar_usuarios.html",  usuarios=usuarios)

@app.route('/mostrar_tareas', methods=['GET', "POST"])
def mostrar_tareas():
    with open(jsnfile_tareas, 'r') as ps:
        tareas = json.load(ps)
    return render_template("mostrar_tareas.html",  tareas=tareas)

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
        with open(jsnfile_usuarios, 'r+') as us:
            usuarios = json.load(us)
        usuarios.append({"id_usuario": id_usuario, "nombre_usuario": nombre_usuario, "apellido_1_usuario": apellido_1_usuario,
                              "apellido_2_usuario": apellido_2_usuario, "telefono_usuario": telefono_usuario, "email_usuario": email_usuario,
                              "horas_semanales_usuario": horas_semanales_usuario, "coste_hora_usuario": coste_hora_usuario,
                              "puesto_trabajo_usuario": puesto_trabajo_usuario, "contador_tareas_usuario": contador_tareas_usuario, "contador_proyectos_usuario": contador_proyectos_usuario,
                              "usuario_usuario": usuario_usuario, "contrasena_usuario": contrasena_usuario, "tipo_usuario": tipo_usuario})
        with open(jsnfile_usuarios, 'w') as us:
            json.dump(usuarios, us)
        return redirect('/')
    

@app.route('/update_usuario/<string:id_usuario>',methods = ['GET','POST'])
def update_usuario(id_usuario):
    with open(jsnfile_usuarios) as ps:
        usuarios = json.load(ps)
    if request.method == 'GET':
        usuario = [x for x in usuarios if x['id_usuario'] == id_usuario][0]
        return render_template("update_usuario.html", usuario=usuario)
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
        with open(jsnfile_usuarios, 'w') as ps:
            json.dump(usuarios, ps)
        return redirect('/')


@app.route('/delete_usuario/<string:id_usuario>')
def delete_usuaario(id_usuario):
    with open(jsnfile_usuarios) as ps:
        usuarios = json.load(ps)
    new_user_list = []
    for usuario in usuarios:
        if(usuario['id_usuario'] != id_usuario):
            new_user_list.append(usuario)
    with open(jsnfile_usuarios, 'w') as uw:
        json.dump(new_user_list, uw)
    return redirect('/')

@app.route("/add_tarea", methods = ['GET', 'POST'])
def addTarea():
    if request.method == 'GET':
        return render_template('add_tarea.html',tarea={})
    if request.method == 'POST':
        id_tarea = request.form["id_tarea"]
        nombre_tarea = request.form["nombre_tarea"]
        fecha_inicio = request.form["fecha_inicio"]
        fecha_fin = request.form["fecha_fin"]
        fecha_limite = request.form["fecha_limite"]
        estado_tarea = request.form["estado_tarea"]
        with open(jsnfile_tareas, 'r+') as ps:
            tareas = json.load(ps)
        tareas.append({"id_tarea": id_tarea, "nombre_tarea": nombre_tarea, "fecha_inicio": fecha_inicio,"fecha_fin": fecha_fin,"fecha_limite": fecha_limite ,"estado_tarea": estado_tarea})
        with open(jsnfile_tareas, 'w') as ps:
            json.dump(tareas, ps)
        return redirect('/')
    

@app.route('/update_tarea/<string:id_tarea>',methods = ['GET','POST'])
def update_tarea(id_tarea):
    with open(jsnfile_tareas) as ps:
        tareas = json.load(ps)
    if request.method == 'GET':
        tarea = [x for x in tarea if x['id_tarea'] == id_tarea][0]
        return render_template("add_tarea.html", tarea=tarea)
    if request.method == 'POST':
        for tarea in tareas:
            if(tarea['id_tarea'] == id_tarea):
                tarea['nombre_tarea'] = request.form["nombre_tarea"]
                tarea['fecha_inicio'] = request.form["fecha_inicio"]
                tarea['fecha_fin'] = request.form["fecha_fin"]
                tarea['fecha_fecha_limite'] = request.form["fecha_limite"]
                tarea['estado_tarea'] = request.form["estado_tarea"]
                break
        with open(jsnfile_tareas, 'w') as ps:
            json.dump(tareas, ps)
        return redirect('/')


@app.route('/delete_tarea/<string:id_tarea>')
def delete_tarea(id_tarea):
    with open(jsnfile_tareas) as ps:
        tareas = json.load(ps)
    new_tarea_list = []
    for tarea in tareas:
        if(tarea['id_tarea'] != id_tarea):
            new_tarea_list.append(tarea)
    with open(jsnfile_tareas, 'w') as uw:
        json.dump(new_tarea_list, uw)
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True, port=5001)