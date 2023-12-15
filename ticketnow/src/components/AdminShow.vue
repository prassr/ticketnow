<style scoped>   
    * {
        box-sizing: border-box;
    }
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
    .col-auto {
        display: flex;
        align-items: center;
        justify-content: center;
        flex-direction: column;
    }
    .wrapper {
        width: 25%;
        /* z-index: 200; */
        margin: 0 auto !important;
        display : flex;
        flex-direction: column !important;
        /* justify-content: center !important; */
        /* max-width: fit-content; */
        padding: 5px;
        border: 1px solid #f1f1f1;
        border-radius: 10px;
        box-shadow: 1px 1px 5px 5px rgba(0, 0, 0, 0.2) !important;
        background-color: #fff;
        min-width: fit-content;
        
        max-height: fit-content !important;
        width: 350px;
        /* position: relative; */
        margin: 2% 4% !important;
        height: 250px;
        
    }

    .wrapper:hover {
        height: 270px;
        transition: height 0.3s ease;
    }
    .mbuttons {
        /* z-index:200; */
        margin-top: 20px;
        position: relative;
        top: 2;
        left: 2;
        height: 0; /* Buttons hidden by default */
        opacity: 0;
        bottom: 10px
    }

    .buttons {
        margin-top: 10px;
        display: flex;
        flex-direction: row;
        justify-content: center;
        /* display: none; */      
    }
    .wrapper:hover > .mbuttons {
        flex-direction: row;
        justify-content: center;
        display: flex;
        height: 50px;
        opacity: 1;
        transition: height 1s ease, opacity 1s ease-in;
    }
    .button > button {
        margin: 0.5px;
        height: 35px;
        width: 100%;
        padding: 0;
        text-align: center;
        display: flex;
        justify-content: center;
        align-items: center;
        border: none;
        background: transparent;
    }
    
    .mbuttons > .button {
        width: 25%;
        margin: 0.5px;
    }

    .button:hover {
        cursor: pointer;
    }
    .edit, .update{
        border-radius: 10px  0 0 10px;
        background-color: rgb(30, 153, 30);
    } 
    .add {
        background-color: rgb(30, 153, 30);
    }
    .delete, .cancel {
        border-radius: 0  10px 10px 0;
        background-color: rgb(187, 43, 43);
    }
    button > img, button > svg {
        height: 25px;
        width: 25px;
        padding: 3px;
    }
    .button:hover {
        cursor: pointer;
    }
    input {
        height: 30px;
        margin: 1px !important;
        transition: top 3s ease;
    }

    .info {
        position: relative;
        /* left: 20%; */
    }
    .title {
        position: relative;
        left: 0;
        text-align: center;
        
    }
    table {
        margin: 0 auto;
    }
    .mwrapper {
        z-index: 10;
        margin-top: 5px;
        /* display : flex; */
        flex-direction: row;
        justify-content: center !important;
        padding: 10px !important;
        min-width: fit-content;
        min-height: fit-content;
        width: 350px;
        border: 1px solid #f1f1f1;
        border-radius: 10px;
        box-shadow: 1px 1px 5px 5px rgba(0, 0, 0, 0.2) !important;
        background-color: #fff;
        margin: 2% 4% !important;
        /* height: 260px; */
    }

    .buttons > .button {
        width: 35% !important;
    }
    .screens {
        margin: 200px;
        position: relative;
        top: -215px;
        left: 29%;
        margin: 0px;
        display: flex;
        flex-direction: row !important;
        margin: 2% 4% !important;
        background-color: white;
        width: 400px;
        height: 190px;
        /* display: none; */
    }
    .mbuttons a {
        width: 100%;
        margin: 0;
        height: 100%;
        
    }
    .screen {
        margin-left: 25px;
        width:150px;
        height: 190px;
        overflow-y: scroll;
        background-color: blue;
    }
    a {
        padding: 0px;
    }
    a:hover {
        background-color: inherit;
    }
    .view img {
        margin-top: 10px;
    }
    [v-vloak] {
        display: none;
    }
</style>

<template>
    <div class="notification" v-if="is_unauth">
        <p>Your session has been expired. Kindly log in again.</p>
    </div>
    <div class="container-fluid">
        <div class="wrapper" v-if="! edit_form">
                <div class="info" v-if="! edit_form">
                    <div class="title">
                        <strong>{{ show.name }}</strong><br>
                    </div>
                    <div class="desc">
                        <table>
                            <tr>
                                <td><b>Movie:</b></td>
                                
                                <td style="{ text-overflow: clip; }"> {{ movie?.name }} </td>
                            </tr>
                            <tr>
                                <td><b>Language:</b></td> 
                                <td> {{ show?.language }} </td> 
                            </tr>
                            <tr>
                                <td><b>Scheduled at:</b></td> 
                                <td> {{ show.start_time.split("-")[0] }} </td> 
                            </tr>
                            <tr>
                                <td><b>Venue:</b></td> 
                            <td> {{ theatre?.name }} {{ theatre?.address }} </td> 
                            </tr>
                            <tr>
                                <td><b> Prices: </b></td>
                            <td> C1: &#8377; {{ show.price_1 }}, C2: &#8377; {{ show.price_2 }} C3: &#8377; {{ show.price_3 }} </td> 
                            </tr>
                        </table>
                    </div>
                </div>
                <div class="mbuttons">
                    <div class="edit button" v-if="! edit_form" @click.prevent="editShow" title="Edit show">
                        <button><img class="" src="@/assets/icons-svg/edit-black.svg" alt="edit"/></button>
                    </div>
                    <!-- <div class="add button" v-if="! edit_form" @click.prevent="addScreen" title="Add screen"> -->
                    <!--     <img class="" src="@/assets/icons-svg/plus-black.svg" alt="edit"/> -->
                    <!-- </div> -->
                    <div class="delete button" v-if="! edit_form" @click.prevent="deleteShow(show.show_id)" title="Delete show">
                        <!-- <img class="" src="@/assets/icons-svg/trash.svg" alt="delete"/> -->
                        <button>
                            <svg xmlns="http://www.w3.org/2000/svg" height="1em" viewBox="0 0 448 512">
                                <path d="M135.2 17.7L128 32H32C14.3 32 0 46.3 0 64S14.3 96 32 96H416c17.7 0 32-14.3 32-32s-14.3-32-32-32H320l-7.2-14.3C307.4 6.8 296.3 0 284.2 0H163.8c-12.1 0-23.2 6.8-28.6 17.7zM416 128H32L53.2 467c1.6 25.3 22.6 45 47.9 45H346.9c25.3 0 46.3-19.7 47.9-45L416 128z"/>
                            </svg>
                        </button>
                    </div>
                </div>
        </div>
        <form @submit.prevent="updateShow" id="update_show" :key="show.show_id">
            <div class="mwrapper" v-if="edit_form">
            <table v-cloak>
                <tbody>
                    <tr>
                      <td>
                        <label for="movieSelect">Movie: </label>
                      </td>
                      <td>
                        <select id="movieSelect" v-model="movie_id" required>
                          <option value="">select</option>
                          <option v-for="mv in movies" :key="mv.movie_id" :value="mv.movie_id" required :selected="mv.movie_id== movie.movie_id">
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
                        <input type="text" id="languageInput" class="form-control" v-model="language" :placeholder="lang_title" required>
                      </td>
                  </tr>
                  <tr>
                      <td>
                        <label for="theatreSelect">Theatre: </label>
                      </td>
                      <td>
                        <select id="theatreSelect" v-model="theatre_id" required>
                          <option value="">select</option>
                          <option v-for="th in theatres" :key="th.theatre_id" :value="th.theatre_id" required :selected="th.theatre_id == theatre.theatre_id">
                                        {{ th.name }}
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
                        <input class="form-control" type="date" id="datePicker" :min="current_date" v-model="date">
                      </td>
                  </tr>
                  <tr>
                      <td>
                        <label for="timePicker">Time:</label>
                      </td>
                      <td>
                        <input class="form-control" type="time" id="timePicker" v-model="time">
                      </td>
                  </tr>

                </tbody>
              </table>
                    <div class="buttons">
                        <div class="col-auto update button">
                            <button><img class="" src="@/assets/icons-svg/check-black.svg" alt="edit"/></button>
                        </div>
                        <div class="col-auto cancel button" @click.prevent="clearForm">
                            <!-- <button class="btn btn-primary" >Cancel</button> -->
                            <button><img class="" src="@/assets/icons-svg/delete-black.svg" alt="edit"/></button>
                        </div>
                    </div>

            </div>
        </form>
    </div>
</template>

<script>
import {getShowById, updateShowById, getMoviesForShow, deleteShowById, getTheatreById, getScreenById }  from '@/js/requests.js';
// import { fetchIndexDB } from '@/js/indexDB.js';
import { currentDate, clog, delay } from '@/js/helpers.js';

export default {
    name: "AdminShow",
    props: {
        show: {
            type: Object,
        },
        index: Number,
    },
    created() {
        this.movieLoader(this.show.movie_id);
        this.theatreLoader(this.show.screen_id);
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
            edit_form: false,
            movie: null,
            theatre: null, 
            movies: null,
            theatres: null,
            movie_title:"Movie",
            lang_title: "Language",
            theatre_title: "Theatre",
            screen_title:'Screen',
            price_1_title: "Class 1 price",
            price_2_title: "Class 2 price",
            price_3_title: "Class 3 price",
            movie_id: "",
            language: "",
            screen_id:"",
            price_1: null,
            price_2: null,
            price_3:  null,
            formatted_date_time: null,
            date: "",
            time: "",
            current_date:"",
            edit_form: false,
            is_unauth: false,
            movie_id: null,
            languageSuggestions: [],
            theatre_id: "",
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

        updateShowData(index, data) {
            this.$emit('updateShowData', index, data)
        },
        deleteParentShow(index) {
            this.$emit('deleteParentShow', index)
        },

        capitalizeFirstLetter(str) {
            return str.charAt(0).toUpperCase() + str.slice(1);
        },

        editShow() {
            this.edit_form = true;
            this.movie_id = this.show.movie_id;
            this.language = this.show.language;
            this.theatre_id = this.theatre.theatre_id;
            this.screen_id = this.show.screen_id;
            this.price_1 = this.show.price_1;
            this.price_2 = this.show.price_2;
            this.price_3 = this.show.price_3;
            this.selectedMovieName = this.movie.name
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
            this.edit_form = false;
        },
        async movieLoader(id) {
            await delay(100);
            let movies = sessionStorage.getItem('movies');
            let moviesArray = JSON.parse(movies);
            this.movies = moviesArray;
            this.movie = moviesArray.find((movie) => movie.movie_id === id);
        },
        
        async theatreLoader(screen_id) {
            await delay(100);
            let theatres = sessionStorage.getItem('theatres');
            
            let theatresArray = JSON.parse(theatres)
            this.theatres = theatresArray;

            for (const theatre of theatresArray) {
                const foundScreen = theatre.screens?.find((screen) => screen.screen_id === screen_id);
                if (foundScreen) {
                    this.theatre = theatre;
                }
            }
        },
        
        async updateShow(){
            const d = {
                movie_id: this.movie_id,
                language: this.language,
                screen_id: this.screen_id,
                price_1: this.price_1,
                price_2: this.price_2,
                price_3: this.price_3,
                start_time: this.start_time,
            };

            if (this.start_time.length > 0) {
                d["start_time"] = this.start_time;
            }
            else {
                d["start_time"] = this.show.start_time;
            }
            let api_key = this.$store.getters.getApiKey;
            try {
                const resp = await updateShowById(d, this.show.show_id, api_key);
                this.edit_form = false;
                this.updateShowData(this.index, d);
                alert("Show updated successfully!");
            } catch (e) {
                const is_un_auth = this.unAuth(e);
            }
        },
        async deleteShow(id) {
            const del = confirm("Do you really want to delete this show?");
            let api_key = this.$store.getters.getApiKey;
            try {
                if (del) {
                    const deleted = await deleteShowById(id, api_key)
                    if (deleted) {
                        this.deleteParentShow(this.index);
                        alert("Show deleted successfully!");
                    }
                }
            } catch (e) {
                const is_un_auth = this.unAuth(e);
            }
        },
    },
}
</script>
