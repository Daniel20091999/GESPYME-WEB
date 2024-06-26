import json

class Proyecto:
    def __init__(self, id_proyecto, nombre_proyecto, manager_proyecto, empledos_proyecto, tareas_proyecto, estado_proyecto):
        self.id_proyecto = id_proyecto
        self.nombre_proyecto = nombre_proyecto   
        self.manager_proyecto = manager_proyecto
        self.empledos_proyecto = empledos_proyecto
        self.tareas_proyecto = tareas_proyecto
        self.estado_proyecto = estado_proyecto

    def __repr__(self) -> str:
        return f"Proyecto(id_proyecto={self.id_proyecto}, nombre_proyecto={self.nombre_proyecto}, manager_proyecto = {self.manager_proyecto},
                empleados_proyecto = {self.empledos_proyecto}, tareas_proyecto = {self.tareas_proyecto},estado_proyecto = {self.estado_proyecto})"
    
    @classmethod
    def from_json(cls, json_data):
        return cls(json_data['id_proyecto'], json_data['nombre_proyecto'],json_data['manager_proyecto'], json_data['empledos_proyecto'],
                   json_data['tareas_proyecto'], json_data['estado_proyecto'])
    
# Función para cargar datos desde un archivo JSON y convertirlos en objetos Proyecto
def cargar_proyectos_desde_json(data):
    with open(data, 'r') as dt:
        datos_json = json.load(dt)
        return [Proyecto.from_json(proyecto) for proyecto  in datos_json]

# Función para guardar datos (objetos Proyecto) en un archivo JSON
def guardar_proyectos_en_json(proyectos, data):
    datos_json = [proyecto.__dict__ for proyecto in proyectos]
    with open(data, 'w') as dt:
        json.dump(datos_json, dt, indent=4)

# Ejemplo de uso
if __name__ == "__main__":
    # Cargar datos desde el archivo JSON
    proyectos = cargar_proyectos_desde_json('data.json')

    # Imprimir los usuarios cargadas
    for proyecto in proyectos:
        print(proyecto)

    # Modificar un proyecto (por ejemplo, cambiar el nombre de proyecto)
    proyectos[0].nombre_proyecto = "Proyecto3"

    # Guardar las proyectos modificadas de vuelta al archivo JSON
    guardar_proyectos_en_json(proyectos, 'data.json')