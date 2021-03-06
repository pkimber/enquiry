# -*- encoding: utf-8 -*-
from django.core.urlresolvers import reverse

from base.tests.test_utils import PermTestCase
from enquiry.tests.scenario import default_scenario_enquiry
from login.tests.scenario import default_scenario_login


class TestViewPerm(PermTestCase):

    def setUp(self):
        default_scenario_login()
        default_scenario_enquiry()

    def test_create(self):
        url = reverse('example.enquiry.create')
        self.assert_any(url)
