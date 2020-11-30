from typing import Dict


def validate_batch_data(data: Dict) -> bool:
    """Validate request data for batch load"""
    return 'field_id' in data \
           and isinstance(data.get('data', None), list)
