import React, { useEffect, useState } from 'react';
import { useHistory } from 'react-router-dom';

const Dashboard = () => {
    const [message, setMessage] = useState('');
    const history = useHistory();

    useEffect(() => {
        const token = localStorage.getItem('token');
        if (!token) {
            history.push('/login');
        } else {
            fetch('/dashboard', {
                method: 'GET',
                headers: {
                    'Authorization': token,
                    'Content-Type': 'application/json'
                }
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Token inválido');
                }
                return response.json();
            })
            .then(data => {
                setMessage(data.message);
            })
            .catch(error => {
                console.error('Erro ao carregar o dashboard:', error);
                setMessage('Erro ao carregar o dashboard.');
            });
        }
    }, [history]);

    return (
        <div>
            <h1>Dashboard</h1>
            <p>{message}</p>
        </div>
    );
};

export default Dashboard;