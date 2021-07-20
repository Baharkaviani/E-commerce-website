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
            <div v-if="!admin" class="btn" @click="$refs.modalName.openModal()"><button class="buy">خرید محصول</button></div>
            <div v-else class="btn"><button class="buy">ویرایش محصول</button></div>
        </div>

        <modal ref="modalName">
            <template v-slot:body>
                <input_textfield v-on:childToParent="onChildClick"/>
            </template>
        </modal>
    </div>
</template>

<script>
    import axios from "axios";

    export default {
        name: "product",
        props:{
            product: Object,
            admin: Boolean
        },
        methods: {
            showModal() {
                this.$refs.modal.openModal();
            },
            submit_buy() {
                console.log("Product submit -> add product:" + this.valid);
                this.$refs.modalName.openModal();
                // this.openTheModal();
                if (this.valid.name && this.valid.sname && this.valid.email && this.valid.pass && this.valid.address) {
                    axios({
                        method: 'post',
                        url: 'http://127.0.0.1:5000/signup',
                        data: {
                            email: this.args.email,
                            name: this.args.name,
                            sname: this.args.sname,
                            password: this.args.pass,
                            address: this.args.address
                        }
                    }).then(function (response) {
                        console.log(response);
                        // this.submitted = true
                        if (response.status === 200) {
                            this.modalProp = response.data.message
                        } else {
                            this.modalProp = "ثبت نام نا موفق"
                        }
                        // $refs.modalName.openModal();
                    })
                        .catch((error => {
                            console.log(error);
                        }))
                }
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
</style>