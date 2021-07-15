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
    .footerSection{
        direction: rtl;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 65px;
        position: fixed;
        left: 0;
        right: 0;
        bottom: 0;
        width: 1280px;
        background-color: #000000;
        text-align: center;
        margin: 0 auto;
    }

    #footer {
        color: #bebebe;
        text-align: center;
        display: flex;
        font-size: 16px;
        position: relative;
    }
</style>