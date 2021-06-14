<template>
    <!-- Top navigation -->
    <div class="topnav">

        <!-- Centered link -->
        <div class="topnav-centered">
            <a href="#home" class="active">Home</a>
        </div>

        <!-- Left-aligned links (default) -->
        <a href="#news">News</a>
        <a href="#contact">Contact</a>

        <!-- Right-aligned links -->
        <div class="topnav-centered">
            <a href="#about">About</a>
        </div>

    </div>
</template>

<script>
    export default {
        name: "testMenu"
    }
</script>

<style scoped>
    .topnav {
        background-color: white;
        position: relative;
        border-style: solid;
        overflow: hidden;
        height: 65px;
    }

    .topnav a {
        float: left;
        color: #3c3c3c;
        text-align: center;
        padding: 14px 16px;
        text-decoration: none;
        font-size: 17px;
    }

    .topnav a:hover {
        background-color: #66eff2;
        color: black;
    }

    .topnav a.active {
        background-color: #04AA6D;
        color: white;
    }

    .topnav-centered a {
        position: absolute;
        top: 50%;
        transform: translate(-50%, -50%);
    }

    .topnav-right {
        float: right;
    }
</style>