const fields = [
  {
    label: 'Id',
    key: 'id',
  },
  {
    label: '�������������',
    key: 'name',
    required: true,
    sortable: true,
  },
  {
    label: '���',
    key: 'type',
  },
  {
    label: '������������',
    key: 'location',
  },
];

const wells = [
  {
    label: 'id',
    key: 'id',
  },
  {
    label: '��������',
    key: 'well',
    required: true,
    sortable: true,

  },
  {
    label: '����',
    key: 'pad',

  },
  {
    label: '���',
    key: 'type',

  },
  {
    label: '���������',
    key: 'status',

  },
  {
    label: '�����',
    key: 'bottom',

  },
  {
    label: '���������',
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
    label: '������',
    key: 'lat',
  },
  {
    label: '�������',
    key: 'lng',
  },
];

const inclinometry = [
  {
    label: '��������',
    key: 'well',
  },
  {
    label: '�������',
    key: 'md',
    required: true,
  },
  {
    label: '����',
    key: 'inc',
  },
  {
    label: '������',
    key: 'azi',
  },
];

const mer = [
  {
    label: '��������',
    key: 'well',
  },
  {
    label: '����',
    key: 'date',
    required: true,
  },
  {
    label: '���������',
    key: 'status',
  },
  {
    label: '�����',
    key: 'rate',
  },
  {
    label: '������',
    key: 'production',
  },
  {
    label: '����� ������',
    key: 'work_days',
  },
];

const rates = [
  {
    label: '��������',
    key: 'well',
  },
  {
    label: '����',
    key: 'date',
    required: true,
  },
  {
    label: '������',
    key: 'rate',
  },
  {
    label: '��������',
    key: 'dynamic',
  },
  {
    label: '�������',
    key: 'static',
  },
  {
    label: '��������',
    key: 'pressure',
  },
];

const zones = [
  {
    label: '��������',
    key: 'well',
  },
  {
    label: '��������',
    key: 'name',
    required: true,
  },
  {
    label: '������',
    key: 'top_md',
  },
  {
    label: '�������',
    key: 'bot_md',
  },
  {
    label: '������ ��',
    key: 'top_tvd',
  },
  {
    label: '������� ��',
    key: 'bot_tvd',
  },
  {
    label: '��������',
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
