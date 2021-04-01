const validateRequiredColumn = (header, table) => {
  const requiredColumns = table.filter((col) => col.required);
  const requiredColumnsNames = requiredColumns.map((col) => col.value);
  return requiredColumnsNames.every((col) => header.includes(col));
};

const validateNotEmptyColumns = (header) => header.every((col) => col);

export { validateRequiredColumn, validateNotEmptyColumns };
