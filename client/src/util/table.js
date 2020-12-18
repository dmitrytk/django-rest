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
    obj[header[index]] = cell;
  });
  return obj;
});

export { parseStringTable, getTableData };
