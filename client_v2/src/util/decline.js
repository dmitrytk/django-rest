import parse from 'date-fns/parse';
import format from 'date-fns/format';
import differenceInDays from 'date-fns/differenceInDays';
import { saveAs } from 'file-saver';
import parseCSV from 'csv-parse/lib/sync';
import EI from './ei';

// CSV Template
const template = [
  ['KM', 'A', '', '', '', '', '', ''],
  [80.25, 5.45],
  ['WELL', 'X', 'Y', 'R', '01.10.2020', '31.12.2020', '31.12.2021', '01.10.2022'],
  ['1067', '123123', '5353453', '0.07', '0', '700', '700', '700'],
  ['1068', '2342343', '234234', '0.073', '0', '550', '550', '500'],

];

const arange = (start, stop, step) => {
  const stepCount = Math.ceil((stop - start) / step);
  let counter = start;
  const result = new Array(stepCount + 1);
  for (let i = 0; i < result.length; i += 1) {
    result[i] = counter;
    counter += step;
  }
  return result;
};

/**
 * Get data for calculation from csv file
 * @param {String} fileContent
 * @return {Object}
 * */
const parseData = (fileContent) => {
  // const arr = fileContent.trim().split('\n').map((row) => row.split(';'));
  const sheet = parseCSV(fileContent, {
    delimiter: [';', '\t', ','],
    trim: true,
  });
  const km = Number(sheet[1][0]);
  const a = Number(sheet[1][1]);
  const header = sheet[2];
  const body = sheet.slice(3);
  const dates = header.slice(4).map((date) => parse(date, 'dd.MM.yyyy', new Date()));
  const wells = body.map((row) => ({
    name: row[0],
    x: Number(row[1]),
    y: Number(row[2]),
    r: Number(row[3]),
    rates: row.slice(4).map((el) => Number(el)),
    S: [],
  }));
  return {
    km, a, dates, wells,
  };
};

const distance = (well, x, y) => ((well.x - x) ** 2 + (well.y - y) ** 2) ** 0.5;

/**
 * Calculate declines and create header and body for table
 * @param {Object} data
 * @return {Object}
 * */
const calculateDeclineTable = (data) => {
  const header = ['WELL', 'X', 'Y', 'R']
    .concat(data.dates.map((date) => format(date, 'dd.MM.yyyy')));

  for (let i = 0; i < data.dates.length; i += 1) {
    for (let j = 0; j < data.wells.length; j += 1) {
      const well = data.wells[j];
      let SUM = 0;
      for (let k = 1; k < i + 1; k += 1) {
        for (let l = 0; l < data.wells.length; l += 1) {
          const otherWell = data.wells[l];
          const R = well === otherWell ? well.r : distance(well, otherWell.x, otherWell.y);
          const Q = otherWell.rates[k] - otherWell.rates[k - 1];
          const T = differenceInDays(data.dates[i], data.dates[k - 1]);
          const arg = (-R * R) / 4 / data.a / T / 100000;
          SUM += Q * EI(arg);
        }
      }
      const result = -SUM / 4 / 3.14 / data.km;
      well.S.push(Math.round(result * 100) / 100);
    }
  }
  const body = data.wells.map((well) => [well.name, well.x, well.y, well.r].concat(well.S));
  return { header, body };
};

const calculateGrid = (data, step, margin, additionalDrawdown) => {
  const GRID = {
    XX: data.wells.map((well) => well.x),
    YY: data.wells.map((well) => well.y),
    X: null,
    Y: null,
    Z: [],
  };
  const minX = Math.floor((Math.min(...GRID.XX) - margin) / 1000) * 1000;
  const minY = Math.floor((Math.min(...GRID.YY) - margin) / 1000) * 1000;
  const maxX = Math.ceil((Math.max(...GRID.XX) + margin) / 1000) * 1000;
  const maxY = Math.ceil((Math.max(...GRID.YY) + margin) / 1000) * 1000;

  GRID.X = arange(minX, maxX, step);
  GRID.Y = arange(minY, maxY, step);

  for (let i = 0; i < GRID.Y.length; i += 1) {
    GRID.Z[i] = [];
    for (let j = 0; j < GRID.X.length; j += 1) {
      let SUM = 0;
      // eslint-disable-next-line no-restricted-syntax
      for (const well of data.wells) {
        const R = distance(well, GRID.X[j], GRID.Y[i]);
        for (let k = 0; k < data.dates.length; k += 1) {
          if (k > 0) {
            const Q = well.rates[k] - well.rates[k - 1];
            const T = differenceInDays(data.dates[data.dates.length - 1], data.dates[k - 1]);
            const arg = (-R * R) / 4 / data.a / T / 100000;
            SUM += Q * EI(arg);
          }
        }
      }
      const tempS = -SUM / 4 / 3.14 / data.km;
      GRID.Z[i][j] = (Math.round(tempS * 100)) / 100 + additionalDrawdown;
    }
  }
  return GRID;
};

const writeGrid = (grid) => {
  let grd = 'DSAA\n';
  grd += `${grid.X.length} ${grid.Y.length} \n`;
  grd += `${grid.X[0]} ${grid.X[grid.X.length - 1]} \n`;
  grd += `${grid.Y[0]} ${grid.Y[grid.Y.length - 1]} \n`;

  let max = -Infinity;
  let min = Infinity;
  for (let i = 0; i < grid.Z.length; i += 1) {
    const mx = Math.max(...grid.Z[i]);
    const mn = Math.min(...grid.Z[i]);
    max = max < mx ? mx : max;
    min = min > mn ? mn : min;
  }
  grd += `${max} ${min} \n`;

  let counter = 0;
  for (let i = 0; i < grid.Y.length; i += 1) {
    for (let j = 0; j < grid.X.length; j += 1) {
      grd += `${grid.Z[i][j]} `;
      counter += 1;
      if (counter % 10 === 0) {
        grd += '\n';
      }
    }
  }
  const blob = new Blob([grd], { type: 'text/plain;charset=utf-8' });
  saveAs(blob, 'RESULT.grd');
};

export {
  parseData, calculateDeclineTable, template, calculateGrid, writeGrid,
};
