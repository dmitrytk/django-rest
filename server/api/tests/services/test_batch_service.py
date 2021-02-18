from django.test import TestCase

from api.models import Inclinometry, Mer, Rate, Well, Zone, FieldCoordinate
from api.services.batch_service import load_inclinometry, load_mer, load_rates, _create_new_wells, _delete_old_inc, \
    load_zones, _delete_old_coordinates, load_coordinates, load_wells


class TestBatchService(TestCase):
    fixtures = ['api.json']
    well_name = '99R'

    def test_delete_old_inc(self):
        _delete_old_inc(1, [self.well_name, '1P'])
        self.assertEqual(Inclinometry.objects.count(), 0)  # 2 - 2 = 0

    def test_delete_old_coordinates(self):
        _delete_old_coordinates(1)
        self.assertEqual(FieldCoordinate.objects.count(), 0)  # 3 - 3 = 0

    def test_create_new_wells(self):
        _create_new_wells(1, [self.well_name, '1P', '999'])
        self.assertEqual(Well.objects.count(), 5)  # 3 + 2 = 5

    def test_load_wells(self):
        data = {
            'field_id': 1,
            'rows': [
                {'name': self.well_name, 'bottom': 3000},
                {'name': '1P'},
            ]
        }
        load_wells(data)
        self.assertEqual(Well.objects.count(), 4)  # 3 + 1 = 4  old wells will be updated
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
        self.assertEqual(Inclinometry.objects.count(), 3)  # old inclinometry will be deleted 0 + 3 = 2

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
        self.assertEqual(FieldCoordinate.objects.all().count(), 2)
