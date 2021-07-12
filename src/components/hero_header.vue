<template>
    <div class="main-hero">
        <div class="hero-container">
            <h1>در محصولات سایت جستجو کنید...</h1>
            <input type="text" id="product" name="product" placeholder="نام محصول خود را وارد کنید...">
            <a class="button">جستجو کنید</a>
        </div>
    </div>
</template>

<script>
    export default {
        name: "hero_header"
    }
</script>

<style scoped>
    * {
        direction: rtl;
    }

    .main-hero{
        background-color: #ff6213;
        left: 0;
        right: 0;
        margin: auto 0;
        width: 1280px;
        position: relative;
        /*height: 300px;*/
    }

    .hero-container {
        display: flex;
        align-items: center;
        justify-content: center;
        flex-direction: column;
    }

    h1 {
        margin-top: 80px;
        font-size: 32px;
        color: white;
        text-align: center;
    }

    input {
        text-align: center;
        border-radius: 24px;
        /*position: absolute;*/
        width: 800px;
        margin: 40px 0 0 0;
        /*left: 50%;*/
        /*transform: translate(-50%, 0);*/
        height: 20px;
    }

    input:focus{
        outline: none;
    }

    .button{
        margin-top: 35px;
        border-radius: 24px;
        /*position: absolute;*/
        border: none;
        background-color: #ffcc00;
        font-size: 16px;
        text-align: center;
        padding: 5px 25px;
        /*display: block;*/
    }
</style>