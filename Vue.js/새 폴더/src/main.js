import Vue from "vue";
import App from "./App.vue";
import router from "./router";

// store.js를 불러오는 코드
import { store } from "./store.js";

Vue.config.productionTip = false;

new Vue({
    // 뷰 인스턴스의 store 속성에 연결
    store: store,
    router,
    render: h => h(App)
}).$mount("#app");