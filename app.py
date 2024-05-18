from flask import Flask, request, render_template, json, redirect

app = Flask(__name__)
jsnfile = 'data.json'



@app.route('/', methods=['GET', "POST"])
def index():
    with open(jsnfile, 'r') as ps:
        proyectos = json.load(ps)
    return render_template("index.html",  proyectos=proyectos)

@app.route("/add_proyecto", methods = ['GET', 'POST'])
def addProyecto():
    if request.method == 'GET':
        return render_template('add_proyecto.html',tarea={})
    if request.method == 'POST':
        id_proyecto = request.form["id_proyecto"]
        nombre_proyecto = request.form["nombre_proyecto"]        
        estado_proyecto = request.form["estado_proyecto"]
        with open(jsnfile, 'r+') as ps:
            proyectos = json.load(ps)
        proyectos.append({"id_proyecto": id_proyecto, "nombre_proyecto": nombre_proyecto, "estado_proyecto": estado_proyecto})
        with open(jsnfile, 'w') as ps:
            json.dump(proyectos, ps)
        return redirect('/')
    

@app.route('/update_proyecto/<string:id_proyecto>',methods = ['GET','POST'])
def update_proyecto(id_proyecto):
    with open(jsnfile) as ps:
        proyectos = json.load(ps)
    if request.method == 'GET':
        proyecto = [x for x in proyectos if x['id_proyecto'] == id_proyecto][0]
        return render_template("update_proyecto.html", proyecto=proyecto)
    if request.method == 'POST':
        for proyecto in proyectos:
            if(proyecto['id_proyecto'] == id_proyecto):
                proyecto['nombre_proyecto'] = request.form["nombre_proyecto"]                
                proyecto['estado_proyecto'] = request.form["estado_proyecto"]
                break
        with open(jsnfile, 'w') as ps:
            json.dump(proyectos, ps)
        return redirect('/')


@app.route('/delete_tarea/<string:id_tarea>')
def delete_tarea(id_tarea):
    with open(jsnfile) as ps:
        tareas = json.load(ps)
    new_tarea_list = []
    for tarea in tareas:
        if(tarea['id_tarea'] != id_tarea):
            new_tarea_list.append(tarea)
    with open(jsnfile, 'w') as uw:
        json.dump(new_tarea_list, uw)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True, port=5001)