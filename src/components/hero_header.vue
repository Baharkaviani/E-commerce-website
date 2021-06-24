<template>
    <div class="main-hero">
        <div class="hero-containter">
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
    *{
        direction: rtl;
        left: 0;
        right: 0;
        width: 1280px;
    }

    .main-hero{
        border: 1px solid black;
        /*width: 500px;*/
        height: 700px;
        position: relative;
    }

    h1{
        margin-top: 80px;
        font-size: 32px;
        color: red;
        text-align: center;
        border-color: black;
        border: 1px solid;
        margin-bottom: 0;
    }

    input {
        margin-top: 40px;
        /*width: 400px;*/
        text-align: center;
        border-radius: 24px;
        position: absolute;
        left: 50%;
        transform: translate(-50%, 0);
        height: 20px;
    }

    input:focus{
        outline: none;
    }

    .button{
        margin-top: 95px;
        border-radius: 24px;
        border: none;
        background-color: #ffcc00;
        font-size: 16px;
        text-align: center;
        padding: 5px 25px;
        position: absolute;
        left: 50%;
        transform: translate(-50%, 0);
        display: inline-block;
    }
</style>