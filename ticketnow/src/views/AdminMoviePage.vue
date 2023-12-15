<template>
    <div class="notification" v-if="is_unauth">
        <p>Your session has been expired. Kindly log in again.</p>
    </div>
     <button @click="show_form = !show_form" class="add_button" title="Add Movie"><img src="@/assets/icons-svg/plus-black.svg" alt="Add" /></button>

    <div class="container-fluid" v-if="show_form" style="{ z-index: 1000;}">
        <form @submit.prevent="addMovie" class="" id="add_movie">
            <div class="wrapper">
                <div class="left-side">
                    <div class="col-auto">
                        <input type="file" accept="image/*" id="formFile" @change="encodeImageFileAsURL()"/>
                    </div>
                    <img :src="poster" alt="Select movie poster"/>
                </div>
                <div class="right-side">
                    <div class="col-auto">
                        <input type="text" class="form-control h-input" id="" :placeholder="name_title" v-model="name"  required>
                        <!-- <label for="name">Name <span style="color:red;">*</span></label> -->
                    </div>
                    <div class="col-auto" >
                        <input type="text" class="form-control h-input " id="" :placeholder="lang_title" v-model="language"  >
                        <!-- <label for="name">Language <span style="color:red;">*</span></label> -->
                    </div>
                    <div class="col-auto">
                        <input type="text" class="form-control h-input " id="" :placeholder="gen_title" v-model="genres"  required>
                        <!-- <label for="name">Genres <span style="color:red;">*</span></label> -->
                    </div>
                    <div class="col-auto">
                        <input type="number" min="0" max="500" class="form-control h-input " id="" :placeholder="rt_title" v-model="runtime_min"   required>
                        <!-- <label for="name">Runtime in min <span style="color:red;">*</span></label> -->
                        <input type="date" class="form-control h-input " id="" :placeholder="rd_title"  v-model="release_date"  required>
                        <!-- <label for="name">Release Date <span style="color:red;">*</span></label> -->
                    </div>
                    <div class="col-auto">
                        <input type="textarea" class="form-control h-input " id="" :placeholder="plot_title" v-model="plot" >
                        <!-- <label for="name">Plot</label> -->
                    </div>
                    <div class="col-auto">
                        <input type="text" class="form-control h-input " id="" :placeholder="cast_title" v-model="cast"  required>
                        <!-- <label for="name">Cast <span style="color:red;">*</span></label> -->
                    </div>
                    <div class="col-auto">
                        <input type="text" class="form-control h-input " id="" :placeholder="dir_title" v-model="director"  required>
                        <!-- <label for="name">Director <span style="color:red;">*</span></label> -->
                    </div>
                    <div class="col-auto">
                        <input type="text" class="form-control h-input " id="" :placeholder="wri_title" v-model="writer"  required>
                        <!-- <label for="name">Writer <span style="color:red;">*</span></label> -->
                    </div>
                    <div class="col-auto">
                        <input type="text" class="form-control h-input " id="" :placeholder="cert_title" v-model="certificate"  required>
                        <!-- <label for="name">Certificate <span style="color:red;">*</span></label> -->
                    </div> 
                    <div class="buttons">
                        <div class="col-auto button add">
                            <button><img src="@/assets/icons-svg/check-black.svg" alt="Add" title="Add"/></button>
                        </div>
                        <div class="col-auto button cancel" @click.prevent="clearForm">
                            <button><img src="@/assets/icons-svg/delete-black.svg" alt="Cancel" title="Cancel"/></button>
                        </div>
                    </div>
                </div> <!-- left-side -->
                
            </div> <!-- wrappr --> 
           
        </form>
    </div>
    <div class="movies">
        <admin-movie class="movie" v-for="(movie, index) in movies" :movie="movie" :key="movie.movie_id" @updateMovieData="updateThisMovie" @deleteParentMovie="deleteMovie" :index="index"></admin-movie>
    </div>
    <router-view></router-view>
</template>

<script>
import AdminMovie from '@/components/AdminMovie.vue'
import {createMovie, getMovies, unAuthRedirect} from '@/js/requests.js'

export default {
    name: "AdminMoviePage",
    components: {
        AdminMovie,
    },
    computed: {
    },
    created() {
        this.getAllMovies();
    },      
    data() {
        return {
            isFocused: false, // for new style
            name: "",
            language:"",
            poster:"",
            genres: "",
            runtime_min:"",
            release_date: "",
            plot: "",
            cast: "",
            director: "",
            writer:"",
            certificate:"",
            name_title: "Name",
            lang_title: "Language",
            gen_title: "Genres",
            rt_title: "Runtime in minutes",
            rd_title: "Release Date",
            plot_title: "Plot",
            cast_title: "Cast",
            dir_title: "Director",  
            wri_title: "Writer",           
            cert_title: "Certificate",
            show_form: false,
            movies: null,
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
        encodeImageFileAsURL() {
            var file = document.querySelector('input[type=file]').files[0];
            var reader = new FileReader();
            let rawImg;
            reader.onloadend = () => {
                rawImg = reader.result;
                this.poster = rawImg;
            }

            this.poster = reader.readAsDataURL(file);
        },
        clearForm() {
            this.name = "";
            this.language ="";
            this.poster ="";
            this.genres = "";
            this.runtime_min ="";
            this.release_date = "";
            this.plot = "";
            this.cast = "";
            this.director = "";
            this.writer ="";
            this.certificate ="";
            this.show_form = false;
        },

        deleteMovie(index){
            if (index >= 0 && index <   this.movies.length) {
                this.movies.splice(index, 1);
            }
        },


        updateThisMovie(id, d) {
            this.movies[id].name = d.name;
            this.movies[id].language = d.language;
            this.movies[id].poster = d.poster;
            this.movies[id].genres = d.genres;
            this.movies[id].runtime_min = d.runtime_min;
            this.movies[id].release_date = d.release_date;
            this.movies[id].plot = d.plot;
            this.movies[id].cast = d.cast;
            this.movies[id].director = d.director;
            this.movies[id].writer =d.writer;
            this.movies[id].certificate =d.certificate;
        },

        async addMovie(){
            const d = {
                name: this.name,
                language: this.language,
                poster: this.poster,
                genres: this.genres.toLowerCase(),
                runtime_min: this.runtime_min,
                release_date: this.release_date,
                plot: this.plot,
                cast: this.cast,
                director: this.director,
                writer: this.writer,
                certificate: this.certificate.toUpperCase(),
            };
            let api_key = this.$store.getters.getApiKey;
            console.log("hello "+d.poster);
            try {
                const resp = await createMovie(d, api_key);
                this.movies.push(resp);
                this.show_form = false;
                this.clearForm();
                alert("Movie added successfully!");
            } catch (e) {
                const is_un_auth = this.unAuth(e);
            }
        }, 
        async getAllMovies(){
            let api_key = this.$store.getters.getApiKey;
            try {
                this.movies = await getMovies(api_key);
            } catch (e) {
                const is_un_auth = this.unAuth(e);
            }

        }
    },
}

</script>


<style scoped>
    @import  '/src/css/form.css';
    input {
        height: 30px;
        margin: 5px !important;
    }
    img {
        width: 90%;
        height: 350px;
        z-index:1;
        color: green;
        /* margin-left: 5px !important; */
        position: relative;
        border-radius: 10px;
        left: 0;
    }

    .container-fluid {
        /* position: fixed !important; */
        max-width: fit-content;
        z-index: 2;
        top: 20%;
        /* left: 30%; */
        border-radius: 10px !important;
    }
    .wrapper {
        position: fixed;
        left: 0;
        right: 0;
        top: 150px;
        bottom: 200px;
        z-index: 1000;
        margin: 0 auto !important;
        display : flex;
        justify-content: center !important;
        max-width: fit-content;
        min-height: fit-content;
        height: 450px;
        padding: 10px;
        background-color: #fff;
        border: 2px solid #f1f1f1;
        border-radius: 10px;
        box-shadow: 1px 1px 5px 5px rgba(0, 0, 0, 0.2) !important;
    }

    .left-side, .right-side {
        width: 300px !important;
    }
    .buttons {
        margin-top: 10px;
        padding: 5px;
        display: flex;
        flex-direction: row;
        justify-content: left;
        margin-top: 20px;
        padding: 5px;
        display: flex;
        flex-direction: row;
        justify-content: left;

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

    button > svg, button > img {
        height: 25px;
        width: 25px;
        padding: 3px;
    }

    .add {
        border-radius: 10px  0 0 10px;
        background-color: rgb(30, 153, 30);
    } 
    .cancel {
        border-radius: 0  10px 10px 0;
        background-color: rgb(187, 43, 43);
    }

    /*  For movie */
    .movies {
        margin: 25px;
        margin-left: 5%;
        margin-top: 10%;
        display: flex;
        flex-wrap: wrap;
        min-width: fit-content;
        flex-direction: row;
        justify-content: left;
        gap: 20px 20px;
    }

    @media screen and (max-width: 600px){
        .wrapper {
            flex-direction: column;
            justify-content: center;
            position: relative;
            top: 20px;
            z-index: 0;
            /* left: -20%;  */ 
        }
    }
    @media screen and (max-width: 600px) {
        .movies {
            justify-content: center;
        }
    }
</style>

