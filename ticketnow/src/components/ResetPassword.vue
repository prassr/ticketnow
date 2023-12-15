<template>

    <div class="flex-center">
        <h3>Reset your password</h3>
        <div v-if="eshow" class="">
            <p>Enter your account's verified email address and we will send you an OTP</p>
        </div>
        <form @submit.prevent="sendOTP" v-if="eshow">
            <div class="col-this">
            <div class="fieldset" v-if="eshow">
                <label for="email">Enter your email</label>
                <input type="email" class="form-control" id="email" aria-describedby="emailHelp" v-model="email" autofocus required>
            </div>
            <div class="mbtn">
                <button type="submit" class="" :disabled="isFormValid">{{ submit_text }}</button>
            </div>
                <div v-if="user_nexists" style="{ position: relative; margin-top: 100px;}">
                <p>You do not have any associated account with this email.<br> Please click link below to Sign up.</p>                    
                <p><span><router-link to="/in/signup">Sign Up</router-link></span></p>
            </div>

            </div>
        </form>
        <form @submit.prevent="validateOTP" v-if="oshow">
            <div class="col-this">
            <p v-if="otp_sent" style="color:green;">The OTP is sent successfully.</p>
            <p v-if="otp_valid" style="color:green;">Your OTP is still valid, check email.</p>
            <div class="fieldset">
                <label for="email">Your email</label>
                <input type="email" class="form-control" id="email" aria-describedby="emailHelp" v-model="email" autofocus disabled>
            </div>
            <div class="fieldset">
                <label for="otp">Enter OTP</label>
                <input type="text" class="form-control" id="otp" v-model="otp">
            </div>
            <div v-if="otp_invalid">
                <p>Please enter correct OTP.</p>                
            </div>
            <div class="mbtn">
                <button type="submit" class="" :disabled="isFormValid">{{ submit_text }}</button>
            </div>
            </div>
        </form>
        <form @submit.prevent="savePassword" v-if="pshow">
            <div class="col-this">
            <div v-if="password_set">
                <p>Your password is reset successfully.</p>
            </div>
            <div class="fieldset">
                <label for="password">Enter password</label>
                <input type="password" class="form-control" id="password" v-model="password" autofocus required>
            </div>
            <div v-if="invalid_password">
                  <p class="text-danger">{{ptext}}</p>
            </div>

            <div class="fieldset">
                <label for="cpassword">Confirm password</label>
                <input type="password" class="form-control" id="cpassword" v-model="cpassword" required>
            </div>
            <div v-if="invalid_cpassword">
                  <p class="text-danger">{{ctext}}</p>
            </div>

            <br>
            <div class="mbtn">
                <button type="submit" class="" :disabled="isFormValid">{{ submit_text }}</button>
            </div>
            </div>
        </form>
    </div>
</template>

<script>
import {sendPasswordResetOTP, verifyOTP, passwordReset} from '@/js/requests.js'
import {validatePassword} from '@/js/helpers.js'

export default {
    name : "ForgotPassword",
    watch: {
        password() {
            const obj = validatePassword(this.password);
            this.invalid_password = obj["invalid_password"];
            this.ptext = obj["text"];
        },
    },

    computed: {
        isFormValid(){
            if (this.submit_text === "Verify OTP") {
                let regex = /^[0-9]{6}$/;
                return !this.otp || !(regex.exec(this.otp));
            }
        }
    },
    data() {
        return {
            email: "",
            otp: "",
            cpassword:"",
            password:"",
            eshow:true,
            oshow:false,
            pshow: false,
            submit_text: "Send OTP",
            user_nexists: false,
            invalid_password: false,
            invalid_cpassword: false,
            ptext: "",
            ctext: "",
            otp_sent: false,
            otp_valid: false,
            otp_invalid: false,
            password_set: false,
        };
    },
    methods: {
        async sendOTP() {
            try{
                const resp = await sendPasswordResetOTP({"email":this.email});
                if (resp["message"] == "OTP_SENT"){
                    this.otp_sent = true;
                }
                if (resp["message"] == "OTP_VALID_15") {
                        this.otp_valid = true;
                }
                this.eshow = false;
                this.oshow = true;
                this.submit_text = "Verify OTP";
            }
            catch (e){
                console.log(e);
                if (e["error_message"] === "INVALID_EMAIL"){
                        
                    this.user_nexists = true;
                }
            }
        },
        
        async validateOTP() {
            try{
                const verified = await verifyOTP({
                    "email":this.email,
                    "OTP":this.otp
                })
                if (verified) {
                    this.oshow = false;
                    this.pshow = true;
                    this.submit_text = "Save Password";
                }
                else
                    throw verified;
            }
            catch (e) {
                this.otp_invalid = true;
            }
        },
        async savePassword(){
            if (this.password != this.cpassword) {
                this.invalid_cpassword = true;
                this.ctext = "Those passwords didn't match. Try again.";
                this.cpassword="";
            }
            else {
                let d = {
                "email": this.email,
                "password":this.password,
                }
                try {
                    const saved = await passwordReset(d);
                    if (saved["message"] === "PASSWORD_RESET_SUCCESSFUL") {
                        this.password_set = true;
                        // add redirection to login page code.
                        // this.$router.go("/movies")
                    }
                } catch (e) {
                    console.log("User not found.")
                }
            }
        }
    }
}
</script>

<style scoped>
.login-form {
    background-color: black;
    border-radius: 20px;
    padding: 10px;
}

     .mbtn {
        position: relative;
        float: right;
        margin-top: 10px;
    }
    
    .mbtn button {
        background-color: rgb(9, 102, 63);
        color: white;
        padding: 10px;
        border-radius: 10px;
        border: none;
    }

    .flex-center {
        background-color: red;
        background-color: rgba(0, 0, 0, .7);
        background-color: #fff;
        border: 2px solid #f1f1f1;
        border-radius: 10px;
        box-shadow: 1px 1px 5px 5px rgba(0, 0, 0, 0.2) !important;
        padding: 30px;
        min-height: fit-content;
        width: 374px;

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

    .col-this {
        height: max-content;
        padding : 15px 15px 40px 15px;
    }

</style>
