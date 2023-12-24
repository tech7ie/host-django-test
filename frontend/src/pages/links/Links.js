import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { getLinks } from '../../services/methods';



function Links() {
    const { code } = useParams();
    const [links, setLinks] = useState([]);

    useEffect(() => {
        const fetchLinks = async () => {
            const response = await getLinks(code);
            setLinks(response.data);
        };
        fetchLinks();
    }, [code]);

    if (!links) return <div>loading...</div>;

    return (
        <div>
            {links.map((link, index) => (
                <a 
                    key={index} 
                    href={link.link}
                    target="_blank" 
                    rel="noopener noreferrer"
                    style={{ backgroundColor: 'red', display: 'block', marginBottom: '10px', color: 'white', padding: '10px', textDecoration: 'none' }}
                >
                    Ссылка
                </a>
            ))}
        </div>
    );
}

export default Links;
