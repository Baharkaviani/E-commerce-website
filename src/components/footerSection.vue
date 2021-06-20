<template>
    <footer class="footerSection">
        <p id="footer">تمامی حقوق برای تارا صبا و بهار کاویانی محفوظ است.</p>
    </footer>
</template>

<script>
    export default {
        name: "footerSection"
    }
</script>

<style scoped>
    *{
        /*font-family: ;*/
        /*width: 1280px;*/
    }

    .footerSection{
        direction: rtl;
        display: flex;
        height: 65px;
        position: absolute;
        left: 0;
        bottom: 0;
        width: 1280px;
        background-color: #000000;
        color: #FFFFFF;
        text-align: center;
    }

    #footer {
        color: #bebebe;
        text-align: center;
        display: flex;
        font-size: 16px;
        position: absolute;
        left: 50%;
        transform: translate(-50%, 50%);
    }
</style>