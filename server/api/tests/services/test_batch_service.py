from django.test import TestCase

from api.models import Inclinometry, FieldCoordinate, Well, Mer, Rate, Zone, WellPump, WellCase, WellPerforation
from api.services.batch_service import _delete_old_inc, _delete_old_coordinates, _create_new_wells, load_wells, \
    load_inclinometry, load_mer, load_rates, load_zones, load_coordinates, load_pumps, load_cases, load_perforations
from api.tests.populate import populate_db


class TestBatchService(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.field_name, cls.well_name = populate_db()

    def test__delete_old_inc(self):
        _delete_old_inc(1, {self.well_name})
        self.assertEqual(Inclinometry.objects.count(), 0)  # 2 - 2 = 0

    def test__delete_old_coordinates(self):
        self.assertEqual(FieldCoordinate.objects.count(), 2)
        _delete_old_coordinates(1)
        self.assertEqual(FieldCoordinate.objects.count(), 0)  # 2 - 2 = 0

    def test__create_new_wells(self):
        _create_new_wells(1, {self.well_name, '1P', '999'})  # first well will be skipped
        self.assertEqual(Well.objects.count(), 3)  # 1 + 2 = 3

    def test_load_wells(self):
        data = {
            'field_id': 1,
            'rows': [
                {'name': self.well_name, 'bottom': 3000},
                {'name': '1P'},
            ]
        }
        load_wells(data)
        self.assertEqual(Well.objects.count(), 2)  # 1 + 1 = 2  old well will be updated
        self.assertEqual(Well.objects.filter(name=self.well_name).first().bottom, 3000)
        self.assertEqual(Well.objects.last().name, '1P')

    def test_load_inclinometry(self):
        data = {
            'field_id': 1,
            'rows': [
                {'well': self.well_name, 'md': 10, 'inc': None, 'azi': 78.23},
                {'well': self.well_name, 'md': 20},
                {'well': '1P', 'md': 1},  # add new well
            ]
        }
        load_inclinometry(data)
        self.assertEqual(Inclinometry.objects.count(), 3)  # old inclinometry will be deleted 0 + 3 = 3

    def test_load_mer(self):
        data = {
            'field_id': 1,
            'rows': [
                {'well': self.well_name, 'date': '01.01.2000'},
                {'well': self.well_name, 'date': '01.01.2000'},  # duplicate date will be overwritten
                {'well': '1P', 'date': '01.01.2000'},  # add new well
            ]
        }
        load_mer(data)
        self.assertEqual(Mer.objects.all().count(), 4)  # 2 + 1 + 1 = 4

    def test_load_rates(self):
        data = {
            'field_id': 1,
            'rows': [
                {'well': self.well_name, 'date': '01.01.2000', 'rate': 256.78, 'status': 'work'},
                {'well': self.well_name, 'date': '01.01.2000'},
                {'well': '1P', 'date': '01.01.2000'},  # add new well
            ]
        }
        load_rates(data)
        self.assertEqual(Rate.objects.all().count(), 5)  # 2 + 2 + 1 = 5

    def test_load_zones(self):
        data = {
            'field_id': 1,
            'rows': [
                {'well': self.well_name, 'name': 'pk1', 'top_md': 1500.25},
                {'well': self.well_name, 'name': 'pk2', 'top_md': 1550.26},
                {'well': '1P', 'name': 'uvat', 'top_md': 860.25},  # add new well
            ]
        }
        load_zones(data)
        self.assertEqual(Zone.objects.all().count(), 5)  # 2 + 2 + 1 = 5

    def test_load_coordinates(self):
        data = {
            'field_id': 1,
            'rows': [
                {'lat': 60.23, 'lng': 50.28},
                {'lat': 60.28, 'lng': 50.29},
            ]
        }
        load_coordinates(data)
        self.assertEqual(FieldCoordinate.objects.all().count(), 2)  # old coordinates will be deleted

    def test_load_pumps(self):
        data = {
            'field_id': 1,
            'rows': [
                {'well': self.well_name, 'name': '1100WR', 'md': 1200},
                {'well': '1P', 'name': '800Z'},  # add new well
            ]
        }
        load_pumps(data)
        self.assertEqual(WellPump.objects.all().count(), 2)  # 1 + 1 = 2 old pump will be overwritten
        self.assertEqual(WellPump.objects.first().md, 1200)

    def test_load_cases(self):
        data = {
            'field_id': 1,
            'rows': [
                {'well': self.well_name, 'name': 'кондуктор', 'diameter': 324.0, 'top_md': 0, 'bot_md': 1300},
                {'well': '1P', 'name': 'направление', 'diameter': 425.0, },  # add new well
            ]
        }
        response = load_cases(data)
        self.assertEqual(WellCase.objects.count(), 3)  # 2 + 1 = 3 old case will be overwritten

    def test_load_perforations(self):
        data = {
            'field_id': 1,
            'rows': [
                {'well': self.well_name, 'perforator_type': 'ЗПКМ', 'top_md': 1250.0, 'bot_md': 1260.0},
                {'well': '1P', 'perforator_type': 'UltraJet', 'top_md': 1250.0, 'bot_md': 1260.0},  # add new well
            ]
        }
        response = load_perforations(data)
        print(response)
        self.assertEqual(WellPerforation.objects.count(), 4)  # 2 + 2 = 4
