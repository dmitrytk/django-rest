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
