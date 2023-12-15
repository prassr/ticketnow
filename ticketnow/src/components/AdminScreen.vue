<style scoped>
    * {
        box-sizing: border-box;
        color: black;
    }
    input {
        width: 75%;
    }

    .wrapper {
        padding: 20px;
        margin-top: 20px !important;
        height: 150px;
    }
    
    .wrapper, .mwrapper {
        justify-content: center;
        display : flex;
        flex-direction: column !important;
        border-radius: 10px;
        box-shadow: 1px 1px 5px 5px rgba(0, 0, 0, 0.2) !important;
        background-color: #fff;
        min-width: fit-content;
        width: 300px;
    }
    .mwrapper {
        z-index: 10;
        padding: 20px 0 0 50px;
        margin: 20px auto;
    }


    .wrapper:hover {
        height: 180px;
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

    .mbuttons > .button {
        width: 35%;
        margin: 0.5px;
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
        padding: 5px;
        text-align: center;
        display: flex;
        justify-content: center;
        align-items: center;
        border: none;
        background: transparent;
    }
    
    .buttons > .button {
        width: 35%;
        margin: 0.5px;
    }
    .button:hover {
        cursor: pointer;
    }
    .edit, .update{
        border-radius: 10px  0 0 10px;
        background-color: rgb(30, 153, 30);
    }

    .delete,
    .cancel {
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

    table {
        margin: 0 auto;
    }

    p,
    label {
    font:
        1rem 'Fira Sans',
        sans-serif;
    }

    input {
    /* margin: 0.4rem; */
    }

    input[type="radio"] {
        width: 15px;
    }

</style>

<template>
    <div class="notification" v-if="is_unauth">
        <p>Your session has been expired. Kindly log in again.</p>
    </div>
    <div class="container-fluid">
        <div class="wrapper" v-if="! edit_form">
                <div class="info" v-if="! edit_form">
                    <div class="desc">
                        <table>
                            <tr>
                                <td><b>Class 1:</b></td>
                                <td> {{ screen.tier_1 }} </td>
                            </tr>
                            <tr>
                                <td><b>Class 2:</b></td> 
                                <td> {{ screen.tier_2}} </td> 
                            </tr>
                            <tr :title="screen.is_recliner ? 'Recliner':'Non-recliner'">
                                <td><b>Class 3:</b></td> 
                                <td> {{ screen.tier_3 }}</td> 
                            </tr>
                            <tr>
                                <td><b>Features:</b></td> 
                                <td>{{ screen.sound}}, {{ screen.is_recliner? "R" : "NR" }}</td> 
                            </tr>
                        </table>
                    </div>
                </div>
                <div class="mbuttons">
                    <div class="edit button" v-if="! edit_form" @click.prevent="editScreen" title="Edit screen">
                        <img class="" src="@/assets/icons-svg/edit-black.svg" alt="edit"/>
                    </div>
                    <div class="delete button" v-if="! edit_form" @click.prevent="deleteScreen(screen.screen_id)" title="Delete screen">
                        <svg xmlns="http://www.w3.org/2000/svg" height="1em" viewBox="0 0 448 512">
                            <path d="M135.2 17.7L128 32H32C14.3 32 0 46.3 0 64S14.3 96 32 96H416c17.7 0 32-14.3 32-32s-14.3-32-32-32H320l-7.2-14.3C307.4 6.8 296.3 0 284.2 0H163.8c-12.1 0-23.2 6.8-28.6 17.7zM416 128H32L53.2 467c1.6 25.3 22.6 45 47.9 45H346.9c25.3 0 46.3-19.7 47.9-45L416 128z"/>
                        </svg>
                    </div>
                </div>
            </div>
        <form @submit.prevent="updateScreen" id="update_screen" :key="screen.screen_id">
            <div class="mwrapper" v-if="edit_form">
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
                        <input type="number" class="form-control " id="" min="0" :placeholder="tier_2_title" v-model="tier_2" required>

                    </div>
                    <div class="col-auto">
                        <label for="tier_3">Class 3</label>
                        <input type="number" class="form-control " id="" min="0" :placeholder="tier_3_title" v-model="tier_3" required>
                
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
                        <div class="col-auto update button">
                            <button><img class="" src="@/assets/icons-svg/check-black.svg" alt="Edit"/></button>
                        </div>
                        <div class="col-auto cancel button" @click.prevent="clearForm">
                            <!-- <button class="btn btn-primary" >Cancel</button> -->
                            <button><img class="" src="@/assets/icons-svg/delete-black.svg" alt="Delete"/></button>
                        </div>
                    </div>
            </div>
        </form>
    </div>
</template>

<script>

import { deleteScreenById, updateScreenById } from "@/js/requests.js"
export default {
    tier_1: "AdminScreen",
    props: {
        screen: {
            type: Object,
        },
        index: Number,
    },

    data() {
        return {

            tier_1_title: "Enter capacity",
            tier_2_title: "Enter capacity",
            tier_3_title: "Enter capacity",
            edit_form: false,
            tier_1: 0,
            tier_2: 0,
            tier_3: 0,
            sound: {
                label: "Choose screen type:",
                items: [
                    {key: 1, value: "Dolby 7.1"},
                    {key: 2, value: "Atmos"}
                ],
            },
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
        updateScreenData(index, data) {
            this.$emit('updateScreenData', index, data)
        },
        deleteParentScreen(index) {
            this.$emit('deleteParentScreen', index)
        },
        editScreen() {
            this.edit_form = true;
            this.tier_1 = this.screen.tier_1;
            this.tier_2 = this.screen.tier_2;
            this.tier_3 = this.screen.tier_3;
            this.sound = this.screen.sound;
            this.is_recliner = this.screen.is_recliner;
        },

        clearForm() {
            this.tier_1 = "";
            this.tier_2 ="";
            this.tier_3 = "";
            this.sound = "";
            this.is_recliner = "";
            this.edit_form = false;
        },
        async updateScreen(){
            const d = {
                tier_1: this.tier_1,
                tier_2: this.tier_2,
                tier_3: this.tier_3,
                sound: this.sound,
                is_recliner: this.is_recliner,
            };
            let api_key = this.$store.getters.getApiKey;
            try {
                const resp = await updateScreenById(d, this.screen.screen_id, api_key);
                this.show_form = false;
                this.updateScreenData(this.index, resp);
                alert("Screen updated successfully!");
                this.clearForm()
            } catch (e) {
                const is_un_auth = this.unAuth(e);
            }
        },
        async deleteScreen(id) {
            const del = confirm("Do you really want to delete this screen?");
            let api_key = this.$store.getters.getApiKey;
            try {
                if (del) {
                    const deleted = await deleteScreenById(id, api_key)
                    if (deleted) {
                        alert("Screen deleted successfully!");
                        this.deleteParentScreen(this.index);
                    }
                }
            } catch (e) {
                 const is_un_auth = this.unAuth(e);
            }
        },
    },
}

    
</script>
