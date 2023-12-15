<style scoped>
    .flex-center {
        background-color: red;
        background-color: rgba(0, 0, 0, .7);
        background-color: #fff;
        border: 2px solid #f1f1f1;
        border-radius: 10px;
        box-shadow: 1px 1px 5px 5px rgba(0, 0, 0, 0.2) !important;
        padding: 30px;
        width: 374px;
        height: max-content;
    }

    .fieldset{
        position: relative;
        margin-bottom:25px;
    }

    .fieldset input {
        border: 1px solid rgba(0, 0, 0, 0.2);
        width: 100% !important;
        padding:5px;
        height: 45px;
        font-size: 20px;
    }
    .fieldset > label {
        color: black;
        background-color: white;
        position: absolute;
        top: -12px;
        left: 20px;
        padding: 0px;
    }
    .form-check {
        color:black;
    }

    .mbtn {
        float: right;
    }
    
    .mbtn button {
        background-color: rgb(9, 102, 63);
        color: white;
        padding: 10px;
        border-radius: 10px;
        border: none;
    }

    .signup {
        color: black;
    }
    
    .fgt-btn {
        background-color: rgba(0, 0, 0, 0.1);
        border-radius: 5px;
        box-shadow: 1px 1px 1px 1px rgba(0, 0, 0, 0.3);
        border: none;
        color: black;
    }
    a:hover {
        background: none;
    }
    .fgt-btn a {
        color: black;
    }

</style>

<template>
    <div class="flex-center">
        <div class="">

            <div v-if="error_found" style="{ color: red !important; }">
                <p>{{ error_text }}</p>
            </div>
            <form action="" @submit.prevent="signIn">
                <div class="fieldset">
                    <label for="email">Email</label>
                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" v-model="email" autofocus required>
                </div>
                <div class="fieldset">
                    <label for="password">Password</label>
                    <input type="password" class="form-control input-lg" id="password" v-model="password" required>
                </div>

                <div>
                    <button class="fgt-btn"><router-link to="/in/password_reset">Forgot password?</router-link></button>
                </div>
                <div class="mbtn">
                    <button type="submit" class="" :disabled="isFormValid">Sign in</button>
                    <!-- <button type="submit" class="btn btn-primary">{{submit_text}}</button> -->
                </div>
                <br/>
            </form>
        </div>
        <br>
        <div v-if="this.$route.query.as == 'user'" class="signup">
            Don't have an account?
            <p><span><router-link to="/in/signup">Sign Up</router-link></span>here</p> 
        </div>
    </div>
</template>

<script>
import {appLogin, getUser} from '@/js/requests.js'

export default {
    emits: ["changeDisplay"],
    name : "LoginForm",
    computed: {
        isFormValid(){
            return !this.email || !this.password
        }
    },
    data() {
        return {
            email:"",
            password:"",
            error_found: false,
            error_text: ""
        }
    },
 
    methods: {
        // if submit_text is get otp then send otp to user and valiadate it,
        // after that show him the change password component
        fieldReset() {
            this.email = "";
            this.password = "";
        },
        async signIn() {
            const d = {
                "email":this.email.toLowerCase(),
                "password":this.password,
                "OTP":false
            };
            let q = {
                "as": this.$route.query.as,
            }; // query params
            try {
                const resp = await appLogin(d, q);
                this.$store.commit("setApiKey", resp["x-access-token"]);
                if (q["as"] == "user") {
                    const user = await getUser(this.$store.getters.getApiKey);
                    sessionStorage.setItem("current_user", JSON.stringify(user))
                    this.$router.push({name:"user_home"});
                }
                else if (q["as"] == "admin") {
                    this.$router.push({name:"admin_home"});
                    
                }

            } catch (error) {
                let message = error["error_message"]
                console.log(error)
                if (message == "NO_ADMIN_FOUND") {
                    this.error_found = true;
                    this.error_text = "You are not an Admin.";
                }
                else if (message == "NO_USER_FOUND") {
                    this.error_found = true;
                    this.error_text = "Could not find an existing account with this email. Please, click on Sign up to register."
                }
                else if (message == "INCORRECT_PASSWORD") {
                    this.error_found = true;
                    this.error_text = "It looks like you have entered incorrect password."
                }
                else if (message == "INVALID_OTP") {
                    this.error_found = true;
                    this.error_text = "It looks like you have entered incorrect OTP."

                }
                else {
                    this.error_found = false;
                    this.error_text = "";
                }
            }

        }
    },
    beforeRouteUpdate(to, from, next) {
        if (to.query !== from.query) {
            this.error_found = false;
            this.fieldReset();
        }
        next();
    }
}
</script>
