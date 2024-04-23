from funciones2 import Empleado


def test_aumentar_salario():
    empleado = Empleado('Carlos', 'Perez', 300)
    empleado.test_aumentar_salario()
    assert empleado.salario == 4000
