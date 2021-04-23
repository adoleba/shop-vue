import { createApp } from 'vue';
import App from './App.vue';
import 'bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import router from "./router";
require('bootstrap-icons/font/bootstrap-icons.css');


createApp(App).use(router).mount('#app')
