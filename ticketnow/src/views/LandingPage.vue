<style scoped>
    #main-landing-page {
        opacity: 0.9;
        width: 100%;
        min-width: 100%;
        height: 100% !important;
    }

    h1, h3 {
        color: #fff !important;
        display: block !important;
    }

    .wrapper {
        text-align: center;
        /* min-width: fit-content; */
        width: 100%;
        padding: 20px;
        background-color: #0602028a;

    }
    
    .form-wrapper {
        min-width: fit-content;
        min-height: fit-content;
        margin: 30px auto !important;
        display: flex;
        justify-content: center;
    }

    .form-wrapper .div {
        /* min-width: fit-content; */
    }
</style>

<template>
    <div>
        <div id="main-landing-page">
            <landing-navbar></landing-navbar>
            <div class="wrapper">
                <h1>Welcome to TicketNow</h1>
                <h3>Book your ticket now!</h3>
            </div>
            <div class="form-wrapper">
                <div>
                    <router-view></router-view>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import LandingNavbar from '@/components/LandingNavbar.vue';
export default {
    name: "LandingPage",
    components: {
        LandingNavbar
    },
};
</script>
