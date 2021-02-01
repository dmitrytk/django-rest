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

  static getZones(id) {
    return http.get(`/fields/${id}/zones/`);
  }

  static getCoordinates(id) {
    return http.get(`/fields/${id}/coordinates/`);
  }

  // DELETE CHILD OBJECTS
  static deleteWells(id) {
    return http.delete(`/fields/${id}/wells/`);
  }

  static deleteInclinometry(id) {
    return http.delete(`/fields/${id}/inclinometry/`);
  }

  static deleteMer(id) {
    return http.delete(`/fields/${id}/mer/`);
  }

  static deleteRates(id) {
    return http.delete(`/fields/${id}/rates/`);
  }

  static deleteZones(id) {
    return http.delete(`/fields/${id}/zones/`);
  }

  static deleteCoordinates(id) {
    return http.delete(`/fields/${id}/coordinates/`);
  }
}

export default FieldService;
