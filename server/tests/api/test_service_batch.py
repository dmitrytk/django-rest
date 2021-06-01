import pytest

from api.models import Inclinometry, FieldCoordinate, Well, Field, Mer, Rate, WellHorizon, WellPump, WellCase, \
    WellPerforation
from api.services.batch_service import _delete_old_inc, _delete_old_coordinates, _create_new_wells, load_wells, \
    load_inclinometry, load_mer, load_rates, load_horizons, load_coordinates, load_pumps, load_cases, load_perforations

pytestmark = pytest.mark.django_db


class TestBatchService:

    def test__delete_old_inc(self, well, inc):
        _delete_old_inc(well.field.id, {well.name})
        assert Inclinometry.objects.count() == 0

    def test__delete_old_coordinates(self, field, coordinates):
        assert FieldCoordinate.objects.count() == 10
        _delete_old_coordinates(field.id)
        assert FieldCoordinate.objects.count() == 0

    def test__create_new_wells(self, well):
        _create_new_wells(well.field.id, {well.name, '1P', '999'})
        print(Well.objects.all())
        print(Field.objects.all())
        assert Well.objects.count() == 3

    def test_load_wells(self, field, well):
        data = {
            'field_id': field.id,
            'rows': [
                {'name': well.name, 'bottom': 3000},
                {'name': '1P'},
            ]
        }
        load_wells(data)
        assert Well.objects.count() == 2
        assert Well.objects.filter(name=well.name).first().bottom == 3000
        assert Well.objects.last().name == '1P'

    def test_load_inclinometry(self, well, inc):
        data = {
            'field_id': well.field.id,
            'rows': [
                {'well': well.name, 'md': 10, 'inc': None, 'azi': 78.23},
                {'well': well.name, 'md': 20},
                {'well': '1P', 'md': 1},  # add new well
            ]
        }
        load_inclinometry(data)
        assert Inclinometry.objects.count() == 3

    def test_load_mer(self, well, well_work_type, well_state, mer):
        print(well_state.value_full)
        print(well_work_type.value_full)
        data = {
            'field_id': well.field.id,
            'rows': [
                {'well': well.name, 'date': '01.01.2000', 'state': well_state.value_full,
                 'work_type': well_work_type.value_full},
                {'well': well.name, 'date': '01.01.2000', 'state': well_state.value_full,
                 'work_type': well_work_type.value_full},  # duplicate date will be overwritten
                {'well': '1P', 'date': '01.01.2000', 'state': well_state.value_full,
                 'work_type': well_work_type.value_full},  # add new well
            ]
        }
        load_mer(data)
        assert Mer.objects.all().count() == 12  # 10 + 1 + 1 = 12

    def test_load_rates(self, well, well_work_type, rates):
        data = {
            'field_id': well.field.id,
            'rows': [
                {'well': well.name, 'date': '01.01.2000', 'rate': 256.78, 'work_type': well_work_type.value_full},
                {'well': well.name, 'date': '01.01.2000'},
                {'well': '1P', 'date': '01.01.2000'},  # add new well
            ]
        }
        load_rates(data)
        assert Rate.objects.all().count() == 13  # 10 + 2 + 1 = 13

    def test_load_horizons(self, well, horizon, well_horizon):
        data = {
            'field_id': well.field.id,
            'rows': [
                # duplicate horizon will be overwritten
                {'well': well.name, 'horizon': horizon.value_full, 'top_md': 1500.25},
                {'well': '1P', 'horizon': horizon.value_full, 'top_md': 860.25},  # add new well
            ]
        }
        load_horizons(data)
        assert WellHorizon.objects.all().count() == 2  # 1 + 1 = 2

    def test_load_coordinates(self, field, coordinates):
        data = {
            'field_id': field.id,
            'rows': [
                {'lat': 60.23, 'lng': 50.28},
                {'lat': 60.28, 'lng': 50.29},
            ]
        }
        load_coordinates(data)
        assert FieldCoordinate.objects.all().count() == 2  # old coordinates will be deleted

    def test_load_pumps(self, well, pump):
        data = {
            'field_id': well.field.id,
            'rows': [
                {'well': well.name, 'name': '11000Z', 'md': 1200},
                {'well': '1P', 'name': '800Z'},  # add new well
            ]
        }
        load_pumps(data)
        assert WellPump.objects.all().count() == 2  # 1 + 1 = 2  old pump will be overwritten
        assert WellPump.objects.first().md == 1200

    def test_load_cases(self, well, cases):
        data = {
            'field_id': well.field.id,
            'rows': [
                {'well': well.name, 'name': cases[0].name, 'diameter': 324.0, 'top_md': 0, 'bot_md': 1300},
                {'well': '1P', 'name': 'направление', 'diameter': 425.0, },  # add new well
            ]
        }
        load_cases(data)
        assert WellCase.objects.count() == 11  # 10 + 1 = 11 old case will be overwritten

    def test_load_perforations(self, well, perforations):
        data = {
            'field_id': well.field.id,
            'rows': [
                {'well': well.name, 'perforator_type': 'ЗПКМ', 'top_md': 1250.0, 'bot_md': 1260.0},
                {'well': '1P', 'perforator_type': 'UltraJet', 'top_md': 1250.0, 'bot_md': 1260.0},  # add new well
            ]
        }
        load_perforations(data)
        assert WellPerforation.objects.count() == 12  # 10 + 2 = 12
