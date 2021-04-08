import http from '@/commons/http';
import authHeaders from '../commons/auth-header';

class FieldService {
  // BASIC
  static load(table, payload) {
    return http.post(`/batch/${table}/`, payload, authHeaders());
  }
}

export default FieldService;
