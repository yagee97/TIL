<!-- App.vue(parent) -->
!<template>
  <div id="app">
    Parent counter : {{ parentCounter }} <br>
    <button @click="addCounter">+</button>
    <button @click="subCounter">-</button>
   <child></child> 
  </div>
</template>

<script>
import Child from "./Child.vue";
import { mapGetters } from 'vuex';
import { mapMutations} from 'vuex';

export default {
  components: {
    child : Child
  },

  computed: mapGetters({
    parentCounter : 'getCounter'
  }),

  methods: {
    // addCounter(){
    //   // this.$store.state.counter++;
    //   // commit을 이용하여 mutations 이벤트를 호출해야한다.
    //   this.$store.commit('addCounter');
    // }
    // Vuex의 Mutations 메서드 명과 App.vue 메서드 명이 동일할 때 []사용
    ...mapMutations([
      'addCounter'
    ]),
    // Vuex 의 Mutations 메서드 명과 App.vue 메서드 명을 다르게 매칭할 때 {} 사용
    ...mapMutations({
      addCounter: 'addCounter' // 앞 addCounter는 해당 컴포넌트의 메서드를, 뒤는 Vuex의 Mutations를 의미
    })
  }
};
</script>

<style>

</style>