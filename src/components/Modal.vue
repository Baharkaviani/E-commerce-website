
<template>
  <transition name="fade">
    <div class="modal" v-if="show">
      <div class="modal-backdrop" @click="closeModal()"/>
      <div class="modal-dialog">
        <div class="modal-header">
<!--          <slot name="header"/>-->
          <button type="button" class="modal-close" @click="closeModal()">
            X
          </button>
        </div>
        <div class="modal-body">
          <slot name="body"/>
        </div>

      </div>
    </div>
  </transition>
</template>

<script>
export default {
  name: "Modal",
  data() {
    return {
      show: false
    };
  },
  methods: {
    closeModal() {
      this.show = false;
      document.querySelector("body").classList.remove("overflow-hidden");
    },
    openModal() {
      this.show = true;
      document.querySelector("body").classList.add("overflow-hidden");
    }
  }
};
</script>


<style scoped>
.modal {
  overflow-x: hidden;
  overflow-y: scroll;
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 11;
  text-align: center;
}
  .modal-backdrop {
    background-color: rgba(0, 0, 0, 0.5);
    position: fixed;
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
    z-index: 12;
  }
  .modal-dialog {
    background-color: #ffffff;
    position:relative;
    width: 450px;
    display: flex;
    flex-direction: column;
    border-radius: 24px;
    z-index: 13;
    margin-right: auto;
    margin-left: auto;
    top :0%;
    transform: translate(0%,20%);
    /*overflow-y: auto;*/


  }
  input{
    display: block;
  }

  .modal-close {
    border-radius: 5px;
    width: 30px;
    height: 30px;
    background-color: #ffcc00;
    border:none;
  }
  .modal-header {
    padding: 10px;
    text-align: right;
  }
  .modal-body {
    padding: 0px 40px 20px;
    overflow: auto;
    display: flex;
    flex-direction: column;
    align-items: stretch;

  }

.fade-enter-active,
.fade-leave-active {
  transition: opacity 1s;
}
.fade-enter,
.fade-leave-to {
  opacity: 0;
}
</style>
