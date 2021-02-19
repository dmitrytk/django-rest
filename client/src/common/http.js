import axios from 'axios';
import { API_URL } from './config';

const http = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-type': 'application/json',
  },
  'Access-Control-Allow-Origin': '*',
  timeout: 3000,
});

export default http;
