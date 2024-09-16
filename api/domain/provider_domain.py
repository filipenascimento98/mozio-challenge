from api.domain.base import DomainBase
from api.data_access.provider_repository import ProviderRepository


class ProviderDomain(DomainBase):
    def __init__(self):
        super().__init__(ProviderRepository())