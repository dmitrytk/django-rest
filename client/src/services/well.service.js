import http from '@/commons/http';
import authHeaders from '../commons/auth-header';

class WellService {
  static findOne(id) {
    return http.get(`/wells/${id}/`, authHeaders());
  }

  static create(data) {
    return http.post('/wells/', data, authHeaders());
  }

  static update(id, data) {
    return http.put(`/wells/${id}/`, data, authHeaders());
  }

  static delete(id) {
    return http.delete(`/wells/${id}/`, authHeaders());
  }

  // GET CHILD OBJECTS
  static getInclinometry(id) {
    return http.get(`/wells/${id}/inclinometry/`, authHeaders());
  }

  static getMer(id) {
    return http.get(`/wells/${id}/mer/`, authHeaders());
  }

  static getRates(id) {
    return http.get(`/wells/${id}/rates/`, authHeaders());
  }

  static getHorizons(id) {
    return http.get(`/wells/${id}/horizons/`, authHeaders());
  }

  static getCases(id) {
    return http.get(`/wells/${id}/cases/`, authHeaders());
  }

  static getPerforations(id) {
    return http.get(`/wells/${id}/perforations/`, authHeaders());
  }

  static getPumps(id) {
    return http.get(`/wells/${id}/pumps/`, authHeaders());
  }

  // DELETE CHILD OBJECTS
  static deleteInclinometry(id) {
    return http.delete(`/wells/${id}/inclinometry/`, authHeaders());
  }

  static deleteMer(id) {
    return http.delete(`/wells/${id}/mer/`, authHeaders());
  }

  static deleteRates(id) {
    return http.delete(`/wells/${id}/rates/`, authHeaders());
  }

  static deleteHorizons(id) {
    return http.delete(`/wells/${id}/horizons/`, authHeaders());
  }

  static deleteCases(id) {
    return http.delete(`/wells/${id}/cases/`, authHeaders());
  }

  static deletePerforations(id) {
    return http.delete(`/wells/${id}/perforations/`, authHeaders());
  }

  static deletePumps(id) {
    return http.delete(`/wells/${id}/pumps/`, authHeaders());
  }
}

export default WellService;
