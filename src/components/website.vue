<template>
    <div class="website-container">
        <hero_header class="main-hero"/>
        <sorter class="sorter"/>
        <website_products/>
    </div>
</template>

<script>
    import hero_header from "@/components/hero_header";
    import sorter from "@/components/sorter";
    import website_products from "@/components/website_products";

    export default {
        name: "website",
        components: {
            website_products,
            hero_header,
            sorter
        },
    }

</script>

<style scoped>
    .website-container {
        display: flex;
        align-items: center;
        justify-content: space-between;
        flex-direction: column;
        width: 1280px;
        margin-bottom: 75px;
    }
</style>