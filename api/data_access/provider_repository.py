from api.data_access.base import RepositoryBase
from api.models import Provider


class ProviderRepository(RepositoryBase):
    def __init__(self):
        super().__init__(Provider)