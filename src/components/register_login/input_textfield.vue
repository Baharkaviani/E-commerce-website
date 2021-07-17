<template>
  <div>
    <label :class="{naddrl: attr.class,  addrl:!attr.class, searchlabel:attr.search}" :for="attr.label">{{attr.label}}</label>
    <input  v-if="attr.label=='ایمیل'"  type="email" :class="{wsize: attr.wsize,  nwsize:!attr.wsize, valid: this.error===1, invalid: this.error===2}" :id="attr.label" :name="attr.argument" :minlength="attr.minl" :placeholder="attr.placeholder"
            v-model="inputValue" v-on:keyup="emitToParent" v-on:focusin="emitToParent" v-on:focusout="changeError">
    <input  v-else-if="attr.label=='رمز عبور'" type="password" :class="{wsize: attr.wsize,  nwsize:!attr.wsize , valid: this.error===1, invalid: this.error===2}" :id="attr.label" :name="attr.argument" :minlength="attr.minl" :placeholder="attr.placeholder"
            v-model="inputValue" v-on:keyup="emitToParent" v-on:focusin="emitToParent" v-on:focusout="changeError">
    <input  v-else-if="attr.class" type="text" :class="{search:attr.search, wsize: attr.wsize,  nwsize:!attr.wsize, valid: this.error===1, invalid: this.error===2}"  :id="attr.label" :name="attr.argument" :minlength="attr.minl" :placeholder="attr.placeholder"
            v-model="inputValue" v-on:keyup="emitToParent" v-on:focusin="emitToParent" v-on:focusout="changeError">
    <textarea  v-else-if="!attr.class" :name="attr.argument" v-on:focusout="changeError"  :class="{valid: this.error===1, invalid: this.error===2}" :placeholder="attr.placeholder" v-model="inputValue"
               v-on:keyup="emitToParent" v-on:focusin="emitToParent"  ></textarea>
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
      error : 0,
      inputValue: ''
    }
  },

  methods: {
    changeError(){
      this.error = 0
      this.$emit('focusedOut',this.attr.argument)
    },
    emitToParent() {
      let valid = true
      let message = ""
      let inputVal = this.inputValue.trim()
      if (this.attr.regex )
        if  (!this.attr.regex.test(inputVal)) {
          valid = false
          if (this.attr.argument ==="email")
            message = "ایمیل آدرس نامعتبر است"
          else
            message = "رمز عبور باید شامل عدد و حروف باشد"
        }
      if (inputVal.length<this.attr.minl) {
        if(this.attr.minl ===1)
          message =this.attr.label+ ' باید پر شود'
        else
          message = `رمز عبور باید حداقل شامل ۸ کاراکتر باشد`
        valid = false
      }
      if (inputVal.length>this.attr.maxl) {
        message = 'کاراکتر باشد' +this.attr.maxl+'باید حداکثر شامل'  +this.attr.label
        valid = false
      }
      if (valid)
        this.error = 1
      else
        this.error = 2
      // console.log(message)
      this.$emit('childToParent', inputVal, this.attr.argument,valid,message)

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
.valid{
  border:1px solid green;
}
.invalid{
  border:1px solid red;
}
/*input:invalid:focus {*/
/*  border:1px solid red;*/
/*}*/
/*input["password"]*/

textarea:focus{
  outline: none;
}
</style>