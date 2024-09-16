from api.data_access.base import RepositoryBase
from api.models import ServiceArea


class ServiceAreaRepository(RepositoryBase):
    def __init__(self):
        super().__init__(ServiceArea)