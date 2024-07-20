<template>

  <nav>
    <div class = "nav-bar">
      
      <RouterLink class = "nav-link" to = "/filter">Home</RouterLink>
      <RouterLink class = "nav-link" to = "/planner">Planner</RouterLink>
      <RouterLink class = "nav-link" to = "/about">About</RouterLink>
      
    </div>
    <div class = "nav-line"></div>

  </nav>

  <RouterView/>

</template>

<script setup>
import { RouterView } from 'vue-router'
</script>

<style>

.nav-bar {
  display: flex;
  justify-content: flex-start;
  align-items: flex-end;
  column-gap: 50px;
}

.nav-link {
  text-decoration: none;
  font-style: italic;
  font-size: 45px;
  color: #313346;
}

.nav-line {
  height: 2px;
  width: auto;
  margin: 30px 0px;
  background-color: #313346;
}

.nav-link:hover {
  text-decoration: underline;
}

.router-link-active {
  font-family: "Inter-Regular";
}

</style>