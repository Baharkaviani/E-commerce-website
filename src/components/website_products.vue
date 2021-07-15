<template>
    <div class="product-container">
        <section class="products" style="width: 75%;">
            <Product v-for="product in products"
                     :key="product.title"
                     :product="product"
                     :admin=false
            />
        </section>
        <categories class="categories" style="background-color:#aaa; width: 25%;"/>
    </div>
</template>

<script>
    import Product from "@/components/Product";
    import categories from "@/components/categories";

    export default {
        name: "website_products",
        components: {
            Product,
            categories
        },
        data () {
            return {
                products: [
                    {
                        title: 'ماوس۱',
                        img: require('../assets/mouse.png'),
                        price: 1000,
                        category: 'no1',
                        sold: 20
                    },
                    {
                        title: 'ماوس۲',
                        img: require('../assets/mouse.png'),
                        price: 2000,
                        category: 'دسته‌بندی یک',
                        sold: 40
                    },
                    {
                        title: 'ماوس۳',
                        img: require('../assets/mouse.png'),
                        price: 4000,
                        category: 'no4',
                        sold: 33
                    },
                    {
                        title: 'ماوس گیمینگ ریزر',
                        img: require('../assets/mouse.png'),
                        price: '۳۰,۰۰۰',
                        category: 'دسته‌بندی یک',
                        sold: 34
                    }
                ],
            }
        }
    }
</script>

<style scoped>
    .product-container {
        display: flex;
        align-items: center;
        justify-content: space-between;
        flex-direction: row;
        position: relative;
    }

    .products {
        display: flex;
        align-items: center;
        justify-content: space-between;
        flex-direction: row-reverse;
        flex-wrap: wrap;
    }
</style>