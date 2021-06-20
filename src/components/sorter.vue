<template>
  <nav>
    <div class="sort sortLabel"><label>مرتب سازی بر اساس:</label></div>
    <button  class="sort sortButtons active">بیشترین فروش</button>
    <button class="sort sortButtons">قیمت</button>
  </nav>
</template>

<script>
export default {
  name: "sorter",
  // methods:{
  //   isClicked(){
  //       var mainNav = document.getElementsByTagName("nav");
  //       var sortOptions = mainNav.getElementsByClassName("sortButtons");
  //
  //       for (var i = 0; i < sortOptions.length; i++) {
  //         sortOptions[i].addEventListener("click", function() {
  //           var current = document.getElementsByClassName("active");
  //           if (current.length > 0) {
  //             current[0].className = current[0].className.replace(" active", "");
  //           }
  //           this.className += " active";
  //         });
  //       }
  //   }
  // }
}

</script>

<style scoped>
nav {
  float: right;
  direction: rtl;
  background-color: #FFFFFF;
  display: flex;
  align-items: center;
  text-align: center;
  font-size: 16px;
  position: absolute;
  top: 50%;
  transform: translate(0, -50%);
  width: 1280px;
  height: 50px;

}

nav .sort {
  margin-right: 25px;
  position: relative;
  text-align: center;
  display: flex;
}
.sortLabel{
  color: #404040;
}
.sortButtons{
  background-color:white;
  text-align: center;
  color: #404040;
  padding: 8px 20px;
  font-size: 16px;
  border: none;
  border-radius: 24px;

}
.active, .sortButtons:hover{
  background-color:#009eff;
  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
  color:white;
}

</style>