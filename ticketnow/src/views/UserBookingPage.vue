<style scoped>

    .page {
        margin-top: 100px;
    }
    .booking {
        background-color: rgba(0, 0, 0, 0.589);
        margin: 0 auto;
        color: rgba(255, 255, 255, 0.63);
        margin: 5px;
        padding: 10px;
        border-radius: 10px;
        width: 50%;
        margin: 5px auto;
    }

    h3 {
        margin-left: 300px;
        color: white;
    }
   
   .link {
    cursor: pointer !important;
    background-color: rgba(255, 217, 0, 0.274);
    border-radius: 10px;
    margin-bottom: 10px;
    width: 100%;
    padding: 5px;
    color: white;
   }
   .link:hover {
    cursor: pointer;
   }
</style>

<template>
    <div class="page">
        <div class="notification" v-if="is_unauth">
        <p>Your session has been expired. Kindly log in again.</p>
    </div>
        <h3 v-if="upcomingBookings.length > 0">Upcoming Shows For You</h3>
        <h3 v-else>No new bookings</h3>
        <div class="booking" v-for="booking in upcomingBookings">
           
            <div>
                <div class="link" @click.native="navigateToMovie(booking.movie_id)">
                    {{ booking.movie_name }}
                </div>
                <div>
                    {{ booking.theatre_name }} 
                </div>
                <div>
                    {{ booking.address + ", " + booking.zip_code }} 
                </div>
                
                <div>
                    {{ booking.start_time.split(".")[0].split(" ")[0] + " " + format12(booking.start_time.split(".")[0].split(" ")[1]) }} 
                </div>
                <div>
                    {{ booking.no_of_seats }} {{ booking.seat_class  }}  ticket(s) booked for <span>&#8377;</span> {{ booking.price * booking.no_of_seats }}
                </div>
            </div>

        </div>
        <h3 v-if="previousBookings.length > 0">Shows you already enjoyed</h3>
        <h3 v-else>History unavailable</h3>

        <div v-for="booking in previousBookings" :key="booking.booking_id" class="booking">
            <div>
                <div  class="link" @click.native="navigateToMovie(booking.movie_id)">
                    {{ booking.movie_name }}
                </div>
                <div>
                    {{ booking.theatre_name }} 
                </div>
                <div>
                    {{ booking.address + ", " + booking.zip_code }} 
                </div>
                
                <div>
                    {{ booking.start_time.split(".")[0].split(" ")[0] + " " + format12(booking.start_time.split(".")[0].split(" ")[1]) }} 
                </div>
                <div>
                    {{ booking.no_of_seats }} {{ booking.seat_class }} ticket(s) booked for <span>&#8377;</span> {{ booking.price * booking.no_of_seats }}
                </div>
            </div>
        </div>
    </div>
</template>

<script>
// import UserBooking from '@/components/UserBooking.vue'
import { getBookingsByUser, unAuthRedirect } from "@/js/requests.js";
import { clog, dalay, convertTo12HourFormat } from "@/js/helpers.js"
export default {
    name: "UserBookingPage",
    components: {
        // UserBooking
    },
    created() {
        this.getBookingsByUserId();
    },
    data() {
        return {
            myBookings: {},
            upcomingBookings: {},
            previousBookings: {},
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

        format12(time) {
            return convertTo12HourFormat(time);
        },

        getSortedBookings(s = []) {
            return s.sort((a, b) => {
                const dateA = new Date(a.start_time.split(" -")[0]);
                const dateB = new Date(b.start_time.split(" -")[0]);
                return dateA - dateB;
         });
        },
        async navigateToMovie(movieId) {
            this.$router.push("/in/u/movie/"+movieId);
        },
        async getBookingsByUserId() {
            const api_key = this.$store.getters.getApiKey;
            try {
                const bookings = await getBookingsByUser(api_key);
                this.myBookings = this.getSortedBookings(bookings);
                clog(this.myBookings)
                const currentDate = new Date();
                console.log(this.movies)
                this.upcomingBookings = this.myBookings.filter(booking => {
                    const startTime = new Date(booking.start_time);
                    return startTime >= currentDate;
                });

                this.previousBookings = this.myBookings.filter(booking => {
                    const startTime = new Date(booking.start_time);
                    return startTime < currentDate;
                });
            } catch (e) {
                const is_un_auth = this.unAuth(e);
            }
        }
    },
}

</script>
