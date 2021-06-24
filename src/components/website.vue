<template>
    <div class="website-container">
<!--        <hero_header class="main-hero"/>-->
        <div class="item1">Main</div>
        <div class="item2">Right</div>
    </div>
</template>

<script>
    // import hero_header from "@/components/hero_header";
    export default {
        name: "website",
        components: {
            // hero_header
        },
    }

</script>

<style scoped>
    .website-container {
        width: 1280px;
        height: 100%;
        position: relative;
        display: grid;
        top: 65px;
        left: 0;
        right: 0;
        margin: 0 auto;
        grid-template-areas:
                'header header header right'
                'footer footer footer footer';
        align-content: space-between;
        background-color: #2196F3;
    }

    .website-container > div {
        text-align: center;
        font-size: 30px;
    }
    .website-container > .main-hero {
        grid-area: main-hero;
    }
    .item1 { grid-area: header; }
    .item2 { grid-area: right; }
    .website-container > .footerSection { grid-area: footer; }
</style>