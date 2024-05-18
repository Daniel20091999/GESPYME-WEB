import json

class Proyecto:
    def __init__(self, id_proyecto, nombre_proyecto, estado_proyecto):
        self.id_proyecto = id_proyecto
        self.nombre_proyecto = nombre_proyecto        
        self.estado_proyecto = estado_proyecto

    def __repr__(self) -> str:
        return f"Proyecto(id_proyecto={self.id_proyecto}, nombre_proyecto={self.nombre_proyecto}, estado_proyecto = {self.estado_proyecto})"
    
    @classmethod
    def from_json(cls, json_data):
        return cls(json_data['id_proyecto'], json_data['nombre_proyecto'],  json_data['estado_proyecto'])
    
# Función para cargar datos desde un archivo JSON y convertirlos en objetos Usuario
def cargar_proyectos_desde_json(data):
    with open(data, 'r') as dt:
        datos_json = json.load(dt)
        return [Proyecto.from_json(proyecto) for proyecto  in datos_json]

# Función para guardar datos (objetos Usuario) en un archivo JSON
def guardar_proyectos_en_json(proyectos, data):
    datos_json = [proyecto.__dict__ for proyecto in proyectos]
    with open(data, 'w') as dt:
        json.dump(datos_json, dt, indent=4)

# Ejemplo de uso
if __name__ == "__main__":
    # Cargar datos desde el archivo JSON
    tareas = cargar_proyectos_desde_json('data.json')

    # Imprimir los usuarios cargadas
    for proyecto in proyectos: # type: ignore
        print(proyecto)

    # Modificar un usuario (por ejemplo, cambiar el nombre de usuario)
    tareas[0].nombre_tarea = "Tarea3"

    # Guardar las películas modificadas de vuelta al archivo JSON
    guardar_tareas_en_json(tareas, 'data.json')
    
