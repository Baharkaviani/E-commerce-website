<template>
    <div class="website-container">
        <hero_header class="main-hero"/>
    </div>
</template>

<script>
    import hero_header from "@/components/hero_header";

    export default {
        name: "website",
        components: {
            hero_header
        },
    }

</script>

<style scoped>
    .website-container {
        width: 1280px;
        position: relative;
    }

    .website-container > div {
        text-align: center;
        font-size: 30px;
    }
</style>