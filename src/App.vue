<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <div :key = index v-for="index in 10">
      {{index}}<Menu/>
    </div>

  </div>
</template>

<script>
import Menu from "@/components/Menu";

export default {
  name: 'App',
  components: {
    Menu
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
}
</style>
