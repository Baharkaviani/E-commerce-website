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
}
label{
  background-color: #00bec9;
  color: #f1f1f1;
  width: 100px;
  display: inline-block;
  text-align: center;
  border-top-right-radius: 5px;
  border-bottom-right-radius: 5px;
  left: 0;
  transform: translate(-2%,0%);
  vertical-align: middle;
  margin-right: 0px;
}
.naddrl{
  padding-top: 12px;
  padding-bottom: 12px;
}
.addrl{
  padding-top: 29px;
  padding-bottom: 29px;
}
textarea, input{
  border-bottom-left-radius: 5px;
  border-top-left-radius: 5px;
  border-top: #dddddd;
  border-bottom: #dddddd;
  border-left: #dddddd;
}
input{
  width: 300px;
  padding-right:10px;
  padding-top: 12px;
  padding-bottom: 15px;
  /*border-color:white;*/


}
textarea{
  width: 730px;
  vertical-align: middle;
  resize: none;
  padding-right:10px;
  padding-top: 21px;
  padding-bottom: 21px;
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