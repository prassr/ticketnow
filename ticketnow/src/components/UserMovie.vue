<style scoped>
    
   
     .movie-container { 
         width: px;  
         height: 370px; 
         margin: 0 auto;  
         border-radius: 10px; 
         padding: 10px; 
         margin: 5px;  
         background-size: 200px; 
         background-repeat: no-repeat; 
     } 
 
    
     .title { 
         background-color: rgba(0, 0, 0, 0.8); 
         padding: 3px; 
         border-radius: 10px; 
         text-align: center; 
         max-height: fit-content; 
    
     } 
     .info {
        background-color: rgba(125, 125, 125, 0.1);
        padding: 12px;
        border-radius: 12px;
       line-height: 20px; 
    }       
     /* upper code is for user  */
     input {
        height: 30px;
        margin: 5px !important;

    } 
     .poster {
        width: 90%;
        height: 350px;
        margin-bottom: 10px; 
    } 
    
    .container-fluid {
        position: fixed !important;
        max-width: fit-content;
        top: 15%;
        left: 25%;
        border-radius: 10px !important;
    }

    * {
        color: black !important;
         color: rgba(235,235,235, 1); 
    }

    input {
        width: 250px;
        height: 30px;
        margin: 5px !important;

    }
    
    .left-side, .right-side {
        min-width: fit-content !important;
        width: 250px;
    }
    
    .right-right-side {
       height: 200px;
       overflow: scroll;
    }

    .poster {
        border-radius: 10px;
        width: 230px;
        height: 320px;
        margin-bottom: 10px;
        display: flex;
    }
    .wrapper {
        margin: 0 auto !important;
        display : flex;
        flex-direction:column;
        justify-content: center !important;
        max-width: fit-content;
        padding: 10px;
        background-color: #fff;
        border: 2px solid #f1f1f1;
        border-radius: 15px 0 15px 0;
        background-color: rgba(0, 0, 0, .7);
        box-shadow: 1px 1px 5px 5px rgba(0, 0, 0, 0.2) !important;
        background-color: #fff;
    }

    .buttons {
        margin-top: 20px;
        padding: 5px;
        display: flex;
        flex-direction: row;
        justify-content: left;
        opacity: 0;
        height: 0px;
    }

    .wrapper:hover > .buttons {
        flex-direction: row;
        justify-content: center;
        display: flex;
        opacity: 1;
    }


    .wrapper:hover  .buttons {
        opacity: 1;
        height: 50px;

        transition: height 0.3s ease-in, opacity 0.5s ease-in;
        
    }

    .button > button {
        
        height: 35px;
        width: 100%;
        padding: 1px;
        text-align: center;
        display: flex;
        justify-content: center;
        align-items: center;
        border: none;
        background: transparent;
    }
    .button {
        width: 45%;
    }
    .button:hover {
        cursor: pointer;
    }
    .edit, .update {
        border-radius: 10px  0 0 10px;
        background-color: rgb(30, 153, 30);
    } 
    .delete, .cancel {
        border-radius: 0  10px 10px 0;
        background-color: rgb(187, 43, 43);
    }
    button > svg, button > img {
        height: 25px;
        width: 25px;
        padding: 3px;
    }
      /* For movie  */
     .movies {
        margin: 25px;
        margin-left: 5%;
        display: flex;
        flex-wrap: wrap;
        flex-direction: row;
        justify-content: flex-start;
        gap: 20px 20px;
    } 
     .movie:hover {
        cursor: pointer;
    } 
    label {
        display: none;
    }
    label {
        position: relative;
        opacity: 0;
        left: 10px;
        top: -30px;
        color: #fff;
    }
    .h-input:focus + label {
        display: block;
        top: -35px;
        opacity: 1;
    } 
     .h-input:focus {
        position:relative;
        top: 15px;
    }
  
    .col-auto {
        margin: 0px !important;
    }
    hr {
        width: 75%;
        margin: 0;
        margin-bottom: 5px;
        position: relative;
        z-index: 1;
    }

    .top {
        z-index: 1000;
    }
    
    a:hover {
        background: none;
        max-height: fit-content;
     }

    @media screen and (max-width: 900px){
        .wrapper {
            flex-direction: column;
            justify-content: center;
            margin: 0 auto !important;
            position: relative;
             left: -20%;  
             left: 33%;  
       }
        img {
             margin-left: 15px !important; 
             margin: 0 auto; 
        }
    }
    
     .movie-sub-container div {
         min-width: fit-content;
         width: 200px
     }

    .info {
        height: 200px;
        overflow: scroll;
    }
    
</style>

<template>
    <div class='movie-container'>
        <div class="movie-sub-container">
            <div class="">
                <router-link :to="getMovieLink(movie?.movie_id)" v-slot="{Component}">
                    <img class="poster" :src="movie?.poster" :alt="movie.name"/>
                    <strong>{{ movie.name }}</strong><br>
                </router-link>
            </div>
        </div>
    </div>
</template>

<script>
import {getMovieById}  from '@/js/requests.js';

export default {
    name: "UserMovie",
    props: {
        movie: {
            type: Object,
        },
        getAllMovies: Function,
    },  
    data() {
        return {
        }
    },
    computed: {

    },
    methods: {
        getMovieLink(movieId) {
      // Create the dynamic named route link using the movieId as a parameter
            return {
                name: 'explore_movie',
                params: {
                id: movieId,
                },
            };
        },
        async getMovie(movie_id) {
            let api_key = this.$store.getters.getApiKey;
            try {
                let data = await getMovieById(movie_id, api_key);
                this.movie = data;
                console.log("This is data: ", this.movie);
            } catch (e) {
                alert("Oops! Something went wrong.");
            }
        },
    },
}
</script>
