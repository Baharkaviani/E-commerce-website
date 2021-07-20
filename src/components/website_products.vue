<template>
    <div class="product-container">
        <div style="width: 75%;">
            <section class="products" >
                <Product v-for="product in displayedProducts"
                         :key="product.title"
                         :product="product"
                         :admin=false
                />
            </section>

            <nav aria-label="Page">
                <ul class="pagination">
                    <li class="page-item">
                        <button type="button" class="page-link" v-if="page !== 1" @click="page--"> Previous </button>
                    </li>
                    <li class="page-item">
                        <button type="button" class="page-link" v-for="pageNumber in pages.slice(page-1, page+5)" :key="pageNumber.id" @click="page = pageNumber"> {{pageNumber}} </button>
                    </li>
                    <li class="page-item">
                        <button type="button" @click="page++" v-if="page < pages.length" class="page-link"> Next </button>
                    </li>
                </ul>
            </nav>
        </div>

        <categories :cats="cats" class="categories" style="width: 25%;"/>
    </div>
</template>

<script>
    import Product from "@/components/Product";
    import categories from "@/components/categories";
    import axios from 'axios'
    export default {
        name: "website_products",
        components: {
            Product,
            categories
        },
        data () {
            return {
                page: 1,
                perPage: 10,
                pages: [],
                products: [
                    // {
                    //     title: 'ماوس۱',
                    //     img: require('../assets/mouse.png'),
                    //     price: 1000,
                    //     category: 'no1',
                    //     sold: 20
                    // },
                    // {
                    //     title: 'ماوس۲',
                    //     img: require('../assets/mouse.png'),
                    //     price: 2000,
                    //     category: 'دسته‌بندی یک',
                    //     sold: 40
                    // },
                    // {
                    //     title: 'ماوس۳',
                    //     img: require('../assets/mouse.png'),
                    //     price: 4000,
                    //     category: 'no4',
                    //     sold: 33
                    // },
                    // {
                    //     title: 'ماوس گیمینگ ریزر',
                    //     img: require('../assets/mouse.png'),
                    //     price: '۳۰,۰۰۰',
                    //     category: 'دسته‌بندی یک',
                    //     sold: 34
                    // },
                    // {
                    //     title: 'ماوس۱',
                    //     img: require('../assets/mouse.png'),
                    //     price: 1000,
                    //     category: 'no1',
                    //     sold: 20
                    // },
                    // {
                    //     title: 'ماوس۲',
                    //     img: require('../assets/mouse.png'),
                    //     price: 2000,
                    //     category: 'دسته‌بندی یک',
                    //     sold: 40
                    // },
                    // {
                    //     title: 'ماوس۳',
                    //     img: require('../assets/mouse.png'),
                    //     price: 4000,
                    //     category: 'no4',
                    //     sold: 33
                    // },
                    // {
                    //     title: 'ماوس گیمینگ ریزر',
                    //     img: require('../assets/mouse.png'),
                    //     price: '۳۰,۰۰۰',
                    //     category: 'دسته‌بندی یک',
                    //     sold: 34
                    // },
                    // {
                    //     title: 'ماوس۱',
                    //     img: require('../assets/mouse.png'),
                    //     price: 1000,
                    //     category: 'no1',
                    //     sold: 20
                    // },
                    // {
                    //     title: 'ماوس۲',
                    //     img: require('../assets/mouse.png'),
                    //     price: 2000,
                    //     category: 'دسته‌بندی یک',
                    //     sold: 40
                    // },
                    // {
                    //     title: 'ماوس۳',
                    //     img: require('../assets/mouse.png'),
                    //     price: 4000,
                    //     category: 'no4',
                    //     sold: 33
                    // },
                    // {
                    //     title: 'ماوس گیمینگ ریزر',
                    //     img: require('../assets/mouse.png'),
                    //     price: '۳۰,۰۰۰',
                    //     category: 'دسته‌بندی یک',
                    //     sold: 34
                    // },
                    // {
                    //     title: 'ماوس۱',
                    //     img: require('../assets/mouse.png'),
                    //     price: 1000,
                    //     category: 'no1',
                    //     sold: 20
                    // },
                    // {
                    //     title: 'ماوس۲',
                    //     img: require('../assets/mouse.png'),
                    //     price: 2000,
                    //     category: 'دسته‌بندی یک',
                    //     sold: 40
                    // },
                    // {
                    //     title: 'ماوس۳',
                    //     img: require('../assets/mouse.png'),
                    //     price: 4000,
                    //     category: 'no4',
                    //     sold: 33
                    // },
                    // {
                    //     title: 'ماوس گیمینگ ریزر',
                    //     img: require('../assets/mouse.png'),
                    //     price: '۳۰,۰۰۰',
                    //     category: 'دسته‌بندی یک',
                    //     sold: 34
                    // },
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
                  'دسته‌بندی یک',
                  'دسته‌بندی دو',
                  'دسته‌بندی سه',
                  'دسته‌بندی یک',
                  'دسته‌بندی دو',
                  'دسته‌بندی سه',
                    'دسته‌بندی چهار'
                ],
            }
        },
        methods: {
            setPages () {
                let numberOfPages = Math.ceil(this.products.length / this.perPage);
                for (let index = 1; index <= numberOfPages; index++) {
                    this.pages.push(index);
                }
            },
            paginate () {
                let page = this.page;
                let perPage = this.perPage;
                let from = (page * perPage) - perPage;
                let to = (page * perPage);
                return  this.products.slice(from, to);
            },

        },
        computed: {
            displayedProducts () {
                return this.paginate();
            }
        },
        watch: {
            pages () {
                this.setPages();
            }
        },
      created() {
          // this.getProducts()

            // console.log("hellllo")
              axios({
                method: 'get',
                url: 'http://127.0.0.1:5000/products',

              }).then((response)=>{
                  for (const product of response.data){
                    // console.log(JSON.stringify(product))
                      product.img =require('../assets/mouse.png')
                      this.products.push(product)
                  }

              })
                  .catch((error => {
                    console.log(error)

                  }))
            }



    }
</script>

<style scoped>
    .product-container {
        display: flex;
        justify-content: space-between;
        flex-direction: row;
        position: relative;
        margin: 10px;
    }

    .products {
        display: flex;
        align-items: center;
        justify-content: center;
        flex-direction: row-reverse;
        flex-wrap: wrap;
        gap: 10px;
    }

    /*.pagination {*/
    /*    display: flex;*/
    /*    align-items: center;*/
    /*    justify-content: center;*/
    /*    flex-direction: row-reverse;*/
    /*}*/

    button.page-link {
        display: inline-block;
    }

    button.page-link {
        font-size: 20px;
        color: #29b3ed;
        font-weight: 500;
    }

    .offset{
        width: 500px !important;
        margin: 20px auto;
    }
</style>