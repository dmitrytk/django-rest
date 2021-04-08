import http from '@/commons/http';
import authHeaders from '../commons/auth-header';

class AuthService {
  static login(credentials) {
    return http.post('/users/login/', credentials);
  }

  static getUserProfile() {
    return http.get('/users/me/', authHeaders());
  }
}

export default AuthService;
