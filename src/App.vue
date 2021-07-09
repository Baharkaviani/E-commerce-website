<template>
    <div class="app">
        <nav_menu class="menu"/>
<!--        <website class="main"/>-->
<!--        <div class="app-item">-->
            <login_register class="main"/>
<!--        </div>-->
        <footer-section class="footerSection"/>
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
    // import website from "@/components/website";
    import footerSection from "@/components/fixed/footerSection";
    import login_register from "@/components/register_login/login_register";

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
            // website,
            footerSection,
            login_register
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
    #app {
        display: flex;
        justify-content: center;
    }

    /** {*/
    /*  margin: 0;*/
    /*  padding: 0;*/
    /*  box-sizing: border-box;*/
    /*}*/
    /*body {*/
    /*  font-family: 'montseratt', sans-serif;*/
    /*}*/
    /*#app {*/
    /*  width: 100vw;*/
    /*  min-height: 100vh;*/
    /*  overflow: hidden;*/
    /*  background-color: white;*/
    /*  display: flex;*/
    /*  justify-content: center;*/
    /*  align-items: center;*/
    /*}*/
    /*.products {*/
    /*  display: flex;*/
    /*  max-width: 1280px;*/
    /*  padding: 25px;*/
    /*  margin: 0 auto;*/
    /*}*/

    .app {
        width: 1280px;
        display: grid;
        position: absolute;
        grid-template-areas:
                'menu'
                'main'
                'footer';
        align-content: space-between;
        background-color: #dddddd;
        left: 0;
        right: 0;
        margin: 0 auto;
        height: 100%;

    }


    /*.menu {*/
    /*    flex-basis: 1280px;*/
    /*}*/
    .app-item{
      border: 2px solid red;
    }
    .main {
        top: 0%;
        background-color: #dddddd;
        bottom: 50%;
        position: absolute;
        transform: translate(0, 50%);
        margin-top: 65px;


    }

    /*.footerSection {*/
    /*    flex: 1 100%;*/
    /*}*/
</style>
