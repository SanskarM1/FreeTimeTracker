<template>
  <h3>Compare Your Data With Another User:</h3>

  <form @submit.prevent="getdata">
    <label>Username:</label>
    <input type="username" required v-model="clientusername" />
    <label>Category:</label>
    <input type="category" required v-model="clientcategory" />
    <label>Other Username:</label>
    <select required v-model="otherusername" >
        <option v-for="name in possibleusernames" :key="name" :value="name" >
            {{name}}
            </option> 
        </select>
    <div class="submit">
      <button>Compare Data</button>
    </div>
  </form> 
  <h3>Returned Data:</h3>
  <h4>
    {{data}}
 </h4>
  <!-- <p>{{data}}</p> -->
</template>

<script>
import axios from "axios";
export default {
  name: "compareData",
  mounted: async function () {
    this.populateusernames();
    this.getdata();
    
    console.log("Hello world");
  },
  data() {
    return {
      clientusername: "",
      clientcategory: "",
      otherusername: "",
      possibleusernames: [],
      data: [],
    };
  },
  methods: {
    getdata: async function () {
      try {
        
        console.log(this.clientusername);
        console.log(this.otherusername[0]);
        const response = await axios.get("http://127.0.0.1:8081/comparedata", {
          params: {
            username: this.clientusername,
            username2: this.otherusername[0],
            category: this.clientcategory
          },
        });

        console.log(response.data);
        this.data = response.data;
      } catch (error) {
        console.log(error);
      }
    },
    populateusernames: async function () {
        try {
            const response = await axios.get("http://127.0.0.1:8081/getusernames");
            this.possibleusernames = response.data.usernames;

        }
        catch(error){
            console.log(error);
        }
    }
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
form {
  max-width: 420px;
  margin: 30px auto;
  background: white;
  text-align: left;
  padding: 40px;
  border-radius: 10px;
}
label {
  color: #aaa;
  display: inline-block;
  margin: 25px 0 15px;
  font-size: 0.6em;
  text-transform: uppercase;
  letter-spacing: 1px;
  font-weight: bold;
}
input {
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
  margin-top: 20px;
  color: #dfdfdf;
  border-radius: 20px;
}
.submit {
  text-align: center;
}

.center{
  margin-left:auto;
  margin-right:auto;
}
</style>

