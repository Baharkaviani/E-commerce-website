<template>
    <div class="main-div">
        <div class="page-label">
            <label>فروشگاه - {{getText}}</label>
        </div>
        <form v-if="login" id="login-form">
            <Input_textfield class="login-fields fields" v-for="item in loginitems"
                                  :key="item.label"
                                   :attr="item"
                            />
        </form>
        <form  v-else id="signup-form" @submit.prevent="checkForm" action="https://vuejs.org/"
               method="post">
            <Input_textfield class="signup-fields fields" v-on:childToParent="onChildClick" v-for="item in signupItems"
                             :key="item.label"
                             :attr="item"

            />
            <input_textfield class="address" v-on:childToParent="onChildClick"  :attr="addressItem"/>
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

        onChildClick (value, argument) {
           // console.log(value + argument)
          this.args[argument] = value
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
                      'a b '
                      'c d'
                      /*'e1 e2'*/
                      'e e';
        gap: 15px;
        justify-content: center;
    }

    #login-form{
        display: grid;
        grid-template-rows: auto auto;
        gap: 15px;
        justify-content: center;
    }

    .login-fields{
        margin-top: 15px;
    }
    .signup-fields{
        position: relative;
    }
    .address{
        grid-area: e;
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
</style>