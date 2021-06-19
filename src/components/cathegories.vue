<template>
  <div class="main-cat">

    <label class="cat-label">دسته بندی‌ها</label>
    <hr>
  <div class="container">
    <label v-for="(cat,index) in cats" :key="index" class="labels">{{cat}}
      <input type="checkbox" :name="cat" :value="cat">
      <span class="checkmark"></span>
    </label>
  </div>


  </div>
</template>

<script>
    export default {
      name: "cathegories",
      props:['cats']
    }
</script>

<style scoped>
.main-cat{
  direction: rtl;
  padding-right: 15px;
  color: #585959;
  max-width: 400px;
}
.cat-label{
  font-size: 18px;
}
.container{
  overflow-y: scroll;
  max-height: 150px;

}
.labels {
  display: block;
  position: relative;
  margin-bottom: 10px;
  cursor: pointer;
  font-size: 16px;
  padding-right: 25px;
}

.labels input {
  position: absolute;
  opacity: 0;
  cursor: pointer;
  height: 0;
  width: 0;
}

.checkmark {
  position: absolute;
  top: 15%;
  right: 0;
  height: 15px;
  width: 15px;
  background-color: white;
  border: 1px solid darkgrey;
  border-radius: 100px;
}

.labels input:checked ~ .checkmark {
  background-color:#009eff;
}


</style>