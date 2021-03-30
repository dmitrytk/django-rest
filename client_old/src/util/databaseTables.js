const fields = [
  {
    label: 'Id',
    key: 'id',
    regex: /(id|иден)/i,
  },
  {
    label: 'Название',
    key: 'name',
    required: true,
    sortable: true,
    regex: /(name|назавние)/i,
  },
  {
    label: 'Тип',
    key: 'type',
    regex: /(type|тип)/i,
  },
  {
    label: 'Местонахождение',
    key: 'location',
    regex: /(loc|распол|местона)/i,
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
    key: 'name',
    required: true,
    sortable: true,
    regex: /(well|name|номер|скв)/i,

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
    regex: /(lat|шир)/i,
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
    required: true,
    regex: /(well|скв)/i,
  },
  {
    label: 'Глубина',
    key: 'md',
    required: true,
    regex: /(md|depth|глуб)/i,
  },
  {
    label: 'Угол',
    key: 'inc',
    regex: /(inc|угол)/i,
  },
  {
    label: 'Азимут',
    key: 'azi',
    regex: /(azi|азим)/i,
  },
];

const mer = [
  {
    label: 'Скважина',
    key: 'well',
    required: true,
    regex: /(well|скв)/i,
  },
  {
    label: 'Дата',
    key: 'date',
    required: true,
    regex: /(date|дата)/i,
  },
  {
    label: 'Состояние',
    key: 'status',
    regex: /(stat|сост|стат)/i,
  },
  {
    label: 'Дебит',
    key: 'rate',
    regex: /(rate|дебит|закач)/i,
  },
  {
    label: 'Добыча',
    key: 'production',
    regex: /(prod|добыча)/i,
  },
  {
    label: 'Суток работы',
    key: 'work_days',
    regex: /(days|work|суток|дней)/i,
  },
];

const rates = [
  {
    label: 'Скважина',
    key: 'well',
    required: true,
    regex: /(well|скв)/i,
  },
  {
    label: 'Дата',
    key: 'date',
    required: true,
    regex: /(date|дата)/i,
  },
  {
    label: 'Дебит',
    key: 'rate',
    regex: /(rate|дебит|закач)/i,
  },
  {
    label: 'Динамический уровень',
    key: 'dynamic',
    regex: /(dynam|дин)/i,
  },
  {
    label: 'Статический уровень',
    key: 'static',
    regex: /(stat|стат)/i,
  },
  {
    label: 'Давление',
    key: 'pressure',
    regex: /(press|^p$|давл|^р$)/i,
  },
];

const zones = [
  {
    label: 'Скважина',
    key: 'well',
    required: true,
    regex: /(well|скв)/i,
  },
  {
    label: 'Название',
    key: 'name',
    required: true,
    regex: /(name|zone|plast|пласт|свита|ярус)/i,
  },
  {
    label: 'Кровля',
    key: 'top_md',
    regex: /(top|кровл)/i,
  },
  {
    label: 'Подошва',
    key: 'bot_md',
    regex: /(bot|подошв)/i,
  },
  {
    label: 'Кровля АО',
    key: 'top_tvd',
    regex: /(toptvd|top_tvd|ао)/i,
  },
  {
    label: 'Подошва АО',
    key: 'bot_tvd',
    regex: /(bottvd|bot_tvd|ао)/i,
  },
  {
    label: 'Толщина',
    key: 'h',
    regex: /(^h|толщ|мощн)/i,
  },
];

const cases = [
  {
    label: 'Скважина',
    key: 'well',
    required: true,
    regex: /(well|скв)/i,
  },
  {
    label: 'Название',
    key: 'name',
    required: true,
    regex: /(name|назв|тип)/i,
  },
  {
    label: 'Диаметр',
    key: 'diameter',
    regex: /(diam|диам)/i,
  },
  {
    label: 'Длина',
    key: 'length',
    regex: /(length|длин)/i,
  },
  {
    label: 'От',
    key: 'top_md',
    regex: /(top_md|от)/i,
  },
  {
    label: 'До',
    key: 'bot_md',
    regex: /(bot_md|до)/i,
  },
  {
    label: 'Зацементирована',
    key: 'cemented',
    regex: /(^cement|цемент)/i,
  },
  {
    label: 'Кровля цемента',
    key: 'cement_top',
    regex: /(^cement_top|кровля)/i,
  },
];

const perforations = [
  {
    label: 'Скважина',
    key: 'well',
    required: true,
    regex: /(well|скв)/i,
  },
  {
    label: 'Тип перфоратора',
    key: 'perforator_type',
    required: true,
    regex: /(perforato|тип)/i,
  },
  {
    label: 'Диаметр отверстия',
    key: 'hole_diameter',
    regex: /(diam|диам)/i,
  },
  {
    label: 'Отверстий на погонный метр',
    key: 'holes_per_meter',
    regex: /(holes|отве)/i,
  },
  {
    label: 'От',
    key: 'top_md',
    regex: /(top_md|от)/i,
  },
  {
    label: 'До',
    key: 'bot_md',
    regex: /(bot_md|до)/i,
  },
];

const pumps = [
  {
    label: 'Скважина',
    key: 'well',
    required: true,
    regex: /(well|скв)/i,
  },
  {
    label: 'Марка',
    key: 'name',
    required: true,
    regex: /(name|марка)/i,
  },
  {
    label: 'Глубина установки',
    key: 'md',
    regex: /(md|глуб)/i,
  },
  {
    label: 'Производительность',
    key: 'rate',
    regex: /(rate|произ)/i,
  },
  {
    label: 'Диаметр',
    key: 'diameter',
    regex: /(diam|диам)/i,
  },

];

const coordinates = [
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
    regex: /(lat|шир)/i,
  },
  {
    label: 'Долгота',
    key: 'lng',
    regex: /(lng|long|долг)/i,
  },
];

const tables = {
  fields,
  wells,
  inclinometry,
  mer,
  rates,
  zones,
  cases,
  perforations,
  pumps,
  coordinates,
};

export default tables;
