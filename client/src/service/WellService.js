import http from '@/http-commons';

class WellService {
  static findOne(id) {
    return http.get(`/wells/${id}/`);
  }

  static create(data) {
    return http.post('/wells/', data);
  }

  static update(id, data) {
    console.log(`/wells/${id}/`);
    return http.put(`/wells/${id}/`, data);
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
}

export default WellService;
