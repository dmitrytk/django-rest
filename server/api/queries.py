INCLINOMETRY_LOAD = """INSERT INTO inclinometry
    (well_id, md, inc, azi) VALUES
    ((SELECT id FROM wells w WHERE w.field_id=%s and w.name=%s),%s,%s,%s)
"""

MER_LOAD = """INSERT INTO mer
     (well_id, date, status, rate, production, work_days) VALUES
     ((SELECT id FROM wells w WHERE w.field_id=%s and w.name=%s),%s,%s,%s,%s,%s)
     ON CONFLICT (well_id, date)
     DO UPDATE SET status = EXCLUDED.status,
     rate = EXCLUDED.rate,
     production = EXCLUDED.production,
     work_days = EXCLUDED.work_days
"""

RATE_LOAD = """INSERT INTO rates
    (well_id, date, status, rate, dynamic_level, static_level, pressure) VALUES
    ((SELECT id FROM wells w WHERE w.field_id=%s and w.name=%s),%s,%s,%s,%s,%s,%s)
"""

ZONE_LOAD = """INSERT INTO zones
    (well_id, name, top_md, bot_md, top_tvd, bot_tvd, h) VALUES
    ((SELECT id FROM wells w WHERE w.field_id=%s and w.name=%s),%s,%s,%s,%s,%s,%s)
    ON CONFLICT (well_id, name)
    DO UPDATE SET top_md = EXCLUDED.top_md,
    bot_md = EXCLUDED.bot_md,
    top_tvd = EXCLUDED.top_tvd,
    bot_tvd = EXCLUDED.bot_tvd,
    h = EXCLUDED.h
"""

COORDINATE_LOAD = """INSERT INTO field_coordinates
    (field_id, lat, lng, x, y) VALUES
    (%s,%s,%s,%s,%s)
"""

RATES_RANGE = """WITH r AS (SELECT * FROM rates r WHERE r.well_id = %s)
SELECT
    w.name AS well,
    TO_CHAR(rng.date, 'dd.mm.yyyy') AS date,
    r.status,
    r.rate,
    r.dynamic_level,
    r.static_level,
    r.pressure
FROM r
RIGHT JOIN
(SELECT date_trunc('day', dd):: DATE AS date
FROM GENERATE_SERIES(
    (SELECT min(DATE) FROM r),
    (SELECT MAX(date) FROM r),
    '1 day'::INTERVAL) dd) AS rng
ON rng.date = r.date
JOIN wells w ON w.id = r.well_id
"""

MER_RANGE = """WITH m AS (SELECT * FROM mer m WHERE m.well_id = %s)
SELECT
    w.name AS well,
    TO_CHAR(rng.date, 'dd.mm.yyyy') AS date,
    m.status,
    m.rate,
    m.production,
    m.work_days
FROM m
RIGHT JOIN
(SELECT date_trunc('day', dd):: DATE AS date
FROM GENERATE_SERIES(
    (SELECT min(DATE) FROM m),
    (SELECT MAX(date) FROM m),
    '1 month'::INTERVAL) dd) AS rng
ON rng.date = m.date
JOIN wells w ON w.id = m.well_id"""
