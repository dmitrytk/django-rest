def map_inc(data: dict) -> list:
    keys = ['well', 'md', 'inc', 'azi', ]
    return [data.get(key, None) for key in keys]


def map_mer(data: dict) -> list:
    keys = ['well', 'date', 'status', 'rate', 'production', 'work_days', ]
    return [data.get(key, None) for key in keys]


def map_rate(data: dict) -> list:
    keys = ['well', 'date', 'status', 'rate', 'dynamic_level', 'static_level', 'production', ]
    return [data.get(key, None) for key in keys]


def map_zone(data: dict) -> list:
    keys = ['well', 'name', 'top_md', 'bot_md', 'top_tvd', 'bot_tvd', 'h', ]
    return [data.get(key, None) for key in keys]


def map_coordinate(data: dict) -> list:
    keys = ['lat', 'lng', 'x', 'y']
    return [data.get(key, None) for key in keys]
