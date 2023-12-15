import { createStore } from 'vuex'

export default createStore({
    state: {
        api_key: null,
        movies: [],
        theatres: [],
        screens: [],
        current_user: null,
    },
    getters: {
        getApiKey(state){
            return state.api_key;
        },

        getCurrentUser(state){
            return state.current_user;
        }
    },
    mutations: {
        setApiKey(state, key) {
            state.api_key = key;
        },

        setCurrentUser(state, user) {
            console.log(user)
            state.current_user = user;
        },
        
        updateMovies(state, movie) {
            const index = state.movies.findIndex(movie => movie.id === movie.id);
            if (index !== -1) {
                state.movies[index] = movie;
            } else {
                state.movies.push(movie);
            }
        }    
    },
    actions: {
        updateMovie({ commit }, updatedMovie) {
            setTimeout(() => {
                commit('updateMovies', movie);
            }, 1000);
        },
    },
    modules: {
    }
})
