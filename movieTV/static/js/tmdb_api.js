// require('dotenv').config();
// console.log(process.env);
import { API_KEY_v3 } from "./env.js";

const API_KEY = API_KEY_v3
const API_BASE = 'https://api.themoviedb.org/3'
//const API_BASE = 'https://api.themoviedb.org/4' //nova versao

const basicFetch = async (endpoint) => {
    const req = await fetch(`${API_BASE}${endpoint}`);
    const json = await req.json();
}

export default {
    getHomeList: async () => {
        return [
            {
                slug: 'trending',
                title: 'tendencia',
                items: await basicFetch(`/trending/all/week?language=en-US&api_key=${API_KEY}`)
            },
            {
                slug: 'toprated',
                title: 'em alta',
                items: await basicFetch(`/movie/toprated?language=en-US&api_key=${API_KEY}`)
            }
        ]
    }
}

