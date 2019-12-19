<template>
  <div id="app">
    <rheader></rheader>
    <chat></chat>
    <list></list>
  </div>
</template>

<script>
  import chat from './components/chat/reddit_chat.vue'
  import list from './components/list/reddit_list.vue'
  import rheader from './components/header/reddit_header.vue'

export default {
  components: {
    'chat': chat,
    'list': list,
    'rheader': rheader
  }  
}
</script>

<style>
  body {
    text-align: center;
    background-color: #f6f6f8;
  }
  .shadow {
    box-shadow: 5px 10px 10px rgba(0, 0, 0, 0.03);
  }
  input {
    border-style: groove;
    width: 200px;
  }
</style>