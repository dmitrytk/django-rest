import http from '../common/http';
import { TOKEN_KEY, USER_KEY } from '../common/config';

class AuthService {
  static login(credentials) {
    console.log('Log by auth service');
    return http.post('/users/login/', credentials)
      .then((response) => {
        console.log(response.data);
        if (response.data[TOKEN_KEY]) {
          localStorage.setItem(USER_KEY, JSON.stringify(response.data));
        }
        return response.data;
      });
  }

  static logout() {
    localStorage.removeItem(USER_KEY);
  }
}

export default AuthService;
