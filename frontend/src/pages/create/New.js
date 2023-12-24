import React, { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { createCode } from '../../services/methods';

function CreateCodePage() {
    const navigate = useNavigate();

    useEffect(() => {
        const createNewCode = async () => {
            const response = await createCode();
            const code = response.data;
            navigate(`/create/${code}`);
            window.location.reload();
        };
        createNewCode();
    }, [navigate]);
    
    return null;
}

export default CreateCodePage;

