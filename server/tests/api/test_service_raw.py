import datetime

import pytest

from api import queries
from api.services.raw_sql_service import get_raw_view
from api.utils import mappers
from tests.api.factories import MerFactory, RateFactory

pytestmark = pytest.mark.django_db


class TestBatchService:

    def test_mer_view(self, well):
        MerFactory(well=well, date=datetime.date(2020, 1, 1))
        MerFactory(well=well, date=datetime.date(2020, 5, 1))
        data = get_raw_view(queries.MER_RANGE, [well.id], mappers.map_mer_view)
        assert len(data) == 5

    def test_rates_view(self, well):
        RateFactory(well=well, date=datetime.date(2020, 1, 1))
        RateFactory(well=well, date=datetime.date(2020, 1, 20))
        data = get_raw_view(queries.RATES_RANGE, [well.id], mappers.map_rates_view)
        assert len(data) == 20
