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
  <form v-else id="signup-form">
    <Input_textfield class="signup-fields fields"  v-for="item in signupItems"
                     :key="item.label"
                     :attr="item"
    />
    <input_textfield class="address" :attr="address"/>
  </form>

    <button type="submit" :form="{'login-form': login,  'signup-form':!login}" >{{getText}}</button>
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
      loginitems: [{label:"ایمیل",
        placeholder:"ایمیل خود را وارد کنید...",
        class:true},
        {label:"رمز عبور",
          placeholder:"رمز عبور خود را وارد کنید...",
          class:true}
        ],
      signupItems: [{label:"نام",
        placeholder:"نام خود را وارد کنید...",
        class:true,
        id:"1"},
        {label:"نام خانوادگی",
          placeholder:"نام خانوادگی خود را وارد کنید...",
          class:true,
          id:"2"},
        {label:"ایمیل",
          placeholder:"ایمیل خود را وارد کنید...",
          class:true,
          id:"3"},
        {label:"رمز عبور",
          placeholder:"رمز عبور خود را وارد کنید...",
          class:true,
          id:"4"}],
        address:{label:"آدرس",
          placeholder:"آدرس خود را وارد کنید...",
          class:false,
          id:"5"}
    }
  },
  computed:{
    getText(){
      if(this.login==true)
        return "ورود"
      return "ثبت نام"
    }
  }

}
</script>

<style scoped>
.main-div{
  background-color: #dddddd;
  width: 1280px;
  /*height: 100%;*/

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
                'e e';
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
</style>