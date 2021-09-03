import msvcrt


def run():
    class CalculoMatricula:
        def __init__(self):
            self.valor_matricula = 0
            self.valor_credito = 112000
            self.estrato_estudiante = ""
            self.nombre_estudiante = ""
            self.numero_creditos = 0
            pass

        def Datos_estudiante(self):
            self.nombre_estudiante = input('Ingrese su nombre: ')
            self.estrato_estudiante = input('Ingrese el estrato al que pertenece: ')
            self.numero_creditos = int(input(('Ingrese la cantidad de créditos que desea matricular: ')))
            pass

        def Calculo_matricula(self):
            self.estrato_estudiante = int(self.estrato_estudiante)
            if self.estrato_estudiante > 1:
                self.valor_matricula = self.numero_creditos * self.valor_credito
                pass
            elif self.estrato_estudiante == 1:
                self.valor_matricula = (self.numero_creditos * self.valor_credito) * 0.5
                pass
            else:
                print('El estrato ingresado no es válido')
                pass
            pass

        def Desprendible_matricula(self):
            self.nombre_estudiante = self.nombre_estudiante.title()
            self.estrato_estudiante = str(self.estrato_estudiante)
            self.valor_matricula = str(self.valor_matricula)
            print('El estudiante ' + self.nombre_estudiante + ' perteneciente al estrato ' + self.estrato_estudiante + ' pagará por matrícula $' + self.valor_matricula)
            pass
        pass

    Matricula = CalculoMatricula()
    Matricula.Datos_estudiante()
    Matricula.Calculo_matricula()
    Matricula.Desprendible_matricula()


if __name__ == "__main__":
    run()
    pass

msvcrt.getch()