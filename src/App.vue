<template>
    <div class="app">
        <!--    nav menu of the website    -->
        <nav_menu class="menu"/>

        <!--    website component contains the main part of site!    -->
        <website class="website"/>
<!--        <website_products/>-->

<!--        <user_profile class="test"></user_profile>-->

<!--        <admin_profile></admin_profile>-->

        <!--    login and register section    -->
<!--        <div class="loginRegister">-->
<!--            <login_register class="main" :login="logv"/>-->
<!--        </div>-->

        <!--    footer of the website    -->
        <footer-section class="footerSection"/>




<!--        <categories :cats="cats"></categories>-->

<!--      <Input_textfield v-for="inp in inps"-->
<!--                         :key="inp.label"-->
<!--                         :attr="inp"-->
<!--                    />-->
    </div>
</template>

<script>
    import nav_menu from "@/components/fixed/nav_menu";
    import footerSection from "@/components/fixed/footerSection";

    import website from "@/components/website";
    // import website_products from "@/components/website_products";

    // import user_profile from "@/components/profiles/user_profile";
    // import admin_profile from "@/components/profiles/admin_profile";
    //import Categories from "@/components/categories";
    //import login_register from "@/components/register_login/login_register";
    //import Input_textfield from "@/components/register_login/input_textfield";

    export default {
        name: 'App',
        components: {
            // website_products,
            nav_menu,
            footerSection,
            website,
            // login_register

            // user_profile
            // admin_profile
            // Categories,
        },
        data (){
            return{
                logv : false,
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
</style>
