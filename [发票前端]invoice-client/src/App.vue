<template>
  <div id="center-box">
    <div id="letf-nav">
      <AppNav/>
    </div>
    <div id="nav-view">
      <VAT_invoice/>
    </div>
  </div>
</template>

<script lang="ts" setup>
import VAT_invoice from './VAT_invoice.vue';
import AppNav from './AppNav.vue';

</script>

<style>
.demo-form-inline .el-input {
  --el-input-width: 220px;
}

.demo-form-inline .el-select {
  --el-select-width: 220px;
}
#center-box{
  width: 100%;
  height: auto;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}
#letf-nav{
  width: 100%;
  margin-bottom: 20px;
}
#nav_view{
  width: 100%;
  height: 50%;
}
</style>
