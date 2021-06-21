<template>
    <div id="app">
<!--        <website id="website"></website>-->
<!--        <sorter></sorter>-->
<!--        <section class="products">-->
<!--            <Product v-for="product in products"-->
<!--                 :key="product.title"-->
<!--                 :product="product" -->
<!--            />-->
<!--        </section>-->
<!--        <categories property="cats"></categories>-->
<!--        <categories :cats="cats"></categories>-->
      <hero_header></hero_header>

    </div>
</template>

<script>
    // import website from "@/components/website";
    //import sorter from "@/components/sorter";
    //import Product from "@/components/Product";
    //import Categories from "@/components/categories";
  import hero_header from "@/components/hero_header";
    export default {
        name: 'App',
        components: {
            // website,
            // Categories,
            // sorter,
            // Product,
          hero_header
        },
        data (){
            return{
                products:[
                    {
                      title:'ماوس۱',
                      img:require('./assets/mouse.png'),
                      price:1000,
                      category:'no1'
                    },
                    {
                      title:'ماوس۲',
                      img:require('./assets/mouse.png'),
                      price:2000,
                      category:'دسته‌بندی یک'
                    },
                    {
                      title:'ماوس۳',
                      img:require('./assets/mouse.png'),
                      price:4000,
                      category:'no4'
                    },
                    {
                      title:'ماوس گیمینگ ریزر',
                      img:require('./assets/mouse.png'),
                      price:'۳۰,۰۰۰',
                      category:'دسته‌بندی یک'
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
                ]
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
</style>
