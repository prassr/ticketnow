<template>
      <router-view v-slot="{ Component }">
        <transition name="slide">
            <component :is="Component" />
        </transition>
      </router-view>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* text-align: center; */
  color: #2c3e50;
  width: 100%;
  height: 100%;
}

.slide-enter-active, .slide-leave-active {
    transition: all 0.5s ease;
    }

    .slide-enter-from, .slide-leave-to {
    transform: translateX(-100%);
    opacity: 0;
    }

    .slide-enter-to, .slide-leave-from {
    transform: translateX(0);
    opacity: 1;
    }

</style>
