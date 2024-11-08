from estudiantes import Estudiantes
from profesores import Profesores
from administrativos import Administrativos
from empleado_limpieza import EmpleadoLimpieza

def main():
    # Crear objetos
    estudiante = Estudiantes()
    estudiante.get_nombre()
    estudiante.set_nombre("")
    estudiante.set_apellido("Pérez")
    estudiante.set_edad(20)
    estudiante.set_matricula("123456")
    estudiante.get_carrera()
    estudiante.set_carrera("Ingenieria en Sistemas Computacionales")
    estudiante.get_semestre()
    estudiante.set_semestre(4)

    profesor = Profesores()
    profesor.set_nombre("Maria")
    profesor.set_apellido("López")
    profesor.set_edad(40)
    profesor.set_departamento("Matemáticas")
    profesor.set_categoria("Tiempo completo")
    profesor.set_maximo_grado_de_estudios("Universidad")

    administrativo = Administrativos()
    administrativo.set_nombre("Carlos")
    administrativo.set_apellido("González")
    administrativo.set_edad(35)
    administrativo.set_cargo("Secretario")
    administrativo.set_area("Matematicas")

    empresa = EmpleadoLimpieza()
    empresa.set_nombre("Pedro")
    empresa.set_apellido("Martínez")
    empresa.set_edad(45)
    empresa.set_numero_empleado("E1234")
    empresa.set_nombre_empresa("Limpieza S.A.")
    empresa.set_direccion("Calle Ficticia 123")
    empresa.set_turno("Matutino")

    # Mostrar información
    print("Estudiante:")
    print(estudiante.mostrar_informacion())

    print("\nProfesor:")
    print(profesor.mostrar_informacion())

    print("\nAdministrativo:")
    print(administrativo.mostrar_informacion())

    print("\nEmpleado de Limpieza:")
    print(empresa.mostrar_informacion())

if __name__ == "__main__":
    main()