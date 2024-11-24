import axios from 'axios';

export const API_URL = import.meta.env.VITE_API_BASE_URL || `http://localhost:8000`;

const apiClient = axios.create({
    baseURL: API_URL,
    headers: {
        'Content-Type': 'application/json',
    },
});

export default apiClient;
