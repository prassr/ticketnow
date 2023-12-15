<template>
    <div class="notification" v-if="is_unauth">
        <p>Your session has been expired. Kindly log in again.</p>
    </div>
    <div class="movies-container" >
        <div class="central-pane">
            <div class="upcoming" v-if="upcomingMovies.length > 0">
                <div><h2>Upcoming movies</h2><hr></div>
                <div class="movies">
                    <user-movie class="movie" v-for="movie in upcomingMovies" :movie="movie" :key="movie.movie_id"></user-movie>
                </div>
            </div>
            <div><h2>Movies</h2><hr></div>
            <div class="all-movies">
                <user-movie class="movie" v-for="movie in movies" :movie="movie" :key="movie.movie_id" ></user-movie>
            </div>
        </div>
        
    </div>
    <div class="search-outer" v-if="filteredMovies.length > 0">
            <div class="searched-movies">
                <user-movie class="movie"
                    v-for="movie in filteredMovies"
                    :key="movie.id"
                    :movie="movie"
                    @click.native="navigateToMovie(movie.id)"
                />
            </div>
        </div>
    <div class="search-container">
        <div class="search">
            <input type="text" v-model="searchTerm" @input="performSimpleSearch" placeholder="Search for a movie">
        </div>
    </div>

   <router-view></router-view>
</template>

<script>
import UserMovie from '@/components/UserMovie.vue'
import {createMovie, getMovies, unAuthRedirect} from '@/js/requests.js'
const fuzzball = require('fuzzball')

export default {
   name: "UserMoviePage",
   components: {
       UserMovie,
   },
   computed: {
   },
   created() {
       this.getAllMovies();
       document.title = "Movies";
   },      
   data() {
       return {
           name: "",
           movies: [],
           searchTerm: "",
           filteredMovies: [],
           upcomingMovies: [],
           is_unauth: false,
            }
   },
   methods: {
        unAuth(e) {
            if (e.status == 401) {
                this.is_unauth = true;
                unAuthRedirect(this.$router);
                return true;
            }
            return false;
        },

        performSimpleSearch() {
            if (this.searchTerm.length > 0 ) {
                this.filteredMovies = this.movies.filter(movie =>
                    fuzzball.partial_ratio(movie.name.toLowerCase(), this.searchTerm.toLowerCase()) > 85
                    || fuzzball.partial_ratio(movie.language.toLowerCase(), this.searchTerm.toLocaleLowerCase()) > 85
                    || fuzzball.partial_ratio(movie.cast.toLowerCase(), this.searchTerm.toLocaleLowerCase()) > 85
                    || fuzzball.partial_ratio(movie.director.toLowerCase(), this.searchTerm.toLocaleLowerCase()) > 85
                    || fuzzball.partial_ratio(movie.writer.toLowerCase(), this.searchTerm.toLocaleLowerCase()) > 85
                );

            } else {
                this.filteredMovies = [];
            }
            
        },
        async navigateToMovie(movieId) {
            // Navigate to the respective movie page when a movie is clicked
            this.$router.push({ name: "movie_details", params: { id: movieId } });
        },
        async getAllMovies(){
            let api_key = this.$store.getters.getApiKey;
            try {
                this.movies = await getMovies(api_key);
                const currentDate = new Date();
                console.log(this.movies)
                this.upcomingMovies = this.movies.filter(movie => {
                    const releaseDate = new Date(movie.release_date);
                    return releaseDate > currentDate;
                });
            } catch (e) {
               const is_un_auth = this.unAuth(e);
            }
       },
   },
}

</script>


<style scoped>
   @import  '/src/css/form.css';

   input[type="text"] {
    background-image: url("@/assets/icons-svg/search-black.svg");
    background-repeat: no-repeat;
    background-position: right;
    border: none;
    border-radius: 10px;
    padding-left: 10px;
   }
   input[type="text"]:focus {
    border: none;
    outline: none;
   }
   .movies-container {
        display: flex;
        position: relative;
        top: 100px;
        padding: 0;
        margin-right: 10px;
   }

   .movie {
    margin: 10px;
   }

   .central-pane {
        width: 100%;
   }
    
    h2 {
        position: relative;
        width: 94%;
        margin-left: 10px;
   }
   .movies {
        margin-top: 10px;
        position: relative;
        justify-content: flex-start;
        width: 100%;
        overflow-x: scroll;
        display: flex;
        flex-direction: row;
        min-height: fit-content;
        height: 450px;
   }

   .all-movies {
        /* width: 500px; */
        /* width: 90%; */
        display: flex;
        flex-direction: row;
        flex-wrap: wrap;
        width: 94%;

   }

   .search-outer {
    width: 100%;
    z-index: 10;
    position: fixed;
    top: 7vh;
    bottom: 0;
    left: 50%;
    right: 0;
    transform: translateX(-50%);
    display: flex;
    flex-direction: row;
    background: rgba(255, 255, 255, 0.7);
    margin-top: 50px;
   }
   .searched-movies {
        z-index: 10;
        position: fixed;
        top: 7vh;
        bottom: 0;
        left: 50%;
        right: 0;
        transform: translateX(-50%);
        display: flex;
        flex-direction: row;
        overflow-x: scroll;
        background: transparent;
        overflow: overlay;

   }

   .search-container {
        z-index: 2000;
        position: fixed;
        top: 5%;
        bottom: 0;
        left: 50%;
        min-height: fit-content;
        transform: translateX(-50%);

   }


   @media screen and (max-width: 1024px) {
        .search-container {
            top: 7%;

        }
   }

   @media screen and (max-width: 600px) {
       .movies {
           justify-content: center;
       }
   }

   @media screen and (max-width: 425px){
        .movies, .all-movies {
           width: 100%;
           justify-content: space-between;
       }  

        .searched-movies {
            flex-direction: column;
            overflow-y: scroll;
            height: 400px;
            width: 100%;
        }
        .search-container {
            top: 11%;
            left: 70%;
        }
   }

   @media screen and (max-width: 320px) {
       .search-container {
        top: 11%;
        left: 50%;
       }
   }
  
</style>

