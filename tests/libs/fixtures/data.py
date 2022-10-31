import pytest

from tests.libs.testdata.students_data import StudentData


@pytest.fixture
def student_data():
    return StudentData().return_data()
