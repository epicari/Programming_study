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
  props: {
    msg2: String
  },
  methods: {
    say (message) {
      alert(message)
    },

  }
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
