<template>
  
  <img alt="FTT Logo" src="./src/assets/fttLogo.png">
  <h1>FreeTime Tracker</h1>
  <h3>A Time Tracking Tool in the Process of Being Built</h3>
  <enterInfo />
  <returnInfo />
  <weeklyAverage />
  <setGoals />
  <check-progress />
  
  
</template>

<script>
import enterInfo from './components/enterInfo.vue'
import returnInfo from './components/returnInfo.vue'
import weeklyAverage from './components/weeklyAverage.vue'
import setGoals from './components/setGoals.vue'
import checkProgress from './components/checkProgress.vue'

export default {
  name: 'App',
  components: {
    enterInfo,
    returnInfo,
    weeklyAverage,
    setGoals,
    checkProgress
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
