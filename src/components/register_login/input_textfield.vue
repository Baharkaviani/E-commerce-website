<template>
  <div>
    <label :class="{naddrl: attr.class,  addrl:!attr.class, searchlabel:attr.search}" :for="attr.label">{{attr.label}}</label>
    <input  v-if="attr.label=='ایمیل'"  type="email" :class="{wsize: attr.wsize,  nwsize:!attr.wsize}" :id="attr.label" :name="attr.argument" :minlength="attr.minl" :placeholder="attr.placeholder"
            v-model="inputValue" v-on:keyup="emitToParent">
    <input  v-else-if="attr.label=='رمز عبور'" type="password" :class="{wsize: attr.wsize,  nwsize:!attr.wsize}" :id="attr.label" :name="attr.argument" :minlength="attr.minl" :placeholder="attr.placeholder"
            v-model="inputValue" v-on:keyup="emitToParent">
    <input  v-else-if="attr.class" type="text" :class="{search:attr.search, wsize: attr.wsize,  nwsize:!attr.wsize}"  :id="attr.label" :name="attr.argument" :minlength="attr.minl" :placeholder="attr.placeholder"
            v-model="inputValue" v-on:keyup="emitToParent">
    <textarea  v-else-if="!attr.class" :name="attr.argument" :placeholder="attr.placeholder" v-model="inputValue" v-on:keyup="emitToParent" ></textarea>
  </div>
</template>

<script>
export default {
  name: "input_textfield",
  props: {
    attr: Object,
    modelValue: String
  },
  data() {
    return {
      inputValue: ''
    }
  },
  methods: {

    emitToParent() {
      this.$emit('childToParent', this.inputValue, this.attr.argument)

    }

  }
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
  box-sizing: border-box;
}
.searchlabel{
  width: 200px;
}
.naddrl{
  padding-top: 10px;
  padding-bottom: 10px;
  margin: 0;

}
.addrl{
  padding-bottom: 30px;
  padding-top: 30px;
  margin: 0;
}
.wsize{
  width: 300px;
}
.nwsize{
  width:718px;
}
textarea, input{
  border-bottom-left-radius: 5px;
  border-top-left-radius: 5px;
  border: none;
  margin: 0;
  box-sizing: border-box;
}
.search{
  width: 500px;
}
input{
  padding-right:10px;
  margin: 0;
  padding-top: 10px;
  padding-bottom: 10px;
}

textarea{
  width: 718px;
  vertical-align: middle;
  resize: none;
  padding-right:10px;
  padding-top: 10px;
  padding-bottom: 30px;

  margin: 0;
}

::placeholder{
  opacity: 0.5;
}
input:focus{
  outline: none;
}
input:invalid:focus {
  border:1px solid red;
}
/*input["password"]*/

textarea:focus{
  outline: none;
}
</style>