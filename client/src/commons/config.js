const url = process.env.VUE_APP_DOMAIN || 'localhost';
export const API_URL = `http://${url}:8000/api`;
export const appName = process.env.VUE_APP_NAME;
export const env = process.env.VUE_APP_ENV;
export const TOKEN_KEY = 'horizon_token';
export const USER_KEY = 'horizon_user';
