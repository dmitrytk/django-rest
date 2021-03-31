import authHeaders from '@/commons/auth-header';
import http from '@/commons/http';

class AuthService {
  static login(credentials) {
    return http.post('/users/login/', credentials);
  }

  static getUserProfile() {
    return http.get('/users/me/', authHeaders());
  }
}

export default AuthService;
