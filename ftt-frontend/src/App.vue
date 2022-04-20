<template>
  
  <img alt="FTT Logo" src="./src/assets/fttLogo.png">
  <h1>FreeTime Tracker</h1>
  <h3>A Time Tracking Tool in the Process of Being Built</h3>
  <signup />
  <login />
  <enterInfo />
  <returnInfo />
  <weeklyAverage />
  <setGoals />
  <check-progress />
  <compare-data />
  
  
</template>

<script>
import enterInfo from './components/enterInfo.vue'
import returnInfo from './components/returnInfo.vue'
import weeklyAverage from './components/weeklyAverage.vue'
import setGoals from './components/setGoals.vue'
import checkProgress from './components/checkProgress.vue'
import signup from './components/signup.vue'
import login from './components/login.vue'
import compareData from './components/compareData.vue'

export default {
  name: 'App',
  components: {
    enterInfo,
    returnInfo,
    weeklyAverage,
    setGoals,
    checkProgress,
    signup,
    login,
    compareData
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
