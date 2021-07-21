<template>
    <div class="main-hero">
        <div class="hero-container">
            <h1>در محصولات سایت جستجو کنید...</h1>
            <input type="text" id="product" name="product" v-model="searchedItem" placeholder="نام محصول خود را وارد کنید...">
            <button class="button" @click="search">جستجو کنید</button>

            <div class="slideshow-container">
                <div class="mySlides fade">
                    <img src="../assets/clock.png" style="width:100%; height: 240px" alt="clock">
                </div>

                <div class="mySlides fade">
                    <img src="../assets/pens.png" style="width:100%; height: 240px" alt="pens">
                </div>

                <div class="mySlides fade">
                    <img src="../assets/perfume.png" style="width:100%; height: 240px" alt="perfume">
                </div>
            </div>
            
        </div>
    </div>
</template>

<script>
    export default {
        name: "hero_header",
        data: function() {
            return {
                slideIndex:0,
                searchedItem : ""
            };
        },
        methods: {
            showSlides: function () {
                let i;
                var slides = document.getElementsByClassName("mySlides");
                for (i = 0; i < slides.length; i++) {
                    slides[i].style.display = "none";
                }
                this.slideIndex++;
                if (this.slideIndex > slides.length) {
                    this.slideIndex = 1
                }
                slides[this.slideIndex-1].style.display = "block";
                setTimeout(this.showSlides, 10000); // Change image every 2 seconds
            },
          search(){
            this.$emit('searched', this.searchedItem)
            this.searchedItem =""
          }
        },
        mounted() {
            this.showSlides()
        },


    }
</script>

<style scoped>
    * {
        direction: rtl;
        box-sizing: border-box
    }

    .main-hero{
        background-color: #ff6213;
        left: 0;
        right: 0;
        margin: auto 0;
        width: 1280px;
        position: relative;
    }

    .hero-container {
        display: flex;
        align-items: center;
        justify-content: center;
        flex-direction: column;
    }

    h1 {
        margin-top: 80px;
        font-size: 32px;
        color: white;
        text-align: center;
    }

    input {
        text-align: center;
        border-radius: 24px;
        width: 800px;
        margin: 40px 0 0 0;
        height: 20px;
    }

    input:focus{
        outline: none;
    }

    .button{
        margin-top: 35px;
        border-radius: 24px;
        border: none;
        background-color: #ffcc00;
        font-size: 16px;
        text-align: center;
        padding: 5px 25px;
    }

    img {
        margin-top: 35px;
        max-width: 800px;
        vertical-align: middle;
    }

    /* Slideshow container */
    .slideshow-container {
        max-width: 1000px;
        position: relative;
        margin: auto;
    }

    .active {
        background-color: #717171;
    }

    /* Fading animation */
    .fade {
        -webkit-animation-name: fade;
        -webkit-animation-duration: 1.5s;
        animation-name: fade;
        animation-duration: 1.5s;
    }

    @-webkit-keyframes fade {
        from {opacity: .4}
        to {opacity: 1}
    }

    @keyframes fade {
        from {opacity: .4}
        to {opacity: 1}
    }
</style>