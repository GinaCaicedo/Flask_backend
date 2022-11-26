from Modelos import modeloResultado
from Repositorio.InterfaceRepositorio import InterfaceRepositorio


class RepositorioResultado(InterfaceRepositorio[modeloResultado]):
    pass

    # def getlistResultadosCandidato(self,idC):
    #     theQuery={"Candidato.$id": ObjectId(idC)}
    #     return self.query(theQuery)

    # def getmesamayorparticipacion(self):
    #     query1={
    #             "$group": {
    #                 "_id": "$Resultado",
    #                 "max": {
    #                     "$max": "$numero_votos"
    #                 },
    #                 "doc": {
    #                     "$first": "$$ROOT"
    #                 }
    #             }
    #         }
    #     pipeline=  [query1]
    #     return self.queryAggregation(pipeline)



    #
    # def getpartidomayorparticipacion(self):
    #

