const fields = [
  {
    text: 'Id',
    value: 'id',
    regex: /(id|иден)/i,
  },
  {
    text: 'Название',
    value: 'name',
    required: true,
    sortable: true,
    regex: /(name|назавние)/i,
  },
  {
    text: 'Тип',
    value: 'type',
    regex: /(type|тип)/i,
  },
  {
    text: 'Местонахождение',
    value: 'location',
    regex: /(loc|распол|местона)/i,
  },
];

const wells = [
  {
    text: 'id',
    value: 'id',
    regex: /(id|ид)/i,
  },
  {
    text: 'Номер',
    value: 'name',
    required: true,
    sortable: true,
    regex: /(well|name|номер|скв)/i,

  },
  {
    text: 'Куст',
    value: 'pad',
    regex: /(pad|куст)/i,

  },
  {
    text: 'Тип',
    value: 'type',
    regex: /(type|тип|назна)/i,

  },
  {
    text: 'Состояние',
    value: 'status',
    regex: /(stat|сост|стат)/i,

  },
  {
    text: 'Забой',
    value: 'bottom',
    regex: /(bott|md|забой|глуб)/i,

  },
  {
    text: 'Альтитуда',
    value: 'alt',
    regex: /(alt|альт)/i,
  },
  {
    text: 'X',
    value: 'x',
    regex: /(^x|^х)/i,
  },
  {
    text: 'Y',
    value: 'y',
    regex: /(^y|^у)/i,
  },
  {
    text: 'Широта',
    value: 'lat',
    regex: /(lat|шир)/i,
  },
  {
    text: 'Долгота',
    value: 'lng',
    regex: /(lng|long|долг)/i,
  },
];

const inclinometry = [
  {
    text: 'Скважина',
    value: 'well',
    required: true,
    regex: /(well|скв)/i,
  },
  {
    text: 'Глубина',
    value: 'md',
    required: true,
    regex: /(md|depth|глуб)/i,
  },
  {
    text: 'Угол',
    value: 'inc',
    regex: /(inc|угол)/i,
  },
  {
    text: 'Азимут',
    value: 'azi',
    regex: /(azi|азим)/i,
  },
];

const mer = [
  {
    text: 'Скважина',
    value: 'well',
    required: true,
    regex: /(well|скв)/i,
  },
  {
    text: 'Дата',
    value: 'date',
    required: true,
    regex: /(date|дата)/i,
  },
  {
    text: 'Вид работы',
    value: 'work_type',
    regex: /(wor|вид|харак)/i,
  },
  {
    text: 'Состояние',
    value: 'state',
    regex: /(stat|сост)/i,
  },
  {
    text: 'Добыча',
    value: 'production',
    regex: /(prod|добыча)/i,
  },
  {
    text: 'Часов работы',
    value: 'work_hours',
    regex: /(hour|час)/i,
  },
];

const rates = [
  {
    text: 'Скважина',
    value: 'well',
    required: true,
    regex: /(well|скв)/i,
  },
  {
    text: 'Дата',
    value: 'date',
    required: true,
    regex: /(date|дата)/i,
  },
  {
    text: 'Вид работы',
    value: 'work_type',
    regex: /(wor|вид|харак)/i,
  },
  {
    text: 'Дебит',
    value: 'rate',
    regex: /(rate|дебит|закач)/i,
  },
  {
    text: 'Динамический уровень',
    value: 'dynamic_level',
    regex: /(dynam|дин)/i,
  },
  {
    text: 'Статический уровень',
    value: 'static_level',
    regex: /(stat|стат)/i,
  },
  {
    text: 'Давление',
    value: 'pressure',
    regex: /(press|^p$|давл|^р$)/i,
  },
];

const fieldHorizons = [
  {
    text: 'Название',
    value: 'value_full',
  },
  {
    text: 'Тип',
    value: 'type',
  },
];

const horizons = [
  {
    text: 'Скважина',
    value: 'well',
    required: true,
    regex: /(well|скв)/i,
  },
  {
    text: 'Название',
    value: 'horizon',
    required: true,
    regex: /(name|zone|plast|пласт|свита|ярус)/i,
  },
  {
    text: 'Кровля',
    value: 'top_md',
    regex: /(top|кровл)/i,
  },
  {
    text: 'Подошва',
    value: 'bot_md',
    regex: /(bot|подошв)/i,
  },
  {
    text: 'Кровля АО',
    value: 'top_tvdss',
    regex: /(toptvd|top_tvd|ао)/i,
  },
  {
    text: 'Подошва АО',
    value: 'bot_tvdss',
    regex: /(bottvd|bot_tvd|ао)/i,
  },
];

const cases = [
  {
    text: 'Скважина',
    value: 'well',
    required: true,
    regex: /(well|скв)/i,
  },
  {
    text: 'Название',
    value: 'name',
    required: true,
    regex: /(name|назв|тип)/i,
  },
  {
    text: 'Диаметр',
    value: 'diameter',
    regex: /(diam|диам)/i,
  },
  {
    text: 'Длина',
    value: 'length',
    regex: /(length|длин)/i,
  },
  {
    text: 'От',
    value: 'top_md',
    regex: /(top_md|от)/i,
  },
  {
    text: 'До',
    value: 'bot_md',
    regex: /(bot_md|до)/i,
  },
  {
    text: 'Зацементирована',
    value: 'cemented',
    regex: /(^cement|цемент)/i,
  },
  {
    text: 'Кровля цемента',
    value: 'cement_top',
    regex: /(^cement_top|кровля)/i,
  },
];

const perforations = [
  {
    text: 'Скважина',
    value: 'well',
    required: true,
    regex: /(well|скв)/i,
  },
  {
    text: 'Тип перфоратора',
    value: 'perforator_type',
    required: true,
    regex: /(perforato|тип)/i,
  },
  {
    text: 'Диаметр отверстия',
    value: 'hole_diameter',
    regex: /(diam|диам)/i,
  },
  {
    text: 'Отверстий на погонный метр',
    value: 'holes_per_meter',
    regex: /(holes|отве)/i,
  },
  {
    text: 'От',
    value: 'top_md',
    regex: /(top_md|от)/i,
  },
  {
    text: 'До',
    value: 'bot_md',
    regex: /(bot_md|до)/i,
  },
];

const pumps = [
  {
    text: 'Скважина',
    value: 'well',
    required: true,
    regex: /(well|скв)/i,
  },
  {
    text: 'Марка',
    value: 'name',
    required: true,
    regex: /(name|марка)/i,
  },
  {
    text: 'Глубина установки',
    value: 'md',
    regex: /(md|глуб)/i,
  },
  {
    text: 'Производительность',
    value: 'rate',
    regex: /(rate|произ)/i,
  },
  {
    text: 'Диаметр',
    value: 'diameter',
    regex: /(diam|диам)/i,
  },

];

const coordinates = [
  {
    text: 'X',
    value: 'x',
    regex: /(^x|^х)/i,
  },
  {
    text: 'Y',
    value: 'y',
    regex: /(^y|^у)/i,
  },
  {
    text: 'Широта',
    value: 'lat',
    regex: /(lat|шир)/i,
  },
  {
    text: 'Долгота',
    value: 'lng',
    regex: /(lng|long|долг)/i,
  },
];

const tables = {
  fields,
  wells,
  inclinometry,
  mer,
  rates,
  fieldHorizons,
  horizons,
  cases,
  perforations,
  pumps,
  coordinates,
};

export default tables;
