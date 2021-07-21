<template>
    <div class="product">


        <div v-if="admin" class="sold">{{product.sold}}</div>
        <div class="upper-box">
            <div class="img-div"><img :src="product.img" class="image" /></div>
            <div class="title">{{product.title}}</div>
            <div class="cat">{{product.category}}</div>
        </div>

        <hr>
        <div class="lower-box">
            <div class="price">{{product.price}} تومان</div>
            <div v-if="!admin" class="btn">
                <modal ref="modalName">
                    <template v-slot:body>
                        <label class="modalLabel"> تعداد کالا محصول {{product.title}}</label>
                        <input type="number" @change="showPrice" v-on:keyup="showPrice" v-model="proSelNumber"/>
                        <p>قیمت نهایی: {{finalPrice}} تومان</p>
                        <p :class="{error:merror, safe:!merror}">
                            {{buyingMessage}}
                        </p>
                        <button class="inModal" @click="submit_buy">خرید</button>
                    </template>
                </modal>

                <button class="buy" @click="submiting()">خرید محصول</button>
            </div>
            <div v-else class="btn">
                <button class="buy">ویرایش محصول</button>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from "axios";
    import Modal from "@/components/Modal";

    export default {
        name: "product",
        components: {
            Modal
        },
        props:{
            product: Object,
            admin: Boolean
        },
        data() {
            return {
                proSelNumber: 1,
                buyingMessage:"",
                finalPrice:this.product.price,
                merror:false
            }
        },
        methods: {
            submiting() {
                let ref = this.$refs.modalName;
                ref.openModal();
            },
            showPrice(){
                this.finalPrice = this.proSelNumber * this.product.price
            },
            submit_buy() {
                let self = this;
                let token = window.localStorage.getItem('token');

                axios({
                    method: 'post',
                    url: 'http://127.0.0.1:5000/buy',
                    headers: { 'authorization': `Bare ${token}` },
                    data: {
                        product: this.product.title,
                        number: this.proSelNumber,
                    }
                }).then(function (response) {
                    console.log(response);
                    self.buyingMessage = response.data.message
                    self.merror = false

                })
                    .catch((error => {
                        console.log(error);
                        self.buyingMessage = error.response.data.message
                        self.merror = true
                    }))

            },
        }
    }
</script>

<style scoped>
    .product{
        direction: rtl;
        width: 300px;
        height: 400px;
        display: flex;
        flex-direction: column;
        box-shadow: 0 4px 4px 0 rgba(0,0,0,0.2);
        position: relative;
        background-color: white;
    }

    .img-div{
        margin-top: 15px;
        position: absolute;
        left: 50%;
        transform: translate(-50%, 0%);
        width: 130px;
        height: 150px;
    }

    .image{
        width: 130px;
        height: 170px;
    }

    .title{
        color: #404040;
        font-size: 20px;
        margin-right: 20px;
        margin-top: 200px;
    }

    .cat{
        color: #b8b9ba;
        margin-bottom: 15px;
        font-size: 16px;
        padding-right: 20px;
    }

    .buy{
        text-align: center;
        padding: 8px 20px;
        font-size: 16px;
        border: none;
        border-radius: 24px;
        background-color:#009eff;
        box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
        color:white;
        position: absolute;
        top: 50%;
        left: 0%;
        transform: translate(20%, -50%);
        float: left;
    }

    .price{
        color: #585959;
        size: 18px;
        position: absolute;
        top: 50%;
        right: 0;
        transform: translate(-40%, -50%);
    }

    .upper-box{
        height: 80%;
        display: flex;
        flex-direction: column;
        position: relative;
        mso-page-border-z-order: in-back;
    }

    hr{
        display: inline-block;
        margin-right: 15px;
        margin-left: 15px;
    }

    .lower-box{
        position: relative;
        height: 20%;
        display: flex;
    }

    .sold{
        border-radius: 50%;
        width: 50px;
        height: 50px;
        line-height: 50px;
        background-color: white;
        color: #009eff;
        box-shadow: 0 8px 16px 0 rgba(0,0,0,0.4);
        text-align: center;
        vertical-align:middle;
        box-sizing: border-box;
        top: 0;
        left: 0;
        position: absolute;
        transform: translate(-50%,-50%);
        /*z-index: 2;*/
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
</style>