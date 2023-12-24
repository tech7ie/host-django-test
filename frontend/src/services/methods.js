// import apiClient from './http';

// export const addLink = (code, links) => {
//   return apiClient.post('api/add-link', { code, links });
// };

// export const checkCode = (code) => {
//   return apiClient.get(`api/check-code?code=${code}`);
// };

// export const createCode = () => {
//   return apiClient.post('api/create-code');
// };

// export const getLinks = (code) => {
//   return apiClient.get(`api/links?code=${code}`);
// };

import { requestHandler } from './requestHandler';
import apiClient from './http';

export const addLink = (code, links) => {
  return requestHandler(apiClient.post, 'api/add-link', { code, links });
};

export const checkCode = (code) => {
  return requestHandler(apiClient.get, `api/check-code?code=${code}`);
};

export const createCode = () => {
  return requestHandler(apiClient.post, 'api/create-code');
};

export const getLinks = (code) => {
  return requestHandler(apiClient.get, `api/links?code=${code}`);
};
