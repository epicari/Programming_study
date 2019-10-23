<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <ul>
      <li>Hello Vue</li>
    </ul>
    <h1>{{ msg2 }}</h1>
    <ul>
      <li>Welcome Vue</li>
    </ul>
    <h1>{{ number }}</h1>
    <ul>
      <li>{{ number + 1 }}</li>
      <li>{{ number + 2 }}</li>
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
    }
  },
  props: {
    msg2: String
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
