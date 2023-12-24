// import React, { useState, useEffect } from 'react';
// import axios from 'axios';
// import { useParams } from 'react-router-dom';
// import { useNavigate } from 'react-router-dom';



// function Create() {
//     const navigate = useNavigate();
//     const { code } = useParams();
//     const [links, setLinks] = useState(['']);
//     const [loading, setLoading] = useState(false);  // добавьте состояние для отслеживания загрузки

//     useEffect(() => {
//         const checkCode = async () => {
//             setLoading(true);  // начало загрузки
//             try {
//                 var token = localStorage.getItem('authtoken');
//                 console.log(token);
//                 const response = await axios.get(`https://smurfcat.life/api/check-code?code=${code}`, {
//                     headers: {
//                         'Authorization': token
//                     }
//                 });
//                 console.log(response.data)
//                 if (response.data) {
//                     navigate(`/links/${code}`);
//                     window.location.reload();
//                 }
//             } catch (error) {
//                 console.error('Ошибка при проверке кода:', error);
//             }
//             setLoading(false);  // конец загрузки
//         };
    
//         checkCode();
//     }, [code, navigate]);
    

//     const handleChange = (event, index) => {
//         const newLinks = [...links];
//         newLinks[index] = event.target.value;
//         setLinks(newLinks);
//     };

//     const handleAddLink = () => {
//         setLinks([...links, '']);
//     };

//     const handleRemoveLink = (index) => {
//         const newLinks = [...links];
//         newLinks.splice(index, 1);
//         setLinks(newLinks);
//     };

//     const handleSubmit = async (event) => {
//         event.preventDefault();
//         try {
//             var token = localStorage.getItem('authtoken');
//             console.log(token);
//             const response = await axios.post('https://smurfcat.life/api/add-link', {
//                 headers: {
//                     'Authorization': token
//                 }
//             },{ "code": code, "links": links });
//             navigate(`/links/${code}`);
//             window.location.reload();
//         } catch (error) {
//             console.error('Ошибка при отправке ссылок:', error);
//         }
//     };

//     return (
//         <form onSubmit={handleSubmit}>
//             {loading ? (
//                 <div>Загрузка...</div>  // отображение индикатора загрузки
//             ) : (
//                 <>
//                     {links.map((link, index) => (
//                         <div key={index}>
//                             <input 
//                                 value={link} 
//                                 onChange={(event) => handleChange(event, index)}
//                                 type="url"
//                                 required
//                             />
//                             <button type="button" onClick={() => handleRemoveLink(index)}>X</button>
//                         </div>
//                     ))}
//                     <button type="button" onClick={handleAddLink}>Добавить ссылку</button><br></br>
//                     <button type="submit">Отправить ссылки</button>
//                 </>
//             )}
//         </form>
//     );
// }

// export default Create;
import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import { useNavigate } from 'react-router-dom';
import { checkCode, addLink } from '../../services/methods';

function Create() {
  const navigate = useNavigate();
  const { code } = useParams();
  const [links, setLinks] = useState(['']);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    const fetchCode = async () => {
        setLoading(true);
        const response = await checkCode(code);
        if (response.data && response.data.length > 0) {
            navigate(`/links/${code}`);
            window.location.reload();
        }
        setLoading(false);
    };

    fetchCode();
  }, [code, navigate]);
    

    const handleChange = (event, index) => {
        const newLinks = [...links];
        newLinks[index] = event.target.value;
        setLinks(newLinks);
    };

    const handleAddLink = () => {
        setLinks([...links, '']);
    };

    const handleRemoveLink = (index) => {
        const newLinks = [...links];
        newLinks.splice(index, 1);
        setLinks(newLinks);
    };

    const handleSubmit = async (event) => {
        event.preventDefault();
        try {
          const response = await addLink(code, links);  // используйте функцию addLink
          navigate(`/links/${code}`);
          window.location.reload();
        } catch (error) {
          console.error('Ошибка при отправке ссылок:', error);
        }
      };

    return (
        <form onSubmit={handleSubmit}>
            {loading ? (
                <div>Loading...</div>
            ) : (
                <>
                    {links.map((link, index) => (
                        <div key={index}>
                            <input 
                                value={link} 
                                onChange={(event) => handleChange(event, index)}
                                type="url"
                                required
                            />
                            <button type="button" onClick={() => handleRemoveLink(index)}>X</button>
                        </div>
                    ))}
                    <button type="button" onClick={handleAddLink}>Добавить ссылку</button><br></br>
                    <button type="submit">Отправить ссылки</button>
                </>
            )}
        </form>
    );
}

export default Create;