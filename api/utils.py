def inc_to_tuple(data):
    return (
        data.get('well'),
        data.get('md'),
        data.get('azi', None),
        data.get('inc', None),
    )
