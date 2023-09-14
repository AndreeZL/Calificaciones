class Calificaciones():
    def __init__(self, nota):
        self.nota = nota

    def calcularNota(self):
        if self.nota < 7.5 :
            print("Calificacion: R-Reprobado")
        elif self.nota < 8.0 and self.nota >= 7.5 :
            print("Calificacion: C-Bien")
        elif self.nota < 9.1 and self.nota >= 8.1 :
            print("Calificacion: B-Muy Bien")
        else:
            self.nota < 10.0 and self.nota >= 9.1
            print("Calificacion: A-Excelente")