<style scoped>
    .page {
        margin: 150px;
    }

    .t2 table, .t2 th, .t2 tr, .t2 td {
        border: 1px solid black;
        padding: 5px;
    }

    t
    button {
    margin-top: 10px;
    border-radius: 5px;
    color: white;
    border: none;
    padding: 10px;
    background-color:rgb(0, 128, 0);
    border-radius: 10px;
  } 

  input {
    width: 100%;
  }
</style>

<template>
    <div class="page">
        <div class="notification" v-if="is_unauth">
        <p>Your session has been expired. Kindly log in again.</p>
    </div>
   <div>
    <h1>Admin Report</h1>
    <h2>Select Date Range</h2>

 <div class="t1">
    <table>
        <tr>
            <td>
                <label for="start-date">Start Date:</label>
            </td>
            <td>
                <input type="date" id="start-date" v-model="startDate" required/> 
            </td>
        </tr>
        <tr>
            <td>
                <label for="end-date">End Date:</label>
            </td>
            <td>
                <input type="date" id="end-date" v-model="endDate" required/>
            </td>
        </tr>
        <tr>
            <td>
                <label>Select venue: </label>
            </td>
            <td>
                <select id="theatreSelect" v-model="theatre_id">
            <option value="" selected>select</option>
            <option v-for="theatre in theatres" :key="theatre.theatre_id" :value="theatre.theatre_id">
            {{ theatre.name }}
            </option>
            </select>
            </td>
        </tr>
        <tr>
            <td>
                <input type="checkbox" id="sendEmail" name="sendEmail" :value="via_email" v-model="via_email" :checked="via_email">
            </td>
            <td>
                Send report via email
            </td>
        </tr>
    </table>
 </div>

    <button @click.prevent="getReportData">Generate Report</button>
    <br>
    <br>
    <div class="t2">
        <table>
      <thead>
        <tr>
            <th>Booking ID</th>
            <th>Booked At</th>
            <th>Movie Name</th>
            <th>Show Start Time</th>
            <th>Venue</th>
            <th>Class</th>
            <th>No. of Seats</th>
            <th>Price</th>
            <th>Total</th>   
        </tr>
        </thead>
        <tbody> 
            <tr v-for="booking in bookings" :key="booking.booking_id">
            <td>{{ booking.booking_id }}</td>
            <td>{{ booking.booked_at }}</td>
            <td>{{ booking.movie }}</td>
            <td>{{ booking.start_time }}</td>
            <td>{{ booking.venue }}</td>
            <td>{{ booking.class }}</td>
            <td>{{ booking.no_of_seats }}</td>
            <td>{{ booking.price }}</td> 
           </tr> 
        </tbody>
        </table>
    </div>
    </div>
    </div>
</template>

<script>

import { generateReport, unAuthRedirect, getTheatres } from "@/js/requests.js"

export default {
    name: "AdminReportPage",

    data() {
    return {
        theatre_id: null,
        startDate: "",
        endDate: "",
        bookings: [],
        theatres: [],
        is_unauth: false,
        via_email: false,
    };
  },
  created() {
    this.getReportData();
    this.getAllTheatres();
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
    
    async getAllTheatres(){
            let api_key = this.$store.getters.getApiKey;
            try {
                this.theatres = await getTheatres(api_key);
            } catch (e) {
                const is_un_auth = this.unAuth(e);
            }
        },
    async getReportData(){
        const api_key = this.$store.getters.getApiKey;
        const d = {};
        if (this.startDate != "" && this.endDate != "") {
            d["start_date"] = this.startDate;
            d["end_date"]  =this.endDate;
        }
        if (this.theatre_id != null) {
            d["tid"] = this.theatre_id;
        }
        if (this.via_email == true) {
            d["sm"] = 1;
        }
        try {
            const data = await generateReport(d, api_key);
            console.log("booking" + JSON.stringify(data));
            this.bookings = data;
        } catch (e) {
            const is_un_auth = this.unAuth(e);
        }
            
    },

    shareByEmail() {
      console.log("Sharing via email...");
    },
  },
}

</script>
