const fields = [
  {
    label: 'Id',
    key: 'id',
  },
  {
    label: 'Название',
    key: 'name',
    required: true,
    sortable: true,
  },
  {
    label: 'Тип',
    key: 'type',
  },
  {
    label: 'Местонахождение',
    key: 'location',
  },
];

const wells = [
  {
    label: 'id',
    key: 'id',
  },
  {
    label: 'Номер',
    key: 'well',
    required: true,
    sortable: true,

  },
  {
    label: 'Куст',
    key: 'pad',

  },
  {
    label: 'Тип',
    key: 'type',

  },
  {
    label: 'Состояние',
    key: 'status',

  },
  {
    label: 'Забой',
    key: 'bottom',

  },
  {
    label: 'Альтитуда',
    key: 'alt',
  },
  {
    label: 'X',
    key: 'x',
  },
  {
    label: 'Y',
    key: 'y',
  },
  {
    label: 'Широта',
    key: 'lat',
  },
  {
    label: 'Долгота',
    key: 'lng',
  },
];

const inclinometry = [
  {
    label: 'Скважина',
    key: 'well',
  },
  {
    label: 'Глубина',
    key: 'md',
    required: true,
  },
  {
    label: 'Угол',
    key: 'inc',
  },
  {
    label: 'Азимут',
    key: 'azi',
  },
];

const mer = [
  {
    label: 'Скважина',
    key: 'well',
  },
  {
    label: 'Дата',
    key: 'date',
    required: true,
  },
  {
    label: 'Состояние',
    key: 'status',
  },
  {
    label: 'Дебит',
    key: 'rate',
  },
  {
    label: 'Добыча',
    key: 'production',
  },
  {
    label: 'Суток работы',
    key: 'work_days',
  },
];

const rates = [
  {
    label: 'Скважина',
    key: 'well',
  },
  {
    label: 'Дата',
    key: 'date',
    required: true,
  },
  {
    label: 'Дебит',
    key: 'rate',
  },
  {
    label: 'Динамический уровень',
    key: 'dynamic',
  },
  {
    label: 'Статический уровень',
    key: 'static',
  },
  {
    label: 'Давление',
    key: 'pressure',
  },
];

const zones = [
  {
    label: 'Скважина',
    key: 'well',
  },
  {
    label: 'Название',
    key: 'name',
    required: true,
  },
  {
    label: 'Кровля',
    key: 'top_md',
  },
  {
    label: 'Подошва',
    key: 'bot_md',
  },
  {
    label: 'Кровля АО',
    key: 'top_tvd',
  },
  {
    label: 'Подошва АО',
    key: 'bot_tvd',
  },
  {
    label: 'Толщина',
    key: 'h',
  },
];

const tables = {
  fields,
  wells,
  inclinometry,
  mer,
  rates,
  zones,
};

export default tables;
