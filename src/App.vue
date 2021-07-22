<template>
    <div class="app">
        <!--    nav menu of the website    -->
        <nav_menu class="menu" v-on:childToParent="onChildClick" v-on:emitProd="prodEmitted" ref="navMenu"/>

        <!--    website component contains the main part of site!    -->
        <website v-if="page==='website'" class="website" ref="websitePage"/>

        <!--    admin's page    -->
        <user_profile v-if="page==='profile' & our_page==='user_profile'" class="test" v-on:updateNavName="changeName($refs.navMenu)"></user_profile>
        <admin_profile v-if="page==='profile' & our_page==='admin_profile'"></admin_profile>

        <!--    login and register section    -->
        <div class="loginRegister" v-if="page==='logreg'">
            <login_register class="main" :login="logv" v-on:signin="changeName($refs.navMenu)" v-on:goToRegister="setLogv"/>
        </div>

        <!--    footer of the website    -->
        <footer-section class="footerSection"/>
    </div>
</template>

<script>
    import nav_menu from "@/components/fixed/nav_menu";
    import footerSection from "@/components/fixed/footerSection";
    import website from "@/components/website";
    import user_profile from "@/components/profiles/user_profile";
    import admin_profile from "@/components/profiles/admin_profile";
    import login_register from "@/components/register_login/login_register";

    export default {
        name: 'App',
        components: {
            nav_menu,
            footerSection,
            website,
            login_register,
            user_profile,
            admin_profile
        },
        props:{
            page : {
                default:"website",
                type: String
            }
        },
        data (){
            return{
                our_page: "",
                logv : true,
                inps:[
                    {label:"نام",
                        placeholder:"نام خود را وارد کنید...",
                        class:true},
                    {label:"نام خانوادگی",
                        placeholder:"نام خانوادگی خود را وارد کنید...",
                        class:true},
                    {label:"ایمیل",
                        placeholder:"ایمیل خود را وارد کنید...",
                        class:false}
                ],
            }
        },
        methods:{
            onChildClick(value) {
                let userName = window.localStorage.getItem('name');
                this.page = value;

                if (this.page === "profile") {
                    if (userName === "admin") {
                        this.our_page = "admin_profile";
                        console.log("admin_profile");
                    }
                    else {
                        this.our_page = "user_profile";
                        console.log("user_profile");
                    }
                }
            },
            prodEmitted(){
              this.page = "website"
            },
            changeName(ref) {
                ref.setUserName();
            },
            setLogv(){
                this.logv = false;
            }
        }
    }
</script>

<style>
    * {
        margin: 0;
    }

    .app {
        display: flex;
        align-items: center;
        justify-content: center;
        flex-direction: column;
        background-color: #dddddd;
        width: 1280px;
        left: 0;
        right: 0;
        margin: 0 auto;
        min-height: 100vh;
        overflow-y: hidden;
    }
</style>
