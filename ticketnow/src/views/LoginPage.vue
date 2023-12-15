<style scoped>
</style>

<template>
    <router-view></router-view>
</template>

<script>
import LandingNavbar from '@/components/LandingNavbar.vue';
import LoginForm from '@/components/LoginForm.vue';
import ResetPassword from '@/components/ResetPassword.vue';
export default {
    name: "LoginPage",
    components: {
        LandingNavbar,
        LoginForm,
        ResetPassword
    },
    data() {
        return {
        }
    },
    methods: {
        // hidePassword() {
        //     this.phide=false;
        // }
    }
};
</script>
