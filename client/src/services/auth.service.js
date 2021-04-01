import http from '@/commons/http';

class AuthService {
  static login(credentials) {
    return http.post('/users/login/', credentials);
  }

  static getUserProfile() {
    return http.get('/users/me/');
  }
}

export default AuthService;
