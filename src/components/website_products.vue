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
                    <li v-if="page !== 1" class="page-item">
                        <button type="button" class="page-link" @click="page--"> Previous </button>
                    </li>
                    <li v-for="pageNumber in pages.slice(page-1, page+5)" :key="pageNumber.id" class="page-item">
                        <button type="button" class="page-link" @click="page = pageNumber"> {{pageNumber}} </button>
                    </li>
                    <li v-if="page !== numberOfPages" class="page-item">
                        <button type="button" @click="page++" class="page-link"> Next </button>
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
                perPage: 15,
                numberOfPages: 1,
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
                    //   'دسته‌بندی یک',
                    //   'دسته‌بندی دو',
                    //   'دسته‌بندی سه',
                    //   'دسته‌بندی یک',
                    //   'دسته‌بندی دو',
                    //   'دسته‌بندی سه',
                    //   'دسته‌بندی یک',
                    //   'دسته‌بندی دو',
                    //   'دسته‌بندی سه',
                    //   'دسته‌بندی یک',
                    //   'دسته‌بندی دو',
                    //   'دسته‌بندی سه',
                    //   'دسته‌بندی یک',
                    //   'دسته‌بندی دو',
                    //   'دسته‌بندی سه',
                    // 'دسته‌بندی یک',
                    // 'دسته‌بندی دو',
                    // 'دسته‌بندی سه',
                    // 'دسته‌بندی یک',
                    // 'دسته‌بندی دو',
                    // 'دسته‌بندی سه',
                    //   'دسته‌بندی چهار'
                ],
            }
        },
        methods: {
            setPages () {
                this.numberOfPages = Math.ceil(this.products.length / this.perPage);
                console.log("number:" + Math.ceil(this.products.length / this.perPage));
                for (let index = 1; index <= this.numberOfPages; index++) {
                    this.pages.push(index);
                }
            },
            paginate () {
                let page = this.page;
                let perPage = this.perPage;
                let from = (page - 1) * perPage;
                let to = 0;
                console.log("numberOfPages:" + this.numberOfPages);
                if (page === this.numberOfPages) {
                    to = this.products.length;
                }
                else {
                    to = from + perPage;
                }
                console.log("page:" + this.page + "perpage:" + perPage);
                return this.products.slice(from, to);
            },
            getProducts() {
                axios({
                    method: 'get',
                    url: 'http://127.0.0.1:5000/products',
                    params:{order:'sold'}
                }).then((response)=>{
                    for (const product of response.data){
                        console.log("number of products" + this.products.length);
                        product.img =require('../assets/mouse.png');
                        this.products.push(product)
                    }
                    this.setPages();
                }).catch((error => {
                    console.log(error)
                }));
            },
            getCategories(){
                axios({
                    method: 'get',
                    url: 'http://127.0.0.1:5000/categories',
                }).then((response)=>{
                    for (const category of response.data){
                        // console.log(JSON.stringify(product))
                        this.cats.push(category);
                    }
                }).catch((error => {
                    console.log(error);
                }));
            },
          searchThisItem(searchedItem){
              let self = this
            axios({
              method: 'get',
              url: 'http://127.0.0.1:5000//searchproduct',
              params:{product:searchedItem}

            }).then((response)=>{
              self.products = []
              if (response.data.length >0)
                  for (const product of response.data){
                      product.img =require('../assets/mouse.png');
                      self.products.push(product)
                  }

            })
                .catch((error => {
                  console.log(error)
                }))
          },
          sortGet(order){
              let self = this
            axios({
              method: 'get',
              url: 'http://127.0.0.1:5000/products',
              params:{order:order}

                }).then((response)=>{
                    self.products = []
                    for (const product of response.data){
                        product.img =require('../assets/mouse.png');
                        self.products.push(product)
                    }
                })
                    .catch((error => {
                        console.log(error)
                    }))
            },
        },
        computed: {
            displayedProducts () {
                return this.paginate();
            }
        },
        created() {
            this.getProducts();
            this.getCategories();
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
        width: 1260px;
      gap: 10px;
    }

    .products {
        display: flex;
        align-items: center;
        justify-content: center;
        flex-direction: row-reverse;
        flex-wrap: wrap;
        gap: 10px;
    }

    .pagination {
        display: flex;
        align-items: center;
        justify-content: center;
        flex-direction: row-reverse;
        direction: rtl;
        margin-top: 20px;
        list-style-type: none;
        height: 40px;
    }

    button.page-link {
        display: inline-block;
    }

    button.page-link {
        font-size: 20px;
        color: #29b3ed;
        font-weight: 500;
    }
</style>