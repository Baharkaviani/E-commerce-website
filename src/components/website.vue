<template>
    <div class="website-container">
        <hero_header class="main-hero"/>
        <sorter class="sorter"/>
    </div>
</template>

<script>
    import hero_header from "@/components/hero_header";
    import sorter from "@/components/sorter";

    export default {
        name: "website",
        components: {
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
    }

</style>