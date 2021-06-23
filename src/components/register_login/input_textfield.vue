<template>
  <div>
    <label :class="{naddrl: attr.class,  addrl:!attr.class}" :for="attr.label">{{attr.label}}</label>
    <input v-if="attr.class" type="text"  :id="attr.label" :name="attr.label" :placeholder="attr.placeholder">
    <textarea v-if="!attr.class" :name="attr.label" placeholder="آدرس خود را وارد کنید..."  ></textarea>
  </div>
</template>

<script>
export default {
  name: "input_textfield",
  props:['attr']


}
</script>

<style scoped>
*{
  direction: rtl;
  font-size: 16px;
}
div{
  width: 100%;
  position: relative;
  display: flex;
}
label{
  background-color: #00bec9;
  color: #f1f1f1;
  width: 100px;
  display: block;
  text-align: center;
  border-top-right-radius: 5px;
  border-bottom-right-radius: 5px;
  left: 0;
  vertical-align: middle;
}
.naddrl{
  /*padding-top: 0;*/
  /*padding-bottom: 0;*/
  height: 40px;
  margin: 0;
  box-sizing: border-box;
}
.addrl{
  padding-top: 10px;
  /*padding-bottom: 29px;*/
  height: 70px;
  margin: 0;
  box-sizing: border-box;
}
textarea, input{
  border-bottom-left-radius: 5px;
  border-top-left-radius: 5px;
  border: none;
  margin: 0;
  box-sizing: border-box;
}
input{
  width: 300px;
  padding-right:10px;
  height: 40px;
  margin: 0;
}

textarea{
  width: 730px;
  vertical-align: middle;
  resize: none;
  padding-right:10px;
  padding-top: 10px;
  padding-bottom: 0;
  height: 70px;
  margin: 0;
}

::placeholder{
  opacity: 0.5;
}
input:focus{
  outline: none;
}
textarea:focus{
  outline: none;
}
</style>