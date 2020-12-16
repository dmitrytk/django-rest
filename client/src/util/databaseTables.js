const fields = [
  {
    label: 'Id',
    key: 'id',
    regex: /(id|)/i,
  },
  {
    label: 'Название',
    key: 'name',
    required: true,
    sortable: true,
    regex: /(name|)/i,
  },
  {
    label: 'Тип',
    key: 'type',
    regex: /(type|)/i,
  },
  {
    label: 'Местонахождение',
    key: 'location',
    regex: /(loc|)/i,
  },
];

const wells = [
  {
    label: 'id',
    key: 'id',
    regex: /(id|ид)/i,
  },
  {
    label: 'Номер',
    key: 'well',
    required: true,
    sortable: true,
    regex: /(well|номер|скв)/i,

  },
  {
    label: 'Куст',
    key: 'pad',
    regex: /(pad|куст)/i,

  },
  {
    label: 'Тип',
    key: 'type',
    regex: /(type|тип|назна)/i,

  },
  {
    label: 'Состояние',
    key: 'status',
    regex: /(stat|сост|стат)/i,

  },
  {
    label: 'Забой',
    key: 'bottom',
    regex: /(bott|md|забой|глуб)/i,

  },
  {
    label: 'Альтитуда',
    key: 'alt',
    regex: /(alt|альт)/i,
  },
  {
    label: 'X',
    key: 'x',
    regex: /(^x|^х)/i,
  },
  {
    label: 'Y',
    key: 'y',
    regex: /(^y|^у)/i,
  },
  {
    label: 'Широта',
    key: 'lat',
    regex: /(lat|широ)/i,
  },
  {
    label: 'Долгота',
    key: 'lng',
    regex: /(lng|long|долг)/i,
  },
];

const inclinometry = [
  {
    label: 'Скважина',
    key: 'well',
    regex: /(well|)/i,
  },
  {
    label: 'Глубина',
    key: 'md',
    required: true,
    regex: /(md|depth|)/i,
  },
  {
    label: 'Угол',
    key: 'inc',
    regex: /(inc|)/i,
  },
  {
    label: 'Азимут',
    key: 'azi',
    regex: /(azi|)/i,
  },
];

const mer = [
  {
    label: 'Скважина',
    key: 'well',
    regex: /(well|)/i,
  },
  {
    label: 'Дата',
    key: 'date',
    required: true,
    regex: /(date|)/i,
  },
  {
    label: 'Состояние',
    key: 'status',
    regex: /(stat|)/i,
  },
  {
    label: 'Дебит',
    key: 'rate',
    regex: /(rate|)/i,
  },
  {
    label: 'Добыча',
    key: 'production',
    regex: /(prod|)/i,
  },
  {
    label: 'Суток работы',
    key: 'work_days',
    regex: /(days|work|)/i,
  },
];

const rates = [
  {
    label: 'Скважина',
    key: 'well',
    regex: /(well|)/i,
  },
  {
    label: 'Дата',
    key: 'date',
    required: true,
    regex: /(date|)/i,
  },
  {
    label: 'Дебит',
    key: 'rate',
    regex: /(rate|)/i,
  },
  {
    label: 'Динамический уровень',
    key: 'dynamic',
    regex: /(dynam|)/i,
  },
  {
    label: 'Статический уровень',
    key: 'static',
    regex: /(stat|)/i,
  },
  {
    label: 'Давление',
    key: 'pressure',
    regex: /(press|^p$|)/i,
  },
];

const zones = [
  {
    label: 'Скважина',
    key: 'well',
    regex: /(well|)/i,
  },
  {
    label: 'Название',
    key: 'name',
    required: true,
    regex: /(name|zone|plast)/i,
  },
  {
    label: 'Кровля',
    key: 'top_md',
    regex: /(top|)/i,
  },
  {
    label: 'Подошва',
    key: 'bot_md',
    regex: /(bot|)/i,
  },
  {
    label: 'Кровля АО',
    key: 'top_tvd',
    regex: /(toptvd|top_tvd)/i,
  },
  {
    label: 'Подошва АО',
    key: 'bot_tvd',
    regex: /(bottvd|bot_tvd|)/i,
  },
  {
    label: 'Толщина',
    key: 'h',
    regex: /(^h|)/i,
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
