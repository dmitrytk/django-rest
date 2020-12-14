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
}

export default WellService;
