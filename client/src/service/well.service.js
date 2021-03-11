import http from '../common/http';

class WellService {
  static findOne(id) {
    return http.get(`/wells/${id}/`);
  }

  static create(data) {
    return http.post('/wells/', data);
  }

  static update(id, data) {
    return http.put(`/wells/${id}/`, data);
  }

  static delete(id) {
    return http.delete(`/wells/${id}/`);
  }

  // GET CHILD OBJECTS
  static getInclinometry(id) {
    return http.get(`/wells/${id}/inclinometry/`);
  }

  static getMer(id) {
    return http.get(`/wells/${id}/mer/`);
  }

  static getRates(id) {
    return http.get(`/wells/${id}/rates/`);
  }

  static getZones(id) {
    return http.get(`/wells/${id}/zones/`);
  }

  static getCases(id) {
    return http.get(`/wells/${id}/cases/`);
  }

  static getPerforations(id) {
    return http.get(`/wells/${id}/perforations/`);
  }

  static getPumps(id) {
    return http.get(`/wells/${id}/pumps/`);
  }

  // DELETE CHILD OBJECTS
  static deleteInclinometry(id) {
    return http.delete(`/wells/${id}/inclinometry/`);
  }

  static deleteMer(id) {
    return http.delete(`/wells/${id}/mer/`);
  }

  static deleteRates(id) {
    return http.delete(`/wells/${id}/rates/`);
  }

  static deleteZones(id) {
    return http.delete(`/wells/${id}/zones/`);
  }

  static deleteCases(id) {
    return http.delete(`/wells/${id}/cases/`);
  }

  static deletePerforations(id) {
    return http.delete(`/wells/${id}/perforations/`);
  }

  static deletePumps(id) {
    return http.delete(`/wells/${id}/pumps/`);
  }
}

export default WellService;
