<style scoped>
    a:hover {
        background-color: rgba(0, 0, 0, 0.7);
    }
    a:active {
        background-color: rgba(255, 255, 255, 0.1);
        color: black;
    }
    
    a {
        text-decoration: none  !important;
        font-size: 24px;
        color: rgba(255,255,255, 0.7);
        padding: 10px;
    }

    .header {
        width: 100%;
    }
    .head-logo {
        width:30px;
        height:30px;
        border-radius: 15px;
    }
    .sign-in, .sign-up {
        display: inline;
    }
    .sign-in a, .sign-up a {
        background-color: rgb(53, 145, 20);
        color: white;
        padding: 6px !important;
        margin: 2px;
        border-radius: 5px;
        position: relative;
        top: 5px;
        font-size: medium;
    /* display:  inline-flex; */
        
    }

    .sign-block, .sign-up {
        background-color: #1c4202;
        min-width: fit-content;
        min-height: fit-content;
        height: 36px;
        padding: 0 0 0 5px;
        border-radius: 5px;
        box-shadow: 0.1px 0.1px 1px 1px white;
        margin-right: 5px;
    }
    .sign-up {
        padding: 0 ;
    }
    .sign-block > span {
        position: relative;
        top: 7px;

    }

    .nav-right {
        display: flex;
        flex-direction: row !important;
    }
    span {
        color: white;
    }
</style>

<template>
    <div class="header">
        <div class="logo">
            <a class="app-name" href="#"><img src=""/><img class="head-logo" src="../assets/logo.png" alt=""> TicketNow</a>
        </div>
        <div class="nav-links">
            <div class="nav-left">

            </div>
            <div class="nav-right">
                <div class="sign-in">
                    <div class="sign-block">
                        <span>Sign in</span>
                        <router-link :to="{name: 'login', query: {as:'user'}}" @click="reloadPage({name: 'login', query: {as:'user'}})">User</router-link>
                        <router-link :to="{name: 'login', query: {as:'admin'}}" @click="reloadPage({name: 'login', query: {as:'admin'}})">Admin</router-link>
                    </div>
                </div>
                <div class="sign-up">
                    <router-link :to="{name:'signup'}" @click="reloadPage({name:'signup'})">Sign up</router-link>
                </div>
             </div>
        </div>
    </div>
</template>

<script>
export default{
    name: "LandingNavbar",
    data() {
        return {
            links : [
                {text: "Movies", url:"/in/explore/movies"}
            ],
        }
    },
  methods: {
    reloadPage(page) {
      this.$router.push(page);
    },
  }
    
};
</script>
