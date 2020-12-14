import http from '@/http-commons';

class FieldService {
  // BASIC
  static findAll() {
    return http.get('/fields/');
  }

  static findOne(id) {
    return http.get(`/fields/${id}/`);
  }

  static create(data) {
    return http.post('/fields/', data);
  }

  static update(id, data) {
    return http.put(`/fields/${id}/`, data);
  }

  // GET CHILD OBJECTS
  static getWells(id) {
    return http.get(`/fields/${id}/wells/`);
  }
}

export default FieldService;
