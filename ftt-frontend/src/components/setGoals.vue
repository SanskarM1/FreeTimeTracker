<template>

  
  <h3>Set Goals:</h3>
  
  <form @submit.prevent="submitDatabase">
      <label>Username:</label>
      <input type="username" required v-model="posts.username">
      
      <label>Category:</label>
      <input type="category" required v-model="posts.category">

      <label>Hours:</label>
      <input type="number" required v-model="posts.hours">

    <div class="submit">
        <button>Set a Goal</button>
    </div>
      

  </form>
    

</template>

<script>
import axios from 'axios';
export default {
    name: 'setGoals',
    data() {
        return {
            posts:{
                username: "",
                category : "",
                hours: "",
                 
            }
            
        }
    },
    methods: {
        submitDatabase: async function(){
           console.log('goal submitted');
            console.log(this.posts.date)
            await axios.post("http://127.0.0.1:8081/setgoals", this.posts);
               
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