<template>
  <button :class='{"box":true, "alive":state}' @click="changeState"></button>
</template>

<script>
export default{
  props:{
      row: "",
      col: "",
      state: 0
      
  },
  methods:{
      changeState(){
          this.$emit('update-life', [this.row, this.col, this.state])
          if (this.state == 1) {
              this.state = 0
          } else {
              this.state = 1
          }
      }
  }
}
</script>

<style>
.box{
  background-color: rgb(154, 169, 229);
  padding: 50px;
  margin: 10px;
}
.alive{
  background-color: blue;
}
</style>