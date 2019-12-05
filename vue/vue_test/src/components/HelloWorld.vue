<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <ul>
      <li>Hello Vue</li>
    </ul>
    <!-- App.vue 내 msg를 가져옴(?), props 사용-->
    <h1>{{ msg2 }}</h1>
    <ul>
      <li>Welcome Vue</li>
    </ul>
    <h1>{{ number }}</h1>
    <ul>
      <li>{{ number + 1 }}</li>
      <li>{{ number + 2 }}</li>
    </ul>
    <ul>
      <!-- 'v-on' 디렉티브를 사용하여 DOM 이벤트를 듣고 트리거 -->
      <button v-on:click="count += 1">Add 1</button>
      <p> 버튼 클릭한 횟수는 {{ count }} 번 </p>
    </ul>
    <ul>
      <!-- 인라인 JavaScript 구문에 메소드를 사용 -->
      <button v-on:click="say('hi')">Say hi</button>
      <button v-on:click="say('hello')">Say hello</button>  
    </ul>
    <ul>
      <!-- Create a new data from 'now' -->
      <span>{{ new Date() | moment('dddd, MMMM Do YYYY HH:mm:ss') }}</span>
    </ul>
    <ul>
      <button v-on:click="reverseMsg">문자열 역순</button>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'Hello World',
      number: 1,
      count: 0,
    }
  },
  // props는 상위 컴포넌트에서 하위 컴포넌트로 데이터를 전달할 때 사용, 상위 APP.vue
  props: {
    msg2: String
  },
  methods: {
    say (message) {
      alert(message)
    },
    reverseMsg: function() {
      this.msg = this.msg.split('').reverse().join('');
      return this.msg;
    }
  },

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
