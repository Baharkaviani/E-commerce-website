<template>
  <div class="main-div">
    <div class="page-label">ادمین عزیز، خوش آمدید</div>


    <div class="tab-div">
      <button class="tab product">لیست کالاها</button>
      <button class="tab">لیست دسته‌ها</button>
      <button class="tab invoice">رسیدها</button>
    </div>
    <div  class="btn"><button class="add">+ایجاد محصول جدید</button></div>
<!--    <input_textfield class="search" :attr="search"/>-->

      <div class="table-div cats-div">
        <table class='cats'>
          <tr>
            <th>نام دسته‌بندی</th>
            <th class="col-center">عملیات</th>

          </tr>
          <tr class="tr-button">
            <td>دسته‌بندی</td>
            <td class="tab-btn"><button class="edit bttn">ویرایش دسته‌بندی</button><button class="omit bttn">Xحذف دسته‌بندی</button></td>
          </tr>
        </table>
      </div>

<!--  <div class="table-div invoice-div">-->
<!--    <table class='invoices'>-->
<!--      <tr>-->
<!--        <th>کد پیگیری</th>-->
<!--        <th>کالا</th>-->
<!--        <th>قیمت پرداخت شده</th>-->
<!--        <th>نام خریدار</th>-->
<!--        <th>آدرس ارسال شده</th>-->
<!--      </tr>-->

<!--      <tr>-->
<!--        <td>SHOP102030</td>-->
<!--        <td>موس گیمینگ ریزر</td>-->
<!--        <td>۱۰/۰۰۰ تومان</td>-->
<!--        <td>هادی</td>-->
<!--        <td>تهران، تهران، امیرکبیر</td>-->
<!--      </tr>-->
<!--      <tr>-->
<!--        <td>SHOP102030</td>-->
<!--        <td>موس گیمینگ ریزر</td>-->
<!--        <td>۱۰/۰۰۰ تومان</td>-->
<!--        <td>هادی</td>-->
<!--        <td>تهران، تهران، امیرکبیر</td>-->
<!--      </tr>-->
<!--      <tr>-->
<!--        <td>SHOP102030</td>-->
<!--        <td>موس گیمینگ ریزر</td>-->
<!--        <td>۱۰/۰۰۰ تومان</td>-->
<!--        <td>هادی</td>-->
<!--        <td>تهران، تهران، امیرکبیر</td>-->
<!--      </tr>-->

<!--    </table>-->
<!--  </div>-->
  </div>
</template>

<script>
// import input_textfield from "@/components/register_login/input_textfield";
export default {
  // components: {input_textfield},
  name: "admin_profile",
  data(){
    return{
      search:{
        label: "جستجوی کد پیگیری",
        placeholder:"کد پیگیری را برای جستجو وارد کنید ...",
        class: true,
        wsize: true,
        search:true,
        minl: 0
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
.tab-div{
  text-align: center;
}
.page-label{
  font-size: 25px;
  text-align: center;
  direction: rtl;
  margin-right: auto;
  margin-left: auto;

}

.tab{

  background-color: #e7e5e5;
  margin-top: 20px;
  font-size: 16px;
  text-align: center;
  padding: 5px 40px;
  border-color: #787575;
}
.invoice{
  border-bottom-left-radius: 24px;
  border-top-left-radius: 24px;
}
.product{
  border-bottom-right-radius: 24px;
  border-top-right-radius: 24px;
}
.btn{
  text-align: center;
}
.add{
  text-align: center;
  padding: 15px 30px;
  font-size: 16px;
  border: none;
  border-radius: 24px;
  background-color:#009eff;
  box-shadow: 0px 8px 8px 0px rgba(0, 158, 255,0.5);
  color:white;
  margin-top: 30px;
}

.search{
  margin-left: auto;
  margin-right: auto;
  margin-top: 30px;
}
table{

  margin-top: 50px;
  direction: rtl;
  background-color: white;

  border-collapse: collapse;

  text-align: center;
  margin-right: auto;
  margin-left: auto;
}
.invoices{
  width: 1100px;
}
.cats{
  width: 700px;
}
table th {
  padding-right: 50px;
  padding-top: 15px;
  padding-bottom: 15px;
  color: #d7d6d6;
  font-size: 14px;
  text-align:right;
  background-color: white;

}
.col-center{
  text-align: center;

}
.table-div{
  box-shadow: 0px 4px 8px 0px rgba(0,0,0,0.2);
  background-color: white;

  margin-right: auto;
  margin-left: auto;
}
.cats-div{
  width: 740px;
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
.tr-button tr:hover {
  background-color: white;
}
table tr:hover {
  background-color: white;
}
.edit{
  float: right;
}
.omit{
  float: left;
}
.tab-btn{
  /*margin-left:auto; margin-right:auto;*/
  /*padding-left: 50px;*/
  width: 200px;
}

.bttn{
  color: #787575;
  padding: 5px 10px;
  border: none;
  background-color: white;
}
.tab-btn :hover {
  color: #00bec9;
}
</style>