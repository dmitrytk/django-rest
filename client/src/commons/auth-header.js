import { getToken } from './jwt';

const authHeaders = () => ({
  headers: {
    Authorization: `Bearer ${getToken()}`,
  },
});

export default authHeaders;
