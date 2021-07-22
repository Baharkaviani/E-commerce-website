<template>
    <div class="menu">
        <nav>
            <div class="menu-item store"><a v-on:click="linkClicked($event)" id="website" href="#">فروشگاه</a></div>
            <div class="menu-item"><a href="#">صفحه اول</a></div>
            <div class="menu-item"><a href="#">تماس با ما</a></div>
            <div class="menu-item"><a href="#">پشتیبانی</a></div>
            <div class="menu-item"><a v-on:click="emitProd($event)" href="#">محصولات</a></div>
        </nav>

        <div v-if="isIn" class="sign-in">
            <a class="drop">{{ userName }}</a>
            <i class="arrow"></i>
            <div class="dropdown-content">
                <a  class="first" v-on:click="linkClicked($event)" id="profile" href="#">پروفایل</a>
                <a  class="second"  v-on:click="logout($event)" href="#">خروج از حساب</a>
            </div>
        </div>
      <div v-if="!isIn" class="sign-in">
        <a class="drop" v-on:click="linkClicked($event)" id="logreg">ورود / ثبت نام</a>
      </div>
    </div>
</template>

<script>
    export default {
        name: "nav_menu",
        data() {
            return {
                userName: "",
                isIn :false
            }
        },
        methods: {
            linkClicked(event) {
                this.$emit('childToParent', event.currentTarget.id)
            },
            setUserName() {
              if (window.localStorage.getItem('name')) {
                this.userName = window.localStorage.getItem('name');
                this.isIn = true
              }
              else {
                this.userName = "ورود/ثبت نام";
                this.isIn = false
              }
            },
          logout(){
              window.localStorage.removeItem('name')
              window.localStorage.removeItem('token')
            this.userName = "ورود/ثبت نام";
            this.isIn = false
            this.$emit('childToParent', "website")
          },
          emitProd(){
            this.$emit('emitProd')
          }
        },
        created (){
            this.setUserName();
        }
    }
</script>

<style scoped>
    .menu {
        border: 1px solid;
        border-color: #404040;
        height: 65px;
        position: fixed;
        width: 1278px;
        top: 0;
        left: 0;
        right: 0;
        margin: 0 auto;
        background-color: #FFFFFF;
        z-index: 10;
    }

    nav {
        direction: rtl;
        display: flex;
        align-items: center;
        font-size: 16px;
        position: absolute;
        top: 50%;
        transform: translate(0, -50%);
        width: 1280px;
    }

    nav .menu-item {
        color: #404040;
        margin-right: 25px;
        position: relative;
        text-align: center;
        display: flex;
    }

    nav .menu-item.store {
        font-size: 120%;
        color: #00bec9;
        margin-right: 50px;
    }

    nav .menu-item:active,
    nav .menu-item:hover {
        color: #00bec9;
    }

    nav .menu-item a {
        color: inherit;
        text-decoration: none;
    }

    .drop {
        color: #404040;
        position: absolute;
        top: 50%;
        transform: translate(0, -50%);
        padding: 10px 20px;
        border-radius: 24px;
        border-style: solid;
        border-color: #ffcc00;
        font-size: 16px;
        text-align: center;
        min-width: 90px;

    }

    .sign-in {
        margin-left: 20px;
        position: relative;
        top: 50%;
        transform: translate(0, -50%);
        float: left;
        min-width: 80px;
    }

    .dropdown-content {
        direction: rtl;
        display: none;
        position: absolute;
        top: 0;
        left: 0;
        transform: translate(0%, 10%);
        background-color: #cecece;
        z-index: -1;
        border-bottom-left-radius: 15px;
        border-bottom-right-radius: 15px;

    }

    .dropdown-content a {
        direction: rtl;
        color: black;
        padding: 12px 16px;
        text-decoration: none;
        display: inline-block;
        text-align: right;
        min-width: 103px;
        font-size: 16px;


    }

    .first {
        margin-top: 25px;
    }

    .second {
        margin-bottom: 10px;
    }

    .dropdown-content a:hover {
        background-color: #f1f1f1;
    }

    .sign-in:hover .dropdown-content {
        display: inline-block;
    }

    .sign-in:hover .drop {
        background-color: #ffcc00;
    }

    .arrow {
        border: solid black;
        border-width: 0 3px 3px 0;
        display: inline-block;
        padding: 3px;
        transform: rotate(45deg);
        -webkit-transform: rotate(45deg);
        margin-left: 12px;
        margin-bottom: 5px;
    }
</style>