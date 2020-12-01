from django.test import TestCase

from api.models import Field


class TestModels(TestCase):
    fixtures = ['api.json']
    field_name = 'UpperSalym'
    well_name = '99R'

    def test_object_create(self):
        field = Field.objects.get(name=self.field_name)
        well = field.wells.first()
        inc = well.inc.first()
        mer = well.mer_set.first()
        rate = well.rate_set.first()
        self.assertEqual(field.name, self.field_name)
        self.assertEqual(well.pk, 1)
