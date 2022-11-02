from dataclasses import asdict, dataclass, field
from time import time

from faker import Faker


@dataclass
class AdminData:

    fullname: str = field(default=Faker("en_US").name())
    email: str = field(default=f"{time()}{Faker('en_US').free_email()}")
    password: str = field(default="9{LBupmwc*jVN^kB")

    def return_data(self):
        return asdict(self)
