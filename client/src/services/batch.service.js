import http from '@/commons/http';

class FieldService {
  // BASIC
  static load(table, payload) {
    return http.post(`/batch/${table}/`, payload);
  }
}

export default FieldService;
