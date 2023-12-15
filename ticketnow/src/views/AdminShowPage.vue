<style scoped>
    @import '/src/css/form.css';
    input {
        width: 90%;
        height: 30px;
        margin: 3px !important;
        transition: top 3s ease;
    }

    select { 
        background-color: red;
        border: none;
        width: 90%;
        padding: 5px;
        background-color: white;
        border-radius: 10px;
        box-shadow: 1px 1px 1px 1px rgba(0, 0, 0, 0.2) !important;
    }
    img {
        width: 90%;
        height: 350px;
    }
    .container-auto {
        display: flex;
        flex-direction: column;
    }
    .wrapper {
        z-index: 200;
        
        position: fixed;
        top: 150px;
        left: 0;
        right: 0;
        bottom: 200;
        margin: 0 auto !important;
        display : flex;
        justify-content: center !important;
        max-width: fit-content;
        min-height: fit-content;
        padding: 10px;
        background-color: #fff;
        border: 2px solid #f1f1f1;
        border-radius: 10px;
        box-shadow: 1px 1px 5px 5px rgba(0, 0, 0, 0.2) !important;
    }
    .container {
        z-index: 1000;
        margin-top: 0px !important;
        padding: 0px !important;
    }
    .left-side, .right-side {
        width: 300px !important;
    }
    .buttons {
        margin-top: 10px;
        display: flex;
        flex-direction: row;
        justify-content: left;  
    }
    .button > button {
        margin: 0.5px;
        height: 35px;
        width: 100%;
        padding: 5px;
        display: flex;
        flex-direction: row;
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
    .add {
        border-radius: 10px  0 0 10px;
        background-color: rgb(30, 153, 30);
    } 
    .cancel {
        border-radius: 0  10px 10px 0;
        background-color: rgb(187, 43, 43);
    }
    button > img, button > svg {
        height: 25px;
        width: 25px;
        padding: 3px;
    }

    label {
    }
    a {
        padding: 0px !important;
    }

    .shows {
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

</style>

<template>
    <div class="notification" v-if="is_unauth">
        <p>Your session has been expired. Kindly log in again.</p>
    </div>
     <button @click="show_form = !show_form" class="add_button" title="Add Show"><img src="@/assets/icons-svg/plus-black.svg" alt="Add" /></button>
    <div class="container-fluid" v-if="show_form">
        <div class="movie-form container">
        <form @submit.prevent="addShow" class="">
            <div class="wrapper">
            <div class="right-side">
            <table>
                <tbody>
                    <tr>
                      <td>
                        <label for="movieSelect">Movie: </label>
                      </td>
                      <td>
                        <select id="movieSelect" v-model="movie_id" required>
                            <!-- <option value="" selected>select</option> -->
                          <option v-for="mv in movies" :key="mv.movie_id" :value="mv.movie_id">
                                {{ mv.name }}
                          </option>
                        </select>
                      </td>
                    </tr>
                    <tr>
                      <td>
                        <label for="languageInput">Language:</label>  
                      </td>
                      <td>
                        <input type="text" id="languageInput" class="form-control" v-model="language" list="languageSuggestions" :placeholder="lang_title" @input="updateLanguageSuggestions" required>
                        <datalist id="languageSuggestions">
                            <option v-for="lang in languageSuggestions" :key="lang">{{ lang }}</option>
                        </datalist>
                      </td>
                  </tr>
                  <tr>
                      <td>
                        <label for="theatreSelect">Theatre: </label>
                      </td>
                      <td>
                        <select id="theatreSelect" v-model="theatre_id" required>
                          <option value="" selected>select</option>
                          <option v-for="theatre in theatres" :key="theatre.theatre_id" :value="theatre.theatre_id">
                            {{ theatre.name }}
                          </option>
                        </select>
                      </td>
                  </tr>
                  <tr>
                      <td>
                        <label for="screenSelect">Screen: </label>
                      </td>
                      <td>
                        <select id="screenSelect" v-model="screen_id" required>
                          <option value="">select</option>
                          <option v-for="screen in selectedTheatre?.screens" :key="screen.screen_id" :value="screen.screen_id">
                            Capacity: {{ screen.tier_1 + screen.tier_2 + screen.tier_3 }}, Sound: {{ screen.sound }}, {{ screen.is_recliner ? "Recliner" : "Non-recliner" }}
                          </option>
                        </select>
                      </td>
                  </tr>
                  <tr>
                      <td>
                        <label for="priceInput1">Price 1: &#8377;</label>
                      </td>
                      <td>
                        <input type="number" class="form-control" id="" :placeholder="price_1_title" min="0" v-model="price_1" required>
                      </td>
                  </tr>
                  <tr>
                      <td>
                        <label for="priceInput2">Price 2: &#8377;</label>
                      </td>
                      <td>
                        <input type="number" class="form-control" id="" :placeholder="price_2_title" min="0" v-model="price_2" required>
                      </td>
                  </tr>
                  <tr>
                      <td>
                        <label for="priceInput3">Price 3: &#8377;</label>
                      </td>
                      <td>
                        <input type="number" class="form-control" id="" :placeholder="price_3_title" min="0" v-model="price_3" required>
                      </td>
                  </tr>
                  <tr>
                      <td>
                        <label for="datePicker">Date:</label>
                      </td>
                      <td>
                        <input class="form-control" type="date" id="datePicker" :min="current_date" v-model="date" required>
                      </td>
                  </tr>
                  <tr>
                      <td>
                        <label for="timePicker">Time:</label>
                      </td>
                      <td>
                        <input class="form-control" type="time" id="timePicker" v-model="time" required>
                      </td>
                  </tr>

                </tbody>
              </table>
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
        </div> <!-- movie-form container-->
    </div>
    <div class="shows">
        <!-- <div v-for="show in shows" > -->
        <div v-for="(show, index) in shows" :key="show.show_id">
            <admin-show :show="show" @updateShowData="updatePShow" @deleteParentShow="deletePShow" :index="index"/>
        </div>
    </div>
    <router-view></router-view>
</template>

<script>


import AdminShow from '@/components/AdminShow.vue'

import { getTheatres, getMoviesForShow, getShows, createShow, getScreens, unAuthRedirect } from '@/js/requests';

import { currentDate } from '@/js/helpers.js';

export default {
    name: "AdminShowPage",
    components: {
        AdminShow,
    },
    created() {
        this.getAllShows();
        this.getAllMoviesForShow();
        this.getAllTheatres()
        this.current_date = currentDate();
    },    
    computed: {
        selectedTheatre() {
            return this.theatres?.find(theatre => theatre.theatre_id === this.theatre_id);
        },

        start_time() {
            if (this.date && this.time) {
                const dateTimeString = `${this.date} ${this.time}`;
                const datetime = new Date(dateTimeString);
                const istDatetimeString = datetime.toLocaleString("en-IN", {
                timeZone: "Asia/Kolkata",
                hour12: false,
                });
                return istDatetimeString;
            }
            return "";
        },
    },

    data() {
        return {
            shows: [],
            movies: [],
            screens: [],
            theatres: [],
            movie_title:"Movie",
            lang_title: "Language",
            theatre_title: "Theatre",
            screen_title:'Screen',
            price_1_title: "Class 1 price",
            price_2_title: "Class 2 price",
            price_3_title: "Class 3 price",
            movie_id: "",
            language: "",
            theatre_id: "",
            screen_id:"",
            price_1: null,
            price_2: null,
            price_3:  null,
            current_date: currentDate(),
            date: "",
            time: "",
            show_form: false,
            movie_id: null,
            languageSuggestions: [],
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
        
        deletePShow(index){
            if (index >= 0 && index <   this.shows.length) {
                this.shows.splice(index, 1);
            }
        },

        updatePShow(index, s) {
            this.shows[index].movie_id = s.movie_id;
            this.shows[index].language = s.language;
            this.shows[index].screen_id = s.screen_id;
            this.shows[index].price_1 = s.price_1;
            this.shows[index].price_2 = s.price_2;
            this.shows[index].price_3 = s.price_3;
            this.shows[index].start_time = s.start_time;
        },

        updateLanguageSuggestions() {
            const languages = this.movies.reduce((acc, movie) => {
                const movieLanguages = movie.language.split(",");
                return acc.concat(movieLanguages);
            }, []);

            this.languageSuggestions = [...new Set(languages)].map(lang => this.capitalizeFirstLetter(lang));
        },
        capitalizeFirstLetter(str) {
            return str.charAt(0).toUpperCase() + str.slice(1);
        },

        clearForm() {
            this.movie_id= "",
            this.language= "",
            this.theatre_id= "",
            this.screen_id="",
            this.price_1= "",
            this.price_2= "",
            this.price_3= "",
            this.date = "",
            this.time = ""
            this.show_form = false;
        },
        async getAllShows(){
            let api_key = this.$store.getters.getApiKey;
            try {
                this.shows = await getShows(api_key);
            } catch (e) {
                const is_un_auth = this.unAuth(e);
            }
        },
        async getAllTheatres(){
            let api_key = this.$store.getters.getApiKey;
            try {
                this.theatres = await getTheatres(api_key);
                const theatres = JSON.stringify(this.theatres);
                const key = 'theatres';
                sessionStorage.setItem(key, theatres);
            } catch (e) {
                const is_un_auth = this.unAuth(e);

            }
        },
        async getAllScreens(){
            let api_key = this.$store.getters.getApiKey;
            try {
                this.screens = await getScreens(api_key);
            } catch (e) {
                const is_un_auth = this.unAuth(e);
            }
        },
        async getAllMoviesForShow(){
            let api_key = this.$store.getters.getApiKey;
            try {
                this.movies = await getMoviesForShow(api_key);
                const movies = JSON.stringify(this.movies);
                const key = 'movies';
                sessionStorage.setItem(key, movies);

            } catch (e) {
                const is_un_auth = this.unAuth(e);
            }
        },

        async addShow(){
            const d = {
                movie_id: this.movie_id,
                language: this.language,
                screen_id: this.screen_id,
                price_1: this.price_1,
                price_2: this.price_2,
                price_3: this.price_3,
                start_time: this.start_time,
            };
            let api_key = this.$store.getters.getApiKey;
            try {
                const resp = await createShow(d, api_key);
                this.show_form = false;
                alert("Show added successfully!");
                this.shows.push(resp);
            } catch (e) {
                const is_un_auth = this.unAuth(e);
            }
        }, 
    },
}

</script>
