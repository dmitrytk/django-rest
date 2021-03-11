import http from '../common/http';
import { TOKEN_KEY, USER_KEY } from '../common/config';

class AuthService {
  static login(credentials) {
    return http.post('/users/login/', credentials)
      .then((response) => {
        if (response.data.user.token) {
          localStorage.setItem(USER_KEY, response.data.user.username);
          localStorage.setItem(TOKEN_KEY, response.data.user.token);
        }
        return response.data;
      });
  }

  static logout() {
    localStorage.removeItem(USER_KEY);
  }
}

export default AuthService;
