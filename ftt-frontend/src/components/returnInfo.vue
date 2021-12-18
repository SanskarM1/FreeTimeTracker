<template>
 
 
 
 <h3>Check Log:</h3> 

 <form @submit.prevent="getdata">
   <label>Username:</label>
   <input type="username" required v-model="clientusername">
   <div class="submit">
        <button>Get Log</button>
    </div>
 </form>
 <h3>Returned Data:</h3>
 <p>{{data}}</p>

</template>

<script>
import axios from 'axios';
export default {

  name: 'returnInfo',
  mounted: async function(){
    this.getdata();
    console.log("Hello world");
  },
  data() {      
        return{
          clientusername: '',
          data: [],
        }
      },
  methods: {
    getdata: async function(){
      
      try{
        const response = await axios.get("http://127.0.0.1:8081/getdata", {
          params:{ 
            username: this.clientusername
          }
        });
        
        console.log(response.data);
        this.data = response.data;

      }
      catch(error){
        console.log(error);
      }
    }
    
  }
  
}
    


</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
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

