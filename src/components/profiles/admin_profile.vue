<template>
    <div class="main-div">
        <div class="page-label">ادمین عزیز، خوش آمدید</div>

        <div class="tab-div">
            <button class="tab prdct" :class="{ clickedBtn:this.tab===0}" v-on:click="changeToProduct">لیست کالاها
            </button>
            <button class="tab" :class="{ clickedBtn:this.tab===1}" v-on:click="changeToCats">لیست دسته‌ها</button>
            <button class="tab invoice" :class="{ clickedBtn:this.tab===2}" v-on:click="changeToInvoice">رسیدها</button>
        </div>

        <div v-if="this.tab===0" class="btn">
            <button class="add">+ایجاد محصول جدید</button>

            <section class="products">
                <Product class="proItem"  v-for="product in products"
                         :key="product.title"
                         :product="product"
                         :admin=true
                />
            </section>
        </div>

        <div v-if="this.tab===1" class="table-div cats-div">
            <table v-if="this.tab===1" class='cats'>
                <tr>
                    <th>نام دسته‌بندی</th>
                    <th class="col-center">عملیات</th>
                </tr>
                <tr class="tr-button">
                    <td>دسته‌بندی</td>
                    <td class="tab-btn">
                        <button class="edit bttn">ویرایش دسته‌بندی</button>
                        <button class="omit bttn">Xحذف دسته‌بندی</button>
                    </td>
                </tr>
                <tr class="tr-button">
                    <td>دسته‌بندی</td>
                    <td class="tab-btn">
                        <button class="edit bttn">ویرایش دسته‌بندی</button>
                        <button class="omit bttn">Xحذف دسته‌بندی</button>
                    </td>
                </tr>
                <tr class="tr-button">
                    <td>دسته‌بندی</td>
                    <td class="tab-btn">
                        <button class="edit bttn">ویرایش دسته‌بندی</button>
                        <button class="omit bttn">Xحذف دسته‌بندی</button>
                    </td>
                </tr>
                <tr class="tr-button">
                    <td>دسته‌بندی</td>
                    <td class="tab-btn">
                        <button class="edit bttn">ویرایش دسته‌بندی</button>
                        <button class="omit bttn">Xحذف دسته‌بندی</button>
                    </td>
                </tr>
                <tr class="tr-button">
                    <td>دسته‌بندی</td>
                    <td class="tab-btn">
                        <button class="edit bttn">ویرایش دسته‌بندی</button>
                        <button class="omit bttn">Xحذف دسته‌بندی</button>
                    </td>
                </tr>
                <tr class="tr-button">
                    <td>دسته‌بندی</td>
                    <td class="tab-btn">
                        <button class="edit bttn">ویرایش دسته‌بندی</button>
                        <button class="omit bttn">Xحذف دسته‌بندی</button>
                    </td>
                </tr>
                <tr class="tr-button">
                    <td>دسته‌بندی</td>
                    <td class="tab-btn">
                        <button class="edit bttn">ویرایش دسته‌بندی</button>
                        <button class="omit bttn">Xحذف دسته‌بندی</button>
                    </td>
                </tr>

            </table>
        </div>

        <input_textfield v-if="this.tab===2" class="search" :attr="search"/>

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
                    <td>{{ recp.price }}</td>
                    <td>{{ recp.name }}</td>
                    <td>{{ recp.address }}</td>
                </tr>
                </tbody>
            </table>
        </div>

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
<!--        </div>-->
    </div>
</template>

<script>
    import input_textfield from "@/components/register_login/input_textfield";
    import Product from "@/components/Product";
    import axios from "axios";

    export default {
        components: {
            input_textfield,
            Product
        },
        name: "admin_profile",
        data() {
            return {
                tab: 0,
                search: {
                    label: "جستجوی کد پیگیری",
                    placeholder: "کد پیگیری را برای جستجو وارد کنید ...",
                    class: true,
                    wsize: true,
                    search: true,
                    minl: 0,
                    maxl: 255
                },
                products: [
                    {
                        title: 'ماوس۱',
                        img: require('../../assets/mouse.png'),
                        price: 1000,
                        category: 'no1',
                        sold: 20
                    },
                    {
                        title: 'ماوس۲',
                        img: require('../../assets/mouse.png'),
                        price: 2000,
                        category: 'دسته‌بندی یک',
                        sold: 40
                    },
                    {
                        title: 'ماوس۳',
                        img: require('../../assets/mouse.png'),
                        price: 4000,
                        category: 'no4',
                        sold: 33
                    },
                    {
                        title: 'ماوس گیمینگ ریزر',
                        img: require('../../assets/mouse.png'),
                        price: '۳۰,۰۰۰',
                        category: 'دسته‌بندی یک',
                        sold: 34
                    }
                ],
                receipt: [
                    {
                        id: 'SHOP102031',
                        product: 'موس گیمینگ ۱',
                        price: '۱۰/۰۰۰ تومان',
                        name: 'بهار',
                        address: 'تهران، تهران، امیرکبیر'
                    },
                    {
                        id: 'SHOP102032',
                        product: 'موس گیمینگ ۲',
                        price: '۳۰/۰۰۰ تومان',
                        name: 'تارا',
                        address: 'تهران، تهران، شریف'
                    },
                ]
            }
        },
        methods: {
            changeToProduct() {
                this.tab = 0
            },
            changeToCats() {
                this.tab = 1
            },
            changeToInvoice() {
                this.tab = 2
            }
        },
        created() {
            let token = window.localStorage.getItem('token');

            axios({
                method: 'get',
                url: 'http://127.0.0.1:5000/invoiceadmin',
                headers: { 'authorization': `Bare ${token}` },
            }).then((response)=>{
                for (const rect of response.data){
                    this.receipt.push(rect)
                }
            }).catch((error => {
                console.log(error)
            }))
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

    .bttn {
        color: #787575;
        padding: 5px 10px;
        border: none;
        background-color: white;
    }

    .tab-btn :hover {
        color: #00bec9;
    }
</style>