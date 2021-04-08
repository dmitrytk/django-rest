from typing import List

import pytest

from api.models import Inclinometry, Field, Well, Mer, Rate, FieldCoordinate, Zone, WellCase, WellPump, WellPerforation
from tests.api.factories import IncFactory, FieldFactory, WellFactory, MerFactory, RateFactory, CoordinateFactory, \
    ZoneFactory, CaseFactory, PumpFactory, PerforationFactory


@pytest.fixture
def field() -> Field:
    return FieldFactory()


@pytest.fixture
def well(field: Field) -> Well:
    return WellFactory(field=field)


@pytest.fixture
def coordinates(field: Field) -> List[FieldCoordinate]:
    return CoordinateFactory.create_batch(10, field=field)


@pytest.fixture
def inc(well: Well) -> List[Inclinometry]:
    return IncFactory.create_batch(10, well=well)


@pytest.fixture
def mer(well: Well) -> List[Mer]:
    return MerFactory.create_batch(10, well=well)


@pytest.fixture
def rates(well: Well) -> List[Rate]:
    return RateFactory.create_batch(10, well=well)


@pytest.fixture
def zones(well: Well) -> List[Zone]:
    return ZoneFactory.create_batch(10, well=well)


@pytest.fixture
def cases(well: Well) -> List[WellCase]:
    return CaseFactory.create_batch(10, well=well)


@pytest.fixture
def pump(well: Well) -> WellPump:
    return PumpFactory(well=well)


@pytest.fixture
def perforations(well: Well) -> List[WellPerforation]:
    return PerforationFactory.create_batch(10, well=well)
