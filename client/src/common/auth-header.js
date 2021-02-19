import { TOKEN_KEY, USER_KEY } from './config';

export default function authHeader() {
  const user = JSON.parse(localStorage.getItem(USER_KEY));

  if (user && user[TOKEN_KEY]) {
    return { Authorization: `Bearer ${user[TOKEN_KEY]}` };
  }
  return {};
}
