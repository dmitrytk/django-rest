/**
 * Get header and body from string table data
 * @param {String} data
 * @return {Object}
 * */
const parseStringTable = (data) => {
  const stringTable = data.trimRight().split('\n')
    .map((row) => row.split('\t'));
  const header = stringTable[0];
  const body = stringTable.slice(1);
  return { header, body };
};

/**
 * Get array of row objects from header and body
 * @param {String[]} header
 * @param {String[][]} body
 * @return {Object[]}
 * */
const getTableData = (header, body) => body.map((row) => {
  const obj = {};
  row.forEach((cell, index) => {
    obj[header[index]] = cell === '' ? null : cell;
  });
  return obj;
});

/**
 * Convert header and body of table to TAB (or else) separated string
 * @param {Object[]} header
 * @param {Object[][]} body
 * @param {String} separator
 * @return {String}
 * */
const tableToString = (header, body, separator = '\t') => {
  let result = `${header.map((el) => el.label).join(separator)}\n`;
  result += body.map((row) => header.map((el) => row[el.key]).join(separator)).join('\n');
  return result;
};

export { parseStringTable, getTableData, tableToString };
