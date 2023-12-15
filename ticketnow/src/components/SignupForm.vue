<style scoped>
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
        margin-bottom:15px;
        padding:0px;
        border-radius:3px;
        
    }

    .fieldset label {
        font-size: 16px;
        position: absolute;
        top: -12px;
        left:20px;
        z-index: 10;
        background-color: white;
        width: max-content;
        color: black;
    }

    input {
        border: 1px solid rgba(0, 0, 0, 0.2);
        padding-left: 10px;
        height: 45px;
        font-size: 20px;
    }


    .input-img {
      position: absolute;
      right:10px;
      top:12px;
      background-color:green;
      width:25px;
      padding:2px;
      pointer-events: none;
      border-radius: 2px;
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

    .col-auto {
        height: max-content;
        min-height: fit-content;
        padding : 15px 15px 40px 15px;
    }

    .see-pass input[type='checkbox'] {
        width: 20px;
        height: 20px;
        float: left;
    }

/* 
    input:focus {
        outline: none;
    } */
</style>

<template>
    <div class="flex-center">
        <div>
            <form @submit.prevent="sendOTP" v-if="eshow">
                <div class="col-auto" style="">
                    <div class="form-control-sm fieldset">
                        <label for="email">Enter your email</label>
                        <input type="email" class="form-control" id="email" aria-describedby="emailHelp" v-model.trim="email" required autofocus>
                        <img class="input-img" src="../assets/icons-svg/mail-white.svg" disabled/>
                    </div>
                    <div class="mbtn">
                        <button type="submit" class="btn btn-primary" :disabled="isFormInvalid">{{ submit_text }}</button>
                        <!-- <button type="submit" class="btn btn-primary">{{submit_text}}</button> -->
                    </div> 
                    <div v-if="user_exists">
                        <p>You already have an account. Please, click link below to sign in.</p>
                        <router-link to="/in/login?as=user">Sign in</router-link>
                    </div>

                </div>
            </form>
            <form @submit.prevent="validateOTP" v-if="oshow">
                  <div class="col-auto">
                    <p v-if="otp_sent" style="color:green;">The OTP is sent successfully.</p>
                    <p v-if="otp_valid" style="color:green;">Your OTP is still valid, check email.</p>
                    <div class="form-control-sm fieldset">
                        <label for="otp">Enter OTP</label>
                        <input type="text" class="form-control" id="otp" v-model="otp" required autofocus>
                    </div>
                    <div v-if="otp_invalid">
                        <p>Please enter correct OTP.</p>
                    </div>
                    <div class="mbtn">
                        <button type="submit" class="btn btn-primary" :disabled="isFormInvalid">{{ submit_text }}</button>
                        <!-- <button type="submit" class="btn btn-primary">{{submit_text}}</button> -->
                    </div> 
                  </div>
            </form>
            <form @submit.prevent="signUp" v-if="!oshow && !eshow">
              <div class="col-auto" style="">
                <div class="form-control-sm fieldset">
                  <label for="first_name">Firstname</label>
                  <input type="text" name="first_name" class="form-control" id="first_name" autofocus v-model="first_name" required/>
                </div>
                <div class="form-control-sm fieldset">
                  <label for="last_name">Lastname</label>
                  <input type="text" name="last_name" class="form-control" id="last_name" v-model="last_name" required/>
                </div>
                <div class="form-control-sm fieldset">
                  <label for="email">Email</label>
                  <input type="email" name="email" class="form-control" id="email" v-bind:value="email" disabled/>
                  <img class="input-img" src="../assets/icons-svg/mail-white.svg"/>
                </div>
                <div class="form-control-sm fieldset">
                  <label for="password">Password</label>
                  <input 
                    :type="passtype" name="password" class="form-control" id="password" v-model="password" required/>
                
                <img class="input-img" src="../assets/icons-svg/lock-white.svg"/>
                <div v-if="invalid_password">
                  <p class="text-danger">{{ptext}}</p>
                </div>
                </div>
                <div class="form-control-sm fieldset">
                  <label for="cpassword">Confirm password</label>
                  <input :type="passtype" name="cpassword" class="form-control" id="cpassword" v-model="cpassword" required/>
                  <img class="input-img" src="../assets/icons-svg/lock-white.svg"/>
                </div>
                <div class="see-pass">
                    <input type="checkbox" id="myCheckbox" v-model="showPassword"/>
                    <label for="checkBox">Show password</label>
                </div>

                <div v-if="invalid_cpassword">
                  <p class="text-danger">{{ctext}}</p>
                </div>

               <div class="mbtn">
                  <button type="submit" class="btn btn-primary" :disabled="isFormInvalid">{{ submit_text }}</button>
                  <!-- <button type="submit" class="btn btn-primary">{{submit_text}}</button> -->
                </div>
              </div> 
            </form>
        </div>
    </div>
</template>

<script>
import {sendSignupOTP, verifyOTP, createUser, appLogin} from '@/js/requests.js'
import {validatePassword} from '@/js/helpers.js'
export default {
  name : "SignupForm",
  data() {
    return {
      isEmailVerified: false, // set in local storage, when the user refreshes he should see the sign up page
      first_name:"",
      last_name: "",
      email:"",
      otp:"",
      password:"",
      invalid_password: false,
      cpassword:"",
      invalid_cpassword: false,
      ctext: "",
      ptext: "",
      preferred_genres:"",
      submit_text:"Send OTP",
      eshow: true, // true
      oshow: false, // false
      user_exists: false,
      otp_sent: false,
      otp_valid: false,
      otp_invalid: false,
        showPassword: false,
    }
  },
    computed: {
        isFormInvalid() {
            if (this.submit_text === "Verify OTP") {
                let regex = /^[0-9]{6}$/;
                return !this.otp || (!regex.exec(this.otp));
      }
    },
        passtype() {
            return this.showPassword ? "text" : "password";
        },
  }, // add methds to validate password and otp
  watch: {
    password() {
            const obj = validatePassword(this.password);
            this.invalid_password = obj["invalid_password"];
            this.ptext = obj["text"];
          },
},
    methods: {
        async sendOTP() {
            try{
                const resp = await sendSignupOTP({"email":this.email});
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
                alert(e);
                if (e.error_message == "USER_EXISTS") {
                    this.user_exists = true;
                }
                else {
                    alert("Oops! Something went wrong.");
                }
            }
        },
    async validateOTP() {
        try{
            const verified = await verifyOTP({"email":this.email, "OTP":this.otp}) 
            if (verified) {
                this.oshow = false;
                this.submit_text = "Sign Up"
            }
            else
                throw verified;
            }
        catch (e) {
            this.otp_invalid = true;
        }
    },
    async signUp(){
      if (this.password != this.cpassword) {
        this.invalid_cpassword = true;
        this.ctext = "Those passwords didn't match. Try again.";
        this.cpassword="";
      }
      else {
        let d = {
          "first_name": this.first_name,
          "last_name": this.last_name,
          "email": this.email.toLowerCase(),
          "password":this.password,
        }
        const user = await createUser(d);
        if (user){
            sessionStorage.setItem("current_user", JSON.stringify(user))
            const d = {
                "email":user.email,
                "password": this.password,
                "OTP":false
            };

            let q = {
                "as": "user",
            };

            try {
                const resp = await appLogin(d, q);
                this.$store.commit("setApiKey", resp["x-access-token"]);
                this.$router.push({name:"user_home"});
            } catch(e) {
                    console.log(e);
                     alert("Oops! Something went wrong.")   
            }
        } else {
            alert("Oops! Something went wrong. Kindly try again.")
                    this.$router.push({name:"landing"})
        }
      }
    },
  }
}
</script>
