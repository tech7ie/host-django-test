import axios from 'axios';

export const getTokens = async (authCode) => {
  try {
    const response = await axios.post('https://oauth2.googleapis.com/token', {
      client_id: '169670027013-1e5lmvncjeeq5313q25e0qp4otp11m7v.apps.googleusercontent.com',
      code: authCode,
      redirect_uri: 'https://smurfcat.life',
      grant_type: 'authorization_code',
      client_secret: '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',
    });

    if (response.status === 200) {
      localStorage.setItem('authtoken', response.data.access_token);
      localStorage.setItem('reftoken', response.data.refresh_token);
    }
  } catch (error) {
    console.error('Failed to exchange auth code for tokens', error);
  }
};