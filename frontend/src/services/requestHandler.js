// import axios from 'axios';
// import apiClient from './http';

// export async function requestHandler(request, path, data) {
//   try{
//   const response = await request(path, data);
//   } catch(response) {
//   if (response.status === 401) {
//     const refreshToken = localStorage.getItem('reftoken');
//     console.log(refreshToken);
//     if (refreshToken) {
//       const response = await axios.post('https://oauth2.googleapis.com/token', {
//         client_id: "169670027013-1e5lmvncjeeq5313q25e0qp4otp11m7v.apps.googleusercontent.com",
//         refresh_token: refreshToken,
//         grant_type: "refresh_token",
//         client_secret: "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"
//       });

//       if (response.status === 200) {
//         console.log(response.data.access_token);
//         localStorage.setItem('authtoken', response.data.access_token);
//         apiClient.defaults.headers.common['Authorization'] = `${response.data.access_token}`;
//         return requestHandler(request, path, data);
//       } else {
//         localStorage.removeItem('authtoken');
//         localStorage.removeItem('reftoken');
//       }
//     }
//   }

//   return response;}
// }
import axios from 'axios';
import apiClient from './http';

export async function requestHandler(request, path, data) {
  try {
    const response = await request(path, data);
    return response;
  } catch (error) {
    if (error.response && error.response.status === 401) {
      const refreshToken = localStorage.getItem('reftoken');
      if (refreshToken) {
        try {
          const response = await axios.post('https://oauth2.googleapis.com/token', {
            client_id: "169670027013-1e5lmvncjeeq5313q25e0qp4otp11m7v.apps.googleusercontent.com",
            refresh_token: refreshToken,
            grant_type: "refresh_token",
            client_secret: "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"
          });

          if (response.status === 200) {
            localStorage.setItem('authtoken', response.data.access_token);
            apiClient.defaults.headers.common['Authorization'] = `${response.data.access_token}`;
            return requestHandler(request, path, data);
          } else {
            localStorage.removeItem('authtoken');
            localStorage.removeItem('reftoken');
          }
        } catch (error) {
          console.error('Failed to refresh token', error);
        }
      }
    } else {
      console.error('Request failed', error);
    }
  }
}

