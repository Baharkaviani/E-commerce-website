<template>
  <div class="main-div">
<!--    <div class="page-label">تارا عزیز، خوش آمدید</div>-->
    <div class="label-div">
    <label class="page-label">تارا عزیز، خوش آمدید</label>
     <label class="page-label"> | </label>
    <label>موجودی حساب شما: </label>
    <label class="balance">۱۰/۰۰۰</label>
    <a class="button">افزایش موجودی</a>
    </div>

    <br>
    <div class="tab-div">
      <button class="tab profile">پروفایل</button>
      <button class="tab invoice">رسیدها</button>
    </div>
<!--<div class="ss">-->
<!--    <table>-->
<!--      <tr>-->
<!--        <th>کد پیگیری</th>-->
<!--        <th>کالا</th>-->
<!--        <th>قیمت پرداخت شده</th>-->
<!--        <th>آدرس ارسال شده</th>-->
<!--      </tr>-->

<!--      <tr>-->
<!--        <td>SHOP102030</td>-->
<!--        <td>موس گیمینگ ریزر</td>-->
<!--        <td>۱۰/۰۰۰ تومان</td>-->
<!--        <td>تهران، تهران، امیرکبیر</td>-->
<!--      </tr>-->
<!--      <tr>-->
<!--        <td>SHOP102030</td>-->
<!--        <td>موس گیمینگ ریزر</td>-->
<!--        <td>۱۰/۰۰۰ تومان</td>-->
<!--        <td>تهران، تهران، امیرکبیر</td>-->
<!--      </tr>-->
<!--      <tr>-->
<!--        <td>SHOP102030</td>-->
<!--        <td>موس گیمینگ ریزر</td>-->
<!--        <td>۱۰/۰۰۰ تومان</td>-->
<!--        <td>تهران، تهران، امیرکبیر</td>-->
<!--      </tr>-->

<!--    </table>-->
<!--</div>-->

    <form  id="edit-form">
      <input_textfield class="name" :attr="name"/>
      <input_textfield class="sname" :attr="sname"/>
      <input_textfield class="password" :attr="password"/>
      <input_textfield class="address" :attr="address"/>
    </form>
    <div class="button-div" >
      <button class="sub" type="submit" form="edit-form" >ویرایش اطلاعات</button>
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
      name:{
        label: "نام",
        placeholder: "نام خود را وارد کنید...",
        class: true,
        wsize: true,
        minl: 0
      },
       sname: {
          label: "نام خانوادگی",
          placeholder: "نام خانوادگی خود را وارد کنید...",
          class: true,
          wsize: true,
          minl: 0
        },

        password:{
          label: "رمز عبور",
          placeholder: "رمز عبور خود را وارد کنید...",
          class: true,
          wsize: false,
          minl: 6
        },
       address:{
        label: "آدرس",
        placeholder: "آدرس خود را وارد کنید...",
        class: false,
        wsize: true
      }
    }
  }


}
</script>

<style scoped>
.main-div{
  background-color: #e7e5e5;
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
                      'a b '
                      'c c'
                     'd d';
  gap: 15px;
  justify-content: center;
}
.tab{

  background-color: #e7e5e5;
  margin-top: 20px;
  font-size: 16px;
  text-align: center;
  padding: 5px 50px;
  border-color: #787575;
}
.invoice{
  border-bottom-left-radius: 24px;
  border-top-left-radius: 24px;
}
.profile{
  border-bottom-right-radius: 24px;
  border-top-right-radius: 24px;


}
.password{
  grid-area: c;
}
.address{
  grid-area: d;
}
.button{
  margin-right: 10px;
  border-radius: 24px;
  border: none;
  background-color: #ffcc00;
  font-size: 14px;
  text-align: center;
  padding: 5px 10px;
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
  text-align: center;
}
button .tab:hover{
  background-color: red;
}

table{

  margin-top: 50px;
  direction: rtl;
  background-color: white;
  width: 1100px;
  border-collapse: collapse;

  text-align: center;
  margin-right: auto;
  margin-left: auto;
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
  box-shadow: 0px 4px 8px 0px rgba(0,0,0,0.2);
  background-color: white;
  width: 1120px;
  margin-right: auto;
  margin-left: auto;
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