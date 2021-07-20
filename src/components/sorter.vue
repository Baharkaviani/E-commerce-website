<template>
    <nav>
        <div class="sort sortLabel"><label>مرتب سازی بر اساس:</label></div>
        <button  class="sort sortButtons " :class="{active:this.sorted=='sold'}" @click="soldClicked">بیشترین فروش</button>
        <button class="sort sortButtons" :class="{active:this.sorted=='priceAsc'}" @click="priceAscClicked">کمترین قیمت</button>
      <button class="sort sortButtons" :class="{active:this.sorted=='priceDesc'}" @click="priceDescClicked">بیشترین قیمت</button>
      <button class="sort sortButtons" :class="{active:this.sorted=='date'}" @click="dateClicked">تاریخ ایجاد محصول</button>
    </nav>
</template>

<script>
    export default {
        name: "sorter",
      data () {
        return {
          sorted :""
        }
        },
        methods:{
          soldClicked(){
            this.sorted = "sold"
            this.emitToWebsite()
          },
          priceDescClicked(){
            this.sorted = "priceDesc"
            this.emitToWebsite()
          },
          priceAscClicked(){
            this.sorted = "priceAsc"
            this.emitToWebsite()
          },
          dateClicked(){
            this.sorted = "date"
            this.emitToWebsite()
          },
          emitToWebsite(){
            this.$emit('sortProducts', this.sorted)
          }
        }

    }
</script>

<style scoped>
    nav {
        float: right;
        direction: rtl;
        background-color: #FFFFFF;
        display: flex;
        align-items: center;
        text-align: center;
        font-size: 16px;
        position: relative;
        width: 1260px;
        height: 50px;
        margin-top: 10px;
    }

    nav .sort {
        margin-right: 25px;
        position: relative;
        text-align: center;
        display: flex;
    }

    .sortLabel{
        color: #404040;
    }

    .sortButtons{
        background-color:white;
        text-align: center;
        color: #404040;
        padding: 8px 20px;
        font-size: 16px;
        border: none;
        border-radius: 24px;
    }

    .active, .sortButtons:hover{
        background-color:#009eff;
        box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
        color:white;
    }
</style>