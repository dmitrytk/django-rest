import { getToken } from '@/common/jwt';

const authHeaders = () => ({
  headers: {
    Authorization: `Bearer ${getToken()}`,
  },
});

export default authHeaders;
