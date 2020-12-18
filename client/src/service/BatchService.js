import http from '@/http-commons';

class FieldService {
  // BASIC
  static load(table, payload) {
    return http.post(`/batch/${table}/`, payload);
  }
}

export default FieldService;
