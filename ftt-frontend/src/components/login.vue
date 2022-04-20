<template>

  
  <h3>Login:</h3>
  
  <form @submit.prevent="submitDatabase">
      <label>Username:</label>
      <input type="username" required v-model="user">
      
      <label>Password:</label>
      <input type="password" required v-model="pass">

    <div class="submit">
        <button>Login</button>
    </div>
      

  </form>
    

</template>

<script>
import axios from 'axios';
import {mapActions} from "vuex";
export default {
    name: 'login',
    data() {
        return {
            user: "",
            pass: ""

            
        }
    },
    methods: {
        ...mapActions(["setusername"]), 
        submitDatabase: async function(){
            console.log('form submitted');
            console.log(this.user);
            console.log(this.pass);
            //console.log(this.posts.date)
            const response = await axios.get("http://127.0.0.1:8081/login", {
                params: {
                    username: this.user,
                    password: this.pass
                },

            }
            
            
            );
            //TODO make api call, should return true or false login, if true... 
            
             console.log(response.data);
            if(response.data.login == 0){
                console.log("Youre logged in!")
                this.setusername(this.username)   
            }
            else{
                console.log("user doesn't match password or doesn't exist")
            }

        
        }
    }
}
</script>

<style>
form{
    max-width: 420px;
    margin: 30px auto;
    background: white;
    text-align: left;
    padding: 40px;
    border-radius: 10px
}
label{
    color: #aaa;
    display: inline-block;
    margin: 25px 0 15px;
    font-size: 0.6em;
    text-transform: uppercase;
    letter-spacing: 1px;
    font-weight: bold;
}
input{
    display: block;
    padding: 10px 6px;
    width: 100%;
    box-sizing: border-box;
    border: none;
    border-bottom: 1px solid #ddd;
    color: #555;
}
button {
    background: #001f39;
    border: 0;
    padding: 10px 20px;
    margin-top:20px;
    color: #dfdfdf;
    border-radius: 20px;
}
.submit {
    text-align: center;
}
</style>