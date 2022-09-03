<template>
  <h1>首页</h1>
  <el-row class="mb-4">
    <el-button>Default</el-button>
    <el-button type="primary">Primary</el-button>
    <el-button type="success">Success</el-button>
    <el-button type="info">Info</el-button>
    <el-button type="warning">Warning</el-button>
    <el-button type="danger">Danger</el-button>
    <el-rate v-model="store.value1" :colors="store.colors"> </el-rate>
  </el-row>
</template>

<script setup>
import {reactive} from "vue";
const store = reactive({
  value1: null,
  colors: ['#99A9BF', '#F7BA2A', '#FF9900'],
})
</script>

<style scoped>

</style>