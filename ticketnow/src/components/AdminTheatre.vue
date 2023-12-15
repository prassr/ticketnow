<style scoped>   
    * {
        box-sizing: border-box;
    }
    input {
        width: 75%;
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
        min-height: fit-content;
        width: 300px;
        /* position: relative; */
        margin: 2% 4% !important;
        height: 190px;
    }

    .wrapper:hover {
        height: 235px;
        transition: height 0.3s ease;
    }
    .mbuttons {
        /* z-index:200; */
        margin-top: 5px;
        position: relative;
        top: 2;
        left: 2;
        height: 0; /* Buttons hidden by default */
        opacity: 0;
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
        z-index: 1000;
        margin-top: 5px;
        display : flex;
        flex-direction: column;
        justify-content: center !important;
        padding: 20px !important;
        min-width: fit-content;
        min-height: fit-content;
        width:300px;
        border: 1px solid #f1f1f1;
        border-radius: 10px;
        box-shadow: 1px 1px 5px 5px rgba(0, 0, 0, 0.2) !important;
        background-color: #fff;
        margin: 2% 4% !important;
        height: 260px;
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
</style>

<template>
    <div class="notification" v-if="is_unauth">
        <p>Your session has been expired. Kindly log in again.</p>
    </div>  
    <div class="container-fluid">
        <div class="wrapper" v-if="! edit_form">
                <div class="info" v-if="! edit_form">
                    <div class="title">
                        <strong>{{ theatre.name }}</strong><br>
                    </div>
                    <div class="desc">
                        <table>
                            <tr>
                                <td><b>Address:</b></td>
                                <td> {{ theatre.address}} </td>
                            </tr>
                            <tr>
                                <td><b>City:</b></td> 
                                <td> {{ theatre.city}} </td> 
                            </tr>
                            <tr>
                                <td><b>State:</b></td> 
                                <td> {{ theatre.state}} </td> 
                            </tr>
                            <tr>
                                <td><b>Zip code:</b></td> 
                                <td> {{ theatre.zip_code}} </td> 
                            </tr>
                            <tr>
                                <td><b>Facilities:</b></td> 
                                <td> {{ theatre.facilities}} </td> 
                            </tr>
                            <tr>
                                <td><b>Screens:</b></td> 
                                <td> {{ theatre.screens.length}}/2 </td> 
                            </tr>
                        </table>
                    </div>
                </div>
                <div class="mbuttons">
                    <div class="edit button" v-if="! edit_form" @click.prevent="editTheatre" title="Edit theatre">
                        <button><img class="" src="@/assets/icons-svg/edit-black.svg" alt="edit"/></button>
                    </div>
                    <!-- <div class="add button" v-if="! edit_form" @click.prevent="addScreen" title="Add screen"> -->
                    <!--     <img class="" src="@/assets/icons-svg/plus-black.svg" alt="edit"/> -->
                    <!-- </div> -->
                    <div class="view button" v-if="! edit_form" @click.prevent="viewScreens" title="View screens">
                        <button>
                            <router-link :to="{name: 'theatre_screen_handler', params: { 'theatreId': theatre.theatre_id }}">
                                <img class="" src="@/assets/icons-svg/eye-black.svg" alt="edit"/>
                            </router-link>
                        </button>
                    </div>
                    <div class="delete button" v-if="! edit_form" @click.prevent="deleteTheatre(theatre.theatre_id)" title="Delete theatre">
                        <!-- <img class="" src="@/assets/icons-svg/trash.svg" alt="delete"/> -->
                        <button>
                            <svg xmlns="http://www.w3.org/2000/svg" height="1em" viewBox="0 0 448 512">
                                <path d="M135.2 17.7L128 32H32C14.3 32 0 46.3 0 64S14.3 96 32 96H416c17.7 0 32-14.3 32-32s-14.3-32-32-32H320l-7.2-14.3C307.4 6.8 296.3 0 284.2 0H163.8c-12.1 0-23.2 6.8-28.6 17.7zM416 128H32L53.2 467c1.6 25.3 22.6 45 47.9 45H346.9c25.3 0 46.3-19.7 47.9-45L416 128z"/>
                            </svg>
                        </button>
                    </div>
                </div>
        </div>
        <form @submit.prevent="updateTheatre" id="update_theatre" :key="theatre.theatre_id">
            <div class="mwrapper" v-if="edit_form">
                    <div class="col-auto">
                        
                        <input type="text" class="form-control h-input" :placeholder="name_title" v-model="name" required>
                        <!-- <label for="name">Name</label> -->
                    </div>
                    <div class="col-auto" >
                        <input type="text" class="form-control h-input " :placeholder="addr_title" v-model="address" required>
                        <!-- <label for="name">Address</label> -->
                    </div>
                    <div class="col-auto">
                        <input type="text" class="form-control h-input " :placeholder="city_title" v-model="city" required>
                        <!-- <label for="name">City</label> -->
                    </div>
                    <div class="col-auto">
                        <input type="text" class="form-control h-input " :placeholder="state_title" v-model="state" required>
                        <!-- <label for="name">State</label> -->
                    </div>
                    <div class="col-auto">
                        <input type="text" class="form-control h-input " :placeholder="zip_title" v-model="zip_code" required>
                        <!-- <label for="name">Zip code</label> -->
                    </div>
                    <div class="col-auto">
                        <input type="text" class="form-control h-input " :placeholder="fac_title" v-model="facilities" >
                        <!-- <label for="name">Facilities</label> -->
                    </div>
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
import {getTheatreById, updateTheatreById, deleteTheatreById, unAuthRedirect}  from '@/js/requests.js';

export default {
    name: "AdminTheatre",
    props: {
        theatre: {
            type: Object,
        },
        index: Number,
    },
    data() {
        return {
            edit_form: false,
            name: "",
            name_title: "Name",
            address:"",
            addr_title: "Address",
            city: "",
            city_title: "City",
            state: "",
            state_title: "State",
            zip_code: "",
            zip_title: "Zip code",
            facilities:"",
            fac_title: "Facilities",
            buttonsVisible: false,
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
        updateTheatreData(index, data) {
            this.$emit('updateTheatreData', index, data)
        },
        deleteParentTheatre(index) {
            this.$emit('deleteParentTheatre', index)
        },
        editTheatre() {
            this.edit_form = true;
            this.name = this.theatre.name;
            this.address = this.theatre.address;
            this.city = this.theatre.city;
            this.state = this.theatre.state;
            this.zip_code = this.theatre.zip_code;
            this.facilities = this.theatre.facilities;
        },

        clearForm() {
            this.name = "";
            this.address ="";
            this.city = "";
            this.state = "";
            this.zip_code = "";
            this.facilities ="";
            this.edit_form = false;
        },
        async updateTheatre(){
            const d = {
                name: this.name,
                address: this.address,
                city: this.city,
                state: this.state,
                zip_code: this.zip_code,
                facilities: this.facilities,
            };
            let api_key = this.$store.getters.getApiKey;
            try {
                const resp = await updateTheatreById(d, this.theatre.theatre_id, api_key);
                this.edit_form = false;
                alert("Theatre updated successfully!");
                this.updateTheatreData(this.index, resp);
                this.clearForm();
            } catch (e) {
                const is_un_auth = this.unAuth(e);
            }
        },
        async deleteTheatre(id) {
            const del = confirm("Do you really want to delete this theatre?");
            let api_key = this.$store.getters.getApiKey;
            try {
                if (del) {
                    const deleted = await deleteTheatreById(id, api_key)
                    if (deleted) {
                        alert("Theatre deleted successfully!");
                        this.deleteParentTheatre(this.index);
                    }
                }
            } catch (e) {
                const is_un_auth = this.unAuth(e);
            }
        },
    },
}
</script>
