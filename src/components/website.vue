<template>
    <div class="website-container">
        <nav_menu class="menu"/>
        <div class="item1">Main</div>
        <div class="item2">Right</div>
        <footer-section class="footerSection"/>
    </div>
</template>

<script>
    import nav_menu from "@/components/fixed/nav_menu";
    import footerSection from "@/components/fixed/footerSection";
    export default {
        name: "website",
        components: {
            nav_menu,
            footerSection
        },
    }

</script>

<style scoped>
    .website-container {
        width: 1280px;
        height: 100%;
        position: absolute;
        display: grid;
        grid-template-areas:
                'menu menu menu menu'
                'header header header right'
                'footer footer footer footer';
        align-content: space-between;
        background-color: #2196F3;
    }

    .website-container > div {
        text-align: center;
        font-size: 30px;
    }
    .website-container > .menu { grid-area: menu; }
    .item1 { grid-area: header; }
    .item2 { grid-area: right; }
    .website-container > .footerSection { grid-area: footer; }
</style>