<template>
  <div class="hello">
    <div @click='good' class='button'>좋아요</div>
    <h1>{{ msg }}</h1>
    <h2>Test Vue</h2>
    <ul>
      <li>
        <p>Test Vue View</p>
        <p>{{ data }}</p>
      </li>
    </ul>
  </div>
</template>

<script>

export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      data: 'Test Vue Data'
    }
  },
  methods: {
    good: function () {
      alert('Hello')
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
</style>
