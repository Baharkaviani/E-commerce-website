<template>
  <div id="app">
    <website/>
  </div>
</template>

<script>
import website from "@/components/website";

export default {
  name: 'App',
  components: {
    website
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
