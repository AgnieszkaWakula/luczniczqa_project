from dataclasses import asdict, dataclass, field

from faker import Faker


@dataclass
class StudentData:
    f = Faker("en_US")

    fullname: str = field(default=f.name())
    email: str = field(default=f.free_email())
    course_of_study: str = field(default="Physics")
    year: int = field(default=5)
    gpa: str = field(default="2.2")

    def return_data(self):
        return asdict(self)
