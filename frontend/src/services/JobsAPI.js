import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000'

const api = axios.create({
    baseURL: API_BASE_URL,
    headers: {
        'Content-Type': 'application/json',
    },
});

export const jobsAPI = {
    searchJobs: async (params = {}) => {
        try {
            const response = await api.get('/jobs/search', { params });
            return response.data;
        } catch (error) {
        console.error('Error searching job database:', error);
        throw error;
        }
    },
    testConnection: async () => {
        try {
            const response = await api.get('/');
            return response.data;
        } catch (error) {
            console.error('Error connecting to API:', error);
            throw error;
        }
    },
}

export default api;