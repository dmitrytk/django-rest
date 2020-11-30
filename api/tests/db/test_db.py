from django.db import IntegrityError
from django.test import TestCase

from api.models import Field, Well, Inclinometry, Mer, Rate


class TestDatabase(TestCase):
    fixtures = ['api.json']
    field_name = 'UpperSalym'
    well_name = '99R'
    md = 10
    date = '2020-01-01'
    rate = 756.08

    def setUp(self):
        # Create objects
        inc = Inclinometry.objects.create(well_id=1, md=self.md)
        mer = Mer.objects.create(well_id=1, date=self.date, rate=self.rate)
        rate = Rate.objects.create(well_id=1, date=self.date, rate=self.rate)

    def test_object_create(self):
        field = Field.objects.get(name=self.field_name)
        well = field.wells.first()
        inc = well.inc.first()
        mer = well.mer_set.first()
        rate = well.rate_set.first()
        self.assertEqual(field.name, self.field_name)
        self.assertEqual(well.pk, 1)
        self.assertAlmostEqual(float(inc.md), self.md)
        self.assertAlmostEqual(float(mer.rate), self.rate)
        self.assertAlmostEqual(float(rate.rate), self.rate)

    def test_field_name_unique_constraint(self):
        field = Field.objects.get(name=self.field_name)
        self.assertRaises(IntegrityError, Field.objects.create, name=field.name)

    def test_well_name_unique_constraint(self):
        field = Field.objects.get(name=self.field_name)
        self.assertRaises(IntegrityError, Well.objects.create,
                          field=field, name=self.well_name, )

    def test_inc_required_fields(self):
        well = Well.objects.get(name=self.well_name)
        self.assertRaises(IntegrityError, Inclinometry.objects.create,
                          well=well, inc=10.25)

    def test_mer_required_fields(self):
        well = Well.objects.get(name=self.well_name)
        self.assertRaises(IntegrityError, Mer.objects.create,
                          well=well, rate=10.25)

    def test_rate_required_fields(self):
        well = Well.objects.get(name=self.well_name)
        self.assertRaises(IntegrityError, Rate.objects.create,
                          well=well, rate=10.25)
