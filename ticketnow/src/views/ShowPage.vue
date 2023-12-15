<style scoped>
    .page {
        margin-top: 75px;
    }
    .show-info {
        background-color: rgba(0, 0, 0, 0.432);
        color: rgba(255, 255, 255, 0.781);
        padding: 10px 10px 10px 20px;
        width: 60%;
        border-radius: 10px;
        margin: 0 auto;
    }
    table, button {
        margin-top: 10px;
    }

    button {
        background: none;
        border-radius: 5px;
        color: rgba(255, 255, 255, 0.74);
        border: none;
        padding: 10px;
        background-color:rgb(0, 128, 0);
    }

    button:active {
        background-color: rgb(4, 58, 4);
    }

    table, tr, td {
        border: 1px solid rgba(255, 255, 255, 0.37);
        padding: 3px;
    }

    .show-info button {
        margin: 10px;
    }

    .form {
        color: rgba(255, 255, 255, 0.795);
        width: 50%;
        display: flex;
        flex-direction: column;
        justify-content: center;
        position: fixed;
        /* top: 40%; */
        left: 0;
        right: 0;
        bottom: 20px;
        margin: 0 auto;
        padding: 20px;
        border-radius: 10px;
        background-color: rgba(31, 18, 18, 0.212)
    }

    .form-table, .form-table tr, .form-table td {
        border: none;
    }

    select {
        width: 100%;
    }
    .cancel {
        background-color: red;
        border: none;
        margin-left: 10px;
    }

    .cancel:hover {
        background-color: brown;
    }
    button {
        border: none;
    }

</style>

<template>
    <div class="page">
        <div class="notification" v-if="is_unauth">
            <p>Your session has been expired. Kindly log in again.</p>
        </div>
        <div class="show-info">
            <div>
                <div>{{  stsm?.movie?.name }}</div>
                <div>{{ show_date }}</div>
                <div>{{ show_time }}</div>
                <div>{{ stsm?.theatre?.name+", "+stsm?.theatre?.address }}</div>
                <table>
                <tr>
                    <th>Class</th>
                    <td>Silver</td>
                    <td>Gold</td>
                    <td>Platinum</td>
                </tr>
                <tr>
                    <th>Price</th>
                    <td>&#8377; {{ stsm?.show?.price_1 }}</td>
                    <td>&#8377; {{ stsm?.show?.price_2 }}</td>
                    <td>&#8377; {{ stsm?.show?.price_3 }}</td>
                </tr>
                <tr>
                    <th>Available seats</th>
                    <td>{{ availableSeats?.silver }}</td>
                    <td>{{ availableSeats?.gold }}</td>
                    <td>{{ availableSeats?.platinum }}</td>
                </tr>
                </table>
            </div>
            <div class="">
                <button @click.prevent="showBookingForm">
                    Book Now
                </button>
                <button @click.prevent="refreshSeats"><img src="@/assets/icons-svg/refresh-white.svg" alt="refresh" title="Refresh available seats"/></button>
            </div>
        </div>
        

        <div v-if="show_form" class="form">
            <form @submit.prevent="bookTicket">
                <table class="form-table">
                    <tr>
                        <td>
                            <label>
                                Number of tickets:
                            </label>
                        </td>
                        <td>
                            <select v-model="noOfTickets">
                                <option v-for="number in tickets" :key="number" :value="number">{{ number }}</option>
                            </select>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            Class:
                        </td>
                        <td>
                            <label v-for="tier in seatTiers" :key="tier">
                                <input type="radio" :value="tier" v-model="selectedTier" /> {{ capitalizeFirstLetter(tier) }}
                            </label>
                        </td>
                    </tr>
                    <tr>
                        <td>
                           Total Amount:
                        </td>
                        <td>
                            &#8377; {{ tier_price * noOfTickets }}
                        </td>
                    </tr>
                </table>
                <div class="buttons">
                    <div>
                        <button type="submit" class="add"><img src="@/assets/icons-svg/check-black.svg" alt="Add" title="Add"/></button>
                    </div>
                    <div @click.prevent="clearForm">
                        <button class="cancel"><img src="@/assets/icons-svg/delete-black.svg" alt="Cancel" title="Cancel"/></button>
                    </div>
                </div>
            </form>
        </div>
    </div>
</template>

<script>
// import ShowBooking from '@/components/ShowBooking.vue'
import {  getShowById, getBookingsByShowId, createBooking, getAvailableSeatsByShowId, unAuthRedirect} from "@/js/requests.js"
import { clog, delay, convertTo12HourFormat}  from '@/js/helpers.js';

export default {
    name: "ShowBookingPage",
    components: {
        // ShowBooking
    },

    data() {
        return {
            show_date: "",
            show_time: "",
            // bookings: {},
            stsm: {}, // show, theatre, screen, movie info
            show_form: false,
            tickets: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            selectedTier: "silver",
            seatTiers: ["silver", "gold", "platinum"],
            noOfTickets: 1,
            availableSeats: {},
            is_unauth: false,
        }
    },
    created() {
        // this.getAllBookingsByShowId();
        this.getShowInfo();
        this.getAvailableSeatsForShow();
        setInterval(this.getAvailableSeatsForShow, 30 * 1000);
    },
    computed: {
        tier_price(){
            if (this.selectedTier == "silver"){
                return this.stsm?.show?.price_1;
            }
            if (this.selectedTier == "gold"){
                return this.stsm?.show?.price_2;
            }
            if (this.selectedTier == "platinum"){
                return this.stsm?.show?.price_3;
            }
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

        capitalizeFirstLetter(str) {
            return str.charAt(0).toUpperCase() + str.slice(1);
        },

        async getAllBookingsByShowId(){
            let api_key = this.$store.getters.getApiKey;
            const show_id = this.$route.params.show_id;
            try {
                const booking_by_show_id = await getBookingsByShowId(show_id, api_key);
                this.bookings = booking_by_show_id;
            } catch (e) {
                const is_un_auth = this.unAuth(e);
            }
        },
        


        async getShowInfo() {
            let api_key = this.$store.getters.getApiKey;
            const show_id = this.$route.params.show_id;
            try {
                const show_info = await getShowById(show_id, api_key);
                this.stsm = show_info;
                const date_arr = this.stsm?.show?.start_time.split(" ");
                this.show_date = date_arr.slice(0, 4).join(" ");
                this.show_time = convertTo12HourFormat(date_arr[4]);
            } catch (e) {
                const is_un_auth = this.unAuth(e);
            }
        },

        refreshSeats() {
            this.getAvailableSeatsForShow();
        },

        async getAvailableSeatsForShow() {
            let api_key = this.$store.getters.getApiKey;
            const show_id = this.$route.params.show_id;
            try {
                const seat_stats = await getAvailableSeatsByShowId(show_id, api_key);
                this.availableSeats = seat_stats;
            } catch (e) {
                const is_un_auth = this.unAuth(e);   
            }
            
        },

        showBookingForm() {
            this.show_form = !this.show_form;
        },
            
        clearForm() {
            this.show_form= false;
            this.selectedTier= "silver";
            this.noOfTickets= 1;

        },
        async bookTicket() {
            const d = {
                "movie_name": this.stsm.movie.name,
                "start_time": this.stsm.show.start_time,
                "venue": this.stsm.theatre.name+", "+this.stsm.theatre.address,
                "seat_class": this.selectedTier,
                "no_of_seats": this.noOfTickets,
                "price": this.tier_price,
                "show_id": this.stsm.show.show_id,
                // "user_id": add in the backend
            };
            const is_confirmed = prompt("The booking is non-cancellable.\n Do you still want to continue (YES/NO)?");
            if ( is_confirmed != null && is_confirmed.toLowerCase() === "yes") {
                const api_key = this.$store.getters.getApiKey;
                try {
                    const booked_ticket = createBooking(d, api_key);
                    alert("Tickets booked successfully!");
                    this.clearForm();
                } catch (e) {
                    const is_un_auth = this.unAuth(e);  
                }
            } else {
                return;
            }
        }
    }
}

</script>
