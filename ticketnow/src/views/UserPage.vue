<template>
    <div>
        <user-navbar></user-navbar> 
    </div>
    <div class="page">
        <div class="router-view">
        
        <router-view></router-view>
    </div>
    </div>
</template>

<script>
import UserNavbar from '@/components/UserNavbar.vue'
export default {
    name: "UserPage",
    components: {
        UserNavbar,

    },

   created() {
        if (this.$cookies.get("x-access-token")?.length) {
            this.$store.commit("setApiKey", this.$cookies.get("x-access-token"));
        }
        if (this.$store.getters.getApiKey) {
            this.$cookies.set("x-access-token", this.$store.getters.getApiKey, {
                secure : true,
                expires: "1d"
            })
        }
    }, // add it someshere in home
    data() {
        return {
            currentUser: {
                id: null,
                name: "",
            },
        }
    },
    methods: {

    }
}
</script>

<style scoped>
    h1 {
        color: black !important;
    }
    .router-view {
        padding-top:20px;
    }
    
</style>
