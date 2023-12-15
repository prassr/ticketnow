<style scoped>
    .page {
        margin-top: 100px;
    }

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

    .search-container {
        z-index: 2000;
        position: fixed;
        top: 5%;
        bottom: 0;
        left: 50%;
        min-height: fit-content;
        transform: translateX(-50%);

   }

   .theatre-box {
        background-color: rgba(0, 0, 0, 0.692);
        color: rgba(255, 255, 255, 0.781);
        padding: 10px 10px 10px 20px;
        width: 500px;
        border-radius: 10px;
        margin-bottom: 10px;
        min-height: fit-content;
   }

   .theatre-box, .show-box, .show-info, .theatre-info {
        cursor: pointer !important;
    }


    .wrapper {
        display: flex;
        flex-direction: row;
        justify-content: center;
    }

    .shows {
        color: rgba(255, 255, 255, 0.795);
        width: 500px;
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
        position: fixed;
        left: 0;
        right: 0;
        bottom: 20px;
        margin: 0 auto;
        padding: 20px;
        border-radius: 10px;
        background-color: rgba(255, 255, 255, 0.836);
        height: 200px;
        overflow-y: scroll;
        overflow: overlay;
    }

    .show-box {
        width: 95%;
        min-height: fit-content;
        background-color: rgb(105, 43, 15);
        padding: 10px;
        margin: 10px;
        border-radius: 10px;
    }

    a {
        color: rgba(255, 255, 255, 0.726);
        height: 100px;
    }

    .show-list {
        display: inline-block;
    }
    @media screen and (max-width: 1024px) {
        .search-container {
            top: 7%;

        }
   }

   @media screen and (max-width: 425px){
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

<template>
    <div class="notification" v-if="is_unauth">
        <p>Your session has been expired. Kindly log in again.</p>
    </div>
    <div class="page">
        <div class="search-container">
            <div class="search">
                <input type="text" v-model="searchTerm" @input="performSimpleSearch" placeholder="Search for venue">
            </div>
        </div>
        <div class="wrapper">
	        <div class="theatres">
	            <div class="theatre-box" v-for="(tdata, tid) in filteredTheatres" :key="tid" @click.prevent="showsForTheatre(tid)">
	                <div class="theatre-info" :title="`${tdata.shows.length} show(s) available`">
	                    {{ tdata.theatre_name }}<br>
	                    {{ tdata.address + ", "+ tdata.city +", "+ tdata.zip_code }}<br>
                        {{ tdata.facilities  }} available
	                </div>
	            </div>
	        </div>
        </div>

        <div class="shows" v-if="showsByTheatreId.length > 0">
            <div class="show-box" v-for="(show, index) in showsByTheatreId" :key="index">
                <div class="show-info">
                    <router-link class="anchor" :to="{name:'book_for_show', params: {'show_id':show.show_id}}">
                        <div class="show-list">
                            <span><strong>{{  show.movie_name }}</strong></span><br>
                            <span>
                                {{ show.start_time.split(" ").slice(0, 2).join(" ") + " " + format12(show.start_time.split(" ")[2]) }} 
                            </span> | {{  show.sound }}
                        </div>
                    </router-link>
                </div>
            </div>
        </div>
    </div>
</template>

<script>

import { getShowsByTheatre, unAuthRedirect } from "@/js/requests.js";
import { clog, dalay, convertTo12HourFormat } from "@/js/helpers.js"
const fuzzball = require('fuzzball')

export default {
    name: "TheatrePage",
    components: {

    },
    created() {
        this.getShowsForTheatre()
    },  
    data() {
        return {
            theatreAndShow: [],
            showsByTheatreId: [],
            filteredTheatres: [],
            is_unauth: false,
            searchTerm: "",
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

        getDateFormatted(dt) {
            const parts = dt.split(" ");
            const dateParts = parts[1].split("/");
            const timeParts = parts[2].split(":");
            const jsDate = new Date(
            `${dateParts[2]}-${dateParts[1]}-${dateParts[0]}T${timeParts[0]}:${timeParts[1]}:${timeParts[2]}`
            );
            return jsDate;
        },
        getSortedShows(s = []) {
            if (s==[]) {
                return []
            }
            return s.sort((a, b) => {
                const dateA = new Date(this.getDateFormatted(a.start_time));
                const dateB = new Date(this.getDateFormatted(b.start_time));
                return dateA - dateB;
         }).filter(s => {
            const currDate = new Date();
            const dateA = new Date(this.getDateFormatted(s.start_time));
            return dateA >= currDate;

         });
        },

        performSimpleSearch() {
            const s = this.searchTerm.toLocaleLowerCase()
            if ( s == "") {
                this.filteredTheatres = this.theatreAndShow;
            }
            if (s.length > 0 ) {
                this.filteredTheatres = Object.values(this.theatreAndShow).filter(theatre => {
                    if (
                        fuzzball.partial_ratio(theatre.theatre_name.toLowerCase(), s) > 85 ||
                        fuzzball.partial_ratio(theatre.address.toLowerCase(), s) > 85 ||
                        fuzzball.partial_ratio(theatre.city.toLowerCase(), s) > 85 ||
                        fuzzball.partial_ratio(theatre.state.toLowerCase(), s) > 85 ||
                        fuzzball.partial_ratio(theatre.zip_code.toLowerCase(), s) == 100 ||
                        fuzzball.partial_ratio(theatre.facilities.toLowerCase(), s) > 85
                    ) {
                        return true;
                    }
                })
            }
            return;
        },

        format12(time) {
            return convertTo12HourFormat(time);
        },
        showsForTheatre(tid) {
            this.showsByTheatreId = this.getSortedShows(this.theatreAndShow[tid].shows);
            if (this.showsByTheatreId.length == 0) {
                alert("Currently no shows available for this venue.");
            }
        },
        async getShowsForTheatre() {
            const api_key = this.$store.getters.getApiKey;
            try {
                const data = await getShowsByTheatre(api_key);
                this.theatreAndShow = data;
                this.filteredTheatres = this.theatreAndShow;
            } catch (e) {
                const is_un_auth = this.unAuth(e);
            }
        }
    },
}

</script>
