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
    (well_id, date, rate, dynamic_level, static_level, pressure) VALUES
    ((SELECT id FROM wells w WHERE w.field_id=%s and w.name=%s),%s,%s,%s,%s,%s)
"""
