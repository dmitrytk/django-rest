# BATCH LOAD QUERIES
INCLINOMETRY_LOAD = """INSERT INTO inclinometry
    (well_id, md, inc, azi) VALUES
    ((SELECT id FROM wells w WHERE w.field_id=%s AND w.name=%s),%s,%s,%s)
"""

MER_LOAD = """INSERT INTO mer
     (well_id, date, production, work_hours, work_type_id, state_id) VALUES
     (
         (SELECT id FROM wells w WHERE w.field_id=%s AND w.name=%s),%s,%s,%s,
         (SELECT id FROM well_work_types WHERE value_full = %s),
         (SELECT id FROM well_states WHERE value_full = %s)
     )
     ON CONFLICT (well_id, DATE)
     DO UPDATE SET production = EXCLUDED.production,
     work_hours = EXCLUDED.work_hours,
     work_type_id = EXCLUDED.work_type_id,
     state_id = EXCLUDED.state_id
"""

RATE_LOAD = """INSERT INTO rates
    (well_id, date, rate, dynamic_level, static_level, pressure, work_type_id) VALUES
    (
        (SELECT id FROM wells w WHERE w.field_id=%s AND w.name=%s),
        %s,%s,%s,%s,%s,
        (SELECT id FROM well_work_types WHERE value_full = %s)
    )
"""

HORIZON_LOAD = """WITH field_id_constant AS (VALUES (%s))
INSERT INTO well_horizons
    (well_id, horizon_id, top_md, bot_md, top_tvdss, bot_tvdss) VALUES
    (
        (SELECT id FROM wells w WHERE w.field_id=(TABLE field_id_constant) AND w.name=%s),
        (SELECT id FROM horizons h WHERE h.field_id=(TABLE field_id_constant) AND LOWER(h.value_full)=LOWER(%s)),
        %s,%s,%s,%s
    )
    ON CONFLICT (well_id, horizon_id)
    DO UPDATE SET top_md = EXCLUDED.top_md,
    bot_md = EXCLUDED.bot_md,
    top_tvdss = EXCLUDED.top_tvdss,
    bot_tvdss = EXCLUDED.bot_tvdss
"""

CASE_LOAD = """INSERT INTO cases
    (well_id, name, diameter, length, top_md, bot_md, cemented, cement_top) VALUES
    ((SELECT id FROM wells w WHERE w.field_id=%s AND w.name=%s),%s,%s,%s,%s,%s,%s,%s)
    ON CONFLICT (well_id, NAME)
    DO UPDATE SET diameter = EXCLUDED.diameter,
    LENGTH = EXCLUDED.length,
    top_md = EXCLUDED.top_md,
    bot_md = EXCLUDED.bot_md,
    cemented = EXCLUDED.cemented,
    cement_top = EXCLUDED.cement_top
"""

PERFORATION_LOAD = """INSERT INTO perforations
    (well_id, perforator_type, hole_diameter, holes_per_meter, top_md, bot_md) VALUES
    ((SELECT id FROM wells w WHERE w.field_id=%s AND w.name=%s),%s,%s,%s,%s,%s)
"""

PUMP_LOAD = """INSERT INTO pumps
    (well_id, name, md, rate, diameter) VALUES
    ((SELECT id FROM wells w WHERE w.field_id=%s AND w.name=%s),%s,%s,%s,%s)
    ON CONFLICT (well_id)
    DO UPDATE SET name = EXCLUDED.name,
    md = EXCLUDED.md,
    rate = EXCLUDED.rate,
    diameter = EXCLUDED.diameter
"""

COORDINATE_LOAD = """INSERT INTO field_coordinates
    (field_id, lat, lng, x, y) VALUES
    (%s,%s,%s,%s,%s)
"""

# VIEWS QUERIES
RATES_RANGE = """WITH r AS (SELECT * FROM rates r WHERE r.well_id = %s)
SELECT
    TO_CHAR(rng.date, 'dd.mm.yyyy') AS DATE,
    wrk.value_full AS work_type,
    r.rate,
    r.dynamic_level,
    r.static_level,
    r.pressure
FROM r
RIGHT JOIN
(SELECT date_trunc('day', dd):: DATE AS DATE
FROM GENERATE_SERIES(
    (SELECT MIN(DATE) FROM r),
    (SELECT MAX(DATE) FROM r),
    '1 day'::INTERVAL) dd) AS rng
ON rng.date = r.date
LEFT JOIN well_work_types wrk ON wrk.id = r.work_type_id
"""

MER_RANGE = """WITH m AS (SELECT * FROM mer m WHERE m.well_id = %s)
SELECT
    TO_CHAR(rng.date, 'dd.mm.yyyy') AS DATE,
    wrk.value_full AS work_type,
    st.value_full AS STATE,
    m.production,
    m.work_hours
FROM m
RIGHT JOIN
(SELECT date_trunc('day', dd):: DATE AS DATE
FROM GENERATE_SERIES(
    (SELECT MIN(m.date) FROM m),
    (SELECT MAX(m.date) FROM m),
    '1 month'::INTERVAL) dd) AS rng
ON rng.date = m.date
LEFT JOIN well_work_types wrk ON wrk.id = m.work_type_id
LEFT JOIN well_states st ON st.id = m.state_id
"""
