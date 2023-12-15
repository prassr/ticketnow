<style scoped>
    
    .container-fluid {
        position: fixed !important;
        max-width: fit-content;
        top: 15%;
        left: 25%;
        border-radius: 10px !important;
    }

    * {
        color: black !important;
        /* color: rgba(235,235,235, 1); */
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

    @media screen and (max-width: 900px){
        .wrapper {
            flex-direction: column;
            justify-content: center;
            margin: 0 auto !important;
            position: relative;
            /* left: -20%;  */
            /* left: 33%;  */
       }
        img {
            /* margin-left: 15px !important; */
            /* margin: 0 auto; */
        }
    }
    
    

    .info {
        height: 200px;
        overflow: scroll;
    }
    
</style>

<template>
    <div class="notification" v-if="is_unauth">
        <p>Your session has been expired. Kindly log in again.</p>
    </div>
    <div class='main'>
        <div class="wrapper" v-if="! edit_form">
            <div class="left-side">
                <img class="poster" v-if="!edit_form" :src="movie?.poster" :alt="movie.name"/>
            </div>
            <div class="right-side">
                    <strong>{{ movie.name }}</strong><br>
                    <hr/>

                <div class="info" v-if="! edit_form">

                <table>
                <tr>
                    <td><b>Language:</b></td>
                    <td>{{ movie.language }}</td>
                </tr>
                <tr>
                    <td><b>Genres:</b></td>
                    <td>{{ movie.genres }}</td>
                </tr>
                <tr>
                    <td><b>Runtime:</b></td>
                    <td>{{ movie.runtime_min }} min.</td>
                </tr>
                <tr>
                    <td><b>Release date:</b></td>
                    <td>{{ movie.release_date.split("00")[0] }}</td>
                </tr>
                <tr>
                    <td><b>Cast:</b></td>
                    <td>{{ movie.cast }}</td>
                </tr>
                <tr>
                    <td><b>Director:</b></td>
                    <td>{{ movie.director }}</td>
                </tr>
                <tr>
                    <td><b>Writer:</b></td>
                    <td>{{ movie.writer }}</td>
                </tr>
                <tr>
                    <td><b>Certificate:</b></td>
                    <td>{{ movie.certificate }}</td>
                </tr>
                </table>

                </div>
                <div class="buttons">
                    <div class="edit button" v-if="! edit_form" @click.prevent="editMovie" title="Edit">
                        <button><img class="" src="@/assets/icons-svg/edit-black.svg" alt="edit"/></button>
                    
                    </div>
                    <div class="delete button" v-if="! edit_form" @click.prevent="deleteMovie(movie.movie_id)" title="Delete">
                        <!-- <img class="" src="@/assets/icons-svg/trash.svg" alt="delete"/> -->
                        <button><svg xmlns="http://www.w3.org/2000/svg" height="1em" viewBox="0 0 448 512">
                            <path d="M135.2 17.7L128 32H32C14.3 32 0 46.3 0 64S14.3 96 32 96H416c17.7 0 32-14.3 32-32s-14.3-32-32-32H320l-7.2-14.3C307.4 6.8 296.3 0 284.2 0H163.8c-12.1 0-23.2 6.8-28.6 17.7zM416 128H32L53.2 467c1.6 25.3 22.6 45 47.9 45H346.9c25.3 0 46.3-19.7 47.9-45L416 128z"/>
                        </svg></button>
                    </div>
                </div>

            </div>
        </div>
        <form @submit.prevent="updateMovie" id="update_movie" :key="movie.movie_id">
            <div class="wrapper" v-if="edit_form">
                <div class="left-side">
                    <div class="col-auto">
                        <input type="file" accept="image/*" :id="'formFile_'+movie.movie_id" @change.prevent="encodeImageFileAsURL(movie.movie_id)"/>
                    </div>
                    <img class="poster" :src="poster"/>
                </div>
                <div class="right-side right-right-side">
                    <div class="col-auto">
                        
                        <input type="text" class="form-control h-input" :placeholder="name_title" v-model="name" required>
                        <!-- <label for="name">Name</label> -->
                    </div>
                    <div class="col-auto" >
                        <input type="text" class="form-control h-input " :placeholder="lang_title" v-model="language" required>
                        <!-- <label for="name">Language</label> -->
                    </div>
                    <div class="col-auto">
                        <input type="text" class="form-control h-input " :placeholder="gen_title" v-model="genres" required>
                        <!-- <label for="name">Genres</label> -->
                    </div>
                    <div class="col-auto">
                        <input type="number" min="0" max="500" class="form-control h-input " :placeholder="rt_title" v-model="runtime_min"  required>
                        <!-- <label for="name">Runtime in min</label> -->
                    </div>
                    <div class="col-auto">
                        <input type="date" class="form-control h-input" :placeholder="rd_title"  v-model="release_date" required>
                        <!-- <label for="name">Release Date</label> -->
                    </div>
                    <div class="col-auto">
                        <input type="textarea" class="form-control h-input " :placeholder="plot_title" v-model="plot" @blur="plot_title='Plot'">
                        <!-- <label for="name">Plot</label> -->
                    </div>
                    <div class="col-auto">
                        <input type="text" class="form-control h-input " :placeholder="cast_title" v-model="cast" required>
                        <!-- <label for="name">Cast</label> -->
                    </div>
                    <div class="col-auto">
                        <input type="text" class="form-control h-input " :placeholder="dir_title" v-model="director" required>
                        <!-- <label for="name">Director</label> -->
                    </div>
                    <div class="col-auto">
                        <input type="text" class="form-control h-input " :placeholder="wri_title" v-model="writer" >
                        <!-- <label for="name">Writer</label> -->
                    </div>
                    <div class="col-auto">
                        <input type="text" class="form-control h-input " :placeholder="cert_title" v-model="certificate" required>
                        <!-- <label for="name">Certificate</label> -->
                    </div>
                </div>

                <div class="buttons">
                    <div class="col-auto button update">
                        <button><img class="" src="@/assets/icons-svg/check-black.svg" alt="Update" title="Update"/></button>
                    </div>
                    <div class="col-auto button cancel" @click.prevent="clearForm">
                        <button><img class="" src="@/assets/icons-svg/delete-black.svg" alt="Cancel" title="Cancel"/></button>
                    </div>
                </div>
            </div>
        </form>
    </div>
</template>

<script>
import {getMovieById, updateMovieById, deleteMovieById, unAuthRedirect}  from '@/js/requests.js';
import { stringifyQuery } from 'vue-router';
export default {
    props: {
        movie: {
            type: Object,
        },
        index: Number,
    },
    name: "AdminMovie",
    data() {
        return {
            name: "",
            name_title: "Name",
            language:"",
            lang_title: "Language",
            poster: "",
            genres: "",
            gen_title: "Genres",
            runtime_min:"",
            rt_title: "Runtime in minutes",
            release_date: "",
            rd_title: "Release Date",
            plot: "",
            plot_title: "Plot",
            cast: "",
            cast_title: "Cast",
            director: "",
            dir_title: "Director",
            writer:"",
            wri_title: "Writer",
            certificate:"",
            cert_title: "Certificate",
            edit_form: false,
            is_unauth: false,
        }
    },
    computed: {
        new_poster() {
            return this.poster;
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

        updateMovieData(index, data) {
            this.$emit('updateMovieData', index, data)
        },
        deleteParentMovie(index) {
            this.$emit('deleteParentMovie', index)
        },
        encodeImageFileAsURL(id) {
            let file = document.querySelector('#formFile_'+id).files[0]??"";


            var reader = new FileReader();
            reader.onloadend = () => {
                let rawImg = reader.result;
                this.poster = rawImg;
                console.log(this.poster);
            }

            this.poster = reader.readAsDataURL(file);
            console.log(this.poster);
        },

        editMovie() {
            this.edit_form = true;
            this.name = this.movie.name;
            this.language = this.movie.language;
            this.poster = this.movie.poster;
            this.genres = this.movie.genres;
            this.runtime_min = this.movie.runtime_min;
            this.release_date = this.formatDate(this.movie.release_date);
            this.plot = this.movie.plot;
            this.cast = this.movie.cast;
            this.director = this.movie.director;
            this.writer = this.movie.writer;
            this.certificate = this.movie.certificate;
        },
        
        formatDate(inputDate) {
            const dateObj = new Date(inputDate);
            const addLeadingZero = (num) => (num < 10 ? "0" + num : num);
            const day = addLeadingZero(dateObj.getDate());
            const month = addLeadingZero(dateObj.getMonth() + 1);
            const year = dateObj.getFullYear();
            const formattedDate = `${year}-${month}-${day}`;
            return  formattedDate;
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
            this.edit_form = false;
        },

        async updateMovie(){
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
            try {
                const resp = await updateMovieById(d, this.movie.movie_id, api_key);
                this.edit_form = false;
                this.updateMovieData(this.index, resp);
                alert("Movie updated successfully!");
                this.clearForm();
            } catch (e) {
                const is_un_auth = this.unAuth(e);
            }
        }, 

        async deleteMovie(id) {
            const del = confirm("Do you really want to delete this movie?");
            let api_key = this.$store.getters.getApiKey;
            try {
                if (del) {
                    const deleted = await deleteMovieById(id, api_key)
                    if (deleted) {
                        alert("Movie deleted successfully!");
                        this.deleteParentMovie(this.index);
                    }
                }
                
            } catch (e) {
                const is_un_auth = this.unAuth(e);
            }
                

        },
    },
}

</script>
