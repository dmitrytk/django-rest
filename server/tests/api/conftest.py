import pytest

from api.models import Inclinometry, Field, Well, Mer, Rate, FieldCoordinate, Zone, WellCase, WellPump, WellPerforation
from tests.api.factories import IncFactory, FieldFactory, WellFactory, MerFactory, RateFactory, CoordinateFactory, \
    ZoneFactory, CaseFactory, PumpFactory, PerforationFactory


@pytest.fixture
def field() -> Field:
    return FieldFactory()


@pytest.fixture
def well(field) -> Well:
    return WellFactory(field=field)


@pytest.fixture
def coordinates(field) -> FieldCoordinate:
    return CoordinateFactory.create_batch(10, field=field)


@pytest.fixture
def inc(well) -> Inclinometry:
    return IncFactory.create_batch(10, well=well)


@pytest.fixture
def mer(well) -> Mer:
    return MerFactory.create_batch(10, well=well)


@pytest.fixture
def rates(well) -> Rate:
    return RateFactory.create_batch(10, well=well)


@pytest.fixture
def zones(well) -> Zone:
    return ZoneFactory.create_batch(10, well=well)


@pytest.fixture
def cases(well) -> WellCase:
    return CaseFactory.create_batch(10, well=well)


@pytest.fixture
def pump(well) -> WellPump:
    return PumpFactory(well=well)


@pytest.fixture
def perforations(well) -> WellPerforation:
    return PerforationFactory.create_batch(10, well=well)
