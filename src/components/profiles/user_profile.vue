<template>
  <div class="main-div">
    <div v-if="!this.profile" class="page-label">تارا عزیز، خوش آمدید</div>
    <div v-if="this.profile" class="label-div">
    <label v-if="this.profile" class="page-label">تارا عزیز، خوش آمدید</label>
     <label v-if="this.profile" class="page-label"> | </label>
    <label v-if="this.profile">موجودی حساب شما: </label>
    <label v-if="this.profile" class="balance">۱۰/۰۰۰</label>
    <a v-if="this.profile" class="button">افزایش موجودی</a>
    </div>

<!--    <br v-if="this.profile">-->
    <div  class="tab-div">
      <button v-on:click="changeToProfile" :class="{clickedBtn:this.profile, tab:true, profile:true}">پروفایل</button>
      <button   v-on:click="changeToInvoice" :class="{clickedBtn:!this.profile, tab:true, invoice:true}" >رسیدها</button>
    </div>
<div v-if="!this.profile" class="ss">
    <table v-if="!this.profile">
      <tr>
        <th>کد پیگیری</th>
        <th>کالا</th>
        <th>قیمت پرداخت شده</th>
        <th>آدرس ارسال شده</th>
      </tr>

      <tr>
        <td>SHOP102030</td>
        <td>موس گیمینگ ریزر</td>
        <td>۱۰/۰۰۰ تومان</td>
        <td>تهران، تهران، امیرکبیر</td>
      </tr>
      <tr>
        <td>SHOP102030</td>
        <td>موس گیمینگ ریزر</td>
        <td>۱۰/۰۰۰ تومان</td>
        <td>تهران، تهران، امیرکبیر</td>
      </tr>
      <tr>
        <td>SHOP102030</td>
        <td>موس گیمینگ ریزر</td>
        <td>۱۰/۰۰۰ تومان</td>
        <td>تهران، تهران، امیرکبیر</td>
      </tr>
      <tr>
        <td>SHOP102030</td>
        <td>موس گیمینگ ریزر</td>
        <td>۱۰/۰۰۰ تومان</td>
        <td>تهران، تهران، امیرکبیر</td>
      </tr>
      <tr>
        <td>SHOP102030</td>
        <td>موس گیمینگ ریزر</td>
        <td>۱۰/۰۰۰ تومان</td>
        <td>تهران، تهران، امیرکبیر</td>
      </tr>
      <tr>
        <td>SHOP102030</td>
        <td>موس گیمینگ ریزر</td>
        <td>۱۰/۰۰۰ تومان</td>
        <td>تهران، تهران، امیرکبیر</td>
      </tr>
      <tr>
        <td>SHOP102030</td>
        <td>موس گیمینگ ریزر</td>
        <td>۱۰/۰۰۰ تومان</td>
        <td>تهران، تهران، امیرکبیر</td>
      </tr>
      <tr>
        <td>SHOP102030</td>
        <td>موس گیمینگ ریزر</td>
        <td>۱۰/۰۰۰ تومان</td>
        <td>تهران، تهران، امیرکبیر</td>
      </tr>
      <tr>
        <td>SHOP102030</td>
        <td>موس گیمینگ ریزر</td>
        <td>۱۰/۰۰۰ تومان</td>
        <td>تهران، تهران، امیرکبیر</td>
      </tr>
      <tr>
        <td>SHOP102030</td>
        <td>موس گیمینگ ریزر</td>
        <td>۱۰/۰۰۰ تومان</td>
        <td>تهران، تهران، امیرکبیر</td>
      </tr>
      <tr>
        <td>SHOP102030</td>
        <td>موس گیمینگ ریزر</td>
        <td>۱۰/۰۰۰ تومان</td>
        <td>تهران، تهران، امیرکبیر</td>
      </tr>
      <tr>
        <td>SHOP102030</td>
        <td>موس گیمینگ ریزر</td>
        <td>۱۰/۰۰۰ تومان</td>
        <td>تهران، تهران، امیرکبیر</td>
      </tr>

    </table>
</div>

    <form v-if="this.profile" id="edit-form">
      <input_textfield v-if="this.profile" class="name" v-on:childToParent="onChildClick" v-on:focusedOut="clear" :attr="name"/>
      <input_textfield v-if="this.profile" class="sname" v-on:childToParent="onChildClick" v-on:focusedOut="clear" :attr="sname"/>
      <input_textfield v-if="this.profile" class="password"  v-on:childToParent="onChildClick" v-on:focusedOut="clear" :attr="password"/>
      <input_textfield v-if="this.profile" class="address" v-on:childToParent="onChildClick" v-on:focusedOut="clear" :attr="address"/>

      <p v-if="this.profile && !this.valid['name']" class="name-error error">{{this.error['name']}}</p>
      <p v-if="this.profile && !this.valid['sname']" class="sname-error error">{{this.error['sname']}}</p>
      <p class="pass-error error" v-if="this.profile && !this.valid['pass']">{{this.error['pass']}}</p>
      <p v-if="this.profile && !this.valid['address']" class="address-error error" >{{this.error['address']}}</p>
    </form>
    <div v-if="this.profile" class="button-div" >
      <button v-if="this.profile" class="sub" type="submit" form="edit-form" >ویرایش اطلاعات</button>
    </div>

  </div>

</template>

<script>
 import input_textfield from "@/components/register_login/input_textfield";

export default {
  name: "user_profile",
   components: {input_textfield},
  data(){
    return {
      profile: true,
      args:{
        name: '',
        sname: '',
        pass:'',
        address:''
      },
      error:{
        name: '',
        sname: '',
        pass:'',
        address:''
      },
      valid:{
        name: true,
        sname: true,
        pass:true,
        address:true
      },
      name:{
        label: "نام",
        placeholder: "نام خود را وارد کنید...",
        class: true,
        wsize: true,
        argument:"name",
        minl: 1,
        maxl: 255,
      },
       sname: {
          label: "نام خانوادگی",
          placeholder: "نام خانوادگی خود را وارد کنید...",
          class: true,
         argument:"sname",
          wsize: true,
         minl: 1,
         maxl: 255
        },

        password:{
          label: "رمز عبور",
          placeholder: "رمز عبور خود را وارد کنید...",
          class: true,
          argument:"pass",
          wsize: false,
          minl: 8,
          maxl: 255,
          regex:  /^(?=.*\d)(?=.*[a-z])[0-9a-zA-Z]{8,}$/
        },
       address:{
        label: "آدرس",
        placeholder: "آدرس خود را وارد کنید...",
         argument:"address",
        class: false,
        wsize: true,
         minl: 1,
         maxl: 1000,
      }
    }
  },
  methods:{
    changeToProfile(){
      this.profile = true
    },
    changeToInvoice(){
      this.profile = false
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
  background-color: #dddddd;
  width: 1280px;
  margin-top: 65px;
  box-sizing: border-box;
  direction: rtl;
}

.label-div{

  text-align: center;
}
.page-label{
  font-size: 25px;
  text-align: center;
  direction: rtl;
  margin-right: auto;
  margin-left: auto;

}
label{
  text-align: center;
}
.tab-div{
  text-align: center;

}
form{
  margin-top: 30px;
  text-align: center;
}
#edit-form{
  direction: rtl;
  display: grid;
  grid-template-areas:
                      'name sname '
                      'namee snamee'
                      'pass pass'
                      'passe passe'
                     'addr addr'
                      'addre addre';
  column-gap: 15px;
  justify-content: center;
}
.tab{

  margin-top: 20px;
  font-size: 16px;
  text-align: center;
  padding: 5px 50px;
  border-color: #787575;
  color: #575656;
  background-color: #dddddd;

}
.invoice{
  border-bottom-left-radius: 24px;
  border-top-left-radius: 24px;
}
.profile{
  border-bottom-right-radius: 24px;
  border-top-right-radius: 24px;


}
/*.password{*/
/*  grid-area: c;*/
/*}*/
/*.address{*/
/*  grid-area: d;*/
/*}*/
.name{
  grid-area: name;
}
.name-error{
  margin-top: 15px;
  grid-area: namee;
}
.sname{
  grid-area: sname;
}
.sname-error{
  margin-top: 15px;
  grid-area: snamee;
}
.password{
  margin-top: 15px;
  grid-area: pass;
}
.pass-error{
  margin-top: 15px;
  grid-area: passe;
}
.address{
  margin-top: 15px;
  grid-area: addr;
}
.address-error{
  margin-top: 15px;
  grid-area: addre;
}
.error{
  margin-right: 80px;
  color: red;
  font-size: 14px;
  text-align: right;
}
.button{
  margin-right: 10px;
  border-radius: 24px;
  border: none;
  background-color: #ffcc00;
  font-size: 14px;
  text-align: center;
  padding: 5px 10px;
  color: #dddddd;

}
.tab-div{
  text-align: center;
}
.sub{
  margin-top: 30px;
  border-radius: 24px;
  border: none;
  background-color: #ffcc00;
  font-size: 16px;
  text-align: center;
  padding: 10px 40px;
  font-weight: bold;

}
.button-div{
  margin-top: 30px;
  text-align: center;
}
.clickedBtn{
  background-color: #cdcccc;
  color: #404040;
}

table{

  /*margin-top: 30px;*/
  direction: rtl;
  background-color: white;
  width: 1100px;
  border-collapse: collapse;

  text-align: center;
  margin-right: auto;
  margin-left: auto;
  overflow-y: scroll;
  max-height:290px;
}
table th {
  padding-right: 60px;
  padding-top: 15px;
  padding-bottom: 15px;
  color: #d7d6d6;
  font-size: 14px;
  text-align: right;
  background-color: white;

}
.ss{
  margin-top: 30px;
  box-shadow: 0px 4px 8px 0px rgba(0,0,0,0.2);
  background-color: white;
  width: 1120px;
  margin-right: auto;
  margin-left: auto;
  overflow-y: scroll;
  height: 290px;
  /*max-height:290px;*/
  /*min-height: 200px;*/
}
table td{
  padding-right: 60px;
  padding-top: 15px;
  padding-bottom: 15px;
  color: #787575;
  text-align: right;
}
table tr{
  border-top: 1px solid #ddd;
  padding-right: 5px;
  padding-left: 5px;
}
table tr:hover {
  background-color: #ddd;
 }

</style>