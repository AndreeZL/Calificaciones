from logica.Calificaciones import Calificaciones

if __name__ == '__main__':
    notaEscrita = float(input("Ingrese la nota: "))
    nota = Calificaciones(notaEscrita)
    nota.calcularNota()