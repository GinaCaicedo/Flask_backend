from Modelos.modeloCandidato import ModeloCandidato
from Modelos.modeloPartido import ModeloPartido
from Repositorio.RepositorioCandidato import RepositorioCandidato
from Repositorio.RepositorioPartido import RepositorioPartido


class ControladorCandidato():

    def __init__(self):

        print("Creando Controlador Candidato")
        self.repositorioCandidato = RepositorioCandidato()
        self.repositorioPartido = RepositorioPartido()

    def createCandidato(self, infoCandidato):
        print("Creando el candidato....")
        nuevocandidato = ModeloCandidato(infoCandidato)
        print("candidato a crear en base de datos: ", nuevocandidato.__dict__)
        return self.repositorioCandidato.save(nuevocandidato)


    def showidCandidato(self, id):
        print("Mostrando un candidato con id ", id)
        candidato = ModeloCandidato(self.repositorioCandidato.findById(id))
        return candidato.__dict__

    def showallCandidato(self):
        print("Mostrando las candidato de la base de datos ")
        return self.repositorioCandidato.findAll()


    def updateCandidato(self, id, infoCandidato):
        candidatoactual = ModeloCandidato(self.repositorioCandidato.findById(id))
        print("Actualizando CANDIDATO con id ", candidatoactual)
        candidatoactual.cedula = infoCandidato["cedula"]
        candidatoactual.numero_resolucion = infoCandidato["numero_resolucion"]
        candidatoactual.nombre = infoCandidato["nombre"]
        candidatoactual.apellido = infoCandidato["apellido"]
        return self.repositorioCandidato.save(candidatoactual)

    def deleteCandidato(self, id):
        print("Eliminando Candidato con id ", id)

        return self.repositorioCandidato.delete(id)

# asigna aun candidato partido
    def asigPartido(self,idC, idP):
        candidatoactual = ModeloCandidato(self.repositorioCandidato.findById(idC))
        partidoactual = ModeloPartido(self.repositorioPartido.findById(idP))
        candidatoactual.partido = partidoactual
        print("candidato a crear en base de datos: ", candidatoactual.__dict__)
        return self.repositorioCandidato.save(candidatoactual)
