from typing import List

import pytest

from api.models import Inclinometry, Field, Well, Mer, Rate, FieldCoordinate, WellCase, WellPump, WellPerforation, \
    Horizon, WellHorizon, WellWorkType, WellState
from tests.api.factories import IncFactory, FieldFactory, WellFactory, MerFactory, RateFactory, CoordinateFactory, \
    CaseFactory, PumpFactory, PerforationFactory, HorizonFactory, WellWorkTypeFactory, WellStateFactory, \
    WellHorizonFactory


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
def well_work_type() -> WellWorkType:
    return WellWorkTypeFactory()


@pytest.fixture
def well_state() -> WellState:
    return WellStateFactory()


@pytest.fixture
def mer(well: Well, well_work_type: WellWorkType, well_state: WellState) -> List[Mer]:
    return MerFactory.create_batch(10, well=well, work_type=well_work_type, state=well_state)


@pytest.fixture
def rates(well: Well, well_work_type: WellWorkType) -> List[Rate]:
    return RateFactory.create_batch(10, well=well, work_type=well_work_type)


@pytest.fixture
def horizon(field: Field) -> Horizon:
    return HorizonFactory(field=field)


@pytest.fixture
def well_horizon(horizon: Horizon, well: Well) -> WellHorizon:
    return WellHorizonFactory(well=well, horizon=horizon)


@pytest.fixture
def cases(well: Well) -> List[WellCase]:
    return CaseFactory.create_batch(10, well=well)


@pytest.fixture
def pump(well: Well) -> WellPump:
    return PumpFactory(well=well)


@pytest.fixture
def perforations(well: Well) -> List[WellPerforation]:
    return PerforationFactory.create_batch(10, well=well)
