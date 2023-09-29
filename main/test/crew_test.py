import pytest

from main.crew.user import User, Jobs
from main.crew.user import conductor_rights


class TestCrew:

    def test_conductor(self):
        jobs = Jobs
        test_user = User('conductor', 'password', 'email')
        assert test_user.add_allowed_role(jobs.conductor)

        assert test_user.set_active_role(jobs.conductor)
        test_user.set_active_rights(jobs.conductor)
        print(test_user.active_rights.__str__())







