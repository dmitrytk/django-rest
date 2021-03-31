import { TOKEN_KEY } from './config';

export const getToken = () => localStorage.getItem(TOKEN_KEY);
export const saveToken = (token) => localStorage.setItem(TOKEN_KEY, token);
export const destroyToken = () => localStorage.removeItem(TOKEN_KEY);

export default { getToken, saveToken, destroyToken };
