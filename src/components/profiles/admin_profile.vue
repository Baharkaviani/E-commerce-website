<template>
    <div class="main-div">
        <!--    The label of whole profile page    -->
        <div class="page-label">ادمین عزیز، خوش آمدید</div>

        <!--    List of Tabs in admin's profile    -->
        <div class="tab-div">
            <button class="tab prdct" :class="{ clickedBtn:this.tab===0}" v-on:click="changeToProduct">لیست کالاها
            </button>
            <button class="tab" :class="{ clickedBtn:this.tab===1}" v-on:click="changeToCats">لیست دسته‌ها</button>
            <button class="tab invoice" :class="{ clickedBtn:this.tab===2}" v-on:click="changeToInvoice">رسیدها</button>
        </div>

        <!--    First tab contents    -->
        <div v-if="this.tab===0" class="btn">
          <modal ref="newProModal">
            <template v-slot:body>
              <label class="modalLabel">ایجاد محصول جدید</label>
              <p>نام کالا:</p>
              <input type="text" v-model="newProduct.name"/>
              <p>موجودی انبار:</p>
              <input type="number" v-model="newProduct.available"/>
              <p>دسته بندی:</p>
              <input type="text" v-model="newProduct.category"/>
              <p>قیمت:</p>
              <input type="number" v-model="newProduct.price"/>

              <p :class="{error:merror, safe:!merror}">
                {{creatingMessage}}
              </p>
              <button class="inModal" @click="createNewPro">ثبت محصول</button>
            </template>
          </modal>
            <button class="add" @click="createProduct($refs.newProModal)">+ ایجاد محصول جدید</button>

            <section class="products">
                <Product class="proItem" v-on:updateProduct="getProducts" v-for="product in displayedProducts"
                         :key="product.title"
                         :product="product"
                         :admin=true
                />
            </section>

            <nav aria-label="Page">
                <ul class="pagination">
                    <li v-if="page !== 1" class="page-item">
                        <button type="button" class="page-link" @click="page--"> Previous </button>
                    </li>
                    <li v-for="pageNumber in pages.slice(page-1, page+5)" :key="pageNumber.id" class="page-item">
                        <button type="button" class="page-link" @click="page = pageNumber"> {{pageNumber}} </button>
                    </li>
                    <li v-if="page !== numberOfPages" class="page-item">
                        <button type="button" @click="page++" class="page-link"> Next </button>
                    </li>
                </ul>
            </nav>

<!--            <section class="products">-->
<!--                <Product class="proItem"  v-for="product in products"-->
<!--                         :key="product.title"-->
<!--                         :product="product"-->
<!--                         :admin=true-->
<!--                />-->
<!--            </section>-->
        </div>
      <modal ref="newCatModal">
        <template v-slot:body>
          <label class="modalLabel">ایجاد دسته بندی جدید</label>
          <p>نام دسته بندی:</p>
          <input type="text" v-model="newCat.name"/>

          <p :class="{error:merror, safe:!merror}">
            {{creatingMessage}}
          </p>
          <button class="inModal" @click="createNewCat">ثبت دسته بندی</button>
        </template>
      </modal>
      <div v-if="this.tab===1" class="btn">
      <button v-if="this.tab===1" class="add" @click="createCat($refs.newCatModal)">+ ایجاد دسته بندی جدید</button>
      </div>
        <!--    Second tab contents    -->
        <div v-if="this.tab===1" class="table-div cats-div">


          <!--    table of categories    -->
            <table v-if="this.tab===1" class='cats'>
                <!--    header    -->
                <thead>
                <tr>
                    <th>نام دسته‌بندی</th>
                    <th class="col-center">عملیات</th>
                </tr>
                </thead>

                <!--    body    -->
                <tbody>
                <tr class="tr-button" v-for="(cat, index) in categories" :key="index">
                    <td>{{ cat }}</td>
                    <td class="tab-btn">
                        <!--    button for editing category's name    -->
                        <button class="edit bttn" v-if="cat !== 'دسته بندی نشده'" @click="editingCategory(cat)">ویرایش دسته‌بندی</button>

                        <!--    button for deleting a category    -->
                        <button class="omit bttn" v-if="cat !== 'دسته بندی نشده'" @click="deletingCategory(cat)">Xحذف دسته‌بندی</button>
                    </td>
                </tr>
                </tbody>

                <!--    modal for editing category's name    -->
                <modal ref="editModal">
                    <template v-slot:body>
                        <label class="modalLabel"> ویرایش دسته بندی {{cat}}</label>
                        <p>نام دسته بندی:</p>
                        <input type="text" v-model="newCatName"/>

                        <p :class="{error:merror, safe:!merror}">
                            {{buyingMessage}}
                        </p>
                        <button class="inModal" @click="submit_edit(cat)">ثبت ویرایش</button>
                    </template>
                </modal>

            </table>
<!--        </div>-->

<!--        <div v-if="this.tab===1" class="table-div cats-div">-->
<!--            <table v-if="this.tab===1" class='cats'>-->
<!--                <tr>-->
<!--                    <th>نام دسته‌بندی</th>-->
<!--                    <th class="col-center">عملیات</th>-->
<!--                </tr>-->
<!--                <tr class="tr-button">-->
<!--                    <td>دسته‌بندی</td>-->
<!--                    <td class="tab-btn">-->
<!--                        <button class="edit bttn">ویرایش دسته‌بندی</button>-->
<!--                        <button class="omit bttn">Xحذف دسته‌بندی</button>-->
<!--                    </td>-->
<!--                </tr>-->
<!--                <tr class="tr-button">-->
<!--                    <td>دسته‌بندی</td>-->
<!--                    <td class="tab-btn">-->
<!--                        <button class="edit bttn">ویرایش دسته‌بندی</button>-->
<!--                        <button class="omit bttn">Xحذف دسته‌بندی</button>-->
<!--                    </td>-->
<!--                </tr>-->
<!--                <tr class="tr-button">-->
<!--                    <td>دسته‌بندی</td>-->
<!--                    <td class="tab-btn">-->
<!--                        <button class="edit bttn">ویرایش دسته‌بندی</button>-->
<!--                        <button class="omit bttn">Xحذف دسته‌بندی</button>-->
<!--                    </td>-->
<!--                </tr>-->
<!--                <tr class="tr-button">-->
<!--                    <td>دسته‌بندی</td>-->
<!--                    <td class="tab-btn">-->
<!--                        <button class="edit bttn">ویرایش دسته‌بندی</button>-->
<!--                        <button class="omit bttn">Xحذف دسته‌بندی</button>-->
<!--                    </td>-->
<!--                </tr>-->
<!--                <tr class="tr-button">-->
<!--                    <td>دسته‌بندی</td>-->
<!--                    <td class="tab-btn">-->
<!--                        <button class="edit bttn">ویرایش دسته‌بندی</button>-->
<!--                        <button class="omit bttn">Xحذف دسته‌بندی</button>-->
<!--                    </td>-->
<!--                </tr>-->
<!--                <tr class="tr-button">-->
<!--                    <td>دسته‌بندی</td>-->
<!--                    <td class="tab-btn">-->
<!--                        <button class="edit bttn">ویرایش دسته‌بندی</button>-->
<!--                        <button class="omit bttn">Xحذف دسته‌بندی</button>-->
<!--                    </td>-->
<!--                </tr>-->
<!--                <tr class="tr-button">-->
<!--                    <td>دسته‌بندی</td>-->
<!--                    <td class="tab-btn">-->
<!--                        <button class="edit bttn">ویرایش دسته‌بندی</button>-->
<!--                        <button class="omit bttn">Xحذف دسته‌بندی</button>-->
<!--                    </td>-->
<!--                </tr>-->
<!--            </table>-->
        </div>

        <!--    Third tab contents    -->
        <input_textfield v-if="this.tab===2" class="search" :attr="search" v-on:searchingEvent="searchCode" v-on:childToParent="emptySearchHandler"/>

        <div v-if="this.tab===2" class="table-div invoice-div">
            <table v-if="this.tab===2" class='invoices'>
                <thead>
                <tr>
                    <th>کد پیگیری</th>
                    <th>کالا</th>
                    <th>قیمت پرداخت شده</th>
                    <th>نام خریدار</th>
                    <th>آدرس ارسال شده</th>
                </tr>
                </thead>

                <tbody>
                <tr v-for="(recp, index) in receipt" :key="index">
                    <td>{{ recp.id }}</td>
                    <td>{{ recp.product }}</td>
                    <td>{{ recp.price }} تومان</td>
                    <td>{{ recp.name }}</td>
                    <td>{{ recp.address }}</td>
                </tr>
                </tbody>
            </table>
<!--        </div>-->

<!--        <div v-if="this.tab===2" class="table-div invoice-div">-->
<!--            <table v-if="this.tab===2" class='invoices'>-->
<!--                <tr>-->
<!--                    <th>کد پیگیری</th>-->
<!--                    <th>کالا</th>-->
<!--                    <th>قیمت پرداخت شده</th>-->
<!--                    <th>نام خریدار</th>-->
<!--                    <th>آدرس ارسال شده</th>-->
<!--                </tr>-->
<!--                <tr>-->
<!--                    <td>SHOP102030</td>-->
<!--                    <td>موس گیمینگ ریزر</td>-->
<!--                    <td>۱۰/۰۰۰ تومان</td>-->
<!--                    <td>هادی</td>-->
<!--                    <td>تهران، تهران، امیرکبیر</td>-->
<!--                </tr>-->
<!--                <tr>-->
<!--                    <td>SHOP102030</td>-->
<!--                    <td>موس گیمینگ ریزر</td>-->
<!--                    <td>۱۰/۰۰۰ تومان</td>-->
<!--                    <td>هادی</td>-->
<!--                    <td>تهران، تهران، امیرکبیر</td>-->
<!--                </tr>-->
<!--                <tr>-->
<!--                    <td>SHOP102030</td>-->
<!--                    <td>موس گیمینگ ریزر</td>-->
<!--                    <td>۱۰/۰۰۰ تومان</td>-->
<!--                    <td>هادی</td>-->
<!--                    <td>تهران، تهران، امیرکبیر</td>-->
<!--                </tr>-->
<!--                <tr>-->
<!--                    <td>SHOP102030</td>-->
<!--                    <td>موس گیمینگ ریزر</td>-->
<!--                    <td>۱۰/۰۰۰ تومان</td>-->
<!--                    <td>هادی</td>-->
<!--                    <td>تهران، تهران، امیرکبیر</td>-->
<!--                </tr>-->
<!--                <tr>-->
<!--                    <td>SHOP102030</td>-->
<!--                    <td>موس گیمینگ ریزر</td>-->
<!--                    <td>۱۰/۰۰۰ تومان</td>-->
<!--                    <td>هادی</td>-->
<!--                    <td>تهران، تهران، امیرکبیر</td>-->
<!--                </tr>-->
<!--                <tr>-->
<!--                    <td>SHOP102030</td>-->
<!--                    <td>موس گیمینگ ریزر</td>-->
<!--                    <td>۱۰/۰۰۰ تومان</td>-->
<!--                    <td>هادی</td>-->
<!--                    <td>تهران، تهران، امیرکبیر</td>-->
<!--                </tr>-->
<!--                <tr>-->
<!--                    <td>SHOP102030</td>-->
<!--                    <td>موس گیمینگ ریزر</td>-->
<!--                    <td>۱۰/۰۰۰ تومان</td>-->
<!--                    <td>هادی</td>-->
<!--                    <td>تهران، تهران، امیرکبیر</td>-->
<!--                </tr>-->
<!--            </table>-->
        </div>
    </div>
</template>

<script>
    import input_textfield from "@/components/register_login/input_textfield";
    import Product from "@/components/Product";
    import Modal from "@/components/Modal";
    import axios from "axios";

    export default {
        components: {
            input_textfield,
            Product,
            Modal
        },
        name: "admin_profile",
        data() {
            return {
                page: 1,
                perPage: 15,
                numberOfPages: 1,
                pages: [],
                tab: 0,
                merror:false,
                creatingMessage:"",
                newProduct:{
                  name:"",
                  price :0,
                  available:0,
                  category:""
                },
              newCat:{
                  name:""
              },
                search: {
                    label: "جستجوی کد پیگیری",
                    placeholder: "کد پیگیری را برای جستجو وارد کنید ...",
                    class: true,
                    wsize: true,
                    search: true,
                  argument:"search",
                    minl: 0,
                    maxl: 255
                },
                products: [
                    // {
                    //     title: 'ماوس۱',
                    //     img: require('../../assets/mouse.png'),
                    //     price: 1000,
                    //     category: 'no1',
                    //     sold: 20
                    // },
                    // {
                    //     title: 'ماوس۲',
                    //     img: require('../../assets/mouse.png'),
                    //     price: 2000,
                    //     category: 'دسته‌بندی یک',
                    //     sold: 40
                    // },
                    // {
                    //     title: 'ماوس۳',
                    //     img: require('../../assets/mouse.png'),
                    //     price: 4000,
                    //     category: 'no4',
                    //     sold: 33
                    // },
                    // {
                    //     title: 'ماوس گیمینگ ریزر',
                    //     img: require('../../assets/mouse.png'),
                    //     price: '۳۰,۰۰۰',
                    //     category: 'دسته‌بندی یک',
                    //     sold: 34
                    // }
                ],
                receipt: [
                    // {
                    //     id: 'SHOP102031',
                    //     product: 'موس گیمینگ ۱',
                    //     price: '۱۰/۰۰۰ تومان',
                    //     name: 'بهار',
                    //     address: 'تهران، تهران، امیرکبیر'
                    // },
                    // {
                    //     id: 'SHOP102032',
                    //     product: 'موس گیمینگ ۲',
                    //     price: '۳۰/۰۰۰ تومان',
                    //     name: 'تارا',
                    //     address: 'تهران، تهران، شریف'
                    // },
                ],
                categories: [],
                cat: "",
                newCatName: "",
                buyingMessage: ""
            }
        },
        methods: {
            changeToProduct() {
                this.tab = 0;
            },
          createProduct(ref){
              this.creatingMessage =""
              ref.openModal()
          },
          createCat(ref){
            this.creatingMessage =""
            ref.openModal()
          },
            changeToCats() {
                this.tab = 1;
                this.getCategories();
            },
            changeToInvoice() {
                this.tab = 2;
            },
            setPages () {
                this.numberOfPages = Math.ceil(this.products.length / this.perPage);
                console.log("number:" + Math.ceil(this.products.length / this.perPage));
                this.pages = [];
                for (let index = 1; index <= this.numberOfPages; index++) {
                    this.pages.push(index);
                }
            },
            paginate () {
                let page = this.page;
                let perPage = this.perPage;
                let from = (page - 1) * perPage;
                let to = 0;
                console.log("numberOfPages:" + this.numberOfPages);
                if (page === this.numberOfPages) {
                    to = this.products.length;
                }
                else {
                    to = from + perPage;
                }
                console.log("page:" + this.page + "perpage:" + perPage);
                return this.products.slice(from, to);
            },
            getProducts() {
                axios({
                    method: 'get',
                    url: 'http://127.0.0.1:5000/products',
                    params:{order:'sold'}
                }).then((response)=>{
                    this.products = [];
                    for (const product of response.data){
                        console.log("number of products" + this.products.length);
                        product.img =require('../../assets/mouse.png');
                        this.products.push(product)
                    }
                    this.setPages();
                }).catch((error => {
                    console.log(error)
                }));
            },
          createNewCat(){
            let token = window.localStorage.getItem('token');
            let self = this
            axios({
              method: 'post',
              url: 'http://127.0.0.1:5000/addcat',
              headers: { 'authorization': `Bare ${token}` },
              data:{
                name :self.newCat.name
              }
            }).then((response)=>{
              self.creatingMessage = response.data.message
              self.merror = false
              self.getProducts()
              self.getCategories()
            }).catch((error => {
              self.creatingMessage = error.response.data.message
              self.merror = true
              console.log(error)
            }))
          },
           createNewPro(){
             let token = window.localStorage.getItem('token');
             let self = this
             axios({
               method: 'post',
               url: 'http://127.0.0.1:5000/addproduct',
               headers: { 'authorization': `Bare ${token}` },
               data:{
                 name :self.newProduct.name,
                 cat: self.newProduct.category,
                 price: self.newProduct.price,
                 available: self.newProduct.available
               }
             }).then((response)=>{
               self.creatingMessage = response.data.message
               self.merror = false
               self.getProducts()
               self.getCategories()
             }).catch((error => {
               self.creatingMessage = error.response.data.message
               self.merror = true
               console.log(error)
             }))

           },
            getReceipts() {
                let token = window.localStorage.getItem('token');
                axios({
                    method: 'get',
                    url: 'http://127.0.0.1:5000/invoiceadmin',
                    headers: { 'authorization': `Bare ${token}` },
                }).then((response)=>{
                  this.receipt =[]
                    for (const rect of response.data){
                        this.receipt.push(rect)
                    }
                }).catch((error => {
                    console.log(error)
                }))
            },
            getCategories(){
                axios({
                    method: 'get',
                    url: 'http://127.0.0.1:5000/categories',
                }).then((response)=>{
                    this.categories = [];
                    for (const category of response.data){
                        // console.log(JSON.stringify(product))
                        this.categories.push(category);
                    }
                }).catch((error => {
                    console.log(error);
                }));
            },
            editingCategory(cat) {
                let ref = this.$refs.editModal;
                this.buyingMessage =""
                ref.openModal();
                this.cat = cat;
            },
            submit_edit(cat) {
                let self = this;
                let token = window.localStorage.getItem('token');

                axios({
                    method: 'post',
                    url: 'http://127.0.0.1:5000/editcategory',
                    headers: { 'authorization': `Bare ${token}` },
                    data: {
                        category: cat,
                        newName: this.newCatName,
                    }
                }).then(function (response) {
                    console.log(response);
                    self.buyingMessage = response.data.message;
                    self.merror = false;
                    self.getProducts();
                    self.getCategories();
                }).catch((error => {
                    console.log(error);
                }))
            },
            deletingCategory(cat){
                let self = this;
                let token = window.localStorage.getItem('token');

                axios({
                    method: 'post',
                    url: 'http://127.0.0.1:5000/deletecategory',
                    headers: { 'authorization': `Bare ${token}` },
                    data: {
                        category: cat,
                    }
                }).then(function (response) {
                    console.log(response);
                    self.buyingMessage = response.data.message;
                    self.merror = false;
                    self.getProducts();
                    self.getCategories();
                }).catch((error => {
                    console.log(error);
                }))
            },
          searchCode(code){
            let token = window.localStorage.getItem('token');
              if (code===""){
                this.getReceipts()
              }
              else{
                axios({
                  method: 'get',
                  url: 'http://127.0.0.1:5000/idfilter',
                  headers: { 'authorization': `Bare ${token}` },
                  params:{
                    id:code
                  }
                }).then((response)=>{
                  this.receipt =[]
                  for (const rect of response.data){
                    this.receipt.push(rect)
                  }
                }).catch((error => {
                  console.log(error);
                }));
              }
          },
          // eslint-disable-next-line no-unused-vars
          emptySearchHandler(inputVal,argument,valid,message){

              if (argument === "search" && inputVal =="")
                this.getReceipts()

          }
        },
        computed: {
            displayedProducts () {
                return this.paginate();
            }
        },
        created() {
            this.getProducts();
            this.getReceipts();
            this.getCategories();
        }
    }
</script>

<style scoped>
    .main-div {
        background-color: #dddddd;
        width: 1280px;
        margin-top: 100px;
        margin-bottom: 75px;
        box-sizing: border-box;
        direction: rtl;
    }

    .tab-div {
        text-align: center;
    }

    .page-label {
        font-size: 25px;
        text-align: center;
        direction: rtl;
        margin-right: auto;
        margin-left: auto;
    }

    .tab {

        color: #575656;
        background-color: #dddddd;
        margin-top: 20px;
        font-size: 16px;
        text-align: center;
        padding: 5px 40px;
        border-color: #787575;
    }

    .invoice {
        border-bottom-left-radius: 24px;
        border-top-left-radius: 24px;
    }

    .prdct {
        border-bottom-right-radius: 24px;
        border-top-right-radius: 24px;
    }

    .products {
        display: flex;
        align-items: center;
        justify-content: center;
        flex-direction: row-reverse;
        flex-wrap: wrap;
    }

    .proItem {
        margin: 20px;
    }

    .pagination {
        display: flex;
        align-items: center;
        justify-content: center;
        flex-direction: row-reverse;
        direction: rtl;
        margin-top: 20px;
        list-style-type: none;
        height: 40px;
    }

    .btn {
        text-align: center;
    }

    .clickedBtn {
        background-color: #cdcccc;
        color: #404040;
    }

    .add {
        text-align: center;
        padding: 15px 30px;
        font-size: 16px;
        border: none;
        border-radius: 24px;
        background-color: #009eff;
        box-shadow: 0 8px 8px 0 rgba(0, 158, 255, 0.5);
        color: white;
        margin-top: 30px;
        margin-bottom: 30px;
    }

    .search {
        margin-left: auto;
        margin-right: auto;
        margin-top: 30px;
    }

    table {
        /*margin-top: 50px;*/
        direction: rtl;
        background-color: white;
        border-collapse: collapse;
        text-align: center;
        margin-right: auto;
        margin-left: auto;
    }

    .invoices {
        padding-top: 0;
        width: 1100px;
        /*overflow-y: scroll;*/
        max-height: 280px;
        /*min-height: 280px;*/
    }

    .invoice-div {
        margin-top: 30px;
        width: 1120px;
        overflow-y: scroll;
        height: 280px;
        /*max-height:280px;*/
        /*min-height: 280px;*/
    }

    .cats {
        width: 700px;
    }

    table th {
        padding-right: 50px;
        padding-top: 15px;
        padding-bottom: 15px;
        color: #d7d6d6;
        font-size: 14px;
        text-align: right;
        background-color: white;

    }

    .col-center {
        text-align: center;
    }

    .table-div {
        box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
        background-color: white;
        margin-right: auto;
        margin-left: auto;
    }

    .cats-div {
        width: 740px;
        margin-top: 30px;
        overflow-y: scroll;
        max-height: 350px;
        min-height: 350px;
    }

    table td {
        padding-right: 60px;
        padding-top: 15px;
        padding-bottom: 15px;
        color: #787575;
        text-align: right;
    }

    table tr {
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

    .edit {
        float: right;
    }

    .omit {
        float: left;
    }

    .tab-btn {
        /*margin-left:auto; margin-right:auto;*/
        /*padding-left: 50px;*/
        width: 200px;
    }
    .inModal{
      display: block;
      text-align: center;
      padding: 8px 20px;
      font-size: 16px;
      border: none;
      border-radius: 24px;
      background-color:#009eff;
      position: relative;
      box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
      color:white;

    }
    .bttn {
        color: #787575;
        padding: 5px 10px;
        border: none;
        background-color: white;
    }

    .tab-btn :hover {
        color: #00bec9;
    }
    input{
      margin-bottom: 30px;
      border-radius: 24px;
    }
    p{
      margin-bottom: 30px;
    }
    .error{
      color: red;
    }
    .safe{
      color: green;
    }
    .modalLabel{
      margin-top: 10px;
      margin-bottom: 30px;
    }
    .newCatDiv{
      align-content: center;
    }
</style>