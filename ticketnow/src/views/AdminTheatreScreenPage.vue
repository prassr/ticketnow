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

    .wrapper, .theatre {
        margin: 0 auto !important;
        display : flex;
        justify-content: center !important;
        min-width: fit-content;
        padding: 10px;
        background-color: #fff;
        border: 2px solid #f1f1f1;
        border-radius: 10px;
        box-shadow: 1px 1px 5px 5px rgba(0, 0, 0, 0.2) !important;
        background-color: #fff;
        
    }
    .theatre {
        position: relative;
        top: 150px;
        width: 50%;
    }

    .container-fluid {
        position: relative;
        top: 200px;
    }

    .container {
        z-index: 0;
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
        padding: 1px;
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

    p,
label {
  font:
    1rem 'Fira Sans',
    sans-serif;
}

input {
  margin: 0.4rem;
}
    .screens {
        position: relative;
        margin: 200px;
        align-items: center;
        display: flex;
        flex-direction: column;
    }


</style>

<template>
    <div class="notification" v-if="is_unauth">
        <p>Your session has been expired. Kindly log in again.</p>
    </div>
    <div class="theatre">
        <div class="info">
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
                        <td> {{ theatre?.screens?.length}}/2 </td> 
                    </tr>
                </table>
            </div>
        </div>
    </div>
    <button @click="show_form = !show_form" class="add_button" title="Add screen" v-if="theatre.screens?.length < 2"><img src="@/assets/icons-svg/plus-black.svg" alt="Add" /></button>
    <div class="container-fluid" v-if="show_form">
        
        <div class="container">
        <form @submit.prevent="addScreen" class="">
            <div class="wrapper">
            <div class="right-side">
            <div class="col-auto">
                <label for="tier_1">Class 1</label>
                <input type="number"
                        min="0"
                        class="form-control" 
                        id="tier_1" 
                        title="Class 1" 
                        :placeholder="tier_1_title" 
                        v-model="tier_1" 
                        required>
               
            </div>
            <div class="col-auto" >
                <label for="tier_2">Class 2</label>
                <input type="number" class="form-control " id="" :placeholder="tier_2_title" v-model="tier_2" required>

            </div>
            <div class="col-auto">
                <label for="tier_3">Class 3</label>
                <input type="number" class="form-control " id="" :placeholder="tier_3_title" v-model="tier_3" required>
                
            </div>
            <div class="col-auto">
                <label>Sound: </label>
                <select id="sound" v-model="sound">
                    <option value="Dolby 7.1" selected>Dolby 7.1</option>
                    <option value="Atmos">Atmos</option>
                    <!-- Add more options as needed -->
                </select>
            </div>
            <div class="col-auto">
                <label>Recliner available:</label>
                <input type="radio" id="yes" name="sound" :value="true" v-model="is_recliner"/>
                <label for="yes">Yes</label>
                <input type="radio" id="no" name="sound" :value="false" checked v-model="is_recliner" />
                <label for="no">No</label>
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
    <div class="screens">
        <!-- <div v-for="theatre in theatres" > -->
        <div v-for="(screen, index) in theatre.screens"  :key="screen.screen_id">
            <admin-screen  :screen="screen" :index="index" @updateScreenData="updateScreen" @deleteParentScreen="deleteScreen"></admin-screen>
            <!-- class="theatre" :theatre="theatre" :key="theatre.theatre_id" -->
        </div>
    </div>
    <router-view></router-view>
</template>

<script>


import AdminScreen from '@/components/AdminScreen.vue'

import { getTheatreById, createScreen, updateScreenById, deleteScreenById, unAuthRedirect } from '@/js/requests';

export default {
    name: "AdminTheatreScreenPage",
    components: {
        AdminScreen,
    },
    created() {
        this.getTheatre();
    },    
    data() {
        return {
            theatre: {},
            show_form: false,
            tier_1_title: "Enter capacity",
            tier_2_title: "Enter capacity",
            tier_3_title: "Enter capacity",
            tier_1: "",
            tier_2: "",
            tier_3: "",
            sound: "Dolby 7.1",
            is_recliner: false,
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

        deleteScreen(index){
            if (index >= 0 && index < this.theatre.screens.length) {
                this.theatre.screens.splice(index, 1);
            }
        },
        
        updateScreen(index, d) {
            this.theatre.screens[index].tier_1 = d.tier_1;
            this.theatre.screens[index].tier_2 = d.tier_2;
            this.theatre.screens[index].tier_3 = d.tier_3;
            this.theatre.screens[index].sound = d.sound;
            this.theatre.screens[index].is_recliner = d.is_recliner;
        },

        async getTheatre() {
            let t_id = this.$route.params.theatreId;
            try {
                let api_key = this.$store.getters.getApiKey;
                const theatre = await getTheatreById(t_id, api_key);
                if (! theatre) {
                    alert("Something went wrong.");
                    return
                }
                this.theatre = theatre;
            } catch (e) {
                const is_un_auth = this.unAuth(e);
            }
        },
        clearForm() {
            this.tier_1 = "";
            this.tier_2 ="";
            this.tier_3 = "";
            this.sound = "Dolby 7.1";
            this.is_recliner = "false";
            this.show_form = false;
        },

        async addScreen() {
            const d = {
                tier_1: this.tier_1,
                tier_2: this.tier_2,
                tier_3: this.tier_3,
                sound: this.sound,
                is_recliner: this.is_recliner,
                theatre_id: this.theatre.theatre_id,
            };

            let api_key = this.$store.getters.getApiKey;
            try {
                const resp = await createScreen(d, api_key);
                this.show_form = false;
                this.theatre.screens.push(resp);
                alert("Screen added successfully!");
                this.clearForm()
            } catch (e) {
                const is_un_auth = this.unAuth(e);
            }
        },
    },
}

</script>
