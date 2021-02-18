from typing import List

from api.models import Inclinometry


def _delete_old_inc(field_id: int, well_name_list: List[str]) -> None:
    return Inclinometry.objects \
        .filter(well__field_id=field_id, well__name__in=well_name_list) \
        .delete()
