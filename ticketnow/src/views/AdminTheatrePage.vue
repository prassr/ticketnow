<style scoped>
    @import '/src/css/form.css';
    input {
        height: 30px;
        margin: 5px !important;
        transition: top 3s ease;
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
        display: none;
    }
    a {
        padding: 0px !important;
    }


     .theatres {
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
     <button @click="show_form = !show_form" class="add_button" title="Add Theatre"><img src="@/assets/icons-svg/plus-black.svg" alt="Add" /></button>
    <div class="container-fluid" v-if="show_form">
        <div class="movie-form container">
        <form @submit.prevent="addTheatre" class="">
            <div class="wrapper">
            <div class="right-side">
            <div class="col-auto">
                <input type="text" 
                        class="form-control" 
                        id="name" 
                        title="Theatre Name" 
                        :placeholder="name_title" 
                        v-model="name" 
                        
                        @blur="name_title='Name'"
                        required autofocus>
                <label for="name">Name</label>
            </div>
            <div class="col-auto" >
                <input type="text" class="form-control " id="" :placeholder="add_title" v-model="address"  required>
                <label for="name">Address</label>

            </div>
            <div class="col-auto">
                <input type="text" class="form-control " id="" :placeholder="city_title" v-model="city"  required>
                <label for="name">City</label>

            </div>
            <div class="col-auto inl9">
                <input type="text" class="form-control " id="" :placeholder="state_title" v-model="state"  required>
                <label for="name">State</label>
            </div>
            <div class="col-auto">
                <input type="text" class="form-control " id="" :placeholder="zc_title" v-model="zip_code"  required>
                <label for="name">Zip code</label>
            </div>
            <div class="col-auto">
                <input type="textarea" class="form-control " id="" :placeholder="fac_title" v-model="facilities" >
                <label for="name">Facilities</label>

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
        </div> <!-- movie-form container-->
    </div>
    <div class="theatres">
        <!-- <div v-for="theatre in theatres" > -->
        <div v-for="(theatre, index) in theatres" :key="theatre.theatre_id">
            <admin-theatre :theatre="theatre" @updateTheatreData="updateTheatre" @deleteParentTheatre="deleteTheatre" :index="index"/>
                <!-- class="theatre" :theatre="theatre" :key="theatre.theatre_id" -->
        </div>
    </div>
    <router-view></router-view>
</template>

<script>


import AdminTheatre from '@/components/AdminTheatre.vue'

import { getTheatres, createTheatre, unAuthRedirect } from '@/js/requests';

export default {
    name: "AdminTheatrePage",
    components: {
        AdminTheatre,
    },
    created() {
        this.getAllTheatres();
    },    
    data() {
        return {
            theatres: null,
            name: "",
            name_title:"Venue",
            address:"",
            add_title:'Address',
            city: "",
            city_title: "City",
            state:"",
            state_title: "State",
            zip_code: "",
            zc_title: "Zip code",
            location: "",
            loc_title:"Location",
            facilities: "",
            fac_title: "Facilities",
            show_form: false,
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

        deleteTheatre(index){
            if (index >= 0 && index <   this.theatres.length) {
                this.theatres.splice(index, 1);
            }
        },

        updateTheatre(index, d) {
            this.theatres[index].name = d.name;
            this.theatres[index].address = d.address;
            this.theatres[index].city = d.city;
            this.theatres[index].state = d.state;
            this.theatres[index].zip_code = d.zip_code;
            this.theatres[index].facilities = d.facilities;
        },

        clearForm() {
            this.name = "";
            this.address = "";
            this.city = "";
            this.state = "";
            this.zip_code = "";
            this.facilities = "";
            this.show_form = false;
        },
        async getAllTheatres(){
            let api_key = this.$store.getters.getApiKey;
            try {
                this.theatres = await getTheatres(api_key);
            } catch (e) {
                const is_un_auth = this.unAuth(e);
            }

        },
        async addTheatre(){
            const d = {
                name: this.name,
            	address: this.address,
            	city: this.city,
            	state: this.state,
            	zip_code: this.zip_code,
            	location: this.location,
            	facilities: this.facilities,
            };
            let api_key = this.$store.getters.getApiKey;
            try {
                const resp = await createTheatre(d, api_key);
                this.show_form = false;
                this.clearForm();
                alert("Theatre added successfully!");
                this.theatres.push(resp);
            } catch (e) {
                const is_un_auth = this.unAuth(e);
            }
        }, 
    },
}

</script>
