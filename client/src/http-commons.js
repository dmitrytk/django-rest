import axios from 'axios';

const http = axios.create({
  baseURL: 'http://localhost:8080/api',
  headers: {
    'Content-type': 'application/json',
  },
  'Access-Control-Allow-Origin': '*',
  timeout: 3000,
});

export default http;
