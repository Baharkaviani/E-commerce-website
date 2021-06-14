<template>
    <nav v-bind:class="active" v-on:click.prevent>
        <a href="#" class="home" v-on:click="makeActive('home')">Home</a>
        <a href="#" class="projects" v-on:click="makeActive('projects')">Projects</a>
        <a href="#" class="services" v-on:click="makeActive('services')">Services</a>
        <a href="#" class="contact" v-on:click="makeActive('contact')">Contact</a>
    </nav>
</template>

<script>
    export default {
        name: "Menu"
    }
</script>

<style scoped>
    nav {
        background-color: white;
        height: 65px;
        border-style: solid;
        margin:0;
        padding:0;
        position: relative;
        display:inline-block;
    }

    nav a{
        display:inline-block;
        padding: 18px 30px;
        color:#fff;
        font-weight:bold;
        font-size:16px;
        text-decoration:none;
        line-height:1;
        text-transform: uppercase;
        background-color:transparent;

        float: none;
        position: relative;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);

        -webkit-transition:background-color 0.25s;
        -moz-transition:background-color 0.25s;
        transition:background-color 0.25s;
    }

    nav a:first-child{
        border-radius:2px 0 0 2px;
    }

    nav a:last-child{
        border-radius:0 2px 2px 0;
    }

    nav.home .home,
    nav.projects .projects,
    nav.services .services,
    nav.contact .contact{
        background-color:#e35885;
    }
</style>