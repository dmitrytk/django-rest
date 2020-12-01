def map_inc(data: dict) -> list:
    keys = ['well', 'md', 'inc', 'azi', ]
    return [data.get(key, None) for key in keys]


def map_mer(data: dict) -> list:
    keys = ['well', 'date', 'status', 'rate', 'production', 'work_days', ]
    return [data.get(key, None) for key in keys]


def map_rate(data: dict) -> list:
    keys = ['well', 'date', 'rate', 'dynamic_level', 'static_level', 'production', ]
    return [data.get(key, None) for key in keys]
