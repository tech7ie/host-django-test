// const MainPage = () => {

//   return (
//         <div className="center">
//             <div>
//             <a href="https://accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?client_id=169670027013-1e5lmvncjeeq5313q25e0qp4otp11m7v.apps.googleusercontent.com&redirect_uri=https%3A%2F%2Fsmurfcat.life&response_type=code&scope=email%20profile%20openid&access_type=offline&prompt=consent&service=lso&o2v=2&theme=glif&flowName=GeneralOAuthFlow">
//               <button style={{ height: '100px', width: '300px' }}>
//                   Войти через Google
//               </button>
//             </a>
//             </div>
//         </div>
// );
// }
// export default MainPage;
// MainPage.js
import React, { useEffect } from 'react';
import { getTokens } from '../../components/auth/Gauth';

const MainPage = () => {
  useEffect(() => {
    const urlParams = new URLSearchParams(window.location.search);
    const authCode = urlParams.get('code');

    if (authCode) {
      window.history.replaceState({}, document.title, "/");
      getTokens(authCode).then(() => {
        window.location.reload();
      });
    }
  }, []);

  const token = localStorage.getItem('authtoken');

  return (
    <div>
      <div>
        {!token && (
          <a href="https://accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?client_id=169670027013-1e5lmvncjeeq5313q25e0qp4otp11m7v.apps.googleusercontent.com&redirect_uri=https%3A%2F%2Fsmurfcat.life&response_type=code&scope=email%20profile%20openid&access_type=offline&prompt=consent&service=lso&o2v=2&theme=glif&flowName=GeneralOAuthFlow">
            <button style={{ height: '100px', width: '300px' }}>
              Войти через Google
            </button>
          </a>
        )}
        тут может быть кнопка регистрации через гугл
        <a href="/new">
            <button style={{ height: '100px', width: '300px' }}>
              Создать новую ссылку
            </button>
          </a>
      </div>
    </div>
  );
};

export default MainPage;
