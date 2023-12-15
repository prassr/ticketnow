<style scoped>
    a { 
        text-decoration: none;
        color: rgba(255,255,255, 0.7);
    }
    a:hover {
        background-color: rgba(0, 0, 0, 0.7);
    }
    a:active {
        background-color: rgba(255, 255, 255, 0.1);
        color: black;
        }
    .header {
        position: fixed !important;
        width: 100%;
        z-index: 1000;
        border-radius: 10px !important;
        margin: 0 auto !important;
    }
    .menu-button {
        border: none;
        background-color: black;
        position: relative;
        /* z-index: 10000; */
    }

    .menu {
        
        display: flex;
        justify-content: left;
        overflow: hidden;
        flex-direction: column;
        position: fixed;
        right: 0;
        top: 83px;
        min-height: fit-content;
        height: 150px;
        width: 250px;
        background-color: rgba(70, 29, 29, 0.603);
        padding: 10px;
        padding-left: 20px;
    }

    
    .menu div {
        /* background-color: red; */
        width: 100%;
        max-height: fit-content;
    }

    .menu div a{
        /* background-color: blue; */
        padding: 9px;
        width: 100% !important;
        display: inline-block;
        margin: 0px !important;
    }
    .logout-button {
        margin-top: 10px;
    }
</style>
    
<template>
    <div class="header">
        <div class="logo">
            <strong>TicketNow </strong>
        </div>
        <div class='nav-links'>
	        <div class="nav-left">
                <router-link :to="{name:'movie_handler'}">Movies </router-link>
		        <router-link :to="{name:'theatre_handler'}">Venues </router-link>
		        <router-link :to="{name:'show_handler'}">Shows </router-link>
		        
            </div>
            <div class="nav-right">
                <button class="menu-button" @click.prevent="toggleMenu">
                    <svg width="22px" height="14px" xmlns="http://www.w3.org/2000/svg"><title>Hamburger Menu</title><g fill-rule="nonzero" stroke="#FFF" stroke-width="1.5" fill="none" stroke-linecap="round"><path d="M1.611 1h20.614M1.611 7h20.614M1.611 13h20.614"></path></g></svg>
                </button>
                <div class="menu" v-if="isMenuOpen">
                    <div>
                        <router-link @click.prevent="toggleMenu" :to="{name:'report_handler'}">Get Report</router-link>
                    </div>
                    <div>
                        <!-- <router-link :to="{name:'admin_profile'}">Account Settings</router-link> -->
                    </div>
                    <div>
                        <button class="logout-button" @click="logOut">
                            <svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg">
                                <path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"></path>
                                <polyline points="16 17 21 12 16 7"></polyline>
                                <line x1="21" y1="12" x2="9" y2="12"></line>
                            </svg>
                            Log out
                        </button>
                    </div>
                </div>
            </div>
        </div>
	</div>
</template>

<script>
import {signOut} from '@/js/requests.js'
export default {
    name: "AdminNavbar",
    data() {
        return {
            isMenuOpen: false,
        }
    },
    methods: {
        async logOut() {
            let logged_out = await signOut(this.$store, this.$cookies, this.$router);
        },
        toggleMenu() {
            this.isMenuOpen = ! this.isMenuOpen;
        }   
    }
}
</script>
