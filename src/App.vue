<template>
    <div class="app">
        <!--    nav menu of the website    -->
        <nav_menu class="menu"/>

        <!--    website component contains the main part of site!    -->
        <website class="website"/>

        <!--    login and register section    -->
<!--        <div class="loginRegister">-->
<!--            <login_register class="main"/>-->
<!--        </div>-->

        <!--    footer of the website    -->
        <footer-section class="footerSection"/>

<!--        <user_profile class="test"></user_profile>&ndash;&gt;-->
<!--        <admin_profile></admin_profile>-->
<!--        <sorter></sorter>-->
<!--        <section class="products">-->
<!--            <Product v-for="product in products"-->
<!--                 :key="product.title"-->
<!--                 :product="product"-->
<!--                  :admin=true-->
<!--            />-->
<!--        </section>-->
<!--        <categories property="cats"></categories>-->
<!--        <categories :cats="cats"></categories>-->

<!--      <hero_header></hero_header>-->

<!--      <Input_textfield v-for="inp in inps"-->
<!--                         :key="inp.label"-->
<!--                         :attr="inp"-->
<!--                    />-->
<!--      <login_register :login=false></login_register>-->

    </div>
</template>

<script>
    import nav_menu from "@/components/fixed/nav_menu";
    import website from "@/components/website";
    import footerSection from "@/components/fixed/footerSection";
    //import login_register from "@/components/register_login/login_register";
    // import user_profile from "@/components/profiles/user_profile";
    // import admin_profile from "@/components/profiles/admin_profile";
    //import sorter from "@/components/sorter";
    //import Product from "@/components/Product";
    //import Categories from "@/components/categories";
    //import hero_header from "@/components/hero_header";
    //import login_register from "@/components/register_login/login_register";
    //import Input_textfield from "@/components/register_login/input_textfield";

    export default {
        name: 'App',
        components: {
            nav_menu,
            website,
            footerSection,
            // user_profile
            // admin_profile
            // login_register
            // Categories,
            // sorter,
            // Product,
            // hero_header
        },
        data (){
            return{
                products:[
                    {
                        title:'ماوس۱',
                        img:require('./assets/mouse.png'),
                        price:1000,
                        category:'no1',
                        sold:20
                    },
                    {
                        title:'ماوس۲',
                        img:require('./assets/mouse.png'),
                        price:2000,
                        category:'دسته‌بندی یک',
                        sold:40
                    },
                    {
                        title:'ماوس۳',
                        img:require('./assets/mouse.png'),
                        price:4000,
                        category:'no4',
                        sold: 33
                    },
                    {
                        title:'ماوس گیمینگ ریزر',
                        img:require('./assets/mouse.png'),
                        price:'۳۰,۰۰۰',
                        category:'دسته‌بندی یک',
                        sold: 34
                    }
                ],
                cats:[
                    'دسته‌بندی یک',
                    'دسته‌بندی دو',
                    'دسته‌بندی سه',
                    'دسته‌بندی یک',
                    'دسته‌بندی دو',
                    'دسته‌بندی سه',
                    'دسته‌بندی یک',
                    'دسته‌بندی دو',
                    'دسته‌بندی سه',
                    'دسته‌بندی یک',
                    'دسته‌بندی دو',
                    'دسته‌بندی سه',
                    'دسته‌بندی یک',
                    'دسته‌بندی دو',
                    'دسته‌بندی سه',
                    'دسته‌بندی چهار'
                ],
                inps:[
                    {label:"نام",
                        placeholder:"نام خود را وارد کنید...",
                        class:true},
                    {label:"نام خانوادگی",
                        placeholder:"نام خانوادگی خود را وارد کنید...",
                        class:true},
                    {label:"ایمیل",
                        placeholder:"ایمیل خود را وارد کنید...",
                        class:false}
                ],

            }
        }
    }
</script>

<style>
    * {
        margin: 0;
    }



    .app {
        display: flex;
        align-items: center;
        justify-content: center;
        flex-direction: column;
        /*position: relative;*/
        background-color: #dddddd;
        width: 1280px;
        left: 0;
        right: 0;
        margin: 0 auto;

        min-height: 100vh;
        overflow-y: hidden;
    }

    /*.app {*/
    /*    width: 1280px;*/
    /*    display: grid;*/
    /*    position: absolute;*/
    /*    grid-template-areas:*/
    /*            'menu'*/
    /*            'main'*/
    /*            'footer';*/
    /*    align-content: space-between;*/
    /*    background-color: #dddddd;*/
    /*    left: 0;*/
    /*    right: 0;*/
    /*    margin: 0 auto;*/
    /*    height: 100%;*/
    /*}*/

    /*.app .menu {*/
    /*    flex: 0 1 auto;*/
    /*}*/

    .app .loginRegister {
        /*!*flex: 1 1 auto;*!*/
        /*min-height: 100vh;*/
        /*overflow-y: hidden;*/
    }

    .app .footerSection {
        flex: 0 1 auto;
    }

    .main {
        /*bottom: 50%;*/
        /*position: absolute;*/
        /*transform: translate(0, 50%);*/
    }

    .website {
        margin-top: 60px;
    }
</style>
