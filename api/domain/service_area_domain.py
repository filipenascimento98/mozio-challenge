from api.domain.base import DomainBase
from api.data_access.service_area_repository import ServiceAreaRepository


class ServiceAreaDomain(DomainBase):
    def __init__(self):
        super().__init__(ServiceAreaRepository())