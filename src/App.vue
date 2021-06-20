<template>
  <div id="app">
<!--    <nav_menu></nav_menu>-->
    <sorter></sorter>
<!--    <section class="products">-->
<!--    <Product v-for="product in products"-->
<!--             :key="product.title"-->
<!--             :product="product"-->
<!--    />-->
<!--    </section>-->
<!--    <cathegories property="cats"></cathegories>-->
    <footer-section></footer-section>
  </div>
</template>

<script>

//import nav_menu from './components/nav_menu'
// import sorter from "@/components/sorter";
// import Product from "@/components/Product";
//import Cathegories from "@/components/cathegories";
import footerSection from "@/components/footerSection";
export default {
  name: 'App',
  components: {
    // Cathegories
     //nav_menu
    // sorter
    // Product
    footerSection
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
        'دسته‌بندی چهار'
      ]
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
