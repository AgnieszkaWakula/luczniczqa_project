import pytest

from tests.libs.testdata.admin_data import AdminData
from tests.libs.testdata.students_data import StudentData


@pytest.fixture
def admin_data():
    return AdminData().return_data()


@pytest.fixture
def student_data():
    return StudentData().return_data()
