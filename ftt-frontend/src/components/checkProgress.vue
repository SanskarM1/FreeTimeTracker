<template>
  <h3>Check Progress:</h3>

  <form @submit.prevent="getdata">
    <label>Username:</label>
    <input type="username" required v-model="clientusername" />
    <label>Category:</label>
    <input type="text" required v-model="category" />
    <div class="submit">
      <button>Check</button>
    </div>
  </form>
  <h3>Progress:</h3>
  <h4>
    {{data}}
 </h4>
  <!-- <p>{{data}}</p> -->
</template>

<script>
import axios from "axios";
export default {
  name: "checkProgress",
  mounted: async function () {
    this.getdata();
    console.log("Hello world");
  },
  data() {
    return {
      clientusername: "",
      category: "",
      data: "",
    };
  },
  methods: {
    getdata: async function () {
      try {
        const response = await axios.get("http://127.0.0.1:8081/checkprogress", {
          params: {
            username: this.clientusername,
            category: this.category
          },
        });

        console.log(response.data);
        if(response.data.difference < 0){
            this.data = "You need " + Math.abs(response.data.difference) + " more hours to meet this goal!"
        }
        else if(response.data.difference == 0){
            this.data = "You've met this goal! Good Job!"
        }
        else{
            this.data = "You've exceeded this goal by " + Math.abs(response.data.difference) +  " Great Job!"
        }
        
      } catch (error) {
        console.log(error);
      }
    },
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

