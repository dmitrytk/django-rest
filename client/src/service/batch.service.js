import authHeaders from '@/common/auth-header';
import http from '../common/http';

class FieldService {
  // BASIC
  static load(table, payload) {
    return http.post(`/batch/${table}/`, authHeaders(), payload);
  }
}

export default FieldService;
