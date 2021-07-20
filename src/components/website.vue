<template>
    <div class="website-container">
        <hero_header class="main-hero"/>
        <sorter class="sorter"  v-on:sortProducts="sort($refs.productComponent,$event)"/>
        <website_products ref="productComponent"/>
    </div>
</template>

<script>
    import hero_header from "@/components/hero_header";
    import sorter from "@/components/sorter";
    import website_products from "@/components/website_products";

    export default {
        name: "website",
        components: {
            website_products,
            hero_header,
            sorter
        },
      data(){
          return{
            reference: Object
          }
      },
      methods:{
          sort(ref,order){
            ref.sortGet(order)
          }
      }
    }

</script>

<style scoped>
    .website-container {
        display: flex;
        align-items: center;
        justify-content: space-between;
        flex-direction: column;
        width: 1280px;
        margin-bottom: 75px;
    }
</style>