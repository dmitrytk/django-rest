def map_inc(data: dict) -> list:
    keys = ['well', 'md', 'inc', 'azi', ]
    return [data.get(key, None) for key in keys]


def map_mer(data: dict) -> list:
    keys = ['well', 'date', 'status', 'rate', 'production', 'work_days', ]
    return [data.get(key, None) for key in keys]


def map_rate(data: dict) -> list:
    keys = ['well', 'date', 'status', 'rate', 'dynamic_level', 'static_level', 'production', ]
    return [data.get(key, None) for key in keys]


def map_coordinate(data: dict) -> list:
    keys = ['lat', 'lng', 'x', 'y']
    return [data.get(key, None) for key in keys]


def map_zone(data: dict) -> list:
    keys = ['well', 'name', 'top_md', 'bot_md', 'top_tvd', 'bot_tvd', 'h', ]
    return [data.get(key, None) for key in keys]


def map_case(data: dict) -> list:
    keys = ['well', 'name', 'diameter', 'length', 'top_md', 'bot_md', 'cemented', 'cement_top', ]
    return [data.get(key, None) for key in keys]


def map_perforation(data: dict) -> list:
    keys = ['well', 'perforator_type', 'hole_diameter', 'holes_per_meter', 'top_md', 'bot_md']
    return [data.get(key, None) for key in keys]


def map_pump(data: dict) -> list:
    keys = ['well', 'name', 'md', 'rate', 'diameter']
    return [data.get(key, None) for key in keys]


# Map ranged Views
def map_mer_view(data: tuple) -> dict:
    keys = ['well', 'date', 'status', 'rate', 'production', 'work_days']
    return {key: data[index] for index, key in enumerate(keys)}


def map_rates_view(data: tuple) -> dict:
    keys = ['well', 'date', 'status', 'rate', 'dynamic_level', 'static_level', 'pressure']
    return {key: data[index] for index, key in enumerate(keys)}
