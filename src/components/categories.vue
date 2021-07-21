<template>
    <div class="main-cat">
        <label class="cat-label">دسته بندی‌ها</label>
        <hr>
        <div class="container">
            <label v-for="(cat,index) in cats" :key="index" class="labels">{{cat}}
                <input type="checkbox" @change="returnCats" v-model="selectedCats" :name="cat" :value="cat">
                <span class="checkmark"></span>
            </label>
        </div>
    </div>
</template>

<script>
    export default {
        name: "categories",
        props:['cats'],
      data() {
        return {
          selectedCats:[]
        }
        },
      methods:{
          returnCats(){
            this.$emit('catsChanged', this.selectedCats)
          }
      }
    }
</script>

<style scoped>
    .main-cat {
        direction: rtl;
        padding-right: 10px;
        padding-left: 10px;
        color: #585959;
        background-color: white;
        /*margin-left: 10px;*/
        max-height: 270px;
        /*width: 280px;*/
    }

    hr {
      margin-bottom: 10px;
      color: #787575;
    }
    .cat-label {
        display: block;
        font-size: 18px;
        margin-top: 10px;
        margin-bottom: 10px;
    }

    .container{
        /*margin-top: 10px;*/
        overflow-y: scroll;
        max-height: 210px;
    }

    .labels {
        display: block;
        position: relative;
        margin-bottom: 10px;
        cursor: pointer;
        font-size: 16px;
        padding-right: 25px;
    }

    .labels input {
        position: absolute;
        opacity: 0;
        cursor: pointer;
        height: 0;
        width: 0;
    }

    .checkmark {
        position: absolute;
        top: 15%;
        right: 0;
        height: 15px;
        width: 15px;
        background-color: white;
        border: 1px solid darkgrey;
        border-radius: 100px;
    }

    .labels input:checked ~ .checkmark {
        background-color:#009eff;
    }
</style>