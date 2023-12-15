import { createApp } from 'vue';
import App from './App.vue';
import './registerServiceWorker';
import router from './router';
import store from './store';
import VueCookies from 'vue-cookies';
import 'bootstrap/dist/css/bootstrap.css';

createApp(App).use(VueCookies).use(store).use(router).mount('#app')
