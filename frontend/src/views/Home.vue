<template>
  <div class="home">
    <Header></Header>
    <div id="main">
      <Banner></Banner>
    </div>
    <Footer></Footer>
  </div>
</template>

<script setup>
import Header from "../components/Header.vue"
import Footer from "../components/Footer.vue"
import Banner from "../components/Banner.vue"


// 测试CORS的跨域配置是否有问题
// import axios from "axios"
// const http = axios.create()
// 测试服务端的跨域是否配置成功
// http.get("http://api.education-cloud.com:8000/home/test/").then(response=>{
//   console.log(response.data);
// })
// import http from "../utils/http";
// http.get("/home/test/").then(response=>{
//   console.log(response.data);
// })
</script>

<style scoped>

</style>