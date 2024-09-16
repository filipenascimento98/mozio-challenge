from django.core.exceptions import ObjectDoesNotExist
import logging


class DomainBase:
    def __init__(self, repository):
        self.repository = repository
    
    def create(self, data):
        try:
            ret = self.repository.create(data)
            self.repository.save(ret)
        except Exception as e:
            logging.error(e)
            return {"message": "Não foi possível adicionar o objeto a base de dados.", "status": 400}
        
        return {"message": ret.pk, "status": 201}
    
    def list(self):
        try:
            ret = self.repository.list()
        except ObjectDoesNotExist as e:
            logging.error(e)
            return {"message": "Objeto não encontrado", "status": 404}
        
        return {"message": ret, "status": 200}
    
    def get(self, query_params={}):
        try:
            ret = self.repository.get(query_params=query_params)
        except ObjectDoesNotExist as e:
            logging.error(e)
            return {"message": "Objeto não encontrado", "status": 404}
        
        return {"message": ret, "status": 200}