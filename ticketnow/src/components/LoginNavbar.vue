<style scoped>
    .nav-main {
        padding: 25px;
        background-color: blueviolet;
        height: fit-content;
    }

    .get-in {
        display: inline-block;
        padding: 5px;
        /* float: right; */
    }

    .get-in-a {
        background-color: rgb(255, 142, 142);
        padding: 4px;
        margin: 4px;
    }
    .app-name {
        margin-right: 100px;
        font-size: 28px;
    }
    a {
        text-decoration: none  !important;
        font-size: 24px;
    }
</style>

<template>
    <div class="nav-main">
        <a class="app-name" href="#">TicketNow</a>
        <div class="get-in menu">
            <a class="get-in-a" @click="" href="/in/login">Sign In</a>
            <a class="get-in-a" @click="" href="/in/signup">Sign Up</a>
        </div>
    </div>
</template>

<script>

export default {
    name : "LoginNavbar"
    
};
</script>
