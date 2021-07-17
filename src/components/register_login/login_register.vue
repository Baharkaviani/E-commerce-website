<template>
  <div class="main-div">
    <div class="page-label">
      <label>فروشگاه - {{getText}}</label>
    </div>
    <form v-if="login" id="login-form">
      <Input_textfield class="login-fields fields" v-on:childToParent="onChildClick" v-on:focusedOut="clear" v-for="item in loginitems"
                       :key="item.label"
                       :attr="item"
                       :class="item.argument"
      />
      <p class="email-error error" v-if="!this.valid['email']">{{this.error['email']}}</p>
      <p class="pass-error error" v-if="!this.valid['pass']">{{this.error['pass']}}</p>
    </form>
    <form  v-else id="signup-form" @submit.prevent="checkForm" action="https://vuejs.org/"
           method="post">
      <Input_textfield class="signup-fields fields" v-on:childToParent="onChildClick" v-on:focusedOut="clear"   v-for="item in signupItems"
                       :key="item.label"
                       :attr="item"
                       :class="item.argument"


      />
      <input_textfield class="address fields" v-on:childToParent="onChildClick" v-on:focusedOut="clear"  :attr="addressItem"/>

      <p v-if="!login && !this.valid['name']" class="name-error error">{{this.error['name']}}</p>
      <p v-if="!login && !this.valid['sname']" class="sname-error error">{{this.error['sname']}}</p>
      <p class="email-error error" v-if="!this.valid['email']">{{this.error['email']}}</p>
      <p class="pass-error error" v-if="!this.valid['pass']">{{this.error['pass']}}</p>
      <p v-if="!login && !this.valid['address']" class="address-error error" >{{this.error['address']}}</p>
    </form>


    <button v-if="!login" type="submit" form='signup-form' >{{getText}}</button>
    <button v-else type="submit" form='login-form' >{{getText}}</button>
  </div>
</template>

<script>
import Input_textfield from "@/components/register_login/input_textfield";
export default {
  name: "login_register",
  components: {Input_textfield},
  props: {
    login: Boolean
  },
  data() {
    return {
      args:{
        name: '',
        sname: '',
        email: '',
        pass:'',
        address:''
      },
      error:{
        name: '',
        sname: '',
        email: '',
        pass:'',
        address:''
      },
      valid:{
        name: true,
        sname: true,
        email: true,
        pass:true,
        address:true
      },

      loginitems: [{
        label: "ایمیل",
        placeholder: "ایمیل خود را وارد کنید...",
        argument: "email",
        class: true,
        wsize: true,
        minl: 1,
        maxl: 255,
        regex: /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
      },
        {
          label: "رمز عبور",
          placeholder: "رمز عبور خود را وارد کنید...",
          argument: "pass",
          class: true,
          wsize: true,
          minl: 8,
          maxl: 255,
          regex:  /^(?=.*\d)(?=.*[a-z])[0-9a-zA-Z]{8,}$/
        }
      ],
      signupItems: [{
        label: "نام",
        placeholder: "نام خود را وارد کنید...",
        argument: "name",
        class: true,
        wsize: true,
        minl: 1,
        maxl: 255
      },
        {
          label: "نام خانوادگی",
          placeholder: "نام خانوادگی خود را وارد کنید...",
          argument: "sname",
          class: true,
          wsize: true,
          minl: 1,
          maxl: 255
        },
        {
          label: "ایمیل",
          placeholder: "ایمیل خود را وارد کنید...",
          argument: "email",
          class: true,
          wsize: true,
          minl: 1,
          maxl: 255,
          regex:/^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
        },
        {
          label: "رمز عبور",
          placeholder: "رمز عبور خود را وارد کنید...",
          argument: "pass",
          class: true,
          wsize: true,
          minl: 8,
          maxl: 255,
          regex: /^(?=.*\d)(?=.*[a-z])[0-9a-zA-Z]{8,}$/
        }],
      addressItem: {
        label: "آدرس",
        argument: "address",
        placeholder: "آدرس خود را وارد کنید...",
        class: false,
        wsize: true,
        minl:1,
        maxl: 1000
      }
    }
  },
  computed: {
    getText() {
      if (this.login === true)
        return "ورود";
      return "ثبت نام"
    },
    ispasswordValid(){
      if (this.name ==='tara')
        return true
      return false
    }
  },
  methods:{
    checkForm: function (e) {
      if (this.args['pass'] ==='taraaa')
        console.log('bahar kaviani')
      if (this.args['email'] ==='1234567')
        console.log('bahar')
      e.preventDefault()
    },

    onChildClick (value, argument, isValid, message) {
      // console.log(value + argument)
      this.args[argument] = value
      if(!isValid) {
        this.error[argument] = message
        this.valid[argument] = false
      }
      else {
        this.clear(argument)
      }
    },
    clear(argument){
      this.error[argument] = ''
      this.valid[argument] = true
    }
  }
}
</script>

<style scoped>
.main-div{
  box-sizing: border-box;
  background-color: #dddddd;
  width: 1280px;
  justify-content: center;
  align-items: center;
}

.page-label{
  color: #00bec9;
  font-size: 20px;
  text-align: center;
}

form{
  margin-top: 30px;
  text-align: center;
}

#signup-form{
  direction: rtl;
  display: grid;
  grid-template-areas:
                      'name sname '
                      'namee snamee'
                      'email pass'
                      'emaile passe'
                      'addr addr'
                      'addre addre';
  column-gap: 15px;
  justify-content: center;
}

#login-form{
  display: grid;
  grid-template-areas: 'email' 'emaile' 'pass' 'passe';
  /*gap: 15px;*/
  justify-content: center;
}

.login-fields{
  /*margin-top: 15px;*/
}
.signup-fields{
  position: relative;
}
.address{
  grid-area: addr;
}

button{

  margin-top: 30px;
  border-radius: 24px;
  border: none;
  background-color: #ffcc00;
  font-size: 16px;
  text-align: center;
  padding: 10px 50px;
  position: relative;
  left: 50%;
  transform: translate(-50%, 0);
}
button:hover{
  cursor: pointer;

}
.error{
  margin-right: 80px;
  color: red;
  font-size: 14px;
  text-align: right;
}
.name{
  grid-area: name;
}
.name-error{
  grid-area: namee;
}
.sname{
  grid-area: sname;
}
.sname-error{
  grid-area: snamee;
}
.pass{
  grid-area: pass;
}
.pass-error{
  grid-area: passe;
}
.email{
  grid-area: email;
}
.email-error{
  grid-area: emaile;
}
.address-error{
  grid-area: addre;
}
.fields{
  margin-top: 15px;
}
p{
  margin-top: 15px;
  /*border: 1px solid blue;*/
}
</style>