<template>
    <div>
        <admin-navbar></admin-navbar> 
    </div>
    <div class="router-view">
        <router-view v-slot="Component">
        </router-view>
    </div>
</template>

<script>
import AdminNavbar from '@/components/AdminNavbar.vue'
import AdminMoviePage from '@/views/AdminMoviePage.vue'
import AdminShowPage from '@/views/AdminShowPage.vue'
import AdminTheatrePage from '@/views/AdminTheatrePage.vue'

export default {
    name: "AdminPage",
    components: {
        AdminNavbar,
        AdminMoviePage,
        AdminShowPage,
        AdminTheatrePage
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
}
</script>

<style>
    h1 {
        color: black !important;
    }
    .router-view {
        padding-top:20px;
    }
    
</style>
