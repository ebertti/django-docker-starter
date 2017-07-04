from addict import addict
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from base.tests.mixin import BaseTestMixin


class TestOferta(BaseTestMixin, TestCase):

    def setUp(self):
        pass

    def test_basico(self):

        ad = addict({'minha_chave': 200})

        self.assertEqual(ad.minha_chave, 200)