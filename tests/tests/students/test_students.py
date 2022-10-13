import pytest
import requests

from assertpy import assert_that, soft_assertions


@pytest.mark.students
class TestStudents:

    def test_01_get_list_of_students_reponse_200(self, generate_token):
        student_list = requests.get("http://127.0.0.1:8080/student/",
                                    headers={
                                        "accept": "application / json",
                                        "Authorization": f"Bearer {generate_token}"
                                    })
        with soft_assertions():
            assert_that(student_list.status_code).is_equal_to(200)
            assert_that(student_list.json()["data"]).is_not_empty()

    def test_02_post_get_delete_flow(self, generate_token, student_data):
        new_student = requests.post("http://127.0.0.1:8080/student/",
                                    headers={
                                        "accept": "application/json",
                                        "Authorization": f"Bearer {generate_token}"
                                    },
                                    json=student_data)
        assert_that(new_student.status_code).is_equal_to(200)
        # TODO: add rest of validations: haders, payload and basic performance sanity
        student_id = new_student.json()["data"][0]["id"]
        get_student = requests.get(f"http://127.0.0.1:8080/student/{student_id}",
                                   headers={
                                       "accept": "application/json",
                                       "Authorization": f"Bearer {generate_token}"
                                   })
        assert_that(get_student.status_code).is_equal_to(200)
        # TODO: assertions with json response body too
        delete_student = requests.delete(f"http://127.0.0.1:8080/student/{student_id}",
                                         headers={
                                             "accept": "application/json",
                                             "Authorization": f"Bearer {generate_token}"
                                         })
        assert_that(delete_student.status_code).is_equal_to(200)
        # TODO: assertions for the rest of teh stuff ;)
        get_not_existing_student = requests.get(f"http://127.0.0.1:8080/student/{student_id}",
                                                headers={
                                                    "accept": "application/json",
                                                    "Authorization": f"Bearer {generate_token}"
                                                })
        assert_that(get_not_existing_student.status_code).is_equal_to(404)