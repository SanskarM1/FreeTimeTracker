<template>

  
  <h3>Sign-Up:</h3>
  
  <form @submit.prevent="submitDatabase">
      <label>Username:</label>
      <input type="username" required v-model="posts.user">
      
      <label>Password:</label>
      <input type="password" required v-model="posts.password">

    <div class="submit">
        <button>Sign-Up</button>
    </div>
      

  </form>
    

</template>

<script>
import axios from 'axios';
import {mapState} from "vuex";
import {mapActions} from "vuex";
export default {
    name: 'signup',
    data() {
        return {
            posts: {
                user: "",
                password: ""
            }

            
        }
    },
    computed : mapState(["username"]),
    methods: {
         ...mapActions(["setusername"]),
        submitDatabase: async function(){
            this.setusername(this.user) //added on? 
            console.log('form submitted');
            console.log(this.username);
            console.log(this.password);
            //console.log(this.posts.date)
            const response = await axios.post("http://127.0.0.1:8081/signup", this.posts);
            console.log(response);
               
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