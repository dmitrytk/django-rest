import http from '@/commons/http';
import authHeaders from '../commons/auth-header';

class FieldService {
  // BASIC
  static findAll() {
    return http.get('/fields/', authHeaders());
  }

  static findOne(id) {
    return http.get(`/fields/${id}/`, authHeaders());
  }

  static create(data) {
    return http.post('/fields/', data, authHeaders());
  }

  static update(id, data) {
    return http.put(`/fields/${id}/`, data, authHeaders());
  }

  // GET CHILD OBJECTS
  static getWells(id) {
    return http.get(`/fields/${id}/wells/`, authHeaders());
  }

  static getInclinometry(id) {
    return http.get(`/fields/${id}/inclinometry/`, authHeaders());
  }

  static getMer(id) {
    return http.get(`/fields/${id}/mer/`, authHeaders());
  }

  static getRates(id) {
    return http.get(`/fields/${id}/rates/`, authHeaders());
  }

  static getHorizons(id) {
    return http.get(`/fields/${id}/horizons/`, authHeaders());
  }

  static getCoordinates(id) {
    return http.get(`/fields/${id}/coordinates/`, authHeaders());
  }

  // DELETE CHILD OBJECTS
  static deleteWells(id) {
    return http.delete(`/fields/${id}/wells/`, authHeaders());
  }

  static deleteInclinometry(id) {
    return http.delete(`/fields/${id}/inclinometry/`, authHeaders());
  }

  static deleteMer(id) {
    return http.delete(`/fields/${id}/mer/`, authHeaders());
  }

  static deleteRates(id) {
    return http.delete(`/fields/${id}/rates/`, authHeaders());
  }

  static deleteHorizons(id) {
    return http.delete(`/fields/${id}/horizons/`, authHeaders());
  }

  static deleteCoordinates(id) {
    return http.delete(`/fields/${id}/coordinates/`, authHeaders());
  }
}

export default FieldService;
