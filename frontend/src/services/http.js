// import axios from 'axios';

// const apiClient = axios.create({
//     baseURL: 'https://smurfcat.life/',
//     timeout: 10000,
//     headers: {
//       'Access-Control-Allow-Origin': '*',
//       'Content-Type': 'application/json'
//     },
//   });


// apiClient.interceptors.request.use((config) => {
//   const token = localStorage.getItem('authtoken');
//   if (token) {
//     config.headers.Authorization = token;
//   }
//   return config;
// }, (error) => {
//   return Promise.reject(error);
// });


// apiClient.interceptors.response.use((response) => {
//     return response;
//   }, async (error) => {
//     if (error.response && error.response.status === 401) {
//       const refreshToken = localStorage.getItem('reftoken');
//       if (refreshToken) {
//         const response = await axios.post('https://oauth2.googleapis.com/token', {
//           client_id: '169670027013-1e5lmvncjeeq5313q25e0qp4otp11m7v.apps.googleusercontent.com',
//           refresh_token: refreshToken,
//           grant_type: 'refresh_token',
//           client_secret: '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',
//         });
  
//         if (response.status === 200) {
//           localStorage.setItem('authtoken', response.data.access_token);
//           error.config.headers.Authorization = `Bearer ${response.data.access_token}`;
//           return apiClient.request(error.config);
//         } else {
//             localStorage.removeItem('authtoken');
//             localStorage.removeItem('reftoken');
//         }
//       } else {
//         localStorage.removeItem('authtoken');
//       }
//     }

//     return Promise.reject(error);
//   });

// export default apiClient;
import axios from 'axios';

const apiClient = axios.create({
  baseURL: 'https://smurfcat.life/',
  timeout: 10000,
  headers: {
    'Access-Control-Allow-Origin': '*',
    'Content-Type': 'application/json'
  },
});

export default (() => {
  const token = localStorage.getItem('authtoken');

  if (token) {
    apiClient.defaults.headers.common['Authorization'] = token;
  }

  return apiClient;
})();

