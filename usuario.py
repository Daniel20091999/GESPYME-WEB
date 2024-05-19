import json

class Usuario:
    def __init__(self, id_usuario, nombre_usuario, apellido_1_usuario, apellido_2_usuario, telefono_usuario, email_usuario,
                 horas_semanales_usuario, coste_hora_usuario, puesto_trabajao_usuario, usuario_usuario, contrasena_usuario, tipo_usuario):
        self.id_usuario = id_usuario
        self.nombre_usuario = nombre_usuario
        self.apellido_1_usuario = apellido_1_usuario
        self.apellido_2_usuario = apellido_2_usuario
        self.telefono_usuario = telefono_usuario
        self.email_usuario = email_usuario
        self.horas_semanales_usuario = horas_semanales_usuario
        self.coste_hora_usuario = coste_hora_usuario
        self.puesto_trabajao_usuario = puesto_trabajao_usuario
        self.usuario_usuario = usuario_usuario
        self.contrasena_usuario = contrasena_usuario
        self.tipo_usuario = tipo_usuario

    def __repr__(self) -> str:
        return f"Usuario(id_usuario={self.id_usuario}, nombre_usuario={self.nombre_usuario}, apellido_1_usuario= {self.apellido_1_usuario}, apellido_2_usuario={self.apellido_2_usuario},
                telefono_usuario={self.telefono_usuario}, email_usuario={self.email_usuario}, horas_semanales_usuario={self.horas_semanales_usuario},
                coste_hora_usuario={self.coste_hora_usuario}, puesto_trabajao_usuario={self.puesto_trabajao_usuario}, usuario_usuario={self.usuario_usuario},
                contrasena_usuario={self.contrasena_usuario}, tipo_usuario={self.tipo_usuario})"
    @classmethod
    def from_json(cls, json_data):
        return cls(json_data['id_usuario'], json_data['nombre_usuario'], json_data['apellido_1_usuario'], json_data['apellido_2_usuario'], json_data['telefono_usuario'],
                   json_data['email_usuario'], json_data['horas_semanales_usuario'], json_data['coste_hora_usuario'], json_data['puesto_trabajo_usuario'],
                   json_data['contador_tareas_usuario'], json_data['contador_proyectos_usuario'], json_data['usuario_usuario'], json_data['contrasena_usuario'],
                   json_data['tipo_usuario'])
    
# Función para cargar datos desde un archivo JSON y convertirlos en objetos Usuario
def cargar_usuarios_desde_json(data):
    with open(data, 'r') as dt:
        datos_json = json.load(dt)
        return [Usuario.from_json(usuario) for usuario in datos_json]

# Función para guardar datos (objetos Usuario) en un archivo JSON
def guardar_usuarios_en_json(usuarios, data):
    datos_json = [usuario.__dict__ for usuario in usuarios]
    with open(data, 'w') as dt:
        json.dump(datos_json, dt, indent=4)

# Ejemplo de uso
if __name__ == "__main__":
    # Cargar datos desde el archivo JSON
    usuarios = cargar_usuarios_desde_json('data.json')

    # Imprimir los usuarios cargadas
    for usuario in usuarios:
        print(usuario)

    # Modificar un usuario (por ejemplo, cambiar el nombre de usuario)
    usuarios[0].nombre_usuario = "Antonio"

    # Guardar las películas modificadas de vuelta al archivo JSON
    guardar_usuarios_en_json(usuarios, 'data.json')
    
