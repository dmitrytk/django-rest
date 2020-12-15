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

  static getInclinometry(id) {
    return http.get(`/fields/${id}/inclinometry/`);
  }

  static getMer(id) {
    return http.get(`/fields/${id}/mer/`);
  }

  static getRates(id) {
    return http.get(`/fields/${id}/rates/`);
  }

  static getCoordinates(id) {
    return http.get(`/fields/${id}/coordinates/`);
  }
}

export default FieldService;
