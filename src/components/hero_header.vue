<template>
  <div class="main-hero">
    <div class="hero-containter">
      <h1>در محصولات سایت جستجو کنید...</h1>
      <input type="text" id="product" name="product" placeholder="نام محصول خود را وارد کنید...">
      <button>جستجو کنید</button>
    </div>
  </div>
</template>

<script>
export default {
  name: "hero_header"
}
</script>

<style scoped>
*{
  direction: rtl;
}

.main-hero{
  border: 1px solid black;
  width: 500px;
  height: 700px;
}

h1{
  margin-top: 80px;
  font-size: 32px;
  color: red;
  text-align: center;
  border-color: black;
  border: 1px solid;
}

input {
  margin-top: 40px;
  width: 400px;
  text-align: center;
  border-radius: 24px;
  position: absolute;
  left: 50%;
  transform: translate(-50%, 0);
  height: 20px;
}

button{
  margin-top: 100px;
  border-radius: 24px;
  border: none;
  background-color: #ffcc00;
  font-size: 16px;
  text-align: center;
  padding: 5px 25px;
  position: absolute;
  left: 50%;
  transform: translate(-50%, 0);
}
</style>