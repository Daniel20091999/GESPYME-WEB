import json

class Tarea:
    def __init__(self, id_tarea, nombre_tarea, fecha_inicio, fecha_fin, fecha_limite, estado_tarea):
        self.id_tarea = id_tarea
        self.nombre_tarea = nombre_tarea
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.fecha_limite = fecha_limite
        self.estado_tarea = estado_tarea

    def __repr__(self) -> str:
        return f"Tarea(id_tarea={self.id_tarea}, nombre_tarea={self.nombre_tarea}, fecha_inicio={self.fecha_inicio}, fecha_fin={self.fecha_fin},fecha_limite={self.fecha_limite},estado_tarea = {self.estado_tarea})"
    
    @classmethod
    def from_json(cls, json_data):
        return cls(json_data['id_tarea'], json_data['nombre_tarea'], json_data['fecha_inicio'], json_data['fecha_fin'], json_data['fecha_limite'], json_data['estado_tarea'])
    
# Función para cargar datos desde un archivo JSON y convertirlos en objetos Usuario
def cargar_tareas_desde_json(data):
    with open(data, 'r') as dt:
        datos_json = json.load(dt)
        return [Tarea.from_json(tarea) for tarea  in datos_json]

# Función para guardar datos (objetos Usuario) en un archivo JSON
def guardar_tareas_en_json(tareas, data):
    datos_json = [tarea.__dict__ for tarea in tareas]
    with open(data, 'w') as dt:
        json.dump(datos_json, dt, indent=4)

# Ejemplo de uso
if __name__ == "__main__":
    # Cargar datos desde el archivo JSON
    tareas = cargar_tareas_desde_json('data.json')

    # Imprimir los usuarios cargadas
    for tarea in tareas:
        print(tarea)

    # Modificar un usuario (por ejemplo, cambiar el nombre de usuario)
    tareas[0].nombre_tarea = "Tarea3"

    # Guardar las películas modificadas de vuelta al archivo JSON
    guardar_tareas_en_json(tareas, 'data.json')
    
