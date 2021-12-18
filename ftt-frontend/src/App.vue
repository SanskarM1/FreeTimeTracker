<template>
  <img alt="FTT Logo" src="./assets/fttLogo.png">
  <h1>FreeTime Tracker</h1>
  <h3>A Time Tracking Tool in the Process of Being Built</h3>
  <enterInfo />
  <returnInfo />
  
  
</template>

<script>
import enterInfo from './components/enterInfo.vue'
import returnInfo from './components/returnInfo.vue'

export default {
  name: 'App',
  components: {
    enterInfo,
    returnInfo
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
  margin-bottom: 60px
}
</style>
